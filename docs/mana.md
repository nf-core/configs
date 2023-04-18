# nf-core/configs Mana (at University of Hawaii at Manoa) Configuration

To use, run the pipeline with `-profile mana`. It will use the following parameters for Mana (UHM HPCC):

- Load singularity and use it as default container technology
- Setup a container cache directory in your home (~/.singularity_images_cache)
- Select appropriate queues (currently: `shared,exclusive,kill-shared,kill-exclusive`)
- Set the maximum available resources (available in 09/02/2022):
  - CPUs: 96
  - Memory: 400.GB
  - Time: 72.h

## Pre-requisites

In order to run a nf-core pipeline on Mana, you will need to setup nextflow in your environment.
At the moment, nextflow is not available as a module (but might be in the future).

### Install nextflow in a conda environment

Before we start, we will need to work on an interactive node (currently, mana doesn't let you execute any program in the login node):

```bash
# Request an interactive sandbox node for 30 min
srun --pty -t 30 -p sandbox /bin/bash
```

To setup nextflow on your account, follow these steps.

```bash
# Load the latest anaconda3 module
module load lang/Anaconda3/2022.05

# Initialize environment
. $(conda info --base)/etc/profile.d/conda.sh

# Install nextflow (here in base environment, but you can create a new one if you'd like)
conda install -c bioconda nextflow
```

If you want these settings to be persistent, you can add the first 2 commands in your .bash_profile file like this:

```bash
echo "module load lang/Anaconda3/2022.05" >> ~/.bash_profile
echo "$(conda info --base)/etc/profile.d/conda.sh" >> ~/.bash_profile
```
