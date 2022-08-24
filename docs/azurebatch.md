# nf-core/configs: azurebatch Configuration

To be used with the `azurebatch` profile by specifying the `-profile azurebatch` when running nf-core pipelines.
Custom queue and storage need to be supplied with `params.az_location`, `params.batch_name`, `params.batch_key`, `params.storage_name`, `params.sas_token`.

## Required Parameters

### `--storage_name`

Name of Azure blob storage account.

### `--storage_key`

Access key to Azure blob storage account. `--storage_key` or `--storage_sas` are required, but not both.

### `--storage_sas`

SAS for access to Azure blob storage account (see relevant permissions on Nextflow documentation). `--storage_key` or `--storage_sas` are required, but not both.

### `--az_location`

The Azure Batch region where the computation is executed in VMs. Default (`westus2`).

### `--batch_name`

The Azure Batch account name.

### `--batch_key`

The Azure Batch account key.

### `-w`

The Azure Blob container to be used as Nextflow work directory (`-w az://work`).

### `--vm_type`

VM size to use with Nextflow autopool or when creating a worker pool in Azure Batch. Make sure your Azure account has sufficient quota. Defaults to `Standard_D8s_v3`. See [Azure VM Size documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes) for more information.

### `--autopoolmode`

Whether to use Nextflow autopool mode which creates an autoscaling pool for running Nextflow jobs. Defaults to `true`.

### `--allowpoolcreation`

Allow Nextflow to create a pool for running Nextflow jobs. Defaults to `true`.

### `--deletejobs`

Allow Nextflow to delete pools after completion. Defaults to `true`.

### `--az_worker_pool`

Select an existing pool by name to run Nextflow jobs on. Defaults to `auto` (matching `--autopoolmode`).

### `--acr_registry`

URL to Azure container registry for private docker images.

### `--acr_username`

Username to access private Azure container registry.

### `--acr_password`

Password to access private Azure container registry.

## Azure Batch Setup

Please refer to the [Nextflow](https://www.nextflow.io/docs/edge/azure.html) documentation which describe how to setup the Azure Batch environment.
