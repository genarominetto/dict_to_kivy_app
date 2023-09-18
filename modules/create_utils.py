import os
import re

def create_utils(screen_functions, target_app_directory):
    # Create utils directory if it doesn't exist
    directory = os.path.join(target_app_directory, 'utils')
    if not os.path.exists(directory):
        os.makedirs(directory)

    for screen_name, custom_functions in screen_functions.items():
        # Only create folders for screens with at least one custom function
        if custom_functions:
            screen_directory = os.path.join(directory, screen_name)
            if not os.path.exists(screen_directory):
                os.makedirs(screen_directory)
            
            for function_text in custom_functions:
                sanitized_function_name = re.sub(r'[^a-zA-Z0-9_]', '', function_text.replace(' ', '_')).lower()
                function_path = os.path.join(screen_directory, f"{sanitized_function_name}.py")

                with open(function_path, 'w') as f:
                    f.write(f"""def {sanitized_function_name}():\n\tprint("{function_text}")""")

