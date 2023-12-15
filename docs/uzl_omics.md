# nf-core/configs: UzL OMICS Cluster Configuration

The rnaseq nf-core pipeline has been successfully configured for use on the UzL OMICS cluster at the University of Luebeck.
Implementation of nf-core pipelines for use on the UzL OMICS is in process.

To use, run the pipeline with `-profile uzl_omics`. This will download and launch the `uzl_omics.config` which has been pre-configured with a setup suitable for the UzL OMICS cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on UzL OMICS cluster. You can do this by issuing the commands below:

```bash
module load nextflow
module load singularity
```

nf-core requires a Nextflow version 22.10.1 or higher, so you have to intall a more recent version first.

## Below are non-mandatory information

> note:
> You will need access to the UzL OMICS cluster in order to run the pipeline. In doubt contact IT.
