from app.app import App
from menu.menu import Menu
from utils.utils import Utils

Utils.clear()

menu = Menu()

menu.show_welcome()

mode = menu.get_mode_selection()
hints = menu.get_hints_enabled()
duration = menu.get_duration()

app = App(mode == 1 or mode == 3,
          mode == 2 or mode == 3,
          hints,
          duration)
app.run()
