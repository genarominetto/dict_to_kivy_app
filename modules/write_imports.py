import os
import ast

def _extract_items(file_path):
    """Extract function names and class names from a Python file."""
    with open(file_path, "r") as source:
        tree = ast.parse(source.read())
    functions = [(node.name, [arg.arg for arg in node.args.args]) 
                 for node in tree.body if isinstance(node, ast.FunctionDef) and not node.name.startswith("_")]
    classes = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    return functions, classes

def write_imports(excluded_directories=[]):
    exclude_by_default = ['.config', 'sample_data']
    excluded_directories += exclude_by_default
    """Generate import statements from Python files in the current directory, excluding specified directories."""
    all_directories = [d for d in os.listdir() if os.path.isdir(d) and d not in excluded_directories]
    import_statements = f"\n# Delete this line to see the new imports\n%%capture\n\n\n\n#@title Import Statements\n#Modules: {all_directories}\n\n\n\n"
    filtered_directories = [x for x in excluded_directories if x not in exclude_by_default]
    
    for directory in all_directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".py"):
                    file_path = os.path.join(root, file)
                    function_defs, class_defs = _extract_items(file_path)
                    
                    for function_name, _ in function_defs:
                        import_path = os.path.splitext(file_path.replace("/", "."))[0]
                        import_statements += f"from {import_path} import {function_name}\n"
                    
                    for class_name in class_defs:
                        import_path = os.path.splitext(file_path.replace("/", "."))[0]
                        import_statements += f"from {import_path} import {class_name}\n"
                    
                    import_statements += "\n"
    import_statements += f'\n\n\n\nprint(write_imports({filtered_directories}))\n\n\n\n'
    return import_statements
