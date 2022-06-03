# nf-core/configs: JAX Configuration

All nf-core pipelines have been successfully configured for use on the JAX Sumner cluster at The Jackson Laboratory.

To use, run the pipeline with `-profile jax`. This will download and launch the [`jax.config`](../conf/jax.config) which has been pre-configured with a setup suitable for JAX Sumner cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline and slurm will be used as well.

> NB: You will need an account to use the HPC cluster JAX in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow should not be executed on the login nodes. If in doubt contact IT.
