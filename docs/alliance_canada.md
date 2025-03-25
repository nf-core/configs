# nf-core/configs: Alliance Canada Configuration

Configuration for running nextflow on the clusters of the Digital Research Alliance of Canada. Invoke by specifying `-profile alliance_canada_beluga`, `-profile alliance_canada_narval`, `-profile alliance_canada_rorqual`, `-profile alliance_canada_graham`, `-profile alliance_canada_cedar` depending on which of the clusters you are working on. 

The name of the group under which you are working or whose resource allocation you want to use has to be supplied with `params.alliance_group_name` in your custom config or on the command line with `--alliance_group_name <def-user>`.

For detailed information on running nf-core pipelines on Alliance clusters, please visit the documentation:
https://docs.alliancecan.ca/wiki/Nextflow