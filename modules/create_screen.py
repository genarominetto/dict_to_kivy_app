import os
import re

def sanitize_function_name(name):
    """
    Sanitizes the function name by replacing spaces with underscores, making all characters lowercase, and removing all characters that are not letters or numbers.
    """
    sanitized_name = name.replace(' ', '_').lower()
    sanitized_name = re.sub(r'[^a-zA-Z0-9_]', '', sanitized_name)
    return sanitized_name

def create_screen(key_screen, reachable_screens, custom_functions=[], directory='screens/'):
    """
    Generates a Python (.py) file that defines a screen class with methods to navigate to other screens and custom functions.

    Parameters:
    - key_screen (str): The name of the key screen.
    - reachable_screens (list): A list of strings representing the names of screens that can be reached from the key screen.
    - custom_functions (list): A list of strings representing the names of custom functions for the screen.
    - directory (str): The directory in which to save the Python file.

    Returns:
    - str: The path to the generated Python file.
    """

    if not os.path.exists(directory):
        os.makedirs(directory)

    class_definition = f"""from kivy.uix.screenmanager import Screen
"""

    # Add custom function imports
    for func in custom_functions:
        sanitized_func = sanitize_function_name(func)
        class_definition += f"from utils.{key_screen}.{sanitized_func} import {sanitized_func}\n"
    
    class_definition += f"""
class {key_screen}Screen(Screen):
"""

    # Generate methods to navigate to other screens
    methods = []
    for screen in reachable_screens:
        method = f"""    def go_to_{screen}(self):
        print('Navigating from {key_screen} to {screen}')
        self.manager.current = '{screen}'"""
        methods.append(method)

    # Add on_enter method between go_to methods and staticmethods
    on_enter_method = f"""
    def on_enter(self):
        print('{key_screen} screen has fully loaded')"""

    # Generate custom function placeholders
    custom_methods = []
    for func in custom_functions:
        sanitized_func = sanitize_function_name(func)
        custom_method = f"""    {sanitized_func} = staticmethod({sanitized_func})"""
        custom_methods.append(custom_method)

    # Combine the class definition and methods
    full_class_definition = class_definition + "\n".join(methods) + on_enter_method + "\n" + "\n".join(custom_methods)

    # Write to the Python file
    output_file_path = os.path.join(directory, f"{key_screen}.py")
    with open(output_file_path, 'w') as f:
        f.write(full_class_definition)

    return output_file_path
