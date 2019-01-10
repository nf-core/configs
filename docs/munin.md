# nf-core/configs: MUNIN Configuration

All nf-core pipelines have been successfully configured for use on the MUNIN cluster aka big iron.

To use, run the pipeline with `-profile munin`. This will download and launch the [`munin.config`](../conf/munin.config) which has been pre-configured with a setup suitable for the MUNIN cluster. Using this profile, Nextflow will download either docker or singularity image with all of the required software before execution of the pipeline.

## Running pipeline with Docker

>NB: Make sure when running pipeline using docker to be in docker group

```groovy
// https://github.com/nextflow-io/nextflow/issues/572
docker {
  mountFlags = 'z'
  fixOwnership = true
}
```

## Running pipeline with Singularity

```groovy
// https://github.com/nextflow-io/nextflow/issues/572
singularity {
  autoMounts = true
}
```

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has been made available on MUNIN cluster so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

>NB: You will need an account to use the munin cluster in order to run the pipeline. If in doubt contact @szilva.