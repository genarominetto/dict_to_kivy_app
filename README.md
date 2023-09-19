# Converting Dictionary to Kivy App.

Create Kivy applications with multiple interconnected screens in less then one minute. All you need to do is define the `app_structure` as a Python dictionary and execute the function `create_app`. Includes a `main.ipynb` notebook for demonstration purposes.

To use the program **click on** the **'Open in Colab'** button and execute all cells.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GenaroHacker/dict_to_kivy_app/blob/main/main.ipynb)

## 📌 Table of Contents

1. [📥 Input](#-input)
2. [📤 Output](#-output)
3. [🛠 Modules](#-modules)
4. [📱 Screen Properties](#-screen-properties)
5. [🔧 Parameters](#-parameters)





## 📥 Input

- **Define App Structure Dictionary:**
```python
app_structure = {
    'home': {
        'reachable_screens': ['settings', 'profile', 'cart'],
        'custom_functions': ['Browse Products', 'Search', 'View Promotions', 'Recommendations'],
        'grid_columns': 2,
        'color': (0.9, 0.5, 0),
    },
      ...
}
```

- **Function to Create and Download App:**
```python
create_app(
    screen_dict=app_structure,
    folder_name="example_apps",
    app_name="SampleApp",
    title_height=100,
    button_height=50,
    navigation_columns=3,
    transition='SwapTransition',
    compress_and_download=True
)

```

## 📤 Output


A fully functional Kivy program with multiple screens created with the `create_app` function:



![screens](https://github.com/GenaroHacker/dict_to_kivy_app/assets/95663273/c960b88e-080e-4827-b3af-c29928954284)


![app](https://github.com/GenaroHacker/dict_to_kivy_app/assets/95663273/c3822619-aff6-43fd-80b4-37dca0eb09d7)


**Note**: Each button corresponding to `custom_functions` in the `app_structure` dictionary is linked to a Python function in a file located in the `utils` folder. For example, if you have 'Sign Out' as one of your `custom_functions`, there will be a Python file in the `utils` folder containing a function like this:




```python
def sign_out():
	print("Sign Out")
```


An example of the generated file structure:



![files](https://github.com/GenaroHacker/dict_to_kivy_app/assets/95663273/b9179e8b-7584-4e6b-92b4-58b6bc2272d1)





## 🛠 Modules

The following are available:

- `create_app`: Create the complete Kivy application.
- `create_main`: Create the main execution script for the app.
- `create_screen`: Create individual screens for the Kivy application.
- `create_kv`: Create `.kv` files that holds the application's style and layout.
- `create_screen_and_kv`: Create both the screen and `.kv` files simultaneously.
- `create_utils`: Create utility methods for the `custom_functions`.





## 📱 Screen Properties

For each screen in the `app_structure` dictionary, you can define the following properties:

- `reachable_screens`: A list of screens that can be navigated to.
- `custom_functions`: A list of buttons, each of which prints a string when pressed.
- `grid_columns`: Number of columns in the layout.
- `color`: Background color.


## 🔧 Parameters

For the `create_app` function, you can define the following parameters:

- `screen_dict`: Previously defined dictionary with the app's structure.
- `folder_name`: Name of the folder where the created files will reside.
- `app_name`: Name of the created Kivy application.
- `title_height`: Height of the title bar in the app.
- `button_height`: Height of the buttons in the app.
- `navigation_columns`: Number of columns for navigation buttons.
- `transition`: The type of screen transition to use.
- `compress_and_download`: Whether to compress and download the created app.


To use the program **click on** the **'Open in Colab'** button and execute all cells.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/GenaroHacker/dict_to_kivy_app/blob/main/main.ipynb)

Contributions or suggestions are more than welcome.

