# nf-core/configs: MUNIN rnafusion specific configuration

Extra specific configuration for rnafusion pipeline

## Usage

To use, run the pipeline with `-profile munin`.

This will download and launch the rnafusion specific [`munin.config`](../../../conf/pipeline/rnafusion/munin.config) which has been pre-configured with a setup suitable for the `MUNIN` cluster.

Example: `nextflow run nf-core/rnafusion -profile munin`

## rnafusion specific configurations for MUNIN

Specific configurations for `MUNIN` has been made for rnafusion.

- `cpus`, `memory` and `time` max requirements.
- Paths to specific references and indexes
