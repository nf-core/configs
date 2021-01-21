# nf-core/configs: Section for Evolutionary Genomics at GLOBE, Univeristy of Copenhagen (hologenomics partition on HPC) Configuration

> **NB:** You will need an account to use the HPC cluster to run the pipeline. If in doubt contact IT.

The profile is configured to run with Singularity version 3.6.3-1.el7 which is part of the OS installtion and does not need to be loaded as a module.

Before running the pipeline you will need to load Java, miniconda and Nextflow. You can do this by including the commands below in your SLURM/sbatch script:

```bash
## Load Java and Nextflow environment modules
module purge
module load lib
module load java/v1.8.0_202-jdk miniconda nextflow/v20.07.1.5412
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
The config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completeed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space.

This configuration will automatically choose the correct SLURM queue (short,medium,long) depending on the time and memory required by each process.

> **NB:** Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be submitted from one of the login nodes.
