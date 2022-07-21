from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
import hashily

Window.size = (375, 667)

class MainApp(MDApp):
    cont = 0
    cont1 = 0
    def build(self):
        screen_manager = ScreenManager()

        screen_manager.add_widget(Builder.load_file("m.kv"))
        screen_manager.add_widget(Builder.load_file("en.kv"))
        screen_manager.add_widget(Builder.load_file("de.kv"))
        return screen_manager

    def encrROT13(self):
        data_to_encrypt = self.root.get_screen('main').ids.user.text
        text = hashily.ROT13.encode(data_to_encrypt)
        self.root.get_screen('main').ids.textt.text = text

    def encrBacon(self):
        data_to_encrypt = self.root.get_screen('main').ids.user.text
        text = hashily.Bacon.encode(data_to_encrypt)
        self.root.get_screen('main').ids.textt.text = text

    def encrCaesar(self):
        data_to_encrypt = self.root.get_screen('main').ids.user.text
        text = hashily.Caesar.encode(data_to_encrypt)
        self.root.get_screen('main').ids.textt.text = text

    def encrAtBash(self):
        data_to_encrypt = self.root.get_screen('main').ids.user.text
        text = hashily.AtBash.encode(data_to_encrypt)
        self.root.get_screen('main').ids.textt.text =text

    def decyROT13(self):
        data_to_decrypt = self.root.get_screen('main').ids.user.text
        self.root.get_screen('main').ids.textt.text =  hashily.ROT13.decode(data_to_decrypt)


    def decyCaesar(self):
        data_to_decrypt = self.root.get_screen('main').ids.user.text
        self.root.get_screen('main').ids.textt.text = hashily.Caesar.decode(data_to_decrypt)

    def decyAtBash(self):
        data_to_decrypt = self.root.get_screen('main').ids.user.text
        self.root.get_screen('main').ids.textt.text =  hashily.AtBash.decode(data_to_decrypt)

    def decyBacon(self):
        data_to_decrypt = self.root.get_screen('main').ids.user.text
        self.root.get_screen('main').ids.textt.text = hashily.Bacon.decode(data_to_decrypt)

MainApp().run()
