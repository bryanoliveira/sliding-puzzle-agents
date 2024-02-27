#!/bin/bash


while true; do
  # Check if there are any scripts in the "experiments/to_run" folder
  if [ -n "$(ls -A experiments/to_run)" ]; then
    # Get the first script in the "experiments/to_run" folder
    script=$(ls experiments/to_run | head -n 1)

    # Move the executing script to "experiments/running" folder
    echo "---- Moving $script to queued"
    mv "experiments/to_run/$script" "experiments/queued/$script"
    echo "---- Queued $script"

    # Check if there is at least 30% of RAM available
    ram_usage=$(free | awk '/Mem/{printf("%.2f"), $3/$2*100}')
    # Check if there is at least 30% of VRAM available
    vram_usage=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n 1)

    while true; do
      if (( $(echo "$ram_usage < 70" | bc -l) )) && (( $(echo "$vram_usage < 20000" | bc -l) )); then
        # If there is enough RAM available, break the loop and continue with the execution
        echo "---- Running $script"
        break
      else
        # If there is not enough RAM available, print current timestamp and sleep
        echo "---- Waiting. RAM usage: $ram_usage% / VRAM usage: $vram_usage MB"
        date
        sleep 180

        ram_usage=$(free | awk '/Mem/{printf("%.2f"), $3/$2*100}')
        vram_usage=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -n 1)
      fi
    done

    # Move the executing script to "experiments/running" folder
    echo "---- Moving $script to running"
    mv "experiments/queued/$script" "experiments/running/$script"

    # Execute the script
    source "experiments/running/$script"

    # Move the executed script to "experiments/executed" folder
    echo "---- Moving $script to executed"
    mv "experiments/running/$script" "experiments/executed/$script"
  else
    # If there are no scripts in the "experiments/to_run" folder, print current timestamp and sleep
    echo "---- No scripts to run"
    date
    sleep 10
  fi
done
