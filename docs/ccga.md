# nf-core/configs: CCGA Configuration

Deployment and testing of nf-core pipelines at the CCGA cluster is on-going.

To use, run the pipeline with `-profile ccga`. This will download and launch the [`ccga.config`](../conf/ccga.config) which has been pre-configured with a setup suitable for the CCGA cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on the cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load IKMB
module load Java/1.8.0
module load Nextflow
module load singularity3.1.0
```

>NB: Access to the CCGA cluster is restricted to IKMB/CCGA employes. Please talk to Marc Hoeppner to get access (@marchoeppner).
