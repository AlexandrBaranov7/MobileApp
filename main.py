from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.app import App


class MainApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, MApp!", halign="center")


MainApp().run()