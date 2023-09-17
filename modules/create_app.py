import os
import shutil
from dict_to_kivy_app.modules.generate_main_py_file import generate_main_py_file
from dict_to_kivy_app.modules.generate_screen_and_kv_files import generate_screen_and_kv_files

def generate_app(screen_dict, folder_name, app_name, compress_and_download=True):
    if not screen_dict:
        raise ValueError("No screens provided. Aborting app generation.")

    all_screens = set(screen_dict.keys())
    for key, screen_data in screen_dict.items():
        reachable_screens = screen_data.get('reachable_screens', [])
        for reachable in reachable_screens:
            if reachable not in all_screens:
                raise ValueError(f"No Screen with name '{reachable}'. Aborting app generation.")

    main_apps_directory = f"{folder_name}/"

    # Delete the app directory if it already exists
    target_app_directory = os.path.join(main_apps_directory, app_name)
    if os.path.exists(target_app_directory):
        shutil.rmtree(target_app_directory)

    # Create the main apps directory if it doesn't exist
    if not os.path.exists(main_apps_directory):
        os.makedirs(main_apps_directory)

    # Generate the individual app
    print(f"Generating app: {app_name}")
    try:
        app_directory = generate_main_py_file(screen_dict, folder_name=app_name)
        if app_directory is not None:
            shutil.move(app_directory, target_app_directory)
    except ValueError as e:
        print(e)

    # If compress_and_download is True, compress the folder and attempt to download
    if compress_and_download:
        shutil.make_archive(main_apps_directory[:-1], 'zip', '.', main_apps_directory[:-1])
        try:
            from google.colab import files
            files.download(f"{main_apps_directory[:-1]}.zip")
        except ModuleNotFoundError:
            print("Note: The folder was compressed, but you're not running this in Google Colab, so automatic downloading did not occur.")
    
    return target_app_directory
