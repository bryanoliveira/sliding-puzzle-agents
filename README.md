# Sliding Puzzle Agents

- Create a conda environment: `conda env create -f environment.yml`
- Install the puzzle environment:
    - `git clone https://github.com/bryanoliveira/sliding-puzzle-env`
    - `cd sliding-puzzle-env`
    - `pip install -e .`
    - [Download the datasets](https://drive.google.com/file/d/1iqhTiMJysTC-i-Gu9XdnL1z8jLl5y62-/view?usp=sharing) and extract the imgs folder
- Run as many experiment daemons your computer can handle: `bash experiments/daemon.sh`

Notes

- If RAM usage is too high, reduce the number of envs per worker in `configs/ray.yaml`
- By default the daemon triggers a training job only if there is at least 50% of RAM and VRAM available. To increase this limit you may set the `MAX_RAM` and `MAX_VRAM` variables: `MAX_RAM=0.6 MAX_VRAM=0.8 bash experiments/daemon.sh`
