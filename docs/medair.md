# nf-core/configs: Medair Configuration

All nf-core pipelines have been successfully configured for use on the medair cluster at Clinical Genomics Gothenburg.

To use, run the pipeline with `-profile medair`. This will download and launch the [`medair.config`](../conf/medair.config) which has been pre-configured with a setup suitable for the medair cluster. 
It will enable Nextflow to manage the pipeline jobs via the `SGE` job scheduler.
Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Download nf-core pipelines

### Set-up

First you need to load relevant softwares: Nextflow and nf-core tools. You can do it as follow:

```bash
## Load Nextflow
module load nextflow
## Load nf-core tools
module load miniconda
source activate nf-core
```

### Download a pipeline

We have started to download pipelines in the following location: `/apps/bio/repos/nf-core/`

Use the `nf-core download --singularity-cache-only` command to start a download. It will open an interactive menu. Choose `singularity` for the software container image, and `none` for the compression type.

### Storage of Singularity images

When downloading a new nf-core pipeline for the first time (or a specific version of a pipeline), you can choose to store the Singularity image for future use. A central location for these images is: `/apps/bio/dependencies/nf-core/singularities`

Cached Singularity images can be accessed by running (or adding to your `.bashrc`) the following: 

```
export NXF_SINGULARITY_CACHEDIR="/apps/bio/dependencies/nf-core/singularities"
```

This was also added to cronuser.

## Run nf-core pipelines

### Set-up

Before running a pipeline you will need to load Nextflow and Singularity using the environment module system on medair. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load nextflow
module load singularity
```

### Choose a profile

Depending on what you are running, you can choose between the `wgs` and `production` profiles. Jobs running with the `wgs` profile run on a queue with higher priority. Jobs running with the `production` profile can last longer (max time: 20 times, versus 2 days for the `wgs` profile).

>Usage: -profile medair,wgs ?? (Check)

## iGenomes specific configuration

>TODO modify this part. Do we want to have the iGenomes somewhere?

A local copy of the iGenomes resource has been made available on PROFILE CLUSTER so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

>NB: You will need an account to use the HPC cluster on PROFILE CLUSTER in order to run the pipeline. If in doubt contact IT.
>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
