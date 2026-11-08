# nf-core/configs: Imperial CX3 HPC Configuration

All nf-core pipelines have been configured for use on the CX3 cluster at Imperial College London HPC.

To use, run the pipeline with `-profile imperial`. This will download and launch the [`imperial.config`](../conf/imperial.config) which has been pre-configured with a setup suitable for the CX3 cluster. Jobs are submitted to PBS Pro, which routes each one to a queue by the resources it asks for, so do not set a queue. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity (Apptainer) image before execution of the pipeline.

Nextflow is available as an environment module on CX3:

```bash
module load Nextflow/25.10.2
nextflow run nf-core/<pipeline> -profile imperial --outdir <OUTDIR> -work-dir $EPHEMERAL/<RUN_NAME>
```

`module avail Nextflow` lists the versions installed. Alternatively, Nextflow can be installed into a conda environment, following the [`RCS guidance on using conda`](https://icl-rcs-user-guide.readthedocs.io/en/latest/hpc/applications/guides/conda/):

```bash
module load miniforge/3
miniforge-setup
eval "$(~/miniforge3/bin/conda shell.bash hook)"
conda create -n nextflow -c bioconda nextflow
```

Images are cached in `$NXF_SINGULARITY_CACHEDIR` if it is set, otherwise in `/rds/general/user/$USER/ephemeral/singularity_cache`. Groups that share images can set `NXF_SINGULARITY_CACHEDIR` to a folder in their project space, so each image is only downloaded once.

> NB: You will need an Imperial account to use any HPC cluster managed by the RCS team. If in doubt contact the [`RCS team`](https://icl-rcs-user-guide.readthedocs.io/en/latest/support/)
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes (inside `tmux` or `screen`, so the run survives a disconnect) or from within a PBS job. A PBS job running Nextflow itself is limited to 72 hours; use `-resume` to continue a run that outlives it.
> NB: Each task can use at most one node: 128 CPUs, 920 GB of memory and 72 hours. Larger requests are capped at these limits.
> NB: Any task with an `accelerator` directive is given GPUs. In nf-core pipelines this means `process_gpu` tasks when the pipeline is run with `-profile imperial,gpu`. Pipelines that used the `with_gpus` label from earlier versions of this profile should set `accelerator 1` on those processes instead. To ask for a particular GPU type, `export IMPERIAL_GPU_TYPE=L40S` (or `A100`) before launching.
> NB: To submit jobs to the Imperial College MEDBIO cluster, use `-profile imperial,medbio` instead.
> NB: You will need a restricted access account to use the HPC cluster MEDBIO.
