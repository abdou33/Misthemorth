from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.uix.label import Label
from data import db
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
import bidi.algorithm
from kivy.uix.camera import Camera
from functools import partial
import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture

Window.size = (400, 600)

class MainApp(MDApp):
    
    def build(self):
        Window.right = True
       
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file('ui/main.kv'))
        screen_manager.add_widget(Builder.load_file('ui/page1.kv'))
        screen_manager.add_widget(Builder.load_file('ui/page2.kv'))
        # screen_manager.add_widget(Builder.load_file('ui/page3.kv'))
        Builder.load_file('ui/page3.kv')
        screen_manager.add_widget(page3(name='page3'))
        Builder.load_file('ui/page4.kv')
        screen_manager.add_widget(page4(name='page4'))


        return screen_manager


    # open mic and recognize voice
    def on_mic_button_press(self, page, state, container, language1, language2, language3):
        import speech_recognition as sr
        command=sr.Recognizer()
        with sr.Microphone() as mic:
            print('say command sir')
            command.phrase_threshold=0.4
            audio=command.listen(mic, timeout=5, phrase_time_limit=2)
            query=command.recognize_google(
                audio,
                language='ar-DZ',
                with_confidence=False,
                show_all=True)
            print(query)
            if len(query) != 0:
                words_list = query["alternative"][0]["transcript"].split(' ')
                print(f"Recognized text: {words_list}")
                if(state == '1'):
                    for word in words_list:
                        self.search_word(word, page, container, language1, language2, language3)
                elif(state == '1'):
                    page3.update_image(words_list[0], 'fr')

    
    # search for the word in tha list
    def search_word(self, user_input, page, container, language1,language2, language3):
        tmp = ""
        tmp2 = ""
        for item in db:
            words = item['words']
            vocals = item['vocal']
            if user_input == words[language1]:
                # print(words[language2])
                print(f"Match found in language '{words[language1]}': {words[language2]}")
                if language1 == "am1":
                    user_input = words['fr']
                tmp = words[language2]
                tmp2 = words[language3]
                break

        if(tmp != ""):
            print(f"words22: {words}")
            message_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)

            bidi_text1 = arabic_reshaper.reshape(user_input)
            reshaped_text1 = bidi.algorithm.get_display(bidi_text1)
            left_label = Label(text=reshaped_text1, size_hint=(None, 1), font_name='ARIAL1', width=93.33, markup=True)
            left_label.color = (1, 0, 0, 1)

            bidi_text2 = arabic_reshaper.reshape(tmp)
            reshaped_text2 = bidi.algorithm.get_display(bidi_text2)
            middle_label = Label(text=reshaped_text2, size_hint=(None, 1), font_name='ARIAL1', width=93.33, markup=True)
            middle_label.color = (0, 0, 0, 1)

            bidi_text3 = arabic_reshaper.reshape(tmp2)
            reshaped_text3 = bidi.algorithm.get_display(bidi_text3)
            right_label = Label(text=reshaped_text3, size_hint=(None, 1), font_name='ARIAL1', width=93.33, markup=True)
            right_label.color = (0, 0, 1, 1)

            play_button1 = Button(text='▶', font_size='20sp', font_name='ui/fonts/arial-unicode-ms.ttf', size_hint=(None, None), size=(40, 40))
            partial_play_audio1 = partial(self.play_audio, vocals[language1])
            play_button1.bind(on_press=partial_play_audio1)
            play_button2 = Button(text='▶', font_size='20sp', font_name='ui/fonts/arial-unicode-ms.ttf', size_hint=(None, None), size=(40, 40))
            partial_play_audio2 = partial(self.play_audio, vocals[language2])
            play_button2.bind(on_press=partial_play_audio2)
            play_button3 = Button(text='▶', font_size='20sp', font_name='ui/fonts/arial-unicode-ms.ttf', size_hint=(None, None), size=(40, 40))
            partial_play_audio3 = partial(self.play_audio, vocals[language3])
            play_button3.bind(on_press=partial_play_audio3)

            message_layout.add_widget(left_label)
            message_layout.add_widget(play_button1)
            message_layout.add_widget(middle_label)
            message_layout.add_widget(play_button2)
            message_layout.add_widget(right_label)
            message_layout.add_widget(play_button3)
            self.root.get_screen(page).ids[container].add_widget(message_layout)



        print(f"No match found for '{user_input}'")

    def play_audio(self, audio_file, instance):
        from playsound import playsound as play
        play("vocals/"+audio_file)
        print("Button pressed, playing audio")


    def detector():
        import os
        import cv2
        import time
        import uuid

        for label in labels:
            cap=cv2.VideoCapture(0)
            print('Collecting images for {}'.format(label))

            for imgnum in range(number_of_images):
                ret,frame=cap.read()
                cv2.imshow('frame',frame)
                time.sleep(2)
                
                if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
            cap.release()

class page3(Screen):
    def __init__(self, **kwargs):
        super(page3, self).__init__(**kwargs)
        self.image_widget = Image(source="images/1.png")
        self.ids.chat_container3.add_widget(self.image_widget)

    def update_image(self, user_input, language1):
        tmp = ""
        for item in db:
            words = item['words']
            images = item['image']
            if user_input == words[language1]:
                # print(words[language2])
                print(f"Match found in language '{words[language1]}'")
                tmp = images['sign']
                break
        # Change the image source here based on your requirements
        new_image_source = "images/" + tmp
        self.image_widget.source = new_image_source
        self.image_widget.reload()

class page4(Screen):
    def __init__(self, **kwargs):
        super(page4, self).__init__(**kwargs)
        self.image_widget = Image()
        self.ids.camera_box.add_widget(self.image_widget)
        self.yolov5_detector = YOLOv5Detector(self, self.ids.camera_box)

    def update_processed_image(self, frame):
        # Update the Kivy Image widget with the processed frame
        image_texture = self.load_image(frame)
        self.image_widget.texture = image_texture

    def load_image(self, frame):
        # Convert OpenCV frame to Kivy Texture
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='rgb')
        image_texture.blit_buffer(frame.tobytes(), colorfmt='rgb', bufferfmt='ubyte')
        return image_texture

    def on_leave(self):
        # Stop YOLOv5 detection when leaving the screen
        self.yolov5_detector.capture.release()

    
class YOLOv5Detector:
    def __init__(self, app, camera_box):
        self.app = app
        self.camera_box = camera_box
        self.capture = cv2.VideoCapture(0)  # Change the index if necessary
        Clock.schedule_interval(self.detect, 1.0 / 30)  # Adjust the interval as needed

    def detect(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Perform YOLOv5 detection on the frame (replace this with your YOLOv5 logic)
            # For example, you can use a function like detect_objects(frame) to get the processed frame
            processed_frame = self.detect_objects(frame)

            # Update the Kivy Image widget with the processed frame
            self.app.update_processed_image(processed_frame)

    def detect_objects(self, frame):
        # Replace this with your YOLOv5 detection logic
        # ...
        return frame  # Placeholder


if __name__ == '__main__':
    LabelBase.register(name='ARIAL', fn_regular='ui/fonts/ARIALBD.TTF')
    LabelBase.register(name='ARIAL1', fn_regular='ui/fonts/ARIAL.TTF')
    
    MainApp().run()