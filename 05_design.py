import kivy 
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout # FloatLayout, BoxLayout, AnchorLayout, StackLayout, RelativeLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    # no need to pass instance in case of when you are using design file
    # def press(self, instance):
    def press(self):
        name = self.name.text 
        pizza = self.pizza.text 
        color = self.color.text 

        print(f"Hello {name}, you like {pizza} pizza and your favorite color is {color}!")
        # print this to the screen 
        # self.add_widget(Label(text=f"Hello {name}, you like {pizza} pizza and your favorite color is {color}!"))
        
        # Clear the input boxes 
        self.name.text = ''
        self.pizza.text = ''
        self.color.text = ''


# if the class name is MyApp then the design file name is my.kv 
# if the class name is Elder then the design file name is elder.kv 
class MyApp(App):
    def build(self):
        # return Label(text="Hello Rittwick", font_size=72)
        return MyGridLayout()
    
if __name__=='__main__':
    MyApp().run()