import os
import shutil
from collections import deque
from dict_to_kivy_app.modules.create_main import create_main
from dict_to_kivy_app.modules.create_screen_and_kv import create_screen_and_kv
from dict_to_kivy_app.modules.create_utils import create_utils  # Import create_utils

def _bfs_is_reachable(start, graph):
    visited = set()
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        visited.add(current)
        
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
                
    return visited

def _validate_reachability(screen_dict):
    all_screens = set(screen_dict.keys())
    graph = {}
    
    for screen, attributes in screen_dict.items():
        graph[screen] = attributes.get('reachable_screens', [])
    
    for start_screen in all_screens:
        reachable_screens = _bfs_is_reachable(start_screen, graph)
        
        if reachable_screens != all_screens:
            missing_screens = all_screens - reachable_screens
            example_missing_screen = next(iter(missing_screens), None)  # Get the first missing screen as an example
            raise ValueError(f"Screen '{start_screen}' cannot reach screen '{example_missing_screen}'. Aborting app generation.")

def create_app(screen_dict, folder_name, app_name, title_height, transition='FadeTransition',
               compress_and_download=True, button_height=100, navigation_columns=1):

    # Validate screen dictionary
    if not screen_dict:
        raise ValueError("No screens provided. Aborting app generation.")
    
    _validate_reachability(screen_dict)  # New validation step

    # Create main directory if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Create or recreate the specific app directory
    target_app_directory = os.path.join(folder_name, app_name)
    if os.path.exists(target_app_directory):
        shutil.rmtree(target_app_directory)
    os.makedirs(target_app_directory)

    # Create utils directory and function files
    screen_functions = {k: v.get('custom_functions', []) for k, v in screen_dict.items()}
    create_utils(screen_functions, target_app_directory)

    # Generate main.py file
    main_py_file_path = create_main(screen_dict, title_height, transition)
    shutil.move(main_py_file_path, os.path.join(target_app_directory, 'main.py'))

    # Generate screen and kv files
    py_files, kv_files = create_screen_and_kv(screen_dict, title_height, button_height, navigation_columns)  # Passed navigation_columns

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


