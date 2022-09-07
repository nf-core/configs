# nf-core/configs: UNIBE_IBU Configuration

Configuration file to run nf-core pipelines on the cluster of the [Interfaculty Bioinformatics Unit](https://www.bioinformatics.unibe.ch/) of the University of Bern.

To use, run the pipeline with `-profile unibe_ibu`. This will download and launch the profile.config which has been pre-configured with a setup suitable for the IBU cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. **This requires a local installation of singularity**. It is easiest to submit the pipeline from a compute node. Once the image is cached, you can also submit from the login node.
