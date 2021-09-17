# nf-core/configs: Rosalind Configuration

All nf-core pipelines have been successfully configured for use on the Rosalind CLuster at [Kings College London](https://rosalind.kcl.ac.uk/).
To use, run the pipeline with `-profile rosalind`. This will download and launch the [`rosalind.config`](../conf/rosalind.config) which has been pre-configured with a setup suitable for the rosalind cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Using Nextflow on Rosalind

Before running the pipeline you will need to configure Nextflow and Singularity. There is no Nextflow module on Rosalind at this time. This can be done with the following commands:

```bash
## Load Singularity environment modules - these commands can be placed in your ~/.bashrc also
module load apps/openjdk
module load apps/singularity

## Download Nextflow-all
wget https://github.com/nextflow-io/nextflow/releases/download/v21.04.3/nextflow-21.04.3-all
chmod a+x nextflow-21.04.3-all
mv nextflow-21.04.3-all ~/bin/nextflow
```

By default, the shared partition is used for job submission. Other partitions can be specified using the `--partition <PARTITION NAME>` argument to the run.

## Additional information

The default shared partition resource limits are defined as ten percent of the total available to the cluster at any one point in time. The limitations defined by this configuration are conservative and are projected to be increased as greater computational resources are introduced in the near future.
