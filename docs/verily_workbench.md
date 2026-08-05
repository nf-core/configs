# nf-core/configs: Verily Workbench Configuration

Run nf-core pipelines on [Verily Workbench](https://workbench.verily.com/) using the Google Cloud Batch executor, by adding `-profile verily_workbench` to your run command.

The profile reads the project and worker service account from the environment variables that Workbench injects into every job (`GOOGLE_CLOUD_PROJECT`, `GOOGLE_SERVICE_ACCOUNT_EMAIL`), and targets the VPC network layout that Workbench provisions in each workspace. In most cases you only need to set a work directory and `--outdir`.

For a step-by-step walkthrough of running Nextflow on Verily Workbench, see the [hello-nf-on-vwb tutorial](https://github.com/verily-src/workbench-examples/tree/main/nextflow/hello-nf-on-vwb).

## Usage

Launch a pipeline from a Workbench workflow job with `verily_workbench` in the profiles field (compose it with `test` to run the bundled test dataset):

```
-profile test,verily_workbench
```

Because Batch has no local launch directory, both the work directory and `--outdir` must be Cloud Storage locations. Supply `--outdir` as a `gs://` path (e.g. via the job's parameters file); it is a per-run value and is intentionally not set by this profile.

## Required Parameters

### `--workdir_bucket`

Cloud Storage location for the Nextflow work directory, e.g. `gs://my-workspace-bucket/work`. On Workbench this is typically set for you from the job's output bucket.

## Optional Parameters

### `--project_id`

Google Cloud project in which Batch resources are created. Defaults to the `GOOGLE_CLOUD_PROJECT` environment variable set by Workbench.

### `--workers_service_account`

Service account used by the Batch worker VMs. Defaults to the `GOOGLE_SERVICE_ACCOUNT_EMAIL` environment variable set by Workbench.

### `--location`

Region where Batch provisions compute. Defaults to `us-central1`.

### `--use_spot`

Use Spot VMs when `true` (with up to 5 attempts). Defaults to `false`.

### `--boot_disk`

Boot disk size for worker VMs. Defaults to `100 GB`.

### `--use_private_ip`

Run worker VMs without external IP addresses. Defaults to `true`, matching the Workbench workspace network. When `true`, a Cloud NAT on the VPC is required for workers to reach the internet (e.g. to pull container images).

### `--custom_vpc`

VPC network for worker VMs, in the format `global/networks/[custom_VPC]`. Defaults to the network Workbench provisions in every workspace; override only if yours differs.

### `--custom_subnet`

Subnetwork for worker VMs, in the format `regions/[GCP_Region]/subnetworks/[custom_subnet]`. Defaults to the Workbench subnet for the selected `location` when left unset.

## Networking note

Worker VMs run without external IP addresses by default (`--use_private_ip`), so they reach the internet only through the Cloud NAT on the workspace VPC. Pulling large or numerous remote inputs directly from public URLs (for example a pipeline's default test-data on GitHub) can be throttled. For reliable runs, stage inputs and reference files in Cloud Storage and point the pipeline parameters at `gs://` paths.
