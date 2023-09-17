import os
import shutil

import shutil

def generate_multiple_apps(app_dicts, apps_folder_name="apps"):
    """
    Generates a complete Kivy apps structure based on a list of dictionaries of screens and their attributes.
    The apps will have the following folder structure:

    - apps_folder_name/
        - app1/
            - main.py
            - screens/
                - *.py
            - kv/
                - *.kv
        - app2/
            ...

    Parameters:
    - app_dicts (list): A list of dictionaries, where each dictionary is similar to the `screen_dict` parameter
                        in `generate_complete_app` function.
    - apps_folder_name (str): The name of the main folder that will contain all individual app folders.

    Returns:
    - str: The path to the generated apps folder.
    """
    # Delete the main apps directory if it already exists
    if os.path.exists(apps_folder_name):
        shutil.rmtree(apps_folder_name)

    # Create the main apps directory
    main_apps_directory = f"{apps_folder_name}/"
    os.makedirs(main_apps_directory)

    # Generate each individual app
    for i, app_dict in enumerate(app_dicts):
        app_name = f"app{i + 1}"
        print(f"Generating app: {app_name}")
        try:
            app_directory = generate_complete_app(app_dict, folder_name=app_name)
            if app_directory is not None:
                shutil.move(app_directory, os.path.join(main_apps_directory, app_name))
        except ValueError as e:
            print(e)

    # Compress the main apps directory for easy downloading
    shutil.make_archive(apps_folder_name, 'zip', '.', apps_folder_name)

    # Download the compressed folder (specific to Google Colab)
    try:
        from google.colab import files
        files.download(f"{apps_folder_name}.zip")
    except ModuleNotFoundError:
        print("Note: The folder was compressed, but you're not running this in Google Colab, so automatic downloading did not occur.")

    return main_apps_directory