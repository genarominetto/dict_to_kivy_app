import os
import shutil

def generate_complete_app(screen_dict, folder_name):
    """
    Generates a complete Kivy app structure based on a given dictionary of screens and their attributes.
    The app will have the following folder structure:

    - folder_name/
        - main.py
        - screens/
            - *.py
        - kv/
            - *.kv

    Parameters:
    - screen_dict (dict): A dictionary where the key is the name of the key screen,
                          and the value is another dictionary containing all the data for the screen,
                          including reachable_screens and customization parameters.
    - folder_name (str): The name of the main folder for the app.

    Returns:
    - str: The path to the generated app folder.
    """
    # Check for empty screen dictionary and missing screens
    if not screen_dict:
        raise ValueError("No screens provided. Aborting app generation.")

    all_screens = set(screen_dict.keys())
    for key, screen_data in screen_dict.items():
        reachable_screens = screen_data.get('reachable_screens', [])
        for reachable in reachable_screens:
            if reachable not in all_screens:
                raise ValueError(f"No Screen with name '{reachable}'. Aborting app generation.")

    # Create the main directory if it doesn't exist
    main_directory = f"{folder_name}/"
    if not os.path.exists(main_directory):
        os.makedirs(main_directory)

    # Generate the main.py file inside the main directory
    main_py_file_path = generate_main_py_file(screen_dict)
    if main_py_file_path:
        shutil.move(main_py_file_path, os.path.join(main_directory, 'main.py'))

    # Generate the Python (.py) and Kivy (.kv) files inside 'screens/' and 'kv/' folders
    py_files, kv_files = generate_screen_and_kv_files(screen_dict)

    # Move generated Python (.py) and Kivy (.kv) files to the main directory
    for file_path in py_files + kv_files:
        file_name = os.path.basename(file_path)
        sub_folder = os.path.basename(os.path.dirname(file_path))
        target_directory = os.path.join(main_directory, sub_folder)
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)
        shutil.move(file_path, os.path.join(target_directory, file_name))

    return main_directory