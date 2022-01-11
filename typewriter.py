import time

def typewriter(message):
        for char in str(message):
            print(char,end='')
            time.sleep(0.03)
        return('')
