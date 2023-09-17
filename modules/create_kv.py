import os

# Function to generate Kivy (.kv) file content for a screen
def create_kv(key_screen, reachable_screens,
                                      grid_color=(0, 0, 1), scroll_color=(1, 0, 0), grid_columns=1,
                                      button_height=40, button_text_prefix='Go to Screen ', padding=10,
                                      box_layout_height=30, scroll_x=False, grid_height='self.minimum_height',
                                      size_hint_y=None, directory='kv/'):
    """
    Generates a Kivy (.kv) file that defines the layout and elements of a screen.

    Parameters:
    - key_screen (str): The name of the key screen.
    - reachable_screens (list): A list of strings representing the names of screens that can be reached from the key screen.
    - grid_color (tuple): The RGB color of the grid.
    - scroll_color (tuple): The RGB color of the scroll view.
    - grid_columns (int): The number of columns in the grid.
    - button_height (int): The height of the buttons.
    - button_text_prefix (str): The prefix to be added before the screen name on buttons.
    - padding (int): The padding around the grid.
    - box_layout_height (int): The height of the box layout.
    - scroll_x (bool): Whether to enable horizontal scrolling.
    - grid_height (str): The height expression for the grid.
    - size_hint_y (str): The size hint for the y-axis.
    - directory (str): The directory in which to save the .kv file.

    Returns:
    - str: The path to the generated .kv file.
    """
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate .kv content for the screen
    kv_content = f"""<{key_screen.capitalize()}Screen>:
    ScrollView:
        canvas.before:
            Color:
                rgb: {scroll_color[0]}, {scroll_color[1]}, {scroll_color[2]}
            Rectangle:
                pos: self.pos
                size: self.size
        do_scroll_x: {str(scroll_x)}
        GridLayout:
            cols: {grid_columns}
            size_hint_y: {size_hint_y}
            height: {grid_height}
            padding: {padding}
            canvas.before:
                Color:
                    rgb: {grid_color[0]}, {grid_color[1]}, {grid_color[2]}
                Rectangle:
                    pos: self.pos
                    size: self.size
            BoxLayout:
                size_hint_y: None
                height: {box_layout_height}
"""

    # Generate buttons for each reachable screen
    buttons = []
    for screen in reachable_screens:
        button = f"""            Button:
                text: '{button_text_prefix}{screen.capitalize()}'
                size_hint_y: None
                height: {button_height}
                on_press: root.go_to_{screen}()"""
        buttons.append(button)

    # Combine the .kv content and buttons
    full_kv_content = kv_content + "\n".join(buttons)

    # Write the generated text to the .kv file
    output_file_path = os.path.join(directory, f"{key_screen}.kv")
    with open(output_file_path, 'w') as f:
        f.write(full_kv_content)

    return output_file_path

# Test the function
#generate_kv_content_and_save_file("a", ["b"])
