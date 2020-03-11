# nf-core/configs: shh eager specific configuration

Extra specific configuration for eager pipeline

## Usage

To use, run the pipeline with `-profile shh`.

This will download and launch the eager specific [`shh.config`](../../../conf/pipeline/eager/shh.config) which has been pre-configured with a setup suitable for the shh cluster.

Example: `nextflow run nf-core/eager -profile shh`

## eager specific configurations for shh

Specific configurations for shh has been made for eager.

* If running with the MALT module turned on, the MALT process by default will be sent  to the long queue with a resource requirement minimum of 725GB and 64 cores. If this fails, the process will be tried once more only and sent to the supercruncher queue. The module will not retry after this, and pipeline will fail.
