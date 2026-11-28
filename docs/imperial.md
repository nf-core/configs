# nf-core/configs: Imperial CX3 HPC Configuration

All nf-core pipelines have been configured for use on the CX3 cluster at Imperial College London HPC.

To use, run the pipeline with `-profile imperial`. This will download and launch the [`imperial.config`](../conf/imperial.config) which has been pre-configured with a setup suitable for the CX3 cluster. Jobs are submitted to PBS Pro, which routes each one to a queue by the resources it asks for, so do not set a queue. Using this profile, a docker image containing all of the required software will be downloaded, and converted to an Apptainer (Singularity) image before execution of the pipeline. Apptainer is installed on all CX3 nodes, so no module needs to be loaded for it.

Nextflow is available as an environment module on CX3:

```bash
module load Nextflow/25.10.2
nextflow run nf-core/<pipeline> -profile imperial --outdir <OUTDIR> -work-dir $EPHEMERAL/<RUN_NAME>
```

`module avail Nextflow` lists the versions installed. Alternatively, install Nextflow in your home directory (Java 17 or later is needed: `module load Java/17`):

```bash
mkdir -p $HOME/bin && cd $HOME/bin
curl -s https://get.nextflow.io | bash
```

Set `NXF_VER` (e.g. `export NXF_VER=25.10.2`) to run a particular Nextflow version.

## Running the pipeline as a PBS job

Nextflow itself has to keep running for as long as the pipeline does, and submits each task as its own PBS job. It can run on a login node inside `tmux` or `screen`, so the run survives a disconnect, or as a PBS job of its own:

```bash
#!/bin/bash
#PBS -l select=1:ncpus=2:mem=8gb
#PBS -l walltime=72:00:00
#PBS -N nextflow

cd $PBS_O_WORKDIR
module load Nextflow/25.10.2
nextflow run nf-core/<pipeline> -profile imperial --outdir <OUTDIR> -work-dir $EPHEMERAL/<RUN_NAME> -resume
```

72 hours is the longest a job can run on CX3. If the pipeline needs longer, submit the same script again: `-resume` (an option of `nextflow run`) reuses the tasks that already finished.

## Images

Images are cached in `$NXF_SINGULARITY_CACHEDIR` if it is set, otherwise in `/rds/general/user/$USER/ephemeral/singularity_cache`. A group that wants to share images can keep them in a folder that only a few trusted people can write to, and point `NXF_SINGULARITY_LIBRARYDIR` at it: Nextflow reads images from there and downloads any that are missing to the cache. A folder that everyone can write to means trusting everyone who can write there to run code as you.

## GPUs

Any task with an `accelerator` directive is given GPUs. In nf-core pipelines this means `process_gpu` tasks when the pipeline is run with `-profile imperial,gpu`. Pipelines that used the `with_gpus` label from earlier versions of this profile should set `accelerator 1` on those processes instead.

CX3 has A100, A40, L40S and RTX6000 GPUs. A task that doesn't name a GPU type gets an L40S. To use another type, set `--imperial_gpu_type RTX6000` (or `export IMPERIAL_GPU_TYPE=RTX6000` before launching), or give the type in the pipeline's `accelerator` directive.

## Notes

> NB: You will need an Imperial account to use any HPC cluster managed by the RCS team. If in doubt contact the [`RCS team`](https://icl-rcs-user-guide.readthedocs.io/en/latest/support/)
> NB: Each task can use at most one node: 128 CPUs, 920 GB of memory and 72 hours. Larger requests are capped at these limits.
> NB: To submit jobs to the Imperial College MEDBIO cluster, use `-profile imperial,medbio` instead.
> NB: You will need a restricted access account to use the HPC cluster MEDBIO.
