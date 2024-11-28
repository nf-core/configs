# nf-core/configs: uppmax ampliseq specific configuration

Extra specific configuration for the ampliseq pipeline.

## Usage

To use, run the pipeline with `-profile uppmax`.

This will download and launch the ampliseq specific [`uppmax.config`](../../../conf/pipeline/ampliseq/uppmax.config) which has been pre-configured with a setup suitable for the UPPMAX cluster.

Example: `nextflow run nf-core/ampliseq -profile uppmax`

## ampliseq specific configurations for uppmax

Specific configurations for UPPMAX has been made for ampliseq.

- Makes sure that a fat node is allocated for training and applying a Bayesian classifier.
