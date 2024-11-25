import os
import json

avail_profiles_path = 'AvailProfiles.json'
airports_dir = 'Airports'

def get_profiles_data():
    profiles_data = []
    for root, dirs, files in os.walk(airports_dir):
        for file in files:
            if file == 'profiles.json':
                with open(os.path.join(root, file)) as f:
                    data = json.load(f)
                    profiles_data.append(data)
    return profiles_data

def update_avail_profiles(profiles_data):
    avail_profiles = []
    for profile in profiles_data:
        entry = {
            "Folder": os.path.basename(os.path.dirname(profile)),
            "ProfileICAO": profile["ProfileICAO"],
            "Scenery": profile["Scenery"],
            "Creator": profile["Creator"],
            "Version": profile["Version"],
            "Files": []
        }
        for root, dirs, files in os.walk(os.path.dirname(profile)):
            for file in files:
                if file.endswith('.ini') or file.endswith('.py'):
                    entry["Files"].append({"Name": file})
        avail_profiles.append(entry)
    return avail_profiles

def main():
    profiles_data = get_profiles_data()
    avail_profiles = update_avail_profiles(profiles_data)
    with open(avail_profiles_path, 'w') as f:
        json.dump(avail_profiles, f, indent=4)

if __name__ == '__main__':
    main()
