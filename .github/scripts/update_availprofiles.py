import os
import json
import logging

avail_profiles_path = 'AvailProfiles.json'
airports_dir = 'Airports'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_airports():
    if os.path.exists(avail_profiles_path):
        with open(avail_profiles_path) as f:
            data = json.load(f)
    else:
        data = []

    existing_profiles = {profile["Folder"]: profile for profile in data}
    updated_profiles = []

    for root, dirs, _ in os.walk(airports_dir):
        for dir_name in dirs:
            profile_path = os.path.join(root, dir_name)
            logging.info(f"Processing {dir_name}")

            if dir_name in existing_profiles:
                profile = existing_profiles[dir_name]
                logging.info(f"Updating existing profile for {dir_name}")
            else:
                profile = {"Folder": dir_name}
                logging.info(f"Creating new profile for {dir_name}")

            with open(profile_path + '/profile.json', 'r') as profile_file:
                profile_data = json.load(profile_file)
                profile["ProfileICAO"] = profile_data["ProfileICAO"]
                profile["Scenery"] = profile_data["Scenery"]
                profile["Creator"] = profile_data["Creator"]
                profile["Version"] = str(profile_data["Version"])
                profile["FileNames"] = profile.get("FileNames", [])

                # Check for missing files in profile_path
                for file_name in profile["FileNames"]:
                    file_path = os.path.join(profile_path, file_name)
                    if not os.path.exists(file_path):
                        logging.warning(f"File {file_name} does not exist in {profile_path}. Removing it.")
                        profile["FileNames"].remove(file_name)

                # Add missing files to profile
                for file_name in os.listdir(profile_path):
                    if file_name.endswith('.ini') or file_name.endswith('.py'):
                        if file_name not in profile["FileNames"]:
                            logging.warning(f"File {file_name} does not exist in {avail_profiles_path}. Adding it.")
                            profile["FileNames"].append(file_name)

            updated_profiles.append(profile)

    # Write the updated profiles
    with open(avail_profiles_path, 'w') as f:
        json.dump(updated_profiles, f, indent=4)

get_airports()
