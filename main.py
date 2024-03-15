from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
class SamrtHome(App):
    def build(self):
        self.window = GridLayout()

        # Set the size of the app window to 360x640 pixels
        Window.size = (360, 640)
        # Create a Label widget with the window size information
        self.size_label = Label(text=f'Window Size: {Window.width}x{Window.height}')

        # set columns as 1
        self.window.cols = 1
        #margin of the widgits
        self.window.size_hint=(0.7, 0.7)
        self.window.pos_hint={"center_x": 0.5 , "center_y": 0.5}

        #add widgets to window
        # image widget
        self.window.add_widget(Image(source="smarthome2.png"))
        #lable widgit
        self.greeting_label = Label(
            text='What is Your Name?',
            font_size=18,
            color='#00FFCE'
        )

        self.window.add_widget(self.greeting_label)

        self.user=TextInput(
                            multiline=False,
                            padding_y= (20,20),
                            size_hint=(1, 0.5)
        )
        self.window.add_widget(self.user)

        self.button= Button(
                            text="GREET",
                            size_hint=(1,0.5),
                            bold=True,
                            background_color='#00FFCE'
        )
        self.window.add_widget(self.button)

        self.button.bind(on_press=self.callback)
        return self.window

    def callback(self, instance):
        self.greeting_label.text= "Welcome " + self.user.text + " to your SMART HOME Application!"



if __name__ == "__main__":
    SamrtHome().run()