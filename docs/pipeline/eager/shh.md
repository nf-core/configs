# nf-core/configs: shh eager specific configuration

Extra specific configuration for eager pipeline

## Usage

To use, run the pipeline with `-profile shh`.

This will download and launch the eager specific [`shh.config`](../conf/pipeline/eager/shh.config) which has been pre-configured with a setup suitable for the shh cluster.

Example: `nextflow run nf-core/eager -profile shh`

## eager specific configurations for shh

Specific configurations for shh has been made for eager.

* Running with the MALT module turned on, will by default be sent either to long or supercruncher queues with a minimum of 756GB and 64 cores.
