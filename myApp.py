from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
from kivy.clock import Clock
from kivy.graphics import Color
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.properties import ObjectProperty


code = """ 
<ScreenOne>:
       
    Button:
        text: "Screen 2"
        size: 55, 55
        size_hint: None, None #
        on_press:root.manager.current='screen2'
        
        
<ScreenTwo>:
    Button:
        text: "Screen 3"
        size: 55, 55
        size_hint: None, None #
        on_press:root.manager.current='screen3'
        
<ScreenThree>:
    Button:
        text: "Screen 1"
        size: 55, 55
        size_hint: None, None #
        on_press:root.manager.current='screen1'

<Registers>:




        
<Manager>:

    id: screen_manager
    screen_one:screen_one
    screen_two:screen_two
    screen_three:screen_three
    login:login

    
    Registers:
        id:login
        name:'register'
        manager:screen_manager


    ScreenOne:
        id:screen_one
        name:'screen1'
        manager:screen_manager

    ScreenTwo:
        id:screen_two
        name:'screen2'
        manager:screen_manager

    ScreenThree:
        id:screen_three
        name:'screen3'
        manager:screen_manager
"""

'''
    name:'registers'
    container: container
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Return to Login'
            on_press: root.manager.current = 'screen1'
        Button:
            text: 'Next Screen'
            on_press: root.manager.current = 'screen2'
        BoxLayout:
            id: container
            orientation: 'vertical'
            
            
            Label:
            markup: True
            text: '[b] Type something... [/b]'
            halign: 'center'
            valign: 'middle'
        
'''


class Registers(Screen):
    def on_pre_enter(self):
        def login(instance):
            username = str(self.username.text)
            label2 = Label(text="Hola " + username)
            self.inside.add_widget(label2)

        def close(instance):
            App.get_running_app().stop()


        Window.size = (360, 640)
        self.inside = GridLayout(rows=5,row_force_default=True, row_default_height=35)  # Create a new grid layout
        #self.inside.cols = 5
        #self.inside.rows = 5

        self.inside.add_widget(Label(text="Username: "))
        self.username = TextInput(multiline=False,halign= "center",padding=10)
        self.inside.add_widget(self.username)

        self.inside.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False,halign= "center",padding=10)
        self.inside.add_widget(self.password)

        self.inside.add_widget(BoxLayout())


        # Agrego botones

        # Agrego Login Button
        self.loginButton = Button(text="Login", font_size=20)
        # Doy funcion al login button
        self.loginButton.bind(on_press=login)

        # Agrego register button
        self.registerButton= Button(text="Register", font_size=20)

        # Agrego close Button
        self.closeButton = Button(text="Close", font_size=20)
        # Doy funcion al close button
        self.closeButton.bind(on_press=close)


        self.inside.add_widget(self.loginButton)
        self.inside.add_widget(self.registerButton)
        self.inside.add_widget(self.closeButton)

        self.add_widget(self.inside)




        #self.add_widget(self.button)



class ScreenOne(Screen):
    pass

class ScreenTwo(Screen):
    pass

class ScreenThree(Screen):
    pass


class Manager(ScreenManager):
    screen_one=ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    register = ObjectProperty(None)

class Estudio1App(App):

    def build(self):
        m=Manager(transition=WipeTransition())
        return m

Builder.load_string(code)
janela=Estudio1App()




if __name__ == '__main__':
    janela.run()

