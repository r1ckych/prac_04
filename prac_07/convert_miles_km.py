
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConverterApp(App):

    message = StringProperty()

    def build(self):
         self.title = "Convert Miles to Kilometres"
         self.root = Builder.load_file('convert_miles_km.kv')
         return self.root

    def handle_calculate(self):
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = self.message


ConverterApp().run()
