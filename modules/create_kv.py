import os
import re

def create_kv(key_screen, reachable_screens, custom_functions,
              navigation_columns,
              grid_columns=1, button_height=100,
              title_height=30, color=(1, 0, 0)):

    def adjust_color(c, amount=0.1):
        return min(1, max(0, c + amount))

    avg_color = sum(color) / 3.0
    adjust_amount = 0.1 if avg_color > 0.5 else -0.1
    title_color = (adjust_color(color[0], adjust_amount), 
                   adjust_color(color[1], adjust_amount), 
                   adjust_color(color[2], adjust_amount))

    text_color = (0, 0, 0) if avg_color > 0.5 else (1, 1, 1)

    directory = 'kv/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    kv_content = f"""<{key_screen.capitalize()}Screen>:
    ScrollView:
        canvas.before:
            Color:
                rgb: {color[0]}, {color[1]}, {color[2]}
            Rectangle:
                pos: self.pos
                size: self.size
        do_scroll_x: False
        GridLayout:
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            padding: 30
            spacing: 30
            Label:
                text: '{key_screen.capitalize()}'
                color: {text_color}
                canvas.before:
                    Color:
                        rgb: {title_color[0]}, {title_color[1]}, {title_color[2]}
                    Rectangle:
                        pos: self.pos
                        size: self.size
                size_hint_y: None
                height: {title_height}
            GridLayout:
                cols: {navigation_columns}
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 10
                canvas.before:
                    Color:
                        rgb: 0.5, 0.5, 0.5
                    Rectangle:
                        pos: self.pos
                        size: self.size"""

    buttons = []
    for screen in reachable_screens:
        button = f"""                Button:
                    text: '{screen.capitalize()}'
                    size_hint_y: None
                    height: {button_height}
                    on_press: root.go_to_{screen}()"""
        buttons.append(button)

    custom_functions_grid = f"""            GridLayout:
                cols: {grid_columns}
                size_hint_y: None
                height: self.minimum_height
                padding: 10
                spacing: 10
                canvas.before:
                    Color:
                        rgb: {title_color[0]}, {title_color[1]}, {title_color[2]}
                    Rectangle:
                        pos: self.pos
                        size: self.size"""

    custom_function_buttons = []
    for function_text in custom_functions:
        function_name = re.sub('[^0-9a-zA-Z_]', '', function_text.replace(' ', '_')).lower()
        custom_button = f"""                Button:
                    text: '{function_text}'
                    size_hint_y: None
                    height: {button_height}
                    on_press: root.{function_name}()"""
        custom_function_buttons.append(custom_button)

    full_kv_content = "\n".join([kv_content] + buttons + [custom_functions_grid] + custom_function_buttons)

    output_file_path = os.path.join(directory, f"{key_screen}.kv")
    with open(output_file_path, 'w') as f:
        f.write(full_kv_content)

    return output_file_path
