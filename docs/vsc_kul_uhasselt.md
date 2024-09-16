# nf-core/configs: KU Leuven/UHasselt Tier-2 High Performance Computing Infrastructure (VSC)

> **NB:** You will need an [account](https://docs.vscentrum.be/en/latest/access/getting_access.html#required-steps-to-get-access) to use the HPC cluster to run the pipeline.

1. Install Nextflow on the cluster

```bash
conda create --name nf-core python=3.12 nf-core nextflow
```

:::note
A nextflow module is available that can be loaded `module load Nextflow` but it does not support plugins. So it's not recommended
:::

2. Set up the environment variables in `~/.bashrc` or `~/.bash_profile`:

```bash
export SLURM_ACCOUNT="<your-credential-account>"

# Needed for running Nextflow jobs
export NXF_HOME="$VSC_SCRATCH/.nextflow"
export NXF_WORK="$VSC_SCRATCH/work"

# Needed for running Apptainer containers
export APPTAINER_CACHEDIR="$VSC_SCRATCH/.apptainer/cache"
export APPTAINER_TMPDIR="$VSC_SCRATCH/.apptainer/tmp"
export NXF_CONDA_CACHEDIR="$VSC_SCRATCH/miniconda3/envs"

# Optional tower key
# export TOWER_ACCESS_TOKEN="<your_tower_access_token>"
# export NXF_VER="<version>"      # make sure it's larger then 24.04.0
```

:::warning
The current config is setup with array jobs. Make sure nextflow version >= 24.04.0, read [array jobs in nextflow](https://www.nextflow.io/docs/latest/process.html#array) you can do this in

```bash
export NXF_VER=24.04.0
```

:::

3. Make the submission script.

> **NB:** you should go to the cluster you want to run the pipeline on. You can check what clusters have the most free space using following command `sinfo --cluster wice|genius`.

```bash
$ more job.pbs
#!/bin/bash -l
#SBATCH --account=...
#SBATCH --chdir=....
#SBATCH --partition=batch_long
#SBATCH --nodes="1"
#SBATCH --ntasks-per-node="1"

# module load Nextflow # does not support plugins
conda activate nf-core

nextflow run <pipeline> -profile vsc_kul_uhasselt,<CLUSTER> <Add your other parameters>
```

> **NB:** You have to specify your credential account, by setting `export SLURM_ACCOUNT="<your-credential-account>"` else the jobs will fail!

Here the cluster options are:

- genius
- wice
- superdome

> **NB:** The vsc_kul_uhasselt profile is based on a selected amount of SLURM partitions. Should you require resources outside of these limits (e.g.gpus) you will need to provide a custom config specifying an appropriate SLURM partition (e.g. 'gpu\*').

Use the `--cluster` option to specify the cluster you intend to use when submitting the job:

```shell
sbatch --cluster=wice|genius job.slurm 
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
