# nf-core/configs: Medair Configuration

All nf-core pipelines have been successfully configured for use on the Medair cluster at Clinical Genomics Gothenburg.

To use, run the pipeline with `-profile medair`. This will download and launch the [`medair.config`](../conf/medair.config) which has been pre-configured with a setup suitable for the Medair cluster.
It will enable Nextflow to manage the pipeline jobs via the `SGE` job scheduler.
Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

You will need an account to use the Medair cluster in order to download or run pipelines. If in doubt, contact cgg-it.

## Download nf-core pipelines

### Set-up: load Nextflow and nf-core tools

First you need to load relevant softwares: Nextflow and nf-core tools. You can do it as follow:

```bash
## Load Nextflow
module load nextflow
## Load nf-core tools
module load miniconda
source activate nf-core
```

### Storage of Singularity images

When downloading a nf-core pipeline for the first time (or a specific version of a pipeline), you can choose to store the Singularity image for future use. We chose to have a central location for these images on medair: `/apps/bio/dependencies/nf-core/singularities`.

For Nexflow to know where to store new images, run or add the following to your `.bashrc`:

```bash
export NXF_SINGULARITY_CACHEDIR="/apps/bio/dependencies/nf-core/singularities"
```

> Comment: This was also added to cronuser.

### Download a pipeline

We have started to download pipelines in the following location: `/apps/bio/repos/nf-core/`

Use the `nf-core download --singularity-cache-only` command to start a download. It will open an interactive menu. Choose `singularity` for the software container image, and `none` for the compression type.

## Run nf-core pipelines

Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands below will have to be executed on one of the login nodes. If in doubt contact cgg-it (cgg-it[at]gu.se).

### Set-up: load Nextflow and Singularity

Before running a pipeline you will need to load Nextflow and Singularity using the environment module system on Medair. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load nextflow
module load singularity
```

### Choose a profile

Depending on what you are running, you can choose between the `wgs` and `production` profiles. Jobs running with the `wgs` profile run on a queue with higher priority. Jobs running with the `production` profile can last longer (max time: 20 days, versus 2 days for the `wgs` profile).

For example, the following job would run with the `wgs` profile:

```bash
run nextflow nf-core/raredisease -profile medair,wgs
```

### Sentieon

In some pipelines (sarek, raredisease) it is possible to use Sentieon for alignment and variant calling. If ones uses the label `sentieon` for running a process, the config file contains the path to the Sentieon singularity image on Medair.
