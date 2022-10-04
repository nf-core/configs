# nf-core/configs: BINAC Configuration

All nf-core pipelines have been successfully configured for use on the BinAC cluster at Baden-Württemberg HPC.

To use, run the pipeline with `-profile binac`. This will download and launch the [`binac.config`](../conf/binac.config) which has been pre-configured with a setup suitable for the BINAC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on BINAC cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load devel/java_jdk/1.8.0u112
module load devel/singularity/3.0.1
```

> NB: You will need an account to use the HPC cluster BINAC in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
