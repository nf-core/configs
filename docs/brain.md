# nf-core/configs: Brain Image Library Analysis Ecosystem Configuration

All nf-core pipelines have been successfully configured for use on the Brain Image Libraryy (BIL) cluster at the Pittsburgh Supercomputing Center.

To use, run the pipeline with `-profile brain`. This will download and launch the [`brain.config`](../conf/brain.config) which has been pre-configured with a setup suitable for the Brain Image Library (BIL) Analysis Ecosystem. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Running the workflow on the Brain Image Library (BIL) Analysis Ecosystem

Nextflow is not installed by default on the Brain Image Library Analysis Ecosystem.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

Nextflow manages each process as a separate job that is submitted to the cluster by using the `sbatch` command.

Nextflow shouldn't run directly on a login node but on a compute node, so the `nextflow run` command should be also submitted using an `sbatch` command itself.

For example, run the following Nextflow command on a compute node with submit host capability:

```bash
# Run nextflow workflow
nextflow run \\
nf-core/chipseq \\
-resume \\
-profile test,brain
```
