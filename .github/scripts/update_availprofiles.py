import os
import json
import logging

avail_profiles_path = 'AvailProfiles.json'
airports_dir = 'Airports'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_existing_profiles():
    if os.path.exists(avail_profiles_path):
        try:
            with open(avail_profiles_path, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error reading {avail_profiles_path}: {e}")
    return []

def update_profiles_data(existing_profiles, new_profile):
    for profile in existing_profiles:
        if profile["Folder"] == new_profile["Folder"]:
            profile.update(new_profile)
            return
    existing_profiles.append(new_profile)

def get_profiles_data(existing_profiles):
    profiles_data = existing_profiles.copy()
    for root, dirs, files in os.walk(airports_dir):
        logging.info(f"Scanning directory: {root}")
        for file_name in files:
            if file_name == 'profile.json':
                profile_path = os.path.join(root, file_name)
                logging.info(f"Found profile.json at: {profile_path}")
                try:
                    with open(profile_path) as f:
                        data = json.load(f)
                        configurations = data.get("Configurations", [])
                        file_names = set()
                        for config in configurations:
                            for file in config.get("Files", []):
                                if "FileName" in file:
                                    file_names.add(file["FileName"])
                        new_profile = {
                            "Folder": os.path.basename(root),
                            "ProfileICAO": data.get("ProfileICAO", ""),
                            "Scenery": data.get("Scenery", ""),
                            "Creator": data.get("Creator", ""),
                            "Version": str(data.get("Version", "0")),
                            "FileNames": list(file_names)
                        }
                        update_profiles_data(profiles_data, new_profile)
                except (IOError, json.JSONDecodeError) as e:
                    logging.error(f"Error reading {profile_path}: {e}")
    return profiles_data

def main():
    logging.info("Starting profile update process.")
    existing_profiles = load_existing_profiles()
    profiles_data = get_profiles_data(existing_profiles)
    if not profiles_data:
        logging.warning("No profile.json files found.")
        print("No profile.json files found.")
    else:
        try:
            with open(avail_profiles_path, 'w') as f:
                json.dump(profiles_data, f, indent=4)
            logging.info("AvailProfiles.json has been updated.")
            print("AvailProfiles.json has been updated.")
        except Exception as e:
            logging.error(f"Error writing to {avail_profiles_path}: {e}")

if __name__ == '__main__':
    main()
