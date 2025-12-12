# nf-core/configs: Imperial CX3 HPC Configuration

All nf-core pipelines have been successfully configured for use on the CX3 cluster at Imperial College London HPC.

To use, run the pipeline with `-profile imperial,standard`. This will download and launch the [`imperial.config`](../conf/imperial.config) which has been pre-configured with a setup suitable for the CX3 cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to install Nextflow into a conda environment. The instructions below at taken from the [`RCS guidance on using conda`](https://icl-rcs-user-guide.readthedocs.io/en/latest/hpc/applications/guides/conda/)

```bash
## Load Nextflow and Singularity environment modules
module load miniforge/3
miniforge-setup
eval "$(~/miniforge3/bin/conda shell.bash hook)"
conda create -n nextflow -c bioconda  nextflow
```

> NB: You will need an Imperial account to use any HPC cluster managed by the RCS team. If in doubt contact the [`RCS team`](https://icl-rcs-user-guide.readthedocs.io/en/latest/support/)
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes.
> NB: To submit jobs to the Imperial College MEDBIO cluster, use `-profile imperial,medbio` instead.
> NB: You will need a restricted access account to use the HPC cluster MEDBIO.
