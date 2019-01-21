# nf-core/configs: MUNIN Configuration

All nf-core pipelines have been successfully configured for use on the MUNIN cluster aka big iron.

To use, run the pipeline with `-profile munin`. This will download and launch the [`munin.config`](../conf/munin.config) which has been pre-configured with a setup suitable for the MUNIN cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Example: `nextflow run -profile munin`

## Docker

It is also possible to execute the pipeline using Docker.

Example: `nextflow run -profile munin,docker`

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on the MUNIN cluster so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

>NB: You will need an account to use the MUNIN cluster in order to run the pipeline. If in doubt contact @szilva.
