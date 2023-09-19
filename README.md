# Dict to Kivy App

Generate Kivy applications with multiple screens by defining the app's structure in a Python **dictionary**. Includes a `main.ipynb` notebook for demonstration.

To use the program **click on** the **main.ipynb** file, then click on the **'Open in Colab'** button, and finally execute all cells.


![open](https://github.com/GenaroHacker/dict_to_kivy_app/assets/95663273/d716fcb5-08f8-4ee7-bffa-312c2270dde1)



## 📌 Table of Contents

1. [⚙️ Input and Output](#️-input-and-output)
2. [🛠 Modules](#-modules)
3. [🖥 Screen Properties](#-screen-properties)
4. [🔧 Parameters](#-parameters)




## ⚙️ Input and Output

### 📥 Input

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
```

- **Generate App Function:**
```python
# Generate a single app
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

### 📤 Output

A fully functional Kivy program with multiple screens.

Example of generated screens from the `dict_to_kivy_app` package:


![screens](https://github.com/GenaroHacker/dict_to_kivy_app/assets/95663273/c960b88e-080e-4827-b3af-c29928954284)

An example of the generated file structure:



![files](https://github.com/GenaroHacker/dict_to_kivy_app/assets/95663273/b9179e8b-7584-4e6b-92b4-58b6bc2272d1)


## 🛠 Modules

The following are available:

- `create_app`: Generate the complete Kivy application.
- `create_main`: Generate the main execution script for the app.
- `create_screen`: Create individual screens for the Kivy application.
- `create_kv`: Create `.kv` files that holds the application's style and layout.
- `create_screen_and_kv`: Generate both the screen and `.kv` files simultaneously.
- `create_utils`: Create utility methods for the `custom_functions`.





## 🖥 Screen Properties

For each screen in the `app_structure` dictionary, you can define the following properties:

- `reachable_screens`: A list of screens that can be navigated to.
- `custom_functions`: Each button prints a string when pressed
- `grid_columns`: Number of columns in the layout.
- `color`: Background color.


## 🔧 Parameters

For the `create_app` function, you can define the following parameters:

- `screen_dict`: Previously defined dictionary with the app's structure.
- `folder_name`: Name of the folder where the generated files will reside.
- `app_name`: Name of the generated Kivy application.
- `title_height`: Height of the title bar in the app.
- `button_height`: Height of the buttons in the app.
- `navigation_columns`: Number of columns for navigation buttons.
- `transition`: The type of screen transition to use.
- `compress_and_download`: Whether to compress and download the generated app.


To use the program **click on** the **main.ipynb** file, then click on the **'Open in Colab'** button, and finally execute all cells.
