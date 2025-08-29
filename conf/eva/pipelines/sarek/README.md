# nf-core/configs: eva sarek specific configuration

Extra specific configuration for sarek pipeline

## Usage

To use, run the pipeline with `-profile eva`.

This will download and launch the sarek specific [`eva.config`](../../../conf/pipeline/sarek/eva.config) which has been pre-configured with a setup suitable for the MPI-EVA cluster.

Example: `nextflow run nf-core/sarek -profile eva`

## sarek specific configurations for eva

Specific configurations for eva has been made for sarek.

### General profiles

- The general MPI-EVA profile runs with default nf-core/sarek parameters, but with modifications to account for issues SGE have with Java tools.
