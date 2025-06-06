# nf-core/configs: Fred Hutch Cancer Center Configuration

Configuration file to run nf-core pipelines on the cluster of the [Fred Hutchinson Cancer Center](https://www.fredhutch.org/).

# Before running the pipeline

You may need to load the Nextflow module or otherwise have a Nextflow executable in your path. Apptainer is also required, but is specified in the default `beforeScript` of this configuration, so you shouldn't need to load the module manually, but if you encounter issues with containers, consider loading it yourself. 

```shell
module load Nextflow
```

# Quick start

```shell
nextflow run -profile fred_hutch ...
```

# Additional resources

https://sciwiki.fredhutch.org/datascience/using_workflows/
https://sciwiki.fredhutch.org/compdemos/nextflow/
