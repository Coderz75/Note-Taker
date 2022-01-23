import sys, time 
import os
password = os.environ['password']

def write(write):
    for char in write: 
        print(char, end='') 
        sys.stdout.flush() 
        time.sleep(0.05) 
    print("")
def start():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    write('hello')
    write('Welcome to Note taker')
    write("plz enter password below:")
    uinput = input()
    if uinput == password:
        write("Great! Enter item you want to find below")
    else:
        write("incorrect")
        start()
start()