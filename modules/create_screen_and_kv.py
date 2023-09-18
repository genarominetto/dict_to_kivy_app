import os
from dict_to_kivy_app.modules.create_screen import create_screen
from dict_to_kivy_app.modules.create_kv import create_kv

def create_screen_and_kv(screen_dict, title_height, button_height):
    generated_py_files = []
    generated_kv_files = []

    py_specific_params = set()
    kv_specific_params = {'grid_color', 'scroll_color', 'grid_columns', 'button_height',
                          'button_text_prefix', 'padding', 'title_height', 'scroll_x',
                          'grid_height', 'size_hint_y', 'color'}

    py_directory = 'app/screens/'
    kv_directory = 'app/kv/'
    if not os.path.exists(py_directory):
        os.makedirs(py_directory)
    if not os.path.exists(kv_directory):
        os.makedirs(kv_directory)

    for key_screen, attributes in screen_dict.items():
        reachable_screens = attributes.get('reachable_screens', [])
        custom_functions = attributes.get('custom_functions', [])
        py_custom_params = {k: v for k, v in attributes.items() if k in py_specific_params}
        kv_custom_params = {k: v for k, v in attributes.items() if k in kv_specific_params}

        py_file_path = create_screen(key_screen, reachable_screens, custom_functions, directory=py_directory, **py_custom_params)
        generated_py_files.append(py_file_path)

        kv_custom_params['title_height'] = title_height
        kv_custom_params['button_height'] = button_height
        kv_file_path = create_kv(key_screen, reachable_screens, custom_functions, **kv_custom_params)
        generated_kv_files.append(kv_file_path)

    return generated_py_files, generated_kv_files
