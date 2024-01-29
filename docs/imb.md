# nf-core/configs: IMB Configuration

All nf-core pipelines have been successfully configured for use on the HPC system at the Institute of Molecular Biology (IMB) in Mainz / Germany.

To use this profile, run the pipeline with `-profile imb`. This will download and launch the [`imb.config`](../conf/imb.config) which has been pre-configured with a setup suitable for the IMB HPC system. Using this profile, container images with all required software will be downloaded before execution of the pipeline.

Before running the pipeline, you will need to load Nextflow using the environment module system on the IMB HPC system. You can do this by issuing the command below:

```bash
module load nextflow
```

:::note
You will need an account to use the IMB HPC cluster in order to run the pipeline. If in doubt contact IT.
:::
