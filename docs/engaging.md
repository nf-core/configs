# nf-core/configs: Engaging Configuration

All nf-core pipelines have been successfully configured for use on the [MIT Engaging Cluster](https://engaging-web.mit.edu/eofe-wiki/).

To use, run the pipeline with `-profile engaging`. This will download and launch the [`engaging.config`](../conf/engaging.config) which has been pre-configured with a setup suitable for the Engaging Cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to install Nextflow and load Singularity using the environment module system on Engaging Cluster. You can do this by issuing the commands below:

```bash
## Load Java and Singularity environment modules
module purge
module load jdk/18.0.1.1
module load singularity/3.7.0

# Download Nextflow
curl -s https://get.nextflow.io | bash
```

> NB: You will need an account to use the HPC cluster on Engaging in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
