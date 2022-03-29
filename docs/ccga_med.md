# nf-core/configs: CCGA Med Cluster Configuration

Deployment and testing of nf-core pipelines at the CCGA Med cluster is on-going.

To use, run the pipeline with `-profile ccga_med`. This will download and launch the [`ccga_med.config`](../conf/ccga_med.config) which has been pre-configured with a setup suitable for the CCGA cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on the cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load nextflow
module load singularity
```

> NB: Access to the CCGA Med cluster is restricted to IKMB/CCGA employees. Please talk to Marc Hoeppner to get access (@marchoeppner).
