# nf-core/configs: Leicester Configuration

All nf-core pipelines have been successfully configured for use on the ALICE and SPECTRE cluster at the University of Leicester.

To use, run the pipeline with `-profile leicester`. This will download and launch the [`leicester.config`](../conf/leicester.config) which has been pre-configured with a setup suitable for the Leicester cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

> NB: You will need an account to use the ALICE and SPECTRE cluster in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
