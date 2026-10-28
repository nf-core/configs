# nf-core/configs: uppmax sarek specific configuration

Extra specific configuration for sarek pipeline

## Usage

To use, run the pipeline with `-profile m3c`.

This will download and launch the sarek specific [`m3c.config`](../../../conf/pipeline/sarek/m3c.config) which has been pre-configured with a setup suitable for m3cx clusters.

Example: `nextflow run nf-core/sarek -profile m3c`

## Sarek specific configurations for the M3 cluster

Specific configurations for the M3 Cluster has been made for sarek.

- Runtime for `process_high`:
  In nf-core/sarek the time is set to `32.h`, that means all jobs are being sent to `cpu3-long` which is not needed and stalls the pipeline.
  Therefore we set the time to `24.h` and only processes with label `process_long` that need more time will be sent to `cpu3-long`.
