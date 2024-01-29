import os
import yaml

def update_config(folder_path):
    """
    Update the configuration file in the given folder.

    Args:
    folder_path (str): Path to the folder containing the config file.
    """
    config_file_path = os.path.join(folder_path, "configs.yaml")

    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)

    edited = False
    if config.get("env_image_folder") == "./imgs/imagenet-1k/val_images":
        config["env_image_folder"] = "./imgs/imagenet-1k"
        edited = True

    if config.get("env_image_folder") == "./imgs/mnist/trainingSet":
        config["env_image_folder"] = "./imgs/mnist"
        edited = True

    if edited:
        with open(config_file_path, 'w') as file:
            yaml.dump(config, file)

def main():
    base_folder = "./runs"

    # Scan for experiment folders
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)
        
        # Check if it's a directory
        if os.path.isdir(folder_path):
            update_config(folder_path)
            print(f"Updated config in {folder_path}")

if __name__ == "__main__":
    main()
