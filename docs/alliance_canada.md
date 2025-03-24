# nf-core/configs: Alliance Canada Configuration

Configuration for running nextflow on the clusters of the Digital Research Alliance of Canada. Invoke by specifying `-profile alliance_canada,<beluga/narval/cedar/graham>` where the second entry is the name of the cluster on which you are working. 

The name of the group under which you are working or whose resource allocation you want to use has to be supplied with `params.alliance_group_name` in your custom config or on the command line with `--alliance_group_name <def-user>`.

For detailed information on running nf-core pipelines on Alliance clusters, please visit the documentation:
https://docs.alliancecan.ca/wiki/Nextflow