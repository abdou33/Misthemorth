import pyttsx3 
import speech_recognition as sr
from tkinter import*
from playsound import playsound
root=Tk()
root.title('مترجم صوتي')
root.geometry('370x470+500+100')
root.resizable(FALSE,FALSE)
wel= pyttsx3.init()
voices= wel.getProperty('voices')
wel.setProperty('voices', voices[0].id)

# def speak(audio):
#     wel.say(audio)
#     wel.runAndWait()
# speak('Bonjour madame rim')

def takecommond():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
        print('say command sir')
        command.phrase_threshold=0.4
        audio=command.listen(mic)
        try:
           print('تسجبل......')
           query=command.recognize_google(audio,language='ar')
           print(f'you said: {query}')
        except Exception as Error :
           return None 
        return query.lower()
   
def b1():
    query=takecommond()
    name=query
    E2.insect(0,name) 

def b2():
    query=takecommond()
    name=query
    E1.insect(0,name) 



heading = Label( text = "العربية")
heading.place(x=300,y=20)
E2=Entry(root,fon=('tajawel',14))
E2.place(x=80,y=70)
b2=Button(root,text='العربية',bg='black',fg='white',font=('tajawal',9),command=b1
)
b2.place(x=20,y=70)
headin= Label( text = "تارقية")
headin.place(x=300,y=180)
E1=Entry(root,fon=('tajawel',14))
E1.place(x=80,y=250)
b2=Button(root,text='التارقية',bg='black',fg='white',font=('tajawal',9),command=b2)
b2.place(x=10,y=250)

mainloop()