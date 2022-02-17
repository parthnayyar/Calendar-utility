
import mysql.connector as mysql, input_file as inp, typewriter as t, dates, login, features

t.typewriter('WELCOME TO YOUR PERSONAL CALENDAR!\n\n\n')

(mydb,cursor,loginid)=login.login()
while True:
    comm1=input('''\n\n
'v' -> view your calendars
's' -> open settings
'e' -> exit the program\nEnter your command here: ''')
    if comm1.lower() in ['v','s','e']:
        if comm1.lower()=='v':
            input_year=inp.user_input()
            try:
                cursor.execute('create table calendar'+str(input_year)+'''
(YYYY_MM_DD char(10) primary key)''')
                values=dates.year(input_year)
                cursor.executemany('insert into calendar'+str(input_year)+'''
(YYYY_MM_DD) values(%s)''',values)
                mydb.commit()
            except:
                pass
            
            while True:
                comm2=input('''\n\n
'a' -> access calendar '''+str(input_year)+'''
'e' -> exit to main menu
Enter your command here: ''')
                if comm2.lower() in ['a','e']:
                    if comm2.lower()=='a': 
                        while True:
                            comm3=input('''\n

'v' -> view all events
'c' -> check events
'a' -> add new events
'u' -> update events
'd' -> delete events
'g' -> go back
Enter your command here: ''')
                            if comm3.lower() in ['v','c','a','u','d','g']:
                                if comm3.lower()=='c':
                                    features.check(cursor,loginid,input_year)
                                    continue
                                elif comm3.lower()=='a':
                                    features.add(cursor,loginid,input_year,mydb)
                                    continue
                                elif comm3.lower()=='u':
                                    features.update(cursor,loginid,input_year,mydb)
                                    continue
                                elif comm3.lower()=='d':
                                    features.delete(cursor,loginid,input_year,mydb)
                                    continue
                                elif comm3.lower()=='v':
                                    features.view(cursor,loginid,input_year)
                                    continue
                                else:
                                    break
                            else:
                                t.typewriter('Please enter a valid input.')
                                continue
                    else:
                        t.typewriter('\nExitted calendar '+str(input_year))
                        break
                else:
                    t.typewriter('Please enter a valid input.')
                    continue
        elif comm1.lower()=='s':
            try:
                login.settings(mydb,cursor,loginid)
                continue
            except:
                break
        else:
            break
    else:
        t.typewriter('Please enter a valid input.')

t.typewriter('\n\n\nThanks for using the program. Have a good day!')
