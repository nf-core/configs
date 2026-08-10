# nf-core/configs: Queen's University Belfast Kelvin2 HPC Configuration

nf-core pipelines have been configured for use on Queen's University Belfast's [Kelvin2](https://ni-hpc.github.io/nihpc-documentation/) HPC cluster. To use this profile, run a pipeline with `-profile kelvin2`, which loads the pre-configured [`kelvin2.config`](../conf/kelvin2.config).

This profile was tested with Nextflow `26.04.4` and the `nf-core/rnaseq` pipeline `3.26.0`.

## Set up Nextflow and Apptainer

### Option 1: Environment modules (recommended)

Kelvin2 provides Nextflow and Apptainer as modules:

```bash
module load nextflow/24.07.27/java-22.0.2
module load apps/apptainer/1.3.4
```

To run a newer Nextflow release without replacing the module launcher, set `NXF_VER` (the launcher downloads and caches that version under `$NXF_HOME`):

```bash
NXF_VER=26.04.4 nextflow info
```

### Option 2: Up-to-date Nextflow binary + module Apptainer

If you need a newer Nextflow than the module provides, install the Nextflow launcher onto scratch and keep using the system Apptainer module:

```bash
# Install Nextflow to a directory on scratch (example path)
mkdir -p /mnt/scratch2/users/$USER/bin
curl -fsSL https://get.nextflow.io -o /mnt/scratch2/users/$USER/bin/nextflow
chmod +x /mnt/scratch2/users/$USER/bin/nextflow
export PATH="/mnt/scratch2/users/$USER/bin:$PATH"

module load apps/apptainer/1.3.4
```

### Option 3: Conda or Mamba

Conda/Mamba environments are also fine on Kelvin2:

```bash
conda create --name nextflow --channel bioconda --channel conda-forge nextflow apptainer
conda activate nextflow
```

### Confirm the install

After any of these options, confirm both tools are available:

```bash
nextflow info
apptainer --version
```

## Run a pipeline

Launch a pipeline with the `kelvin2` profile:

```bash
nextflow run nf-core/<PIPELINE> -profile kelvin2 --outdir <RESULTS> [other arguments]
```

The Nextflow driver process must keep running for the whole pipeline. Use a terminal multiplexer such as `tmux` or `screen` so it survives an SSH disconnect. Note which login node you are on so you can reconnect to the same one:

```bash
tmux new -s nextflow        # detach: Ctrl-b then d; reattach: tmux attach -t nextflow
```

Once Apptainer images are cached, the driver is light enough to run on a login node inside `tmux`. The first run of a pipeline (or any run that pulls many new images) can be CPU-heavy on the login node while container images are fetched. For those cases, start the driver on a compute node via `srun` inside `tmux`, or submit a hands-free batch job:

```bash
#!/usr/bin/env bash
#SBATCH --job-name=nextflow_pipeline
#SBATCH --output=nextflow_pipeline_%j.log
#SBATCH --partition=k2-medpri
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem-per-cpu=4G

module load nextflow/24.07.27/java-22.0.2
module load apps/apptainer/1.3.4

nextflow run nf-core/<PIPELINE> -profile kelvin2 --outdir <RESULTS> [other arguments]
```

Save that as e.g. `run_nextflow.sh` and submit with `sbatch run_nextflow.sh`.

## Cluster specifications

- **Scheduler**: SLURM
- **Container engine**: Apptainer
- **Maximum CPUs**: 128 per job
- **Maximum memory**: 786 GB on general-access nodes, up to 2 TB on high-memory (`k2-himem`) nodes
- **Maximum time**: 720 hours (30 days)

### Partition selection

The SLURM partition is chosen automatically from each task's requested resources, so you never need to set one:

| Task requirements    | Partitions used                      |
| -------------------- | ------------------------------------ |
| ≤ 3 hours walltime   | `k2-hipri`, `k2-medpri`, `k2-lowpri` |
| ≤ 24 hours walltime  | `k2-medpri`, `k2-lowpri`             |
| > 24 hours walltime  | `k2-lowpri`                          |
| > 786 GB memory      | `k2-himem` only (2 TB, 3-day limit)  |
| > 12 GB per core     | also offered `k2-himem`              |

## Notes

- **Resuming runs**: The `work/` directory is retained on completion (`cleanup` is left at its default). To reclaim scratch space, set `cleanup = true` in your own config, or run `nextflow clean` afterwards.
- **Container cache**: Apptainer images are cached under `/mnt/scratch2/users/$USER/apptainer_cache`, so each image is pulled once and reused across runs. To cache elsewhere - for example a shared group directory - set `NXF_APPTAINER_CACHEDIR` to override this.

## Support

For questions about this configuration profile, contact the maintainer listed in `config_profile_contact`. For general Kelvin2 cluster support, see the [Kelvin2 documentation](https://ni-hpc.github.io/nihpc-documentation/) or [contact the NI-HPC team](https://www.ni-hpc.ac.uk/contact/).
