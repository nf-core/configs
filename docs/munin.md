# nf-core/configs: MUNIN Configuration

All nf-core pipelines have been successfully configured for use on the MUNIN cluster.

## Usage

To use, run the pipeline with `-profile munin`.

This will download and launch the [`munin.config`](../conf/munin.config) which has been pre-configured with a setup suitable for the MUNIN cluster.

Example: `nextflow run -profile munin`

### Singularity

This is the default behavior of this configuration profile.

Using this profile, if no singularity image are available, one will be downloaded from dockerhub, and converted to a Singularity image before execution of the pipeline.

It is also possible to specify the singularity profile:

Example: `nextflow run -profile munin,singularity`

### Docker

It is also possible to execute the pipeline using Docker.

Using this profile, if no docker image are available, one will be downloaded from dockerhub before execution of the pipeline.

Example: `nextflow run -profile munin,docker`

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on the MUNIN cluster so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

> NB: You will need an account to use the MUNIN cluster in order to run the pipeline. If in doubt contact @szilva.
