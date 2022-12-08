import os
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen,SlideTransition
from kivy import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, 
Permission.READ_EXTERNAL_STORAGE])


class Debug_screen(Screen):

    def print_hi(self):
        print("hi")

    def print_bye(self):
        print("bye")


GUI = Builder.load_string("""
GridLayout:
    cols: 1
    ScreenManager:
        id: screen_manager

        Debug_screen:
            name: "Debug_screen"
            id: Debug_screen


<Debug_screen>:

    GridLayout:
        cols:1
        size: root.width,  root.height

        Button:
            text : "print to console hi"
            on_press : root.print_hi()


        Button:
            text : "print to console bye"
            on_press : root.print_bye()

""")




class ScreenEx(App):


    def build(self):
        return GUI

    def on_start(self, **kwargs):

        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CAMERA, Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


if __name__ == '__main__':
    ScreenEx().run()
