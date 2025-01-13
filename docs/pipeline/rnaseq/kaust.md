# nf-core/configs: kaust rnaseq specific configuration

Specific configuration for [nf-co.re/rnaseq](https://nf-co.re/rnaseq) pipeline

## Usage

To use, run the pipeline with `-profile kaust`.

This will download and launch the rnaseq specific [`kaust.config`](../../../conf/pipeline/rnaseq/kaust.config) which has been pre-configured with a setup suitable for the Ibex cluster.

Example: `nextflow run nf-core/rnaseq -profile kaust`

## rnaseq specific configurations for kaust

Specific configurations for kaust has been made for rnaseq, primarily increasing the default resource allocations especeially for high demand processes. 
