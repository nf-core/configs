# nf-core/configs: INCLIVA Configuration

All nf-core pipelines have been successfully configured for use on the vlinuxcervantes3 & vlinuxcervantes4 servers at the INCLIVA Health Research Institute. Using this config file will automatically detect which one you are working on, so you do not need to specify it yourself.

To use, run the pipeline with `-profile incliva`. This will download and launch the [`incliva.config`](../conf/incliva.config) which has been pre-configured with a setup suitable for the vlinuxcervantes3 & vlinuxcervantes4 servers. When using this profile, if Singularity images have not been downloaded already, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. Downloaded images can be checked in the singularity_path directory defined in the config file.

## Running the workflow on the INCLIVA vlinuxcervantes3 & vlinuxcervantes4 servers

Nextflow and Singularity are needed to run any nf-core workflow:

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)
- Install Singularity : [here](https://docs.sylabs.io/guides/3.0/user-guide/installation.html)

By default, Nextflow uses the local executor. The processes are parallelised by spawning multiple threads, taking advantage of the multi-core architecture of the CPU.
