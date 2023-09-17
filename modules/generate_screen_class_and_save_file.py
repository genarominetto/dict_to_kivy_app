import os

# Update the function to avoid capitalizing the left part of the screen class name in the .py file
def generate_screen_class_and_save_file(key_screen, reachable_screens, directory='screens/'):
    """
    Generates a Python (.py) file that defines a screen class with methods to navigate to other screens.

    Parameters:
    - key_screen (str): The name of the key screen.
    - reachable_screens (list): A list of strings representing the names of screens that can be reached from the key screen.
    - directory (str): The directory in which to save the Python file.

    Returns:
    - str: The path to the generated Python file.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate the class definition without capitalizing the left part of the screen class name
    class_definition = f"""from kivy.uix.screenmanager import Screen

class {key_screen}Screen(Screen):
"""

    # Generate methods to navigate to other screens
    methods = []
    for screen in reachable_screens:
        method = f"""    def go_to_{screen}(self):
        print('Navigating from Screen {key_screen} to Screen {screen}')
        self.manager.current = '{screen}'"""
        methods.append(method)

    # Combine the class definition and methods
    full_class_definition = class_definition + "\n".join(methods)

    # Write the generated text to the Python file
    output_file_path = os.path.join(directory, f"{key_screen}.py")
    with open(output_file_path, 'w') as f:
        f.write(full_class_definition)

    return output_file_path