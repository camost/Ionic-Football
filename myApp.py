import random

from kivy.app import App
from kivy.uix.modalview import ModalView
from kivy.uix.popup import Popup
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
from kivymd.dialog import MDDialog
from kivymd.slider import MDSlider
from kivymd.spinner import MDSpinner
from kivymd.textfields import MDTextField

from kivymd.theming import ThemeManager

from kivymd.label import MDLabel
from kivymd.button import MDIconButton

from KivyMD.build.lib.kivymd.button import MDRaisedButton

'''
    GridLayout:

        MDLabel:
            text:str(round(progress_slider.value,2 ))

        MDSlider:
            id:progress_slider
            min:0
            max:100
            value: 0
            
    

'''

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
#MDProgressBar:
#value: progress_slider.value




<ScreenOne>:

    AsyncImage:
        source: 'E:\Desarrollo\KivyAPP\P_field2.jpg'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.55}


    MDRaisedButton:
        text: "Back to login"
        elevation_normal: 2
        opposite_colors: True
        on_release: root.manager.current='register'
               
    MDRaisedButton:
        text: "Continue"
        elevation_normal: 2
        pos:260,0
        opposite_colors: True
        on_release: root.manager.current='screen1'


        
<ScreenTwo>:
       

    AsyncImage:
        source: 'E:\Desarrollo\KivyAPP\P_field2.jpg'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.55}
        
    Label:
        id:points
        name:'points'
        text:'[color=#000000]Total Points Available: '+str(points.value)+'[/color]'
        markup:True
        pos: -80,-280
        value:0
    
    MDRaisedButton:
        text: "Continue"
        elevation_normal: 2
        pos:260,0
        opposite_colors: True
        on_release: root.manager.current='screen3'

       
    Button:
        id:arquero_button
        pos: 163, 550
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(arquero.name,arquero.value) 
        
    Label:
        id:arquero
        name:'arquero'
        text:'[color=#000000]Arquero '+str(arquero.value)+'[/color]'
        markup:True
        pos: 0, 220
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 155, 550
            

    
    Button:
        id:def1_button
        pos: 123, 440
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(def1.name,def1.value) 
        
    Label:
        id:def1
        name:'def1'
        text:'[color=#000000]Def '+str(def1.value)+'[/color]'
        markup:True
        pos: -40, 110
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 115, 440
            
    
    
    Button:
        id:def2_button
        pos: 43, 440
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(def2.name,def2.value) 
        
    Label:
        id:def2
        name:'def2'
        text:'[color=#000000]Def '+str(def2.value)+'[/color]'
        markup:True
        pos: -120, 110
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 35, 440
    
    
    Button:
        id:def3_button
        pos: 203, 440
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(def3.name,def3.value) 
        
    Label:
        id:def3
        name:'def3'
        text:'[color=#000000]Def '+str(def3.value)+'[/color]'
        markup:True
        pos: 40, 110
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 195, 440

            
    Button:
        id:def4_button
        pos: 283, 440
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(def4.name,def4.value) 
        
    Label:
        id:def4
        name:'def4'
        text:'[color=#000000]Def '+str(def4.value)+'[/color]'
        markup:True
        pos: 120, 110
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 275, 440
            
    
    
    Button:
        id:med1_button
        pos: 283, 300
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(med1.name,med1.value) 
        
    Label:
        id:med1
        name:'med1'
        text:'[color=#000000]Med '+str(med1.value)+'[/color]'
        markup:True
        pos: 120, -40
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 275, 300
    
    
    
    Button:
        id:med2_button
        pos: 203, 300
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(med2.name,med2.value) 
        
    Label:
        id:med2
        name:'med2'
        text:'[color=#000000]Med '+str(med2.value)+'[/color]'
        markup:True
        pos: 40, -40
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 195, 300

    
    

    Button:
        id:med3_button
        pos: 123, 300
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(med3.name,med3.value) 
        
    Label:
        id:med3
        name:'med3'
        text:'[color=#000000]Med '+str(med3.value)+'[/color]'
        markup:True
        pos: -40, -40
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 115, 300
    



    Button:
        id:med4_button
        pos: 43, 300
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(med4.name,med4.value) 
        
    Label:
        id:med4
        name:'med4'
        text:'[color=#000000]Med '+str(med4.value)+'[/color]'
        markup:True
        pos: -120, -40
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 35, 300



    Button:
        id:ata1_button
        pos: 83, 200
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(ata1.name,ata1.value) 
        
    Label:
        id:ata1
        name:'ata1'
        text:'[color=#000000]Ata '+str(ata1.value)+'[/color]'
        markup:True
        pos: -80, -140
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 75, 200


    Button:
        id:ata2_button
        pos: 243, 200
        size_hint: 0.1, 0.08
        background_color: [0,0,0,0]
        on_release: root.setPlayerValue(ata2.name,ata2.value) 
        
    Label:
        id:ata2
        name:'ata2'
        text:'[color=#000000]Ata '+str(ata2.value)+'[/color]'
        markup:True
        pos: 80, -140
        value:0
    
        Image:
            source: 'E:\Desarrollo\KivyAPP\person.png'
            size: 50, 50
            pos: 235, 200


        
