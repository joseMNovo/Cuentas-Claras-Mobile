import kivy
kivy.require('2.1.0')
from kivy.utils import platform
from kivy.lang import Builder
from kivymd.app import MDApp 
from kivy.uix.screenmanager import ScreenManager 
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton  
from kivy.core.window import Window
from kivymd.uix.responsivelayout import MDResponsiveLayout

Window.fullscreen = 'auto'

""" if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE]) """


class WindowManager(ScreenManager):
    pass

class FirstWindow(MDScreen):
    pass

class SecondWindow(MDScreen):
    pass


class MainApp(MDApp, MDResponsiveLayout):
    dialog = None

    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Orange"
        self.mobile_view = WindowManager()
        self.mobile_view = FirstWindow()
        self.mobile_view = SecondWindow()


    def close_dialog(self, obj):
        self.dialog.dismiss()


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Error",
                text="Debe escribir un numero",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release = self.close_dialog
                    ),
                ],
            )
        self.dialog.open()


    def limpiar(self):
        self.root.ids.sueldo1.text = ""
        self.root.ids.sueldo2.text = ""
        self.root.ids.totalapagar.text = ""
        self.root.ids.resultado1.text = ""
        self.root.ids.resultado2.text = ""
       

    def calcular(self):  # sourcery skip: extract-method
        sueldo1 = self.root.ids.sueldo1.text
        sueldo2 = self.root.ids.sueldo2.text
        totalapagar = self.root.ids.totalapagar.text          

        if sueldo1.isnumeric() and sueldo2.isnumeric() and totalapagar.isnumeric():
            sueldo1 = int(self.root.ids.sueldo1.text)
            sueldo2 = int(self.root.ids.sueldo2.text)
            totalapagar = int(self.root.ids.totalapagar.text)

            sumaSueldos = sueldo1 + sueldo2

            #calculoPrimerPorcentaje = (sueldo1 * 100) / sumaSueldos
            primerPortentaje = (sueldo1 * 100) / sumaSueldos

            #calculoSegundoPorcentaje = (sueldo2 * 100) / sumaSueldos
            segundoPorcentaje = (sueldo2 * 100) / sumaSueldos

            # Calculo a pagar
            primerPago =round(((totalapagar * primerPortentaje) / 100),2)
            segundoPago =round(((totalapagar * segundoPorcentaje) / 100),2)

            self.root.ids.resultado1.text = str(f"Sueldo 1 -> {primerPago}")
            self.root.ids.resultado2.text = str(f"Sueldo 2 -> {segundoPago}")

        else:
            self.show_alert_dialog()
            self.limpiar()

    def build(self):
        Window.size
        return Builder.load_file('main.kv')


def main():
    MainApp().run()


if __name__ == '__main__':
    main()
