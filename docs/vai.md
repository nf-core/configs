# nf-core/configs: VAI configuration

All nf-core pipelines have been successfully configured for use on the HPC cluster at Van Andel Institute.

To use, run the pipeline with `-profile vai`. This will download and launch the [`vai.config`](../conf/vai.config) which has been pre-configured with a setup suitable for the VAI HPC. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

```bash
module load singularity
NXF_OPTS="-Xmx500m" MALLOC_ARENA_MAX=4 nextflow run <pipeline>
```

> NB: You will need an account to use the HPC in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on the login node. If in doubt contact IT.
> NB: The submit node limits the amount of memory available to each user. The `NXF_OPTS` and `MALLOC_ARENA_MAX` parameters above prevent Nextflow from allocating more memory than the scheduler will allow.
