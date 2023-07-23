# Define nested dictionary structure
class AppDetails(dict):
    pass

class UserDetails(dict):
    pass

class DeviceDetails(dict):
    pass

# Transformation function
def transform(ad):
    result = {}
    for username, user_details in ad.items():
        username = "John Doe" if username == "" else username
        result[username] = {}
        for device, device_details in user_details.items():
            device = "Unknown" if device == "" else device
            result[username][device] = {}
            for location, time_used in device_details.items():
                location = "Unknown" if location == "" else location
                if time_used > 10:
                    result[username][device][location] = time_used
    return result

# GraphSearch function
def graph_search(data, keys, level):
    result = {}
    if level == len(keys) - 1:
        for key, value in data.items():
            if not key:
                key = "Unknown"
                result[key] = value
            else:   
                result[key] = value
    else:
        for key, value in data.items():
            
            if not key:
                key = "John Doe" if level==0 else "Unknown"
            result[key] = graph_search(value, keys, level + 1)
    return result



# Test data
ad = AppDetails()
ud = UserDetails()
android_details = DeviceDetails()
android_details["Hyderabad"] = 20
android_details["Mumbai"] = 12
android_details["Chennai"] = 35

mac_details = DeviceDetails()
mac_details["Delhi"] = 30
mac_details["Mumbai"] = 10
mac_details["Hyderabad"] = 17

ud["android"] = android_details
ud["mac"] = mac_details
ad["gaurav.sen"] = ud

unknown_device_details = DeviceDetails()
unknown_device_details["Hyderabad"] = 90
unknown_device_details[""] = 12

unknown_user_details = UserDetails()
unknown_user_details[""] = unknown_device_details

ad[""] = unknown_user_details

import json
# print(transform(ad))
print(json.dumps(transform(ad), indent=4))

keys = ["username", "device", "location"]
# print(graph_search(ad, keys, 0))
print(json.dumps(graph_search(ad, keys, 0), indent=4))
