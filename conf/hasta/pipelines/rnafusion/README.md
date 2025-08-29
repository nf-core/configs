# nf-core/configs: HASTA rnafusion specific configuration

Extra specific configuration for rnafusion pipeline

## Usage

To use, run the pipeline with `-profile hasta`.

This will download and launch the rnafusion specific [`hasta.config`](../../../conf/pipeline/rnafusion/munin.config) which has been pre-configured with a setup suitable for the `HASTA` cluster.

Example: `nextflow run nf-core/rnafusion -profile hasta`

## rnafusion specific configurations for HASTA

Specific configurations for `HASTA` has been made for rnafusion.

- Always run all the analysis steps (all = true)
- Use trimming (trim = true)
- Take the fusions identified by at least 2 fusion detection tools to the fusioninspector analysis (fusioninspector_filter = true)
