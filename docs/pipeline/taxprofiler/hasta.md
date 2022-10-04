# nf-core/configs: eva taxprofiler specific configuration

Extra specific configuration for taxprofiler pipeline

## Usage

To use, run the pipeline with `-profile hasta`.

This will download and launch the taxprofiler specific [`hasta.config`](../../../conf/pipeline/taxprofiler/hasta.config) which has been pre-configured with a setup suitable for the hasta cluster.

Example: `nextflow run nf-core/taxprofiler -profile hasta`

## taxprofiler specific configurations for hasta

Specific configurations for hasta has been made for taxprofiler.

### General profiles

- The general hasta profile runs with default nf-core/taxprofiler parameters, but with modifications to account for issues with: BBDUK and MALT.
