from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
from kivy.lang import Builder 

Builder.load_file('08_box.kv')

class MyLayout(Widget):

    pass 

class AwesomeApp(App):
    def build(self):
        # return Label(text="Hello Rittwick", font_size=72)
        return MyLayout()
    
if __name__=='__main__':
    AwesomeApp().run()