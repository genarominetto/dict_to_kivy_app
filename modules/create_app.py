import os
import shutil
from dict_to_kivy_app.modules.create_main import create_main
from dict_to_kivy_app.modules.create_screen_and_kv import create_screen_and_kv

def create_app(screen_dict, folder_name, app_name, compress_and_download=True):
    """
    Generates a single Kivy app structure based on a given dictionary of screens and their attributes.
    
    Parameters:
    - screen_dict (dict): A dictionary where the key is the name of the screen, 
                          and the value is another dictionary containing all the data for the screen.
    - folder_name (str): The name of the main folder for the apps.
    - app_name (str): The name of the individual app folder.
    - compress_and_download (bool): Whether to compress the generated app folder and download it. 
                                    True by default.

    Returns:
    - str: The path to the generated app folder.
    """
    
    # Validate screen dictionary
    if not screen_dict:
        raise ValueError("No screens provided. Aborting app generation.")

    all_screens = set(screen_dict.keys())
    for key, screen_data in screen_dict.items():
        reachable_screens = screen_data.get('reachable_screens', [])
        for reachable in reachable_screens:
            if reachable not in all_screens:
                raise ValueError(f"No Screen with name '{reachable}'. Aborting app generation.")

    # Create main directory if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create or recreate the specific app directory
    target_app_directory = os.path.join(folder_name, app_name)
    if os.path.exists(target_app_directory):
        shutil.rmtree(target_app_directory)
    os.makedirs(target_app_directory)

    # Generate main.py file
    main_py_file_path = create_main(screen_dict)
    shutil.move(main_py_file_path, os.path.join(target_app_directory, 'main.py'))

    # Generate screen and kv files
    py_files, kv_files = generate_screen_and_kv_files(screen_dict)

    # Move the generated files to the target directory
    for file_path in py_files + kv_files:
        file_name = os.path.basename(file_path)
        sub_folder = os.path.basename(os.path.dirname(file_path))
        target_sub_directory = os.path.join(target_app_directory, sub_folder)
        if not os.path.exists(target_sub_directory):
            os.makedirs(target_sub_directory)
        shutil.move(file_path, os.path.join(target_sub_directory, file_name))
        
    # If compress_and_download is True, compress the folder and attempt to download
    if compress_and_download:
        shutil.make_archive(folder_name, 'zip', '.', folder_name)
        try:
            from google.colab import files
            files.download(f"{folder_name}.zip")
        except ModuleNotFoundError:
            print("Note: The folder was compressed, but you're not running this in Google Colab, so automatic downloading did not occur.")
    
    return target_app_directory
