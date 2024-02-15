# nf-core/configs: Pawsey Setonix HPC Configuration

nf-core pipelines have been successfully run on Setonix HPC at [Pawsey Supercomputing Centre](https://pawsey.org.au/).

To run an nf-core pipeline at Pawsey's Setonix HPC, run the pipeline with `-profile singularity,pawsey_setonix`. This will download and launch the [`pawsey_setonix.config`](../conf/pawsey_setonix.config) which has been pre-configured with a setup suitable for the Setonix HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Access to Setonix HPC

Please be aware that you will need to have a user account, be a member of a Setonix project, and have a service unit allocation to your project in order to use this infrastructure. See documentation for details regarding [access mechanisms for Setonix HPC](https://support.pawsey.org.au/documentation/display/US/Requesting+Access+to+Pawsey+Supercomputers).

## Launch an nf-core pipeline on Setonix

### Prerequisites

Before running the pipeline you will need to load Nextflow and Singularity, both of which are globally installed modules on Setonix. You can do this by running the commands below:

```bash
module purge
module load nextflow singularity
```

### Execution command

```bash
module load nextflow
module load singularity

nextflow run <nf-core_pipeline>/main.nf \
  -profile singularity,pawsey_setonix \
  <additional flags>
```

### Cluster considerations

This config currently determines which Setonix queue to submit your task to based on the amount of memory required. For the sake of resource and service unit efficiency, the following rules are applied by this config:

- Tasks requesting **less than 238 Gb** will be submitted to the work queue
- Tasks requesting **more than 230 Gb and less than 980 Gb** will be submitted to the highmem queue

See the Setonix [documentation](https://support.pawsey.org.au/documentation/pages/viewpage.action?pageId=121479736#RunningJobsonSetonix-Overview) for details regarding queue resource structure and resource limits.
