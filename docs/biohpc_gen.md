# nf-core/configs: BioHPC Genomics (BIOHPC_GEN) Configuration

All nf-core pipelines have been successfully configured for use on the BioHPC Genomics (biohpc_gen) cluster that is housed at the Leibniz Rechenzentrum (LRZ) for research groups at the Faculty of Biology of the Ludwig-Maximilians-University (LMU) in Munich.

To use, run the pipeline with `-profile biohpc_gen`. This will download and launch the [`biohpc_gen.config`](../conf/biohpc_gen.config) which has been pre-configured with a setup suitable for the biohpc_gen cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

> NB: You will need an account to use the LRZ Linux cluster as well as group access to the biohpc_gen cluster in order to run nf-core pipelines.

To correctly submit jobs into the `biohpc_gen` cluster the `SLURM_CLUSTERS` variable needs to be set:

```bash
export SLURM_CLUSTERS=biohpc_gen
```

We recommend using nextflow >= 25.04.2 and apptainer (1.3.4).
These are then available as modules (please confirm the module name using module avail):

```bash
## Load Nextflow and apptainer environment modules
module load nextflow/25.04.2 apptainer/1.3.4
```

> NB: bioHPC compute nodes are submit hosts. This means you can submit the nextflow head job via sbatch.

> NB: Sometimes you may want to have jobs submitted 'locally' in a large nextflow job. Details on this can be found here https://doku.lrz.de/nextflow-on-hpc-systems-test-operation-788693597.html
