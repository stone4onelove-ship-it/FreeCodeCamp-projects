test_settings = {
    "low": "ball",
    "high": "goggins",
    'gigapotam' : "gtr"
}

def add_setting(set_dict,vsd):
    key = vsd[0].lower()
    value = vsd[1].lower()
    if key in set_dict.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    set_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
def update_setting(set_dict,vsd):
    key = vsd[0].lower()
    value = vsd[1].lower()
    if key in set_dict.keys():
        set_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
def delete_setting(set_dict,vsd):
    key = vsd.lower()
    if key in set_dict.keys():
        del set_dict[key]
        return f"Setting '{key}' deleted successfully!"
    return "Setting not found!"
def view_settings(set_dict):
    if set_dict == {}:
        return "No settings available."
    line = ''
    for key in set_dict:
        line += (key.capitalize() + ": " + set_dict[key]) + '\n'
    final_line = "Current User Settings:\n"+ line
    return final_line
print(view_settings(test_settings))
