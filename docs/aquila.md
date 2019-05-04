# nf-core/configs: Aquila Configuration

All nf-core pipelines have been successfully configured for use on the Aquila cluster at A*STAR Singapore.

To use, run the pipeline with `-profile aquila`. This will download and launch the [`aquila.config`](../conf/aquila.config) which has been pre-configured with a setup suitable for the Aquila cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

>NB: You will need an account to use the HPC cluster Aquila in order to run the pipeline. If in doubt contact IT.
>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
