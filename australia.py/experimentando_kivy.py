from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def on_press(btn):
    btn.text = 'click'

def on_release(btn):
    btn.text = ''

class Meuapp(App):
    def build(self):
        main = BoxLayout()
        painel = BoxLayout(orientation='vertical')
        aside = BoxLayout()
        area_butao = BoxLayout()

        area_butao.add_widget(Button(on_press=on_press, on_release=on_release, size_hint=(0.8, 0.8)))
        painel.add_widget(area_butao)

        painel.add_widget(Label(text='teste2', size_hint=(0.2,0.2)))

        aside.add_widget(Label(text='teste', size_hint=(0.1,1)))

        main.add_widget(painel)
        main.add_widget(aside)
        return main

Meuapp().run()