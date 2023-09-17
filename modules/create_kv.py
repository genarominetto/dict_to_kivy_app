import os

def create_kv(key_screen, reachable_screens,
              grid_columns=1, button_height=40, 
              title_height=30, color=(1, 0, 0)):

    def lighten_color(c, amount=0.1):
        return min(1, c + amount)

    # Calculate lighter color for the title
    title_color = (lighten_color(color[0]), lighten_color(color[1]), lighten_color(color[2]))

    # Calculate contrast color for the title text
    avg_color = sum(color) / 3.0
    if avg_color > 0.5:
        text_color = (0, 0, 0)  # black
    else:
        text_color = (1, 1, 1)  # white

    # Create the directory if it doesn't exist
    directory = 'kv/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Generate .kv content for the screen
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
            padding: 10
            canvas.before:
                Color:
                    rgb: {title_color[0]}, {title_color[1]}, {title_color[2]}
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: '{key_screen.capitalize()}'
                color: {text_color}
                size_hint_y: None
                height: {title_height}
            GridLayout:
                cols: {grid_columns}
                size_hint_y: None
                height: self.minimum_height
                padding: 10"""

    # Generate buttons for each reachable screen
    buttons = []
    for screen in reachable_screens:
        button = f"""                Button:
                    text: '{screen.capitalize()}'
                    size_hint_y: None
                    height: {button_height}
                    on_press: root.go_to_{screen}()"""
        buttons.append(button)

    # Combine the .kv content and buttons
    full_kv_content = "\n".join([kv_content] + buttons)

    # Write the generated text to the .kv file
    output_file_path = os.path.join(directory, f"{key_screen}.kv")
    with open(output_file_path, 'w') as f:
        f.write(full_kv_content)

    return output_file_path
