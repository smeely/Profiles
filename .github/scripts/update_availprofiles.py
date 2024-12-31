import os
import json

avail_profiles_path = 'AvailProfiles.json'
airports_dir = 'Airports'

def get_profiles_data():
    profiles_data = []
    for root, dirs, files in os.walk(airports_dir):
        for file_name in files:
            if file_name == 'profile.json':
                profile_path = os.path.join(root, file_name)
                with open(profile_path) as f:
                    data = json.load(f)
                    configurations = data.get("Configurations", [])
                    file_names = set()
                    for config in configurations:
                        for file in config.get("Files", []):
                            if "FileName" in file:
                                file_names.add(file["FileName"])
                    profiles_data.append({
                        "Folder": os.path.basename(root),
                        "ProfileICAO": data.get("ProfileICAO", ""),
                        "Scenery": data.get("Scenery", ""),
                        "Creator": data.get("Creator", ""),
                        "Version": str(data.get("Version", "0")),
                        "FileNames": list(file_names)
                    })
    return profiles_data

def main():
    profiles_data = get_profiles_data()
    if not profiles_data:
        print("No profile.json files found.")
    else:
        with open(avail_profiles_path, 'w') as f:
            json.dump(profiles_data, f, indent=4)
        print("AvailProfiles.json has been updated.")

if __name__ == '__main__':
    main()
