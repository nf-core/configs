# nf-core/configs: googlebatch Configuration

To be used with the `googlebatch` profile by specifying the `-profile googlebatch` when running nf-core pipelines.
project id and workdir bucket need to be supplied with `params.project_id`, `params.workdir_bucket `.

## Required Parameters

### `--project_id`

Project id of the project where compute resources will be created

### `--workdir_bucket`

Cloud Storage Bucket to be used for the workdir

## Optional Parameters

### `--location`

The region where compute resources will be provisioned. If not specified, it will default to `us-central1`.

### `--use_spot`

Defines which provisioning model to be used. When set to false, standard VM instances will be used. Defaults to `true`.

### `--boot_disk`

Defines the size of boot disk on compute instances. Defaults to `100GB`.

### `--workers_service_account`

Defines which service account will be used by Compute instances running the pipeline. If not specified, the default compute service account of the project will be used.

### `--use_private_ip`

Defines whether real IP addresses will be assigned to compute instance runningn the pipeline. Defaults to `false`. If set to `true` a Cloud NAT needs to be provisioned on the same VPC to enable workers to access the Internet to download any necessary artifacts such as container images or communicate with Tower if it is configured. It is recommeneded to use private IP addresses.

### `--custom_vpc`

If you don't want to use the default VPC network or if it is not available, you need to specify both the `custom_vpc` and the `custom_subnet`. Custom VPC should be in this format `global/networks/[custom_VPC]`.

### `--custom_subnet`

When `custom_vpc` is specified, you must also specify the `custom_subnet`. Custom subnet should be in this format `regions/[GCP_Region]/subnetworks/[custom_subnet]`.

## Gogole Batch Setup

Please refer to the [Nextflow](https://www.nextflow.io/docs/latest/google.html) documentation which describe how to setup the Google Cloud environment.
