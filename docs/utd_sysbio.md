# nf-core/configs: UTD Sysbio Configuration

All nf-core pipelines have been successfully configured for use on the Sysbio HPC cluster at the [The Univeristy of Texas at Dallas](https://www.utdallas.edu/).

To use, run the pipeline with `-profile utd_sysbio`. This will download and launch the [`utd_sysbio.config`](../conf/utd_sysbio.config) which has been pre-configured with a setup suitable for the Sysbio HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Singularity using the environment module system on Sysbio. You can do this by issuing the commands below:

```bash
## Singularity environment modules
module purge
module load singularity
```

> NB: You will need an account to use the HPC cluster on Sysbio in order to run the pipeline. If in doubt contact OIT.
> NB: Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact OIT.
