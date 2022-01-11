import mysql.connector as mysql, typewriter as t

def login():
    while True:
        acc=input(t.typewriter('Do you have an existing account?(yes/no): '))
        if acc.lower() in ['yes','no']:
            if acc.lower()=='yes':
                while True:
                    try:
                        loginid=str(input(t.typewriter('\nEnter your LoginID: ')))
                        mydb=mysql.connect(host='localhost',
                                           user='root',
                                           passwd='30Aug2003',
                                           database=loginid)
                        cursor=mydb.cursor()
                        passwd=input(t.typewriter('Enter your password: '))
                        cursor.execute('select pass from pass')
                        if passwd==cursor.fetchall()[0][0]:
                            t.typewriter('\nLogged in as '+loginid+'.')
                            break
                        else:
                            error=int('a')
                                
                    except:
                        t.typewriter('Incorrect loginID or password. Please try again.')
                        continue
                break
            if acc.lower()=='no':
                while True:
                    try:
                        mydb=mysql.connect(host='localhost',user='root', passwd='30Aug2003')
                        cursor=mydb.cursor()
                        while True:
                            loginid=str(input(t.typewriter('\nCreate new LoginID: ')))
                            if 5<len(loginid)<21:
                                if ' ' in loginid:
                                    t.typewriter('''You cannot have a blank space
in your ID. Please try again.''')
                                    continue
                                else:
                                    cursor.execute('show databases')
                                    databases=cursor.fetchall()
                                    if tuple([loginid]) in databases:
                                        a=int('a')
                                    else:
                                        t.typewriter('''This loginID is available.
Creating new account...''')
                                        break
                            else:
                                t.typewriter('''Your ID must be of 6-20 characters.
Please try again.''')
                                continue
                        while True:
                            pw=tuple([input(t.typewriter('\nCreate your password: '))])
                            if 7<len(pw[0])<17:
                                if pw==tuple([input(t.typewriter('Confirm password: '))]):
                                    break
                                else:
                                    t.typewriter('''Passwords do not match.
Please try again.''')
                                    continue
                            else:
                                t.typewriter('''Your password must be of 8-16 characters.
Please try again''')
                                continue
                        cursor.execute('create database '+loginid)
                        cursor.execute('use '+loginid)
                        cursor.execute('create table pass(pass char(16))')
                        cursor.executemany('insert into pass(pass) values (%s)',[pw])
                        mydb.commit()
                        t.typewriter('''\nYour account has been successfully created.
\nLogged in as '''+loginid+'.')
                        break
                    except:
                        t.typewriter('''This LoginID is already in use.
Please try a different LoginID.''')
                        continue
                break
        else:
            t.typewriter('Please enter a valid input.\n')
            continue
    return(mydb,cursor,loginid)





def settings(mydb,cursor,loginid):
    while True:
        setting=input(t.typewriter('''\n
'c' -> change password\n
'd' -> delete account\n
'e' -> exit settings\n
Enter your command here: '''))
        if setting.lower() in ['c','d','e']:
            if setting.lower()=='c':
                cpw=input(t.typewriter('\nEnter your current password: '))
                cursor.execute('select pass from pass')
                if cpw==cursor.fetchall()[0][0]:
                    while True:
                        npw=tuple([input(t.typewriter('\nEnter new password: '))])
                        if 7<len(npw[0])<17:
                            if npw==tuple([input(t.typewriter('Confirm password: '))]):
                                break
                            else:
                                t.typewriter('''Passwords do not match.
Please try again.''')
                                continue
                        else:
                            t.typewriter('''Your password must be of 8-16 characters.
Please try again''')
                            continue
                    cursor.execute('drop table pass')
                    cursor.execute('create table pass(pass char(16))')
                    cursor.executemany('insert into pass(pass) values (%s)',[npw])
                    mydb.commit()
                    t.typewriter('\nYour password has been successfully changed.')
                    break
                else:
                    t.typewriter('''The password you have entered is incorrect.
Please try again.''')
                    continue
            elif setting.lower()=='d':
                while True:
                    confirmation=input(t.typewriter('''\nConfirm account delete
(yes/no): '''))
                    if confirmation.lower() in ['yes','no']:
                        if confirmation.lower()=='yes':
                            cursor.execute('drop database '+loginid)
                            t.typewriter('\nYour account has been deleted.')
                            a=int('a')
                        else:
                            break
                    else:
                        t.typewriter('Please enter a valid input.')
                        continue
                break
            else:
                break
        else:
            t.typewriter('Please enter a valid input.')
            continue
