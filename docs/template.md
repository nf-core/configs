# nf-core/configs: PROFILE Configuration

All nf-core pipelines have been successfully configured for use on the PROFILE CLUSTER at the insert institution here.

To use, run the pipeline with `-profile PROFILENAME`. This will download and launch the [`profile.config`](../conf/profile.config) which has been pre-configured with a setup suitable for the PROFILE cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on PROFILE CLUSTER. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load Nextflow/0.32.0
module load Singularity/2.6.0
```

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on PROFILE CLUSTER so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

> NB: You will need an account to use the HPC cluster on PROFILE CLUSTER in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
