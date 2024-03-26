# nf-core/configs: azurebatch rnaseq specific configuration

Specific configuration for [nf-co.re/rnaseq](https://nf-co.re/rnaseq) pipeline

## Usage

To use, run nextflow with the pipeline using `-profile azurebatch`.

This will download and launch the rnaseq specific [`azurebatch_pools_Edv4.config`](../../../conf/pipeline/rnaseq/azurebatch_pools_Edv4.config) which has been pre-configured with a setup suitable for Azure Batch. Low-cost virtual machines are used by default.

To use dedicated virtual machines changes are required (see [`azurebatch_pools_Edv4.config`](../../../conf/pipeline/rnaseq/azurebatch_pools_Edv4.config) header). Before the first use on dedicated nodes check your Azure Batch account quota for Edv4 Series, adjust it if needed.

Example: `nextflow run nf-core/rnaseq -profile azurebatch`
