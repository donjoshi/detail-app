import kivy

from kivy.config import Config
Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
from kivy import platform
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics.vertex_instructions import Line
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Rectangle, Ellipse,Quad
from kivy.properties import Clock
from kivy.properties import NumericProperty

class childApp(GridLayout):
    
    def __init__(self, **kwargs):
        super(childApp,self).__init__(**kwargs)
        self.cols=2
        self.add_widget(Label(text='Student Name'))
        self.s_name=TextInput(multiline=False)
        self.add_widget(self.s_name)
        
        self.add_widget(Label(text='Student Marks'))
        self.s_marks=TextInput(multiline=False)
        self.add_widget(self.s_marks)
        
        self.add_widget(Label(text='Student Gender'))
        self.s_gender=TextInput(multiline=False)
        self.add_widget(self.s_gender)
        
        self.press=Button(text='Submit')
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        
    def click_me(self,instance):
        print("Name:",self.s_name.text)
        print("Marks:",self.s_marks.text)
        print("Gender:",self.s_gender.text)
        print("")
        
class parentApp(App):
    def build(self):
        return childApp()
    
if __name__=='__main__':
    parentApp().run()
    
    
    