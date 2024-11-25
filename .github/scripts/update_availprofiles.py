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
                    profiles_data.append({
                        "Folder": os.path.basename(root),
                        "ProfileICAO": data["ProfileICAO"],
                        "Scenery": data["Scenery"],
                        "Creator": data["Creator"],
                        "Version": data["Version"],
                        "Files": []
                    })
    return profiles_data

def update_avail_profiles(profiles_data):
    for profile in profiles_data:
        profile_folder = os.path.join(airports_dir, profile["Folder"])
        for root, dirs, files in os.walk(profile_folder):
            for file in files:
                if file.endswith('.ini') or file.endswith('.py'):
                    profile["Files"].append({"Name": file})
    return profiles_data

def main():
    profiles_data = get_profiles_data()
    avail_profiles = update_avail_profiles(profiles_data)
    with open(avail_profiles_path, 'w') as f:
        json.dump(avail_profiles, f, indent=4)

if __name__ == '__main__':
    main()
