# nf-core/configs: Hebbe Configuration

All nf-core pipelines have been successfully configured for use on the Hebbe at the Chalmers University of Technology.

To use, run the pipeline with `-profile hebbe`. This will download and launch the [`hebbe.config`](../conf/hebbe.config) which has been pre-configured with a setup suitable for the Hebbe cluster. To use this profile on Hebbe make sure to use the [Singularity image available at Singularity Hub](https://www.singularity-hub.org/collections/1837).

## Non-mandatory information

Before running the pipeline you will need to make sure Singularity is available by trying

```bash
singularity version
```
Next, [install Nextflow](https://www.nextflow.io/docs/latest/getstarted.html).

## Below are non-mandatory information on iGenomes specific configuration

A local copy of the iGenomes resource has *not* been made available on Hebbe. If it were, you could be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline, by simply using the `--genome <GENOME_ID>` parameter.
>NB: You will need an account to use the HPC cluster on Hebbe in order to run the pipeline. If in doubt contact IT.

>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
