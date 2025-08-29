# nf-core/configs: eva taxprofiler specific configuration

Extra specific configuration for taxprofiler pipeline

## Usage

To use, run the pipeline with `-profile eva`.

This will download and launch the taxprofiler specific [`eva.config`](../../../conf/pipeline/taxprofiler/eva.config) which has been pre-configured with a setup suitable for the MPI-EVA cluster.

Example: `nextflow run nf-core/taxprofiler -profile eva`

## taxprofiler specific configurations for eva

Specific configurations for eva has been made for taxprofiler.

### General profiles

- The general MPI-EVA profile runs with default nf-core/taxprofiler parameters, but with modifications to account for issues SGE have with Java and python tools, nameling: BBDUK, MALT, MetaPhlAn3, and MEGAN
