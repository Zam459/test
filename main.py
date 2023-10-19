from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar

KV = """
Screen:

    MDTopAppBar:
        title: "My first app"
        elevation: 10
        md_bg_color: app.theme_cls.primary_color
        left_action_items: [["menu", lambda x: x]]
        pos_hint: {"top": 1}

    MDRaisedButton:
        text: "Hello World"
        pos_hint: {"center_x": .5, "center_y": .5}
"""

class HelloWorld(MDApp):
    
	def on_start(self):
	# Код, выполняемый после инициализации приложения (перед взаимодействием с Android API)
		pass

	def build(self):
		return Builder.load_string(KV)

	def on_pause(self):
		return True  # Приложение не должно закрыться при приостановке

	def on_resume(self):
	# Код для восстановления работы приложения
		pass

	def on_stop(self):
	# Код, выполняемый при завершении работы приложения (не используется на Android)
		pass

if __name__ == "__main__":
    HelloWorld().run()
