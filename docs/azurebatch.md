# nf-core/configs: azurebatch Configuration

To be used with the `azurebatch` profile by specifying the `-profile azurebatch` when running nf-core pipelines.
Custom queue and storage need to be supplied with `params.az_location`, `params.batch_name`, `params.batch_key`, `params.storage_name`, `params.sas_token`.

## Azure Batch Setup

Please refer to the [Nextflow](https://www.nextflow.io/docs/edge/azure.html) documentation which describe how to setup the Azure Batch environment.
