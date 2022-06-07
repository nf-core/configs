# nf-core/configs: mpcdf eager specific configuration

Extra specific configuration for eager pipeline for the `cobra` cluster of the MPCDF

## Usage

To use, run the pipeline with `-profile mpcdf,cobra`.

This will download and launch the eager specific [`mpcdf.config`](../../../conf/pipeline/eager/mpcdf.config) which has been pre-configured with a setup suitable for the mpcdf cluster.

Currently this only applies to the `cobra` cluster, where maximum resources are adjusted accordingly.
