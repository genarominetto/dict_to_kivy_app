import os

# Function to generate the main.py file based on the given screens and their attributes
def generate_main_py_file(screen_dict):
    """
    Generates the main.py file based on a given dictionary of screens and their attributes.

    Parameters:
    - screen_dict (dict): A dictionary where the key is the name of the key screen,
                          and the value is another dictionary containing all the data for the screen,
                          including reachable_screens and customization parameters.

    Returns:
    - str: The path to the generated main.py file.
    """
    # Create the directory if it doesn't exist
    directory = 'app/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Initialize parts of the main.py file
    header = """from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
"""

    # Generate KV file loading lines with a preceding comment
    kv_loading_lines = "# Load KV files\n" + "\n".join([f"Builder.load_file('kv/{key}.kv')" for key in screen_dict.keys()])

    # Generate import lines for Python classes
    import_lines = "\n".join([f"from screens.{key} import {key}Screen" for key in screen_dict.keys()])

    # Generate ScreenManager code
    screen_manager_code = """class MainApp(App):

    def build(self):
        sm = ScreenManager(transition=FadeTransition())"""

    # Generate screen addition lines
    screen_addition_lines = []
    for key in screen_dict.keys():
        screen_creation = f"        {key}_screen = {key}Screen(name='{key}')"
        screen_addition = f"        sm.add_widget({key}_screen)"
        screen_addition_lines.extend([screen_creation, screen_addition])
    screen_addition_lines = "\n".join(screen_addition_lines)

    # Add a line to set the current screen (default to the first screen in the dictionary)
    first_screen = list(screen_dict.keys())[0]
    set_current_line = f"        sm.current = '{first_screen}'"

    # Footer
    footer = """        return sm

if __name__ == '__main__':
    MainApp().run()"""

    # Combine all parts to form the full main.py content
    main_py_content = f"{header}\n{kv_loading_lines}\n\n{import_lines}\n\n{screen_manager_code}\n{screen_addition_lines}\n{set_current_line}\n{footer}"

    # Write the generated content to main.py
    output_file_path = os.path.join(directory, 'main.py')
    with open(output_file_path, 'w') as f:
        f.write(main_py_content)

    return output_file_path

# Test the function with the sample dictionary
#generate_main_py_file(sample_dict)
