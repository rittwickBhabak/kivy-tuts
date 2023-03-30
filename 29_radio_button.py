from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 

Builder.load_file("29_radio_button.kv") 

class MyLayout(Widget):
    def checkbox_click(self, instance, value, topping):
        if value:
            self.ids.output_label.text = f"You selected {topping}" 
        else:
            self.ids.output_label.text = "Please select one topping."



class AwesomeApp(App):
    def build(self):
        return MyLayout() 
    

if __name__=='__main__':
    AwesomeApp().run() 