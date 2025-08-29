# nf-core/configs: eva mag specific configuration

Extra specific configuration for mag pipeline

## Usage

To use, run the pipeline with `-profile eva`.

This will download and launch the mag specific [`eva.config`](../../../conf/pipeline/mag/eva.config) which has been pre-configured with a setup suitable for the MPI-EVA cluster.

Example: `nextflow run nf-core/mag -profile eva`

## mag specific configurations for eva

Specific configurations for eva has been made for mag, primarily adjusting SGE memory requirements of Java tools (e.g. FastQC).
