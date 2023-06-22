# nf-core/configs: Hypatia Configuration

All nf-core pipelines have been successfully configured for use on the [Universidad de los Andes Hypatia Cluster](https://exacore.uniandes.edu.co/es/)

To use, run the pipeline with `-profile hypatia`. This will download and launch the [`hypatia.config`](../conf/hypatia.config) which has been pre-configured with a setup suitable for the Hypatia Cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to install Nextflow and load Singularity using the environment module system on Hypatia Cluster. You can do this by issuing the commands below:

```bash
## Load Java, Singularity and Nextflow environment modules
module purge
module load jdk/19.0.2
module load singularity/3.7.1
module load nextflow/22.10.1
```

> NB: You will need an account to use the HPC cluster on Hypatia in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be submited via sbatch. If in doubt contact IT.
