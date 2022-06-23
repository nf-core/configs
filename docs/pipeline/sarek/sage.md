# nf-core/configs: Sage Bionetworks Sarek-Specific Configuration

To use this custom configuration, run the pipeline with `-profile sage`. This will download and load the [`sage.config`](../conf/sage.config), which contains a number of optimizations relevant to Sage employees running workflows on AWS (_e.g._ using Nextflow Tower). This profile will also load any applicable pipeline-specific configuration.

In addition to the global configuration described [here](../../sage.md), this Sarek-specific configuration includes the following tweaks:

- Define the `check_max()` function, which is missing in Sarek v2.
