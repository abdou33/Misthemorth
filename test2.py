import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

class VoiceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recognition App")

        self.record_button = ttk.Button(root, text="Record Voice", command=self.record_voice)
        self.record_button.pack(pady=10)

        self.result_label = ttk.Label(root, text="")
        self.result_label.pack(pady=10)

    def record_voice(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Recording...")
            audio_data = recognizer.listen(source, timeout=5)

        try:
            print("Recognizing...")
            text_result = recognizer.recognize_google(audio_data)
            self.result_label.config(text=f"Result: {text_result}")
        except sr.UnknownValueError:
            print("Recognition failed. Audio not understood.")
            self.result_label.config(text="Recognition failed. Audio not understood.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            self.result_label.config(text="Recognition service unavailable.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecognitionApp(root)
    root.mainloop()
