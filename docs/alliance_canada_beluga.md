# nf-core/configs: Alliance Canada Beluga Configuration

Configuration for running nextflow on the Beluga cluster of the Digital Research Alliance of Canada. Invoke by specifying `-profile alliance_canada_beluga`.

You also need to supply the name of the group under which you are working or whose resource allocation you want to use with `params.alliance_group_name`. This can be supplied in your custom config or on the command line with `--alliance_group_name <def-user>`.

For detailed information on running nf-core pipelines on Alliance clusters, please visit the documentation:
https://docs.alliancecan.ca/wiki/Nextflow