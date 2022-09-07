# nf-core/configs: CBE Configuration

All nf-core pipelines have been successfully configured for use on the CLIP BATCH ENVIRONMENT (CBE) cluster at the Vienna BioCenter (VBC).

To use, run the pipeline with `-profile cbe`. This will download and launch the [`cbe.config`](../conf/cbe.config) which has been pre-configured with a setup suitable for the CBE cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow using the environment module system on CBE. You can do this by issuing the commands below:

```bash
## Load Nextflow environment module
module purge
module load nextflow/21.10.6
```

A local copy of the [AWS-iGenomes](https://registry.opendata.aws/aws-igenomes/) resource has been made available on CBE so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline. You can do this by simply using the `--genome <GENOME_ID>` parameter.

> NB: You will need an account to use the HPC cluster on CBE in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
