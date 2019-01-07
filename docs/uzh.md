# nf-core/configs: UZH Configuration

All nf-core pipelines have been successfully configured for use on the UZH cluster at the insert institution here.

To use, run the pipeline with `-profile uzh`. This will download and launch the [`uzh.config`](../conf/uzh.config) which has been pre-configured with a setup suitable for the UZH cluster. Using this profile, Nextflow will download a singularity image with all of the required software before execution of the pipeline.


>NB: You will need an account to use the HPC cluster UZH in order to run the pipeline. If in doubt contact IT.

>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
