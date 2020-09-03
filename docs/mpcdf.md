# nf-core/configs: MPCDF Configuration

All nf-core pipelines have been successfully configured for use on the HPCs at [Max Planck Computing and Data Facility](https://www.mpcdf.mpg.de/).

> :warning: these profiles are not officially supported by the MPCDF.

To run Nextflow, the `jdk` module must be loaded. To use the nf-core profile(s), run the pipeline with `-profile <cluster>,mpcdf`.

Currently the following clusters are supported: cobra, draco* (* coming soon)

>NB: Nextflow will need to submit the jobs via SLURM to the clusters and as such the commands above will have to be executed on one of the head nodes. Check the [MPCDF documentation](https://www.mpcdf.mpg.de/services/computing).

# cobra

Cobra does not currently support singularity, therefore the anaconda/module is loaded for each process.

Due to this, we also recommend setting the `$NXF_CONDA_CACHEDIR` to a location of your choice to store all environments (so to prevent nextflow building the environment on every run).

To use: `-profile cobra,mpcdf`

Sets the following parameters:

Maximum parallel running jobs: 8
Max. memory: 750.GB
Max. CPUs: 80
Max. walltime: 24.h

# draco

