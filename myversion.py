import speech_recognition as sr


# def speak(audio):
#     wel.say(audio)
#     wel.runAndWait()
# speak('Bonjour madame rim')

def get_am1():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
        print('say command sir')
        command.phrase_threshold=0.2
        audio=command.listen(mic, timeout=3)
        query=command.recognize_google(
            audio,
            language='ar-DZ',
            with_confidence=False,
            show_all=True)
        print(query)
        recognized_text = query["alternative"][0]["transcript"]
        print(f"Recognized text: {recognized_text}")

def get_ar():
    command=sr.Recognizer()
    with sr.Microphone() as mic:
        print('say command sir')
        command.phrase_threshold=0.2
        audio=command.listen(mic, timeout=3)
        query=command.recognize_google(
            audio,
            language='ar-DZ',
            with_confidence=False,
            show_all=True)
        print(query)
        recognized_text = query["alternative"][0]["transcript"]
        print(f"Recognized text: {recognized_text}")
   

get_am1()
# get_ar()