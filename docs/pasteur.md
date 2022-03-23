# nf-core/configs: Institut Pasteur Configuration

All nf-core pipelines have been successfully configured for use on the tars cluster at the Institut Pasteur.

To use, run the pipeline with `-profile pasteur`. This will download and launch the [`pasteur.config`](../conf/pasteur.config) which has been pre-configured with a setup suitable for the Pasteur cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Running the workflow on the Pasteur cluster

Nextflow is not installed by default on the Pasteur cluster.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

Nextflow manages each process as a separate job that is submitted to the cluster by using the `sbatch` command.
Nextflow shouldn't run directly on the submission node but on a compute node.
The compute nodes don't have access to internet so you need to run it offline.

To do that:

1. Create a virtualenv to install nf-core

   ```bash
   module purge
   module load Python/3.6.0
   module load java
   module load singularity
   cd /path/to/nf-core/workflows
   virtualenv .venv -p python3
   . .venv/bin/activate
   ```

2. Install nf-core: [here](https://nf-co.re/tools#installation)
3. Get nf-core pipeline and container: [here](https://nf-co.re/tools#downloading-pipelines-for-offline-use)
4. Get the nf-core Pasteur profile: [here](https://github.com/nf-core/rnaseq/blob/master/docs/usage.md#--custom_config_base)
5. Run nextflow on a compute node:

```bash
# create a terminal
tmux
# Get a compute node
salloc
# Load the dependencies if not done before
module purge
module load java
module load singularity

# Run nextflow workflow
nextflow run \\
/path/to/pipeline-dir/from/step/3/workflow \\
-resume
-profile pasteur \\
-with-singularity /path/to/pipeline-dir/from/step/3/singularity-images/singularity.img \\
--email my-email@pasteur.fr  \\
--custom_config_base /path/to/configs/from/step/4/ \\
-c my-specific.config

```
