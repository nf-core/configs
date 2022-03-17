# nf-core/configs: SAHMRI HPC Configuration

All nf-core pipelines have been successfully configured for use on the HPC cluster at [SAHMRI](https://sahmri.org.au/).  
To use, run the pipeline with `-profile sahmri`. This will download and launch the [`sahmri.config`](../conf/sahmri.config) which has been pre-configured
with a setup suitable for the SAHMRI HPC cluster. Using this profile, either a docker image containing all of the required software will be downloaded,
and converted to a Singularity image or a Singularity image downloaded directly before execution of the pipeline.

The latest version of Nextflow is not installed by default on the SAHMRI HPC cluster. You will need to install it into a directory you have write access to.
Follow these instructions from the Nextflow documentation.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline
has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an account to use the SAHMRI HPC cluster in order to run the pipeline. If in doubt contact the ICT Service Desk.
> NB: Nextflow will need to submit the jobs via SLURM to the SAHMRI HPC cluster and as such the commands above will have to be executed on the login
> node. If in doubt contact ICT.
