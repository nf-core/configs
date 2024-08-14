# nf-core/configs: MPCDF Viper Configuration

All nf-core pipelines have been successfully configured for use on the HPCs at [Max Planck Computing and Data Facility](https://www.mpcdf.mpg.de/).

> :warning: these profiles are not officially supported by the MPCDF.

To run Nextflow, the `jdk` and `apptainer` modules must be loaded.

This `mpcdf_viper` config is for `viper`. For `raven` see the [`mpcdf`](mpcdf.md) profile.

All profiles use `apptainer` as the corresponding containerEngine.
To prevent repeatedly downloading the same apptainer image for every pipeline run, for all profiles we recommend specifying a cache location in your `~/.bash_profile` with the `$NXF_APPTAINER_CACHEDIR` bash variable.

> NB: Nextflow will need to submit the jobs via SLURM to the clusters and as such the commands above will have to be executed on one of the head nodes. Check the [MPCDF documentation](https://www.mpcdf.mpg.de/services/computing).
