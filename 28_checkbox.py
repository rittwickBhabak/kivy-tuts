from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.lang import Builder 

Builder.load_file("28_checkbox.kv") 

class MyLayout(Widget):
    toppings = []
    def checkbox_click(self, instance, value, topping):
        if value:
            self.toppings.append(topping)
            self.ids.output_label.text = f"You selected {', '.join(self.toppings)}" 
        else:
            if topping in self.toppings:
                self.toppings.remove(topping) 
            if len(self.toppings)==0:
                self.ids.output_label.text = "Please select some toppings."
            else:
                self.ids.output_label.text = f"You selected {', '.join(self.toppings)}"


class AwesomeApp(App):
    def build(self):
        return MyLayout() 
    

if __name__=='__main__':
    AwesomeApp().run() 