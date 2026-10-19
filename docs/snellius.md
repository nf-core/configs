# nf-core/configs: Snellius Configuration

All nf-core pipelines have been configured for use on [Snellius](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660184/Snellius), the Dutch national supercomputer hosted at SURF.

To use, run the pipeline with `-profile snellius`. This will download and launch the [`snellius.config`](../conf/snellius.config) which has been pre-configured with a setup suitable for Snellius. Jobs are submitted with Slurm to a partition chosen by the resources a process requests:

| Partition   | Used for processes requesting                                                 |
| ----------- | ----------------------------------------------------------------------------- |
| `rome`      | at most 16 CPUs and at most 28 GB of memory                                   |
| `genoa`     | more than 16 CPUs or 28 GB, up to 336 GB of memory                            |
| `fat_genoa` | more than 336 GB of memory, only with the `fat_genoa` sub-profile (see below) |

Small processes go to `rome` because its smallest allocation (16 cores) is billed for fewer cores than that of `genoa` (24 cores). Software is run in containers with Apptainer, which is the only container engine installed on Snellius.

## Job names

Nextflow names each Slurm job after the process and its tag, for example `NFCORE_RNASEQ:RNASEQ:FASTQC (SAMPLE1)`. Slurm on Snellius does not accept special characters such as `:`, `(` and `)` in job names, so this profile replaces every character other than letters, digits and underscores with an underscore. The job above is submitted as `NFCORE_RNASEQ_RNASEQ_FASTQC__SAMPLE1_`. Use these names to find your jobs in `squeue` and `sacct`.

## Large memory jobs (`fat_genoa`)

The `fat_genoa` partition needs its own budget, which has to be requested in your Snellius application. Without it, jobs submitted to `fat_genoa` fail. By default this profile therefore only uses `rome` and `genoa`, and caps the memory of every process at 336 GB.

If your budget includes `fat_genoa`, add the `fat_genoa` sub-profile to send processes that request more than 336 GB to the `fat_genoa` partition, up to 1440 GB:

```bash
nextflow run nf-core/<pipeline> -profile snellius,fat_genoa <other parameters>
```

## Before running the pipeline

You need a Snellius login with an active budget (SBUs), either through an NWO grant or through your institution's SURF contract. Snellius logins are per person and per project, so jobs are billed to the budget of the login you submit them from. Use `accinfo` or `budget-overview` to check your remaining budget.

Install Nextflow on a login node in one of the following ways.

With mamba, from a [Miniforge](https://github.com/conda-forge/miniforge) installation in your home directory. The environment includes Java, so no modules are needed:

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

Then add the following to your `~/.bashrc`, so that the settings are also passed to the Nextflow job you submit with `sbatch`:

```bash
# Nextflow on Snellius
export NXF_WORK=/scratch-shared/$USER/work
export NXF_APPTAINER_CACHEDIR=/projects/0/<your_project>/apptainer_cache
export NXF_OPTS="-Xms1g -Xmx8g"
```

If you do not have project space, use `/scratch-shared/$USER/apptainer_cache` for the container images instead. They are then removed after 14 days and downloaded again when you next need them.

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
#SBATCH --partition=rome
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

The Nextflow job needs little compute, but it is billed as at least 16 cores, the smallest allocation on `rome`. Set `--time` to how long you expect the whole pipeline to take, up to the maximum walltime of 120 hours on Snellius. If a run does not finish in time, submit the script again with `-resume` added to the `nextflow run` command.

> NB: Snellius bills SBUs per allocated core, and the smallest possible allocation is 1/8 of a node (16 cores and 28 GiB on `rome`, 24 cores and 42 GiB on `genoa`, 24 cores and 180 GiB on `fat_genoa`). Every job is therefore billed as at least 16 cores. `fat_genoa` is billed at 1.5 SBU per core hour, against 1.0 for `rome` and `genoa`. See the [Snellius partitions](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660209/Snellius+partitions) and [accounting](https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/300974104/Snellius+accounting) documentation for details.
