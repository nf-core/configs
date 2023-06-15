# nf-core/configs: McCleary Configuration

All nf-core pipelines have been successfully configured for use on the McCleary at Yale University.

To use, run the pipeline with `-profile mccleary`. This will download and launch the [`mccleary.config`](../conf/mccleary.config) which has been pre-configured with a setup suitable for the McCleary cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running the pipeline you will need to load Java 11 using the environment module system on McCleary. You can do this by issuing the commands below:

```bash
## Load Java 11 environment modules
module purge
module load Java/17.0.4
```

## Recommendation on environment variables to set

Although not required, it is recommended to set certain Nextflow specific environment variables to make better use of cluster resources.

```bash
NXF_OPTS="-Xms500M -Xmx8G"
NXF_WORK="$PALMER_SCRATCH"
NXF_SINGULARITY_CACHEDIR="$PALMER_SCRATCH"
```

Adding these lines to the end of your `~/.bashrc` will load them upon login.

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on McCleary so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

> NB: You will need an account to use the HPC cluster on McCleary in order to run the pipeline. If in doubt contact YCRC.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact YCRC.
