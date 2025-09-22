# nf-core/configs: PROFILE Configuration

All nf-core pipelines have been successfully configured for use on the HPC at RKI.

To use, run the pipeline with `-profile PROFILENAME`. This will download and launch the [`profile.config`](../conf/profile.config) which has been pre-configured with a setup suitable for the HPC. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Before running the pipeline

### Singularity

We highly recommend specifying a location of a cache directory to store singularity images (so you re-use them across runs, and not pull each time), by specifying the location with the `$NXF_SINGULARITY_CACHEDIR` bash environment variable in your `~/.bashrc`, or in your current session:

```bash
# as environment variable
export NXF_SINGULARITY_CACHEDIR="/path/to/your/singularity/image/cache"
# or for one nextflow run
NXF_SINGULARITY_CACHEDIR='/path/to/your/singularity/image/cache' nextflow run <...>
```

:::note
You will need an account to use the HPC cluster on HPC in order to run the pipeline. If in doubt contact IT.
:::

:::note
Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
:::
