# nf-core/configs: WEHI Milton HPC Configuration

All nf-core pipelines have been successfully configured for use on the Milton HPC cluster at [WEHI](https://www.wehi.edu.au/).

To use the WEHI profile, run the pipeline with `-profile wehi`. This will download and launch the [`wehi.config`](../conf/wehi.config) which has been pre-configured
with a setup suitable for the WEHI HPC cluster. Using this profile, either a docker image containing all of the required software will be downloaded,
and converted to a Singularity image or a Singularity image downloaded directly before execution of the pipeline. Note that the WEHI profile is based on the 'regular' SLURM partition, should you require resources outside of this (e.g. more memory, more walltime or gpus) you will need to provide a custom config specifying an appropriate slurm partition. 

A Nextflow module is available on the Milton HPC cluster, to use simply execute `module load nextflow` or `module load nextflow/<version>` prior to running your pipeline. In order to load this module, you with require a 'VAST' scratch directory, which will be used as the the default work directory for nextflow pipelines. Please contact WEHI Research Computing for assistance with setting up a VAST scratch directory.
