# nf-core/configs: Fred Hutch Cancer Center Configuration

Configuration file to run nf-core pipelines on the cluster of the [Fred Hutchinson Cancer Center](https://www.fredhutch.org/).

# Before running the pipeline

You need to have Nextflow and Apptainer available in your path. The easiest way to do this is through modules. 

```shell
module load Nextflow
module load Apptainer
```

# Quick start

```shell
nextflow run -profile fred_hutch ...
```

# Additional resources

https://sciwiki.fredhutch.org/datascience/using_workflows/
https://sciwiki.fredhutch.org/compdemos/nextflow/
