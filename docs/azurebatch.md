# nf-core/configs: azurebatch Configuration

To be used with the `azurebatch` profile by specifying the `-profile azurebatch` when running nf-core pipelines.
Custom queue and storage need to be supplied with `params.az_location`, `params.batch_name`, `params.batch_key`, `params.storage_name`, `params.sas_token`.

## Required Parameters

### `--az_location`

The Azure Batch region where the computation is executed in VMs. Default (`westus2`).

### `--batch_name`

The Azure Batch account name.

### `--batch_key`

The Azure Batch account key.

### `--storage_name`

The Azure Blob Storage name. Example is currently [Illumina Platinum Genomes](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-illumina-platinum-genomes?tabs=azure-storage). **This must be changed to your specific storage account.**

### `--sas_token`

The Azure Blob Storage shared access signature token.  Example is currently [Illumina Platinum Genomes](https://docs.microsoft.com/en-us/azure/open-datasets/dataset-illumina-platinum-genomes?tabs=azure-storage). **This must be changed to your specific storage account.**

## Optional Parameters

### `--work_dir`

The Azure Blob container to be used as Nextflow work directory. Can also be specified with (`-w az://work`).

## Azure Batch Setup

Please refer to the [Nextflow](https://www.nextflow.io/docs/edge/azure.html) documentation which describe how to setup the Azure Batch environment.
