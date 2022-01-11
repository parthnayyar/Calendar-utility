import mysql.connector as sql, typewriter as t, csv

def date_conv(old_date):
    new_date=old_date[6:]+'_'+old_date[3:5]+'_'+old_date[:2]
    return(new_date)

def csv_fun(cursor,loginid,input_year):
    cursor.execute('select * from calendar'+str(input_year))
    result=cursor.fetchall()

    with open(str(loginid)+"'s "+str(input_year)+' calendar.csv','w',newline='') as file:
        records=[]
        for i in result:
            records.append(i)
        csv.writer(file).writerows(records)

    with open(str(loginid)+"'s "+str(input_year)+' calendar.csv',newline='') as file:
        csv_reader=csv.reader(file, delimiter=',')
        records=[]
        for row in csv_reader:
            records.append(row)

    frecords=[]
    for record in range(len(records)):
        ffields=()
        for field in range(len(records[record])):
            if field==0:
                ffields+=tuple([(records[record][field])])
            else:
                if records[record][field]!='':
                    ffields+=tuple([(records[record][field])])
        frecords.append(ffields)
    return(frecords,records)

def view(cursor,loginid,input_year):
    (frecords,records)=csv_fun(cursor,loginid,input_year)
    s=0
    t.typewriter('\n')
    for record in range(len(frecords)):
        if s<len(frecords[record]):
            s=len(frecords[record])
        
        if len(frecords[record])>1:
            for field in range(len(frecords[record])):
                if field==0:
                    print(frecords[record][field],end=' : ')
                elif field!=len(frecords[record])-1:
                    print(frecords[record][field], end=', ')
                else:
                    print(frecords[record][field])
    if s==1:
        t.typewriter('You do not have any events in '+str(input_year)+'.')

    
def check(cursor,loginid,input_year):
    (frecords,records)=csv_fun(cursor,loginid,input_year)
    alldates=[]
    for dates in records:
        alldates.append(dates[0])
    while True:
        input_date=date_conv(input(t.typewriter('\nEnter date in dd/mm/yyyy format for which you want to check your events: ')))
        try:
            if input_date in alldates:
                for fields in frecords:
                    if fields[0]==input_date:
                        if len(fields)==1:
                            a=int('a')
                        else:
                            t.typewriter('\nYour events are:\n')
                            for event_no in range(1,len(fields)):
                                if event_no==len(fields):
                                    print(str(event_no)+' ->',fields[event_no],end=', ')
                                else:
                                    print(str(event_no)+' ->',fields[event_no])
                break
            else:
                t.typewriter('Please enter a valid date.')
                continue
        except:
            t.typewriter('You do not any events on this day.')
            break




def add(cursor,loginid,input_year,mydb):
    (frecords,records)=csv_fun(cursor,loginid,input_year)
    alldates=[]
    for dates in records:
        alldates.append(dates[0])
    while True:
        input_date=date_conv(input(t.typewriter('\nEnter date in dd/mm/yyyy format for which you want to add events: ')))
        if input_date in alldates:
            for fields in frecords:
                if fields[0]==input_date:
                    input_event=input(t.typewriter('Enter the event that you want to add: '))
                    try:
                        cursor.execute('update calendar'+str(input_year)+' set Event'+str(len(fields))+"='"+str(input_event)+"' where YYYY_MM_DD='"+str(input_date)+"'")
                        mydb.commit()
                    except:
                        cursor.execute('alter table calendar'+str(input_year)+' add column Event'+str(len(fields))+' char(100)')
                        mydb.commit()               
                        cursor.execute('update calendar'+str(input_year)+' set Event'+str(len(fields))+"='"+str(input_event)+"' where YYYY_MM_DD='"+str(input_date)+"'")
                        mydb.commit()
                    t.typewriter('Your event has been added.')
            break
        else:
            t.typewriter('Please enter a valid date.')
            continue



            
