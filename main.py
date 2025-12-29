from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import NumericProperty


class SplashScreen(MDScreen):
    """Splash screen that displays for 3 seconds before transitioning to main screen"""
    pass


class MainScreen(MDScreen):
    """Main screen with increment button and counter display"""
    counter = NumericProperty(0)
    
    def increment_counter(self):
        """Increment the counter by 1"""
        self.counter += 1


class CounterApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        
        # Create screen manager
        sm = MDScreenManager()
        
        # Add screens
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(MainScreen(name='main'))
        
        # Schedule transition from splash to main after 3 seconds
        Clock.schedule_once(lambda dt: self.switch_to_main(sm), 3)
        
        return sm
    
    def switch_to_main(self, screen_manager):
        """Switch from splash screen to main screen"""
        screen_manager.current = 'main'


if __name__ == '__main__':
    CounterApp().run()
