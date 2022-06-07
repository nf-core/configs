# nf-core/configs: FGCZ Configuration

Configuration file to run nf-core pipelines on the cluster of the [Functional Genomics Center Zurich](https://fgcz.ch/), a research and training facility of the ETH Zürich and the University of Zurich.

Note that, at present, this config has only been tested with nf-core/viralrecon, but should function similarly for other nf-core pipelines.

To use, run the pipeline with `-profile fgcz`. This will download and launch the profile.config which has been pre-configured with a setup suitable for the FGCZ cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. **This requires a local installation of singularity**. It is easiest to submit the pipeline from a compute node. Once the image is cached, you can also submit from the login node.
The config places the singularity cache in your /srv/GT/ directory for access by all projects.

Example: /usr/local/ngseq/src/nextflow/nextflow run -profile fgcz

## Before running the pipeline

Load the following modules before running any nf-core pipelines.

```bash
module load Dev/Python/3.8.3
```
