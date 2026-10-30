# add_setting_function
def add_setting(settings, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


# update_setting_function
def update_setting(settings, key_value_pair):
    key = key_value_pair[0].lower()
    value = key_value_pair[1].lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# delete_setting_function
def delete_setting(settings, key):
    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


# view_settings_function
def view_settings(settings):
    if not settings:
        return "No settings available."

    result = "Current User Settings:"

    for key, value in settings.items():
        result += f"\n{key.capitalize()}: {value}"

    result += "\n"

    return result


# Test dictionary
test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}