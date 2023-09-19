# Dict to Kivy App 🚀

Generate Kivy applications with multiple screens by simply defining the app's structure in a Python dictionary. Includes a `main.ipynb` notebook for demonstration. 📚✨

## 📌 Table of Contents

1. [📘 Description](#-description)
2. [⚙️ Input and Output](#️-input-and-output)
3. [🖥 Screen Properties](#-screen-properties)
4. [🌟 Features](#-features)
5. [🔧 Parameters](#-parameters)

## 📘 Description

The `dict_to_kivy_app` package allows you to focus solely on defining your app's structure while taking care of the tedious boilerplate code required to create a Kivy app. 🛠🌈

_An example of a generated screen from the `dict_to_kivy_app` package._ 🎨✨

## ⚙️ Input and Output

### 📥 Input

- **Import Required Modules:**
```python
from dict_to_kivy_app.modules.create_screen import create_screen
# ... other imports
```

- **Define App Structure:**
```python
app_structure = {
# ... structure details
}
```

- **Generate App:**
```python
create_app(
# ... parameters
)
```

### 📤 Output

A fully functional Kivy program with multiple screens and more! 🌟🖥

_An example of the generated file structure._ 🗃🌈

## 🖥 Screen Properties

For each screen in the `app_structure` dictionary, you can define the following properties: 🎛✨

- `reachable_screens`: A list of screens that can be navigated to. 🚀
- `custom_functions`: A list of custom functions or features. 🎨
- `grid_columns`: Number of columns in the layout. 📊
- `color`: Background color. 🎨

## 🌟 Features

- `create_screen`, `create_utils`, `create_app` and many more! 🛠✨

## 🔧 Parameters

- `screen_dict`, `folder_name`, `app_name` and other customization parameters! 🎛🌈

Enjoy crafting your Kivy apps! 💎✨
