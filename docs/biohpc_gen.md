# nf-core/configs: BioHPC Genomics (BIOHPC_GEN) Configuration

All nf-core pipelines have been successfully configured for use on the BioHPC Genomics (biohpc_gen) cluster that is housed at the Leibniz Rechenzentrum (LRZ) for research groups at the Faculty of Biology of the Ludwig-Maximilians-University (LMU) in Munich.

To use, run the pipeline with `-profile biohpc_gen`. This will download and launch the [`biohpc_gen.config`](../conf/biohpc_gen.config) which has been pre-configured with a setup suitable for the biohpc_gen cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Charliecloud container before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Charliecloud using the environment module system on a login node. You can do this by issuing the commands below:

```bash
## Load Nextflow and Charliecloud environment modules
module load nextflow/21.04.3 charliecloud/0.25
```

> NB: You will need an account to use the LRZ Linux cluster as well as group access to the biohpc_gen cluster in order to run nf-core pipelines.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes.
