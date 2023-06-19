# nf-core/configs: Academic Leiden Interdisciplinary Cluster Environment (ALICE), Leiden University Configuration

> **NB:** You will need an [account](https://wiki.alice.universiteitleiden.nl/index.php?title=Getting_an_account) to use the HPC cluster to run the pipeline.

The profile is configured to run with Singularity version 3.6.1-Go-1.14 and needs to be loaded as a module.

Before running the pipeline you will need to load Java and Nextflow. You can do this by including the commands below in your SLURM/sbatch script:

```bash
## Load Java and Nextflow environment modules
module load Singularity/3.6.1-Go-1.14
module load Nextflow/21.03.0
module load Java/11.0.2
```

We also highly recommend specifying a location of a cache directory to store singularity images (so you re-use them across runs, and not pull each time), by specifying the location with the `$NXF_SINGULARITY_CACHE_DIR` bash environment variable in your `.bash_profile` or `.bashrc`.

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
The config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completeed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space.

This configuration will automatically choose the correct SLURM queue (short,medium,long) depending on the time required by each process. If there are
high memory requirements (>240GB), e.g. using MALT, use the 'mem' profile:

```bash
run nextflow nf-core/eager -p alice,mem
```

> **NB:** Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be submitted from one of the login nodes.
