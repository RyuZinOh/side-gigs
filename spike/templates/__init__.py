import os

def get_template_content(file_name, folder_name=None):
    """
    Returns the content of a template file based on the file name and folder name.
    This function will load the template files from the 'templates' directory, which contains the
    HTML, CSS, and JS templates.
    """
    # Define the base path for templates
    templates_folder = os.path.dirname(__file__)  # Get the directory of __init__.py
    
    # If folder_name is provided (for css/ or scripts/), we still don't need it
    # because all templates are stored directly in 'templates/'
    template_path = os.path.join(templates_folder, f"{file_name}.txt")
    
    # Read and return the template content
    try:
        with open(template_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Template file '{file_name}.txt' not found in the 'templates/' directory.")
