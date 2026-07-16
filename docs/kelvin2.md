# nf-core/configs: Queen's University Belfast Kelvin2 HPC Configuration

nf-core pipelines have been configured for use on Queen's University Belfast's [Kelvin2](https://ni-hpc.github.io/nihpc-documentation/) HPC cluster. To use this profile, run a pipeline with `-profile kelvin2`, which loads the pre-configured [`kelvin2.config`](../conf/kelvin2.config).

This profile was tested with Nextflow `26.04.4` and the `nf-core/rnaseq` pipeline `3.26.0`.

## Set up Nextflow and Apptainer

Nextflow and Apptainer can both be installed into a Conda or Mamba environment.

```bash
# Create and activate the environment
conda create --name nextflow --channel bioconda --channel conda-forge nextflow apptainer
conda activate nextflow

# Confirm both tools are available
nextflow info
apptainer --version
```

## Run a pipeline

Launch a pipeline with the `kelvin2` profile:

```bash
nextflow run nf-core/<PIPELINE> -profile kelvin2 --outdir <RESULTS> [other arguments]
```

The Nextflow driver process must keep running for the whole pipeline. Two recommendations:

- **Use a terminal multiplexer such as `tmux` or `screen`** so the driver survives an SSH disconnect. Note which login node you are on so you can reconnect to the same one.

  ```bash
  tmux new -s nextflow        # detach: Ctrl-b then d; reattach: tmux attach -t nextflow
  ```

- **Do not run heavy work on a login node.** For anything beyond a quick test with pre-cached container images, start the driver inside an interactive job (it will submit the pipeline's own jobs from there):

  ```bash
  srun --partition=k2-medpri --ntasks=1 --mem-per-cpu=4G --time=24:00:00 --pty bash
  ```

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
