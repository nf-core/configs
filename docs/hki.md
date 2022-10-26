# nf-core/configs: HKI Configuration

All nf-core pipelines have been successfully configured for use on clusters at the [Leibniz Institute for Natural Product Research and Infection Biology Hans Knöll Institute](https://www.leibniz-hki.de/en).

To use, run the pipeline with `-profile hki,<cluster>`. This will download and launch the [`hki.config`](../conf/hki.config) which contains specific profiles for each cluster. The number of parallel jobs that run is currently limited to 8.

The currently available profiles are:

- apate (uses singularity, cleanup set to true by default)
- arges (uses singularity, cleanup set to true by default)
- aither (uses singularity, cleanup set to true by default)
- debug (sets cleanup to false for debugging purposes, use e.g. `profile hki,<cluster>,debug`)

Note that Nextflow is not necessarily installed by default on the HKI HPC cluster(s). You will need to install it into a directory you have write access to.
Follow these instructions from the Nextflow documentation.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline
has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> NB: You will need an account to use the HKI HPC clusters in order to run the pipeline. If in doubt contact the ICT Service Desk.
> NB: Nextflow will need to submit the jobs via SLURM to the HKI HPC clusters and as such the commands above will have to be executed on the login
> node. If in doubt contact ICT.
