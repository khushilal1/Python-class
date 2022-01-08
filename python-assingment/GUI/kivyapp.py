from typing import Text
from kivyapp import App
from kivy.uix.label import label

class Demoapp(App):
    def build(self):
        return label(
            Text="hello"
        )
    
if __name__=="__main__":
    app=Demoapp()
    app.run()

