# nf-core/configs: Alliance Canada Configuration

Configuration for running nextflow on the clusters of the Digital Research Alliance of Canada. Invoke by specifying `-profile alliance_canada`.

You also need to supply the name of the group under which you are working or whose resource allocation you want to use by running `export SLURM_ACCOUNT=<def-user>` before you run any nf-core pipeline. If you run nf-core frequently and always use the same resource allocation, you may find it more convenient to add the `SLURM_ACCOUNT` environment variable to your `~/.bashrc` file.

For detailed information on running nf-core pipelines on Alliance clusters, please visit the documentation:
https://docs.alliancecan.ca/wiki/Nextflow

If you run into issues, please contact Alliance Support:
https://docs.alliancecan.ca/wiki/Technical_support
