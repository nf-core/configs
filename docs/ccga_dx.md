# nf-core/configs: CCGA DX Configuration

Deployment and testing of nf-core pipelines at the CCGA DX cluster is on-going.

To use, run the pipeline with `-profile ccga_dx`. This will download and launch the [`ccga_dx.config`](../conf/ccga_dx.config) which has been pre-configured with a setup suitable for the CCGA cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to have Nextflow installed.

> NB: Access to the CCGA DX cluster is restricted to IKMB/CCGA employes. Please talk to Marc Hoeppner to get access (@marchoeppner).
