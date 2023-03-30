from kivy.app import App 
# from kivy.uix.widget import Widget 
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder 

Builder.load_file("34_tabs.kv") 

class MyLayout(TabbedPanel):
    pass 


class AwesomeApp(App):
    def build(self):
        return MyLayout() 
    

if __name__=='__main__':
    AwesomeApp().run() 