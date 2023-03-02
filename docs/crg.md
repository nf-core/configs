# nf-core/configs: CRG Configuration

All nf-core pipelines have been successfully configured for use on the CRG HPC cluster at the [Centre for Genomic Regulation](https://www.crg.eu/).

To use, run the pipeline with `-profile crg`. This will download and launch the [`crg.config`](../conf/crg.config) which has been pre-configured with a setup suitable for the CRG HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to download Nextflow and load Singularity using the environment module system on CRG cluster. Please check the main README of the pipeline to make sure that the version of Nextflow is compatible with that required to run the pipeline. You can do this by issuing the commands below:

```bash
## Download Nextflow and load Singularity environment modules
wget -qO- https://get.nextflow.io | bash
module use /software/as/el7.2/EasyBuild/CRG/modules/all
module load Singularity/3.7.0
```

> NB: You will need an account to use the HPC cluster on CRG in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via SGE to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
