import os

def sanitize_function_name(text):
    return ''.join(c.lower() for c in text if c.isalnum() or c == '_').replace(' ', '_')

def create_utils(screen_functions, target_app_directory):
    utils_dir = os.path.join(target_app_directory, 'utils')
    if not os.path.exists(utils_dir):
        os.makedirs(utils_dir)

    for screen_name, functions in screen_functions.items():
        screen_utils_dir = os.path.join(utils_dir, screen_name)
        if not os.path.exists(screen_utils_dir):
            os.makedirs(screen_utils_dir)

        for function_text in functions:
            function_name = sanitize_function_name(function_text)
            with open(os.path.join(screen_utils_dir, f"{function_name}.py"), 'w') as f:
                f.write(f"def {function_name}():\n")
                f.write(f"    print('{function_text}')\n")
