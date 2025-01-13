# nf-core/configs: kaust mag specific configuration

Extra specific configuration for [nf-co.re/mag](https://nf-co.re/mag) pipeline

## Usage

To use, run the pipeline with `-profile kaust`.

This will download and launch the mag specific [`kaust.config`](../../../conf/pipeline/mag/kaust.config) which has been pre-configured with a setup suitable for the Ibex cluster.

Example: `nextflow run nf-core/mag -profile kaust`

## mag specific configurations for kaust

Specific configurations for kaust has been made for mag, primarily increasing the default resource allocations especeially for high demand processes. 
