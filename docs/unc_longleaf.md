# nf-core/configs: Longleaf High-Performance Computing Cluster, University of North Carolina at Chapel Hill

> **NB:** You will need an [account](https://help.rc.unc.edu/getting-started-on-longleaf/) to use the HPC cluster to run the pipeline.

We have configured the compute clusters to Apptainer (Singularity) loaded by default. Do not load the Singularity module or it will fail, as it is an older version than what's on the compute nodes.

Before running the pipeline you will need to load Nextflow. You can do this by including the commands below in your SLURM/sbatch script:

```bash
## Load Nextflow environment modules
module load nextflow/23.04.2
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory, which will be generated inside the location you ran the nf-core pipeline. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

This configuration will automatically submit jobs to the `general` SLURM queue, where it may automatically be shuffled to different partitions depending on the time required by each process.

```bash
run nextflow nf-core/rnaseq -profile unc_longleaf
```

> **NB:** Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be submitted from one of the login nodes.
