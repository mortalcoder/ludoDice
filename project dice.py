import random
import os
import socket

def chk_connection():
    try:
        socket.create_connection("google.com",80)
        return True
    except OSError:
        return False

try:
    import pyfiglet
    from colorama import init, Fore, Style
except ImportError:
    if chk_connection() == True:
        os.system('''
        pip install pyfiglet
        pip install colorama
        ''')    
    elif chk_connection() == False:
        print("You are not connected to the internet in order to install reqired packages")
        exit()
  
finally:
    import pyfiglet
    from colorama import init,Fore,Style
    import colorama
    colorama.init()
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    r = Fore.RED
    g = Fore.GREEN
    b = Fore.BLUE
    y = Fore.YELLOW
    rs = Fore.RESET
    clr()
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText('Dicey')
    print(r + logo + rs)
    print(g + "Author: Mortal_coder\n" + rs)

    print(g + "Hello i m the best alternate to a physical dice," + rs)
    print(y + "Here I roll!" + g)
    while True:
        listw = list("123456")
        e = random.choice(listw) #random is the freakin' module that helps u to print random numbers ;)
        print(b+"outcome /",e + g) 
        a = input('Wanna roll me again?[enter/n]')
        if a == 'n':
            exit()
        else:
            pass
