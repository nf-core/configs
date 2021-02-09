# nf-core/configs: Google Cloud Life Sciences Configuration

To be used with the `google` profile by specifying the `-profile google` when running nf-core pipelines.

![Google Cloud](images/google-cloud-logo.svg "https://cloud.google.com/life-sciences/docs/tutorials/nextflow")

## Quick Start

```bash
GOOGLE_APPLICATION_CREDENTIALS=<your_key>.json
NXF_MODE=google
nextflow run nf-core/rnaseq -profile test,google --google_bucket <gs://your_bucket/work>
```

### Required Parameters

#### `--google_bucket`

The Google Cloud Storage bucket location to be used as a Nextflow work directory. Can also be specified with (`-w gs://your_bucket/work`).

### Optional Parameters

#### `--google_zone`

The Google zone where the computation is executed in Compute Engine VMs. Multiple zones can be provided separating them by a comma. Default (`europe-west2-c`).

#### `--google_preemptible`

Enables the usage of preemptible virtual machines with a retry error statergy for up to 5 retries. Default (`true`).

#### `--google_debug`

Copies the /google debug directory from the VM to the task bucket directory. Useful for debugging. Default (`false`).

## Cloud Life Sciences Setup

Please refer to the [Google Cloud](https://cloud.google.com/life-sciences/docs/tutorials/nextflow) and [Nextflow](https://www.nextflow.io/docs/latest/google.html#cloud-life-sciences) documentation which describe how to setup the Google Cloud environment.
