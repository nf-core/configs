# nf-core/configs: Snellius Configuration

All nf-core pipelines have been configured for use on [Snellius](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660184/Snellius), the Dutch national supercomputer hosted at SURF.

To use, run the pipeline with `-profile snellius`. This will download and launch the [`snellius.config`](../conf/snellius.config) which has been pre-configured with a setup suitable for Snellius. Jobs are submitted with Slurm, and software is run in containers with Apptainer, which is the only container engine installed on Snellius.

## Partitions

Jobs can only run on the partitions your budget covers. The fat and high memory nodes need their own budget, which has to be requested in your Snellius application. Run `accinfo` and look at the `Products` line to see which partitions your budget covers.

The profile assumes a budget for `rome` and `genoa`. If your budget covers other CPU partitions, list them with `--snellius_nodes`, for example:

```bash
nextflow run nf-core/<pipeline> -profile snellius --snellius_nodes 'rome,genoa,fat_genoa' <other parameters>
```

The partitions you list set the following:

- **Maximum resources**: processes are capped at the largest node you list, using the memory available to jobs on the [Snellius partitions](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660209/Snellius+partitions) page. The default `rome,genoa` caps processes at 192 CPUs and 336 GB, adding `fat_genoa` raises this to 1440 GB, and adding `himem_8tb` to 7680 GB.
- **Partition**: Slurm on Snellius sends jobs without a partition to `rome`, so the profile sets the partition for each job. Snellius accepts only one partition per job, so each job is sent to the first of the listed partitions it fits on, in the order `rome`, `genoa`, `fat_rome`, `fat_genoa`, `himem_4tb`, `himem_8tb`. This puts jobs on the cheapest and smallest node that fits. With the default `rome,genoa`, jobs go to `rome`, and jobs that need more than 128 CPUs or 224 GB go to `genoa`. Jobs are never sent to a partition you did not list.

If you list a partition your budget does not cover, Slurm refuses the jobs sent there, and the pipeline stops with:

```console
sbatch: error: No compute budget was found for the partition fat_genoa.
sbatch: error: Batch job submission failed: Access/permission denied
```

Remove that partition from `--snellius_nodes` and run the pipeline again with `-resume`.

## GPUs

This profile does not support GPUs yet. It does not send processes to the GPU partitions or request GPUs from Slurm, so all processes run on CPU nodes, including those that pipelines label `process_gpu`. Pipelines that need a GPU for some steps, such as the Parabricks steps in nf-core/sarek, need to run those steps on the CPU alternative the pipeline offers.

## Job names

Nextflow names each Slurm job after the process and its tag, for example `NFCORE_RNASEQ:RNASEQ:FASTQC (SAMPLE1)`. Slurm on Snellius does not accept special characters such as `:`, `(` and `)` in job names, so this profile replaces every character other than letters, digits and underscores with an underscore. The job above is submitted as `NFCORE_RNASEQ_RNASEQ_FASTQC__SAMPLE1_`. Use these names to find your jobs in `squeue` and `sacct`.

## Before running the pipeline

You need a Snellius login with an active budget (SBUs), either through an NWO grant or through your institution's SURF contract. Snellius logins are per person and per project, so jobs are billed to the budget of the login you submit them from. Use `accinfo` or `budget-overview` to check your remaining budget.

Install Nextflow on a login node in one of the following ways. With mamba, from a [Miniforge](https://github.com/conda-forge/miniforge) installation in your home directory. The environment includes Java, so no modules are needed:

```bash
mamba create -n nextflow -c conda-forge -c bioconda nextflow
```

Or with the Java module and the Nextflow installer:

```bash
module load 2024
module load Java/21.0.5

curl -s https://get.nextflow.io | bash
mkdir -p ~/bin && mv nextflow ~/bin/
```

If `~/bin` is not on your `PATH` yet, add `export PATH=$HOME/bin:$PATH` to your `~/.bashrc`.

Check that Nextflow works with:

```bash
nextflow info
```

See the [nf-core installation guide](https://nf-co.re/docs/usage/getting_started/installation) for more on the Java and Nextflow versions pipelines need.

Then add the following to your `~/.bashrc`, so that the settings are also passed to the Nextflow job you submit with `sbatch`:

```bash
# Nextflow on Snellius
export NXF_WORK=/scratch-shared/$USER/work
export NXF_APPTAINER_CACHEDIR=/projects/0/<your_project>/apptainer_cache
export NXF_OPTS="-Xms1g -Xmx8g"
```

## Storage

Your home directory has a quota of 200 GiB, which is too small for most pipeline runs. The settings above put the files on the following file systems:

- **Work directory (`NXF_WORK`)**: `/scratch-shared/$USER/work`. The work directory has to be visible from all nodes, and `/scratch-shared` is. Files that have not changed for 14 days are removed automatically and without notice, so a run cannot be resumed with `-resume` after that.
- **Temporary files (`$TMPDIR`)**: Snellius sets `$TMPDIR` to a directory under `/scratch-local/$USER` in every job, and processes use it without any extra settings. This profile does not use the node-local `/scratch-node` disks, because only some nodes have them.
- **Results (`--outdir`)**: point this to your project space.

Scratch space has a quota of 8 TiB and a soft limit of 3 million files, counted over `/scratch-shared` and `/scratch-local` together. Pipelines with many samples can create a lot of files in the work directory, so remove it once a run has finished and you have checked the results. See the [Snellius filesystems](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/85295828/Snellius+filesystems) documentation for details.

## Running the pipeline

Submit Nextflow itself as a Slurm job. The Nextflow job then submits the pipeline's processes as separate Slurm jobs. Save the following as `nextflow.sbatch`:

```bash
#!/bin/bash
#SBATCH --job-name=nextflow
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=24:00:00
#SBATCH --output=nextflow_%j.log

# If you installed Nextflow with mamba
eval "$(conda shell.bash hook)"
conda activate nextflow

# If you installed Nextflow with the installer, use this instead
# module load 2024
# module load Java/21.0.5

nextflow run nf-core/<pipeline> -profile snellius --outdir /projects/0/<your_project>/results <other parameters>
```

And submit it from a login node with:

```bash
sbatch nextflow.sbatch
```

`sbatch` passes on the environment of the shell you submit from, so the variables from your `~/.bashrc` are also set in the Nextflow job and in the jobs it submits.

The Nextflow job needs little compute, but it is billed as at least the smallest allocation on the partition it runs on (see below). Set `--time` to how long you expect the whole pipeline to take, up to the maximum walltime of 120 hours on Snellius. If a run does not finish in time, submit the script again with `-resume` added to the `nextflow run` command.

> NB: Snellius bills SBUs per allocated core, and the smallest possible allocation is 1/8 of a node (16 cores and 28 GiB on `rome`, 24 cores and 42 GiB on `genoa`, 24 cores and 180 GiB on `fat_genoa`). Every job is therefore billed as at least 16 cores. Jobs are billed in steps of 1/8 of a node, by whichever is larger: the cores or the memory they request. For example, the STAR alignment in nf-core/rnaseq requests 12 CPUs and 72 GB, which on `rome` is the memory of 41 cores, so it is billed as 48 cores (3/8 of a node). `fat_genoa` is billed at 1.5 SBU per core hour, against 1.0 for `rome` and `genoa`. See the [Snellius partitions](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660209/Snellius+partitions) and [accounting](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/300974104/Snellius+accounting) documentation for details.