def update(cursor,loginid,input_year,mydb):
    (frecords,records)=csv_fun(cursor,loginid,input_year)
    alldates=[]
    for dates in records:
        alldates.append(dates[0])
    while True:
        input_date=date_conv(input(t.typewriter('\nEnter date in dd/mm/yyyy format for which you want to update an event: ')))
        try:
            if input_date in alldates:
                for fields in frecords:
                    if fields[0]==input_date:
                        if len(fields)==1:
                            a=int('a')
                        else:
                            t.typewriter('\nYour events are:\n')
                            for event_no in range(1,len(fields)):
                                if event_no==len(fields):
                                    print(str(event_no)+' ->',fields[event_no],end=', ')
                                else:
                                    print(str(event_no)+' ->',fields[event_no])
                            for record in range(len(frecords)):
                                if len(frecords[record])>1:
                                    for field in range(len(frecords[record])):
                                        if field==0:
                                            if frecords[record][field]==input_date:
                                                while True:
                                                    input_event_no=input(t.typewriter('\nEnter the event number that you want to update: '))
                                                    try:
                                                        if int(input_event_no) in range(1,len(fields)):
                                                            cursor.execute('update calendar'+str(input_year)+' set Event'+str(input_event_no)+"='"+str(input(t.typewriter('Enter the updated event: ')))+"' where YYYY_MM_DD='"+str(input_date)+"'")
                                                            mydb.commit()
                                                            t.typewriter('Your event has been updated.')
                                                            break
                                                        else:
                                                            t.typewriter('Please enter a valid input.')
                                                            continue
                                                    except:
                                                        t.typewriter('Please enter a valid input.')
                                                        continue
                break
            else:
                t.typewriter('Please enter a valid date.')
                continue
        except:
            t.typewriter('You do not any events on this day.')
            break
        



def delete(cursor,loginid,input_year,mydb):
    (frecords,records)=csv_fun(cursor,loginid,input_year)
    alldates=[]
    for dates in records:
        alldates.append(dates[0])
    while True:
        input_date=date_conv(input(t.typewriter('\nEnter date in dd/mm/yyyy format for which you want to delete an event: ')))
        try:
            if input_date in alldates:
                for fields in frecords:
                    if fields[0]==input_date:
                        if len(fields)==1:
                            a=int('a')
                        else:
                            t.typewriter('\nYour events are:\n')
                            for event_no in range(1,len(fields)):
                                if event_no==len(fields):
                                    print(str(event_no)+' ->',fields[event_no],end=', ')
                                else:
                                    print(str(event_no)+' ->',fields[event_no])
                            for record in range(len(frecords)):
                                if len(frecords[record])>1:
                                    for field in range(len(frecords[record])):
                                        if field==0:
                                            if frecords[record][field]==input_date:
                                                while True:
                                                    input_event_no=int(input(t.typewriter('\nEnter the event number that you want to delete: ')))
                                                    try:
                                                        if input_event_no in range(1,len(fields)):
                                                            cursor.execute('update calendar'+str(input_year)+' set Event'+str(input_event_no)+"=NULL where YYYY_MM_DD='"+str(input_date)+"'")
                                                            mydb.commit()
                                                            t.typewriter('Your event has been deleted.')
                                                            try:
                                                                cursor.execute('select Event'+str(input_event_no+1)+' from calendar'+str(input_year)+" where YYYY_MM_DD='"+str(input_date)+"'")
                                                                next_event=cursor.fetchall()[0][0]
                                                                if next_event is None:
                                                                    pass
                                                                else:
                                                                    for i in range(1,len(fields)-input_event_no):
                                                                        cursor.execute('select Event'+str(input_event_no+i)+' from calendar'+str(input_year)+" where YYYY_MM_DD='"+str(input_date)+"'")
                                                                        event=cursor.fetchall()[0][0]
                                                                        cursor.execute('update calendar'+str(input_year)+' set Event'+str(input_event_no+i-1)+"='"+str(event)+"' where YYYY_MM_DD='"+str(input_date)+"'")
                                                                        mydb.commit()
                                                                        cursor.execute('update calendar'+str(input_year)+' set Event'+str(input_event_no+i)+"=NULL where YYYY_MM_DD='"+str(input_date)+"'")
                                                                        mydb.commit()
                                                            except:
                                                                pass
                                                            break
                                                        else:
                                                            t.typewriter('Please enter a valid input.')
                                                            continue
                                                    except:
                                                        t.typewriter('Please enter a valid input.')
                                                        continue
                break
            else:
                t.typewriter('Please enter a valid date.')
                continue
        except:
            t.typewriter('You do not any events on this day.')
            break