<ScreenThree>:

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(80)
        center_y: self.parent.center_y

        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Barcelona"
            id:Barcelona
            badge_text: "Barcelona"
            on_release: root.teamSelect(self.text)
            
        NavigationDrawerIconButton:
            icon: 'checkbox-blank-circle'
            text: "Real Madrid"
            id:Real_Madrid
            badge_text: "Real Madrid"
            on_release: root.teamSelect(Real_Madrid.text)

        
    Label:
        id:equipoAEnfrentar
        text:'Elija un equipo'
        markup:True
        pos: 0, 200
        color:[3,2,1,1]
            
    MDRaisedButton:
        text: "Continue"
        elevation_normal: 2
        pos:260,0
        opposite_colors: True
        on_release: root.manager.current='screen1'

<Registers>:

    BoxLayout:
        orientation: 'vertical'
        height: dp(100)
        size_hint_y: None
        height: self.minimum_height
        width: 10
        padding: dp(50)
        spacing: 10
        pos_hint: {'center_x': 0.45, 'center_y': 0.85}
        
        MDTextField:
            id: username
            hint_text: "Username"
            helper_text: ""
            helper_text_mode: "on_focus"
        
        MDTextField:
            id: password
            password: True
            hint_text: "Password"
            helper_text: ""
            helper_text_mode: "on_focus"
        
        BoxLayout:
            orientation: 'horizontal'
            spacing: 5
            padding: dp(-40)
            pos_hint: {'center_x': 0.61}
            
           
            MDRaisedButton:
                text: "Login"
                elevation_normal: 2
                opposite_colors: True
                on_release: root.login()
            
            MDRaisedButton:
                text: "Register"
                elevation_normal: 2
                opposite_colors: True
                on_release: root.manager.current='screen1'
                
            MDRaisedButton:
                text: "Close"
                elevation_normal: 2
                opposite_colors: True
                on_release: root.close()
            
    MDRaisedButton:
        text: "Start"
        elevation_normal: 2
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        opposite_colors: True
        on_release: root.manager.current='screen2'
                
                
        

            
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
class ScreenThree(Screen):

    def teamSelect(self,name):
        self.ids.equipoAEnfrentar.text="El equipo a enfrentar es: "+str(name)



