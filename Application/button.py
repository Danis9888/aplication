from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config



class Container(BoxLayout):
    def click(self, instance):
        if instance.text == "Выход":
            quit()

class BoxApp(App):
    def build(self):
        Window.size = (360, 360 / 9 * 15)
        return Container()


if __name__ == "__main__":
    BoxApp().run()