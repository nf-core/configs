# nf-core/configs: Cambridge HPC Configuration

All nf-core pipelines have been successfully configured for use on the Cambridge HPC cluster at the [The University of Cambridge](https://www.cam.ac.uk/).  
To use, run the pipeline with `-profile cambridge`. This will download and launch the [`cambridge.config`](../conf/cambridge.config) which has been pre-configured
with a setup suitable for the Cambridge HPC cluster. Using this profile, either a docker image containing all of the required software will be downloaded,
and converted to a Singularity image or a Singularity image downloaded directly before execution of the pipeline.

The latest version of Nextflow is not installed by default on the Cambridge HPC cluster. You will need to install it into a directory you have write access to.
Follow these instructions from the Nextflow documentation.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline
has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an account to use the Cambridge HPC cluster in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via SLURM to the Cambridge HPC cluster and as such the commands above will have to be executed on one of the login
> nodes. If in doubt contact IT.
