# nf-core/configs: azurebatch sarek specific configuration

Specific configuration for [nf-co.re/sarek](https://nf-co.re/sarek) pipeline

## Usage

To use, run nextflow with the pipeline using `-profile azurebatch`.

This will download and launch the rnaseq specific [`azurebatch_pools_Ddv4.config`](../../../conf/pipeline/sarek/azurebatch_pools_Ddv4.config) which has been pre-configured with a setup suitable for Azure Batch.

Before the first use check your Azure Batch account quota for Ddv4 Series, adjust it if needed.

Example: `nextflow run nf-core/sarek -profile azurebatch`
