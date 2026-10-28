# nf-core/configs: Fred Hutch Cancer Center Configuration

Configuration file to run nf-core pipelines on the cluster of the [Fred Hutchinson Cancer Center](https://www.fredhutch.org/). Note that the default `workDir` will be based on your `$TMPDIR` if available (e.g. nextflow is launched in an interactive session). This is to avoid large tmp file buildup in hidden nextflow directories, but may prevent resuming pipelines. You can override this by setting `-work-dir <your directory>` at the command line when calling nextflow run.

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
