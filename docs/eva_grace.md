# nf-core/configs: EVA_GRACE Configuration

All nf-core pipelines have been successfully configured for use on the GRACE cluster at the [Max Planck Institute for Evolutionary Anthropology (MPI-EVA)](http://eva.mpg.de).

To use, run the pipeline with `-profile eva_grace`. You can further with optimise submissions by specifying which cluster queue you are using e,g, `-profile eva_grace`. This will download and launch the [`eva_grace.config`](../conf/eva_grace.config) which has been pre-configured with a setup suitable.

Using this profile, a docker image containing all of the required software will be downloaded, and converted to a `singularity` image before execution of the pipeline.
