from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 

Builder.load_file('14_updating_labels.kv')

class MyLayout(Widget):

    def press(self):
        # Create variables for out widgets 
        name = self.ids.name_input.text 
        
        # Update the label 
        self.ids.name_label.text = f"Hello, {name}!"

        # Clear the input box 
        self.ids.name_input.text = ''

class AwesomeApp(App):
    def build(self):
        return MyLayout()
    
if __name__=='__main__':
    AwesomeApp().run()