# nf-core/configs: BI Configuration

All nf-core pipelines have been successfully configured for use at Boehringer Ingelheim.

To use, run the pipeline with `-profile bi`. This will download and launch the [`bi.config`](../conf/bi.config) which has been pre-configured with a setup suitable for the BI systems. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to follow the internal documentation to run Nextflow on our systems. Similar to that, you need to set an environment variable `NXF_GLOBAL_CONFIG` to the path of the internal global config which is not publicly available here.

> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
