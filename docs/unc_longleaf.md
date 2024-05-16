# nf-core/configs: Longleaf High-Performance Computing Cluster, University of North Carolina at Chapel Hill

> **NB:** You will need an [account](https://help.rc.unc.edu/getting-started-on-longleaf/) to use the HPC cluster to run the pipeline.

Before running the pipeline you will need to load Nextflow and Apptainer. You can do this by including the commands below in your SLURM/sbatch script:

```bash
## Load Nextflow environment modules
module load nextflow/23.04.2;
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory, which will be generated inside the location you ran the nf-core pipeline. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway. You can also specify the working directory using the Nextflow [`-w` or `-work-dir` option](https://www.nextflow.io/docs/latest/cli.html#run).

This configuration will automatically submit jobs to the `general` SLURM queue, where it may automatically be shuffled to different partitions depending on the time required by each process.

```bash
run nextflow nf-core/rnaseq -profile unc_longleaf
```

> **NB:** Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be submitted from one of the login nodes.
