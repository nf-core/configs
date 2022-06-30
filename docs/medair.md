# nf-core/configs: Medair Configuration

All nf-core pipelines have been successfully configured for use on the medair cluster at Clinical Genomics Gothenburg.

To use, run the pipeline with `-profile medair`. This will download and launch the [`medair.config`](../conf/medair.config) which has been pre-configured with a setup suitable for the medair cluster. 
It will enable Nextflow to manage the pipeline jobs via the `SGE` job scheduler.
Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Modules to load

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on medair. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load nextflow/21.10.5.5658
module load singularity/v3.4.0
```

>Should we link to Confluence page about new modules? See something about updating modules? etc.
>Is this a good location to mention the nf-core conda environment? module load miniconda; source activate nf-core

## Storage of Singularity images

When downloading a new nf-core pipeline for the first time (or a specific version of a pipeline), you can choose to store the Singularity image for future use. A central location for these images is: `/apps/bio/dependencies/nf-core/singularities`

Cached Singularity images can be accessed by running (or adding to your `.bashrc`) the following line: `export NXF_SINGULARITY_CACHEDIR="/apps/bio/dependencies/nf-core/singularities"` #is that correct??

## Different profiles depending on what you are running

Depending on what you are running, you can choose between the `clinic`, `research`, `byss` and `qd_rnaseq` profiles. This specify for example which queue will be used.

>NB: say more about the different queues?

## iGenomes specific configuration

>TODO modify this part. Do we want to have the iGenomes somewhere?

A local copy of the iGenomes resource has been made available on PROFILE CLUSTER so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

>NB: You will need an account to use the HPC cluster on PROFILE CLUSTER in order to run the pipeline. If in doubt contact IT.
>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
