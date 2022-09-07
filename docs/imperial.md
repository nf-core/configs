# nf-core/configs: Imperial CX1 HPC Configuration

All nf-core pipelines have been successfully configured for use on the CX1 cluster at Imperial College London HPC.

To use, run the pipeline with `-profile imperial,standard`. This will download and launch the [`imperial.config`](../conf/imperial.config) which has been pre-configured with a setup suitable for the CX1 cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow using the environment module system on the CX1 cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module load anaconda3/personal
conda install -c bioconda nextflow
```

> NB: You will need an account to use the HPC cluster CX1 in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
> NB: To submit jobs to the Imperial College MEDBIO cluster, use `-profile imperial,medbio` instead.
> NB: You will need a restricted access account to use the HPC cluster MEDBIO.
