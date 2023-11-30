from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
import arabic_reshaper
from bidi.algorithm import get_display
from kivy.uix.label import Label

Window.size = (400, 600)

class MainApp(MDApp):
    
    def build(self):
       
        screen_manager = ScreenManager()   
        screen_manager.add_widget(Builder.load_file('main.kv'))
        screen_manager.add_widget(Builder.load_file('page1.kv'))
        screen_manager.add_widget(Builder.load_file('page2.kv'))
        screen_manager.add_widget(Builder.load_file('page3.kv'))
        screen_manager.add_widget(Builder.load_file('page4.kv'))
        # Add other screens here
        
        # Access the Label widget using ids
        
        
        return screen_manager

if __name__ == '__main__':
    LabelBase.register(name='Roboto', fn_regular='C:\\Users\\User\\OneDrive\\Bureau\\python\\font\\Roboto-Bold.ttf')
    LabelBase.register(name='Roboto1', fn_regular='C:\\Users\\User\\OneDrive\\Bureau\\python\\font\\Roboto-Light.ttf')
    
    
    
    MainApp().run()
