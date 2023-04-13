# nf-core/configs: KU Leuven/UHasselt Tier-2 High Performance Computing Infrastructure (VSC)

> **NB:** You will need an [account](https://docs.vscentrum.be/en/latest/access/getting_access.html#required-steps-to-get-access) to use the HPC cluster to run the pipeline.

First you should go to the cluster you want to run the pipeline on. You can check what clusters have the most free space using following command `sinfo --cluster wice|genius`.

Before running the pipeline you will need to create a slurm script to submit as a job.

```bash
$ more job.pbs
#!/bin/bash
#SBATCH --account=...
#SBATCH --chdir=....
#SBATCH --nodes="2"
#SBATCH --ntasks-per-node="36"

module load Nextflow

nextflow run <pipeline> -profile vsc_kul_uhasselt,<CLUSTER-option> <Add your other parameters>
```

Here the cluster options are:

- genius (72h)
- genius_long (168h)
- wice (72h)
- wice_long (168h)
- superdome (72h)
- superdome_long (168h)

> **NB:** The vsc_kul_uhasselt profile is based on a selected amount of SLURM partitions. Should you require resources outside of these limits (e.g. more memory or gpus) you will need to provide a custom config specifying an appropriate SLURM partition (e.g. 'bigmem*', or 'gpu*').

Use the `--cluster` option to specify the cluster you intend to use when submitting the job:

```shell
sbatch --cluster=wice|genius job.slurm 
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

The config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space. The default work directory is set to `$VSC_SCRATCH/work` per this configuration

> **NB:** The default directory where the `work/` and `singularity/` (cache directory for images) is located in `$VSC_SCRATCH`.
