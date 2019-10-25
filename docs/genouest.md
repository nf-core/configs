# nf-core/configs: GenOuest Configuration

All nf-core pipelines have been successfully configured for use on the GenOuest cluster.

To use, run the pipeline with `-profile genouest`. This will download and launch the [`genouest.config`](../conf/genouest.config) which has been pre-configured with a setup suitable for the GenOuest cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Running the workflow on the GenOuest cluster

Nextflow is installed on the GenOuest cluster. Some documentation is available on the [GenOuest website](https://www.genouest.org/howto/#nextflow).

You need to activate it like this:

```bash
source /local/env/envnextflow-19.07.0.sh
```

Nextflow manages each process as a separate job that is submitted to the cluster by using the sbatch command.
Nextflow shouldn't run directly on the submission node but on a compute node. Run nextflow from a compute node:

```bash
# Login to a compute node
srun --pty bash

# Load the dependencies if not done before
source /local/env/envnextflow-19.07.0.sh

# Run a downloaded/git-cloned nextflow workflow from
nextflow run \\
/path/to/nf-core/workflow \\
-resume
-profile genouest \\
--email my-email@example.org  \\
-c my-specific.config
...

# Or use the nf-core client
nextflow run nf-core/rnaseq ...
```