class ScreenTwo(Screen):

    def on_pre_enter(self):
        if self.ids.points.value == 0 and self.ids.arquero.value==0 :
            self.ids.points.value =random.randint(400,450)


    def setPlayerValue(self,quien,valor):
        print(quien,valor)
        if (self.ids.points.value)>100:
            sum=30
        elif 100>(self.ids.points.value)>10:
            sum=10
        else:
            sum=1

        if self.ids.points.value>0:
            if quien=="arquero":
                self.ids.arquero.value+=sum
            elif quien=="def1":
                self.ids.def1.value+=sum
            elif quien=="def2":
                self.ids.def2.value+=sum
            elif quien=="def3":
                self.ids.def3.value+=sum
            elif quien=="def4":
                self.ids.def4.value+=sum
            elif quien=="med1":
                self.ids.med1.value+=sum
            elif quien=="med2":
                self.ids.med2.value+=sum
            elif quien=="med3":
                self.ids.med3.value+=sum
            elif quien=="med4":
                self.ids.med4.value+=sum
            elif quien=="ata1":
                self.ids.ata1.value+=sum
            elif quien=="ata2":
                self.ids.ata2.value+=sum

            self.ids.points.value -= sum

        elif self.ids.points.value==0:
            print("Else")

            content = MDLabel(font_style='Body1',halign='center',
                              theme_text_color='Secondary',
                              text="No more points available",
                              size_hint_y=None)
            content.bind(texture_size=content.setter('size'))

            self.dialog = MDDialog(title="Message",
                                   content=content,
                                   size_hint=(.8, None),
                                   height=(200),
                                   auto_dismiss=True)

            self.dialog.add_action_button("Dismiss",
                                          action=lambda *x: self.dialog.dismiss())
            self.dialog.open()

        #quien=str(quien)


        #print(self.ids.quien.value)
        #print(self.ids.arquero.value)

        #val1=int(id.value)
        #valor=int(val1)+1
        #id.value=str(valor)





class Registers(Screen):
    Window.size = (360, 640)
    def login(self):
        username = str(self.ids.username.text)
        password = str(self.ids.password.text)
        content = MDLabel(font_style='Body1',
                          theme_text_color='Secondary',
                          text="This is your password "+password+" That's pretty awesome right?",
                          size_hint_y=None,
                          valign='top')
        content.bind(texture_size=content.setter('size'))
        self.dialog = MDDialog(title="Hola "+username,
                               content=content,
                               size_hint=(.8, None),
                               height=(200),
                               auto_dismiss=False)

        self.dialog.add_action_button("Dismiss",
                                      action=lambda *x: self.dialog.dismiss())
        self.dialog.open()

    def close(instance):
        App.get_running_app().stop()


class ScreenOne(Screen):
    def getValue(self):
        progresBarValue= str(self.ids.progress_slider.value)
        print(round( float(progresBarValue),2) )

    def setPlayerValue(self):
        #playerStat = str(self.ids.progress_slider.value)

        #self.content= MDSpinner()
        #self.content.add_widget()
        #self.content.open()


        self.content=BoxLayout()
        self.progress_slider=MDSlider(min=0,max=100)
        self.content.add_widget(self.progress_slider)

        self.label=MDLabel(text= str(self.progress_slider.value)  )
        self.content.add_widget(self.label)

        self.view = ModalView(auto_dismiss=True,
                         height=(400),
                         width=(300),
                         size_hint=(.8, .5))

        self.content.add_widget(
            MDRaisedButton(text='Accept', opposite_colors=True,
                           on_press=self.view.dismiss,
                           pos=(300, 500)))

        self.view.add_widget(self.content)



        # bind the on_press event of the button to the dismiss function
        self.content.bind(on_press=self.view.dismiss)

        # open the view
        self.view.open(animation=True)

        '''
        self.popup =Popup(     title=" Hola ",title_color=(500, 500, 500, 10),title_align='center',
                               content=self.content,
                               size_hint=(.5, .3),
                               height=(400),
                               width=(300),
                               auto_dismiss=True
                               ,background='white')
                               #,font_color='White')

        self.popup.open()
        

       


        self.dialog = MDDialog(title="Hola",
                               content=content,
                               size_hint=(.5, .3),
                               height=(400),
                               width=(300),
                               auto_dismiss=True,
                               size_hint_y=None )

        self.dialog.add_action_button("Dismiss",action=lambda *x: self.dialog.dismiss())
        #self.dialog.bind(content)
        #self.dialog.add_widget()

     '''








class Manager(ScreenManager):
    screen_one=ObjectProperty(None)
    screen_two = ObjectProperty(None)
    screen_three = ObjectProperty(None)
    register = ObjectProperty(None)

class Estudio1App(App):

    theme_cls = ThemeManager()
    def build(self):
        m=Manager()
        return m

Builder.load_string(code)
janela=Estudio1App()




if __name__ == '__main__':
    janela.run()




    def on_pre_enter(self):

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