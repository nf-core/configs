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

:::note
If you have access to dedicated nodes, you can export these as a command separated list. These queues will only be used if specified task requirements are not available in the normal partitions but they are available in dedicated partitions. AMD is considered a dedicated partition.
:::

```bash
export SLURM_ACCOUNT="<your-credential-account>"

# Comma-separated list of available dedicated partitions (if any)
# For example: export VSC_DEDICATED_QUEUES="dedicated_big_bigmem,dedicated_big_gpu"
export VSC_DEDICATED_QUEUES="<available-dedicated-partitions>"

# Needed for running Nextflow jobs
export NXF_HOME="$VSC_SCRATCH/.nextflow"
export NXF_WORK="$VSC_SCRATCH/work"

# Needed for running Apptainer containers
export APPTAINER_CACHEDIR="$VSC_SCRATCH/.apptainer/cache"
export APPTAINER_TMPDIR="$VSC_SCRATCH/.apptainer/tmp"
export NXF_CONDA_CACHEDIR="$VSC_SCRATCH/miniconda3/envs"

# Optional tower key
# export TOWER_ACCESS_TOKEN="<your_tower_access_token>"
# export NXF_VER="<version>"      # make sure it's larger then 24.10.1
```

:::warning
The current config is setup with array jobs. Make sure nextflow version >= 24.10.1, read [array jobs in nextflow](https://www.nextflow.io/docs/latest/process.html#array) you can do this in

```bash
export NXF_VER=24.10.1
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
- genius_gpu
- wice
- wice_gpu
- superdome

> **NB:** The vsc_kul_uhasselt profile is based on a selected amount of SLURM partitions. The profile will select to its best ability the most appropriate partition for the job. Including modules with a label containing `gpu`will be allocated to a gpu partition when the 'normal' `genius` profile is selected. Select the `genius_gpu` or `wice_gpu` profile to force the job to be allocated to a gpu partition.
> **NB:** If the module does not have `accelerator` set, it will determine the number of GPUs based on the requested resources.

Use the `--cluster` option to specify the cluster you intend to use when submitting the job:

```shell
sbatch --cluster=wice|genius job.slurm 
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

4. Optional use nf-co2footprint

You can monitor the CO2 usage of your pipeline using the [nf-co2footprint plugin](https://nextflow-io.github.io/nf-co2footprint/) using a nextflow version =>24.10.6. Monitoring the CO2 usage is fully optional and will only be activated when running the following command-line.

```bash
nextflow run <pipeline> -profile <CLUSTER> -plugins nf-co2footprint@1.0.0 --outdir your_output_folder <Add your other parameters>
```
