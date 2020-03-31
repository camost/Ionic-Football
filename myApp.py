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
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.bubble import Bubble
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivymd.snackbar import Snackbar
from kivymd.textfields import MDTextField

from kivymd.theming import ThemeManager

from kivymd.label import MDLabel
from kivymd.button import MDIconButton



code = """ 

#:import MDTextField kivymd.textfields.MDTextField
#:import Toolbar kivymd.toolbar.Toolbar
#:import ThemeManager kivymd.theming.ThemeManager
#:import MDNavigationDrawer kivymd.navigationdrawer.MDNavigationDrawer
#:import NavigationLayout kivymd.navigationdrawer.NavigationLayout
#:import NavigationDrawerDivider kivymd.navigationdrawer.NavigationDrawerDivider
#:import NavigationDrawerToolbar kivymd.navigationdrawer.NavigationDrawerToolbar
#:import NavigationDrawerSubheader kivymd.navigationdrawer.NavigationDrawerSubheader
#:import MDCheckbox kivymd.selectioncontrols.MDCheckbox
#:import MDSwitch kivymd.selectioncontrols.MDSwitch
#:import MDList kivymd.list.MDList
#:import OneLineListItem kivymd.list.OneLineListItem
#:import TwoLineListItem kivymd.list.TwoLineListItem
#:import ThreeLineListItem kivymd.list.ThreeLineListItem
#:import OneLineAvatarListItem kivymd.list.OneLineAvatarListItem
#:import OneLineIconListItem kivymd.list.OneLineIconListItem
#:import OneLineAvatarIconListItem kivymd.list.OneLineAvatarIconListItem
#:import MDTextField kivymd.textfields.MDTextField
#:import MDSpinner kivymd.spinner.MDSpinner
#:import MDCard kivymd.card.MDCard
#:import MDSeparator kivymd.card.MDSeparator
#:import MDDropdownMenu kivymd.menu.MDDropdownMenu
#:import get_color_from_hex kivy.utils.get_color_from_hex
#:import colors kivymd.color_definitions.colors
#:import SmartTile kivymd.grid.SmartTile
#:import MDSlider kivymd.slider.MDSlider
#:import MDTabbedPanel kivymd.tabs.MDTabbedPanel
#:import MDTab kivymd.tabs.MDTab
#:import MDProgressBar kivymd.progressbar.MDProgressBar
#:import MDAccordion kivymd.accordion.MDAccordion
#:import MDAccordionItem kivymd.accordion.MDAccordionItem
#:import MDAccordionSubItem kivymd.accordion.MDAccordionSubItem
#:import MDThemePicker kivymd.theme_picker.MDThemePicker
#:import MDBottomNavigation kivymd.tabs.MDBottomNavigation
#:import MDBottomNavigationItem kivymd.tabs.MDBottomNavigationItem


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
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
        padding: dp(50)
        spacing: 10
        pos_hint: {'center_x': 0.45, 'center_y': 0.9}
            
        MDTextField:
            id: username
            hint_text: "Username"
            helper_text: ""
            helper_text_mode: "on_focus"
        
        MDTextField:
            id: password
            hint_text: "Password"
            helper_text: ""
            helper_text_mode: "on_focus"
        BoxLayout:
            orientation: 'horizontal'
            spacing: 5
        
            MDRaisedButton:
                text: "Login"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
                on_release: app.login()
            
            MDRaisedButton:
                text: "Register"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                on_release: app.register()
                
            MDRaisedButton:
                text: "Close"
                elevation_normal: 2
                opposite_colors: True
                pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                on_release: app.close()
        


            
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
    def login(self):
        username = str(self.username.text)
        label2 = Label(text="Hola " + username)
        self.inside.add_widget(label2)

    def on_pre_enter(self):

        def close(instance):
            App.get_running_app().stop()


        Window.size = (360, 640)
        '''
        self.inside = GridLayout(rows=10,row_force_default=True, row_default_height=35)  # Create a new grid layout
        #self.inside.cols = 5
        #self.inside.rows = 5

        self.inside.add_widget(MDLabel(text="Username: "))
        self.username = MDTextField(multiline=False,halign= "center",padding=5)
        self.inside.add_widget(self.username)

        self.inside.add_widget(MDLabel(text="Password: "))
        self.password = MDTextField(multiline=False,halign= "center",padding=5)
        self.inside.add_widget(self.password)

        self.inside.add_widget(BoxLayout())


        # Agrego botones

        # Agrego Login Button
        #self.loginButton = Button(text="Login", font_size=20)
        # Doy funcion al login button
        #self.loginButton.bind(on_press=login)

        # Agrego register button
        #self.registerButton= Button(text="Register", font_size=20)

        # Agrego close Button
        #self.closeButton = Button(text="Close", font_size=20)
        # Doy funcion al close button
        #self.closeButton.bind(on_press=close)


        #self.inside.add_widget(self.loginButton)
        #self.inside.add_widget(self.registerButton)
        #self.inside.add_widget(self.closeButton)

        self.add_widget(self.inside)




        #self.add_widget(self.button)
        '''


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

    def login(self):
        username = str(self.username.text)
        label2 = Label(text="Hola " + username)
        self.inside.add_widget(label2)






    theme_cls = ThemeManager()
    def build(self):
        m=Manager(transition=WipeTransition())
        return m

Builder.load_string(code)
janela=Estudio1App()




if __name__ == '__main__':
    janela.run()

