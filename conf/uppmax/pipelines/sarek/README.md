# nf-core/configs: uppmax sarek specific configuration

Extra specific configuration for sarek pipeline

## Usage

To use, run the pipeline with `-profile uppmax`.

This will download and launch the sarek specific [`uppmax.config`](../../../conf/pipeline/sarek/uppmax.config) which has been pre-configured with a setup suitable for uppmax clusters.

Example: `nextflow run nf-core/sarek -profile uppmax`

## Sarek specific configurations for uppmax clusters

Specific configurations for uppmax clusters has been made for sarek.

- Set paths to reference genomes
