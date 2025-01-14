# nf-core/configs: FGCZ Configuration

Configuration file to run nf-core pipelines on the cluster of the [Functional Genomics Center Zurich](https://fgcz.ch/), a research and training facility of the ETH Zürich and the University of Zurich.

Note that, at present, this config has only been tested with `nf-core/viralrecon` and `nf-core/atacseq`, but should function similarly for other nf-core pipelines.

To use, run the pipeline with `-profile fgcz`. This will download and launch the profile.config which has been pre-configured with a setup suitable for the FGCZ cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to an apptainer image before execution of the pipeline. **This requires a local installation of apptainer**. It is easiest to submit the pipeline from a compute node. Once the image is cached, you can also submit from the login node.
The config places the apptainer cache in your `/srv/GT/software/apptainer/cache` directory for access by all projects.

Example:

```shell
nextflow run -profile fgcz ...
```

## Before running the pipeline

You may need to load the jdk module before running any nextflow pipelines.

```shell
module load Dev/jdk/21
```
