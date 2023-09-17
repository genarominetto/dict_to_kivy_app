import os
from dict_to_kivy_app.modules.generate_screen_class_and_save_file import generate_screen_class_and_save_file
from dict_to_kivy_app.modules.generate_kv_content_and_save_file import generate_kv_content_and_save_file

# Function to generate both Python (.py) and Kivy (.kv) files based on a given dictionary of screens and their attributes
def generate_screen_and_kv_files(screen_dict):
    """
    Generates both Python (.py) and Kivy (.kv) files based on a given dictionary of screens and their attributes.
    The Python files are stored in a 'screens/' directory and the .kv files in a 'kv/' directory.

    Parameters:
    - screen_dict (dict): A dictionary where the key is the name of the key screen,
                          and the value is another dictionary containing all the data for the screen,
                          including reachable_screens and customization parameters.

    Returns:
    - list: A list of paths to the generated Python and .kv files.
    """
    # Create lists to store the paths to the generated files
    generated_py_files = []
    generated_kv_files = []

    # Define parameters specific to Python and .kv files
    py_specific_params = set()
    kv_specific_params = {'grid_color', 'scroll_color', 'grid_columns', 'button_height',
                          'button_text_prefix', 'padding', 'box_layout_height', 'scroll_x',
                          'grid_height', 'size_hint_y'}

    # Create the directories if they don't exist
    py_directory = 'app/screens/'
    kv_directory = 'app/kv/'
    if not os.path.exists(py_directory):
        os.makedirs(py_directory)
    if not os.path.exists(kv_directory):
        os.makedirs(kv_directory)

    # Iterate over each key_screen in the dictionary
    for key_screen, attributes in screen_dict.items():

        # Extract reachable_screens and customization parameters from the attributes dictionary
        reachable_screens = attributes.get('reachable_screens', [])
        py_custom_params = {k: v for k, v in attributes.items() if k in py_specific_params}
        kv_custom_params = {k: v for k, v in attributes.items() if k in kv_specific_params}

        # Generate the Python (.py) file using the existing function
        py_file_path = generate_screen_class_and_save_file(key_screen, reachable_screens, directory=py_directory, **py_custom_params)
        generated_py_files.append(py_file_path)

        # Generate the .kv file using the existing function
        kv_file_path = generate_kv_content_and_save_file(key_screen, reachable_screens, directory=kv_directory, **kv_custom_params)
        generated_kv_files.append(kv_file_path)

    return generated_py_files, generated_kv_files

# Test the function with the sample dictionary
#generate_screen_and_kv_files(sample_dict)
