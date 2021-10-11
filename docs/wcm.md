# nf-core/configs: Weill Cornell Medicine Configuration

All nf-core pipelines have been successfully configured for use on the panda cluster at the WCM.

To use, run the pipeline with `-profile wcm`. This will download and launch the [`wcm.config`](../conf/wcm.config) which has been pre-configured with a setup suitable for the WCM slurm cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Running the workflow on the Pasteur cluster

Nextflow is not installed by default on the WCM cluster.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

Nextflow manages each process as a separate job that is submitted to the cluster by using the `sbatch` command.
Nextflow shouldn't run directly on a login node but on a compute node or lab-specific interactive server when configured as a submit host.

1. Run nextflow on a compute node or interactive server with submit host capability:

```bash
# Run nextflow workflow
nextflow run \\
nf-core/chipseq \\
-resume \\
-profile test,wcm
```
