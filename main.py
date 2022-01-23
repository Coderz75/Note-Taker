import sys, time 
import os
from replit import db
password = os.environ['password']

#IMPORTANT
# If you wish to fork or make this project your own, go to the secrets tab, and added (or make) a token called password, and set the value to be your password

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def write(write):
    for char in write: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.05) 
    print("")


def start():
    clear()
    write('hello')
    write('Welcome to Note taker')
    write("plz enter password below:")
    uinput = input()
    if uinput != password:
        write("incorrect")
        time.sleep(1)
        start()

def findIfKey(key):
    matches = db.prefix(key)
    write('Do you wish to read this key or edit it/make new? (type r for read, e for edit or make)')
    command = input()
    if command == 'r':
        value = db[key]
        write("Writing key " + key)
        write('')
        write(value)
        write('')
        write('Type anything below when your done')
        uinput = input()
        return
    elif command == 'e':
        write('Ok, wht does this "key" contain?')
        value = input()
        db[key] = value
        write('Done!')
        return

        



start()
clear()
write('Great! You got it right!')
time.sleep(1)
clear()
while 1 == 1:
    clear()
    write("Enter command below, or if you are unsure, type all")
    command = input()
    if command == 'all':
        keys = db.keys()
        write('Items (Just type the key to read it)')
        write(keys)
        write('Type anything below when you are done')
        a = input()

    else:
        findIfKey(command)
    


