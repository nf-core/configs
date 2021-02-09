# nf-core/configs: Imperial MEDBIO HPC Configuration

All nf-core pipelines have been successfully configured for use on the MEDBIO cluster at Imperial College London HPC.

To use, run the pipeline with `-profile imperial_mb`. This will download and launch the [`imperial_mb.config`](../conf/imperial_mb.config) which has been pre-configured with a setup suitable for the MEDBIO cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow using the environment module system on the head node. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module load Nextflow
```

>NB: You will need an account to use the HPC cluster MEDBIO in order to run the pipeline. Access to the MEDBIO queue is exclusive.  If in doubt contact IT.
>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
>NB: To submit jobs to the standard CX1 cluster at Imperial College, use `-profile imperial` instead.
