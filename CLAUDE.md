# How this repo is used currently

In each nf-core con or pipeline, these lines are included. So basically, nf-core custom.config and the pipeline rnaseq.config will get pulled in.

```nextflow
// Load nf-core custom profiles from different institutions

// If params.custom_config_base is set AND either the NXF_OFFLINE environment variable is not set or params.custom_config_base is a local path, the nfcore_custom.config file from the specified base path is included.
// Load nf-core/rnaseq custom profiles from different institutions.
includeConfig params.custom_config_base && (!System.getenv('NXF_OFFLINE') || !params.custom_config_base.startsWith('http')) ? "${params.custom_config_base}/nfcore_custom.config" : "/dev/null"

// Load nf-core/rnaseq custom profiles from different institutions.
includeConfig params.custom_config_base && (!System.getenv('NXF_OFFLINE') || !params.custom_config_base.startsWith('http')) ? "${params.custom_config_base}/pipeline/rnaseq.config" : "/dev/null"
```
