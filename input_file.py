import calendar as cal, typewriter as t

def user_input():
    while True:
        input_year=input(t.typewriter('\nEnter a year to access its calendar: '))
        try:
            input_year=int(input_year)
            t.typewriter('\n\n')
            print(cal.calendar(input_year))
            break
        except:
            t.typewriter('Please enter a valid input.')
            continue
    return(input_year)
