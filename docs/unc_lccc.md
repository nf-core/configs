# nf-core/configs: PROFILE Configuration

All nf-core pipelines have been successfully configured for use on the Lineberger Bioinformatics Group cluster at the University of North Carolina at Chapel Hill Lineberger Comprehensive Cancer Center.

To use, run the pipeline with `-profile unc_lccc`. This will download and launch the [`unc_lccc.config`](../conf/unc_lccc.config) which has been pre-configured with a setup suitable for the LBG cluster. Using this profile, docker images containing all of the required software will be downloaded, and converted to a Singularity/Apptainer image before execution of the pipeline.

## Below are non-mandatory information e.g. on modules to load etc

Before running pipelines you will need to login to a compute node and install nextflow https://www.nextflow.io/. You can do this by issuing the commands below:

```bash
## install Nextflow
module purge
module load Nextflow/0.32.0
module load Singularity/2.6.0
```

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on PROFILE CLUSTER so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

> NB: You will need an account to use the  in order to run the pipelines. If in doubt contact <informaticshelp@unc.edu>.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
