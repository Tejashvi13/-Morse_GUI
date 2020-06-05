from tkinter import *
import RPi.GPIO as GPIO
import time

MORSE = {' ': ' ',
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '&': '.-...',
        '@': '.--.-.',
        ')': '-.--.-',
        '(': '-.--.',
        ':': '---...',
        ',': '--..--',
        '=': '-...-',
        '!': '-.-.--',
        '.': '.-.-.-',
        '-': '-....-',
        '+': '.-.-.',
        '"': '.-..-.',
        '?': '..--..',
        '/': '-..-.'}

window = Tk()
window.geometry("1000x600")
window.title("Blink Morse code")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)


entry = Entry(window,fg="yellow", bg="black", width = 50)
entry.pack()

def dot():
    GPIO.output(7, True)
    time.sleep(0.5)
    GPIO.output(7, False)
    time.sleep(0.5)
    
def line():
    GPIO.output(7, True)
    time.sleep(1)
    GPIO.output(7, False)
    time.sleep(0.5)
       
def blink():
    
    user_input = entry.get()
    
    if len(user_input) > 12:
        print('Please enter between 1-12 characters')
        window.destroy()   

    for letter in user_input:
        for symbol in MORSE[letter]:
            if symbol == '-':
                line()
            elif symbol == ".":
                    dot()
            else:
                time.sleep(1)
        time.sleep(1)
    
myLabel = Label(window, text = "Please enter between 1-12 character")
myLabel.pack()       

B1 = Button(window, text = "BLINK", width = 20, bg = "yellow", fg="black", command=blink)
B1.pack()
               
window.mainloop()


    

