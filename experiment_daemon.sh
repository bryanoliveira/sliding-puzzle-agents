#!/bin/bash
#!/bin/bash


while true; do
  # Check if there are any scripts in the "experiments/to_run" folder
  if [ -n "$(ls -A experiments/to_run)" ]; then
    # Get the first script in the "experiments/to_run" folder
    script=$(ls experiments/to_run | head -n 1)

    # Print the script name
    echo "---- Running $script"

    # Execute the script
    source "experiments/to_run/$script"

    # Move the executed script to "experiments/executed" folder
    echo "---- Moving $script"
    mv "experiments/to_run/$script" "experiments/executed/$script"
  else
    # If there are no scripts in the "experiments/to_run" folder, print current timestamp and sleep
    date
    sleep 10
  fi
done
