#!/bin/bash

# Path to the base directory containing experiment folders
base_folder="./runs"

# Loop through each subfolder in the base directory
for folder in "$base_folder"/*/; do
    # Check if model.zip exists in the folder
    if [ ! -f "${folder}model.zip" ]; then
        echo "Deleting ${folder} as it does not contain model.zip"
        rm -rf "${folder}"
    fi
done
