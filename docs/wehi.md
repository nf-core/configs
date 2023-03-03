# nf-core/configs: WEHI Milton HPC Configuration

nf-core pipelines have been successfully configured for use on the Milton HPC cluster at [WEHI](https://www.wehi.edu.au/).

To use the WEHI profile, run the pipeline with `-profile wehi`. This will download and apply [`wehi.config`](../conf/wehi.config) which has been pre-configured for the WEHI HPC cluster "Milton". Using this profile, all Nextflow processes will be run within singularity containers, which will be downloaded and converted from docker containers as required.

> Note: the WEHI profile is based on the 'regular' SLURM partition. Should you require resources outside of these limits (e.g. more memory, more walltime or gpus) you will need to provide a custom config specifying an appropriate SLURM partition (e.g. 'bigmem', 'long' or 'gpuq').

A Nextflow module is available on the Milton HPC cluster, to use run `module load nextflow` or `module load nextflow/<version>` prior to running your pipeline. In order to load this module, you with require a "VAST" scratch directory, which will be used as the the default work directory for nextflow pipelines. Please contact WEHI Research Computing for assistance with setting up a VAST scratch directory.
