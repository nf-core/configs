# nf-core/configs: Cannon Configuration

All nf-core pipelines have been successfully configured for use on the Cannon CLUSTER at Harvard FAS.

To use, run the pipeline with `-profile cannon`. This will download and launch the [`cannon.config`](../conf/cannon.config) which has been pre-configured with a setup suitable for the Cannon cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to load Java and Python using the environment module system on Cannon. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load jdk
module load python
```

:::note
You will need an account to use the HPC cluster on PROFILE CLUSTER in order to run the pipeline. If in doubt contact IT.
:::

:::note
Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
:::
