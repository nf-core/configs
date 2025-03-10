# nf-core/configs: UNIBE_IBU Configuration

Configuration file to run nf-core pipelines on the cluster of the [Interfaculty Bioinformatics Unit](https://www.bioinformatics.unibe.ch/) of the University of Bern.

To use, run the pipeline with `-profile unibe_ibu` (one hyphen). This requires a local installation of singularity, so you have to run the pipeline from a compute node.

For accounting, you can specify an IBU project id with the --project flag (two hyphens) when launching Nextflow. If no project is specified, it will default to the username.
