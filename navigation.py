import webbrowser as wb
import speech_recognition as sr

#wb.open('https://shimla.kvs.ac.in/')


listener= sr.Recognizer()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
                
    except:
        pass
    return command

def program():
    command = take_command()
    print(command)
    if 'open' in command:
        #ws = command.replace('opening', '')
        wb.open('https://shimla.kvs.ac.in/')

while True:
    program()
