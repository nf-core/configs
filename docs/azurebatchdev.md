# nf-core/configs: azurebatch Configuration

To be used with the `azurebatchdev` profile by specifying the `-profile azurebatchdev` when running nf-core pipelines.
Custom queue and storage need to be supplied with `params.az_location`, `params.batch_name`, `params.storage_name`, `params.principal_id`, `params.principal_secret`, `params.tenant_id`

## Required Parameters

### `--storage_name`

Name of Azure blob storage account.

### `--az_location`

The Azure Batch region where the computation is executed in VMs. Default (`westus2`).

### `--principal_id`

The service principal client ID.

### `--principal_secret`

The service principal client secret.

### `--tenant_id`

The Azure tenant ID.

### `-w`

The Azure Blob container to be used as Nextflow work directory (`-w az://work`).

### `--autopoolmode`

Whether to use Nextflow autopool mode which creates an autoscaling pool for running Nextflow jobs. Defaults to `false`.

### `--allowpoolcreation`

Allow Nextflow to create a pool for running Nextflow jobs. Defaults to `false`.

### `--deletejobs`

Allow Nextflow to delete pools after completion. Defaults to `true`.

### `--acr_registry`

URL to Azure container registry for private docker images.

### `--acr_username`

Username to access private Azure container registry.

### `--acr_password`

Password to access private Azure container registry.

## Azure Batch Setup

Please refer to the [Nextflow](https://www.nextflow.io/docs/edge/azure.html) documentation which describe how to setup the Azure Batch environment.
