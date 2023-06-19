# nf-core/configs: MPCDF Configuration

All nf-core pipelines have been successfully configured for use on the HPCs at [Max Planck Computing and Data Facility](https://www.mpcdf.mpg.de/).

> :warning: these profiles are not officially supported by the MPCDF.

To run Nextflow, the `jdk` module must be loaded. To use the nf-core profile(s), run the pipeline with `-profile mpcdf,<cluster>`.

Currently profiles for the following clusters are supported: `cobra`, `raven`

All profiles use `singularity` as the corresponding containerEngine. To prevent repeatedly downloading the same singularity image for every pipeline run, for all profiles we recommend specifying a cache location in your `~/.bash_profile` with the `$NXF_SINGULARITY_CACHEDIR` bash variable.

> NB: Nextflow will need to submit the jobs via SLURM to the clusters and as such the commands above will have to be executed on one of the head nodes. Check the [MPCDF documentation](https://www.mpcdf.mpg.de/services/computing).

## Global Profiles

### cobra

To use: `-profile mpcdf,cobra`

Sets the following parameters:

- Maximum parallel running jobs: 8
- Max. memory: 725.GB
- Max. CPUs: 40
- Max. walltime: 24.h

### raven

To use: `-profile mpcdf,raven`

Sets the following parameters:

- Maximum parallel running jobs: 8
- Max. memory: 2000000.MB (2.TB)
- Max. CPUs: 72
- Max. walltime: 24.h

## Pipeline Profiles

### nf-core/eager

We offer a pipeline specific profile optimised for [nf-core/eager](https://nf-co.re/eager)

- Maximum parallel running jobs: 30

### nf-core/rnaseq

We offer a pipeline specific profile optimised for [nf-core/rnaseq](https://nf-co.re/rnaseq)
