# nf-core/configs: SHH Configuration

All nf-core pipelines have been successfully configured for use on the Department of Archaeogenetic's SDAG cluster at the [Max Planck Institute for the Science of Human History (MPI-SHH)](http://shh.mpg.de).

To use, run the pipeline with `-profile shh`. This will download and launch the [`shh.config`](../conf/shh.config) which has been pre-configured with a setup suitable for the SDAG cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Note that the configuration file is currently optimised for `nf-core/eager`. It
will submit to the medium queue but with a walltime of 48 hours.

## Preparation
Before running the pipeline you will need to create a the following folder in your `/projects1/users/` directory. This will be used to store the singularity software images, which will take up too much space for your home directory.

This should be named as follows, replacing `<your_user>` with your username:

```bash
"/projects1/users/<your_user>/nextflow/nf_cache/singularity/"
```

>NB: You will need an account and VPN access to use the cluster at MPI-SHH in order to run the pipeline. If in doubt contact IT.

>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the lhead nodes. If in doubt contact IT.
