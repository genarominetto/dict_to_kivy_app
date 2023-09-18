import os
import re
import importlib

def create_main(screen_dict, title_height, transition='FadeTransition'):
    directory = 'app/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    header = f"""from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, {transition}
"""

    kv_loading_lines = "# Load KV files\n" + "\n".join([f"Builder.load_file('kv/{key}.kv')" for key in screen_dict.keys()])

    import_lines = "\n".join([f"from screens.{key} import {key}Screen" for key in screen_dict.keys()])

    # Generate import statements for custom utility functions
    import_code = """try:
    import importlib
except ImportError:
    pass  # Handle ImportError if necessary"""

    import_statements = [
        f"    importlib.import_module('utils.{screen_name}.{function_name}')"
        for screen_name, attributes in screen_dict.items()
        for function_name in attributes.get('functions', [])
    ]
    import_code += "\n" + "\n".join(import_statements)

    screen_manager_code = f"""class MainApp(App):

    def build(self):
        sm = ScreenManager(transition={transition}())"""

    screen_addition_lines = []
    for key in screen_dict.keys():
        screen_creation = f"        {key}_screen = {key}Screen(name='{key}')"
        screen_addition = f"        sm.add_widget({key}_screen)"
        screen_addition_lines.extend([screen_creation, screen_addition])
    screen_addition_lines = "\n".join(screen_addition_lines)

    first_screen = list(screen_dict.keys())[0]
    set_current_line = f"        sm.current = '{first_screen}'"

    footer = """        return sm

if __name__ == '__main__':
    MainApp().run()"""

    # Combine all the parts to form the full main.py content
    main_py_content = f"{header}\n{kv_loading_lines}\n\n{import_lines}\n\n{import_code}\n\n{screen_manager_code}\n{screen_addition_lines}\n{set_current_line}\n{footer}"

    output_file_path = os.path.join(directory, 'main.py')
    with open(output_file_path, 'w') as f:
        f.write(main_py_content)

    return output_file_path
