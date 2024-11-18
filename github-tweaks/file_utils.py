import json

# Function to save data to a JSON file
def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Function to load data from a JSON file
def load_json(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Function to save the list of users not following back
def save_not_following_back(filename, not_following_back):
    with open(filename, 'w') as out_file:
        if not_following_back:
            out_file.write("\n".join(not_following_back))
        else:
            out_file.write("Everyone you're following is also following you back.")
