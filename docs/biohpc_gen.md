# nf-core/configs: BioHPC Genomics (BIOHPC_GEN) Configuration

All nf-core pipelines have been successfully configured for use on the BioHPC Genomics (biohpc_gen) cluster that is housed at the Leibniz Rechenzentrum (LRZ) for research groups at the Faculty of Biology of the Ludwig-Maximilians-University (LMU) in Munich.

To use, run the pipeline with `-profile biohpc_gen`. This will download and launch the [`biohpc_gen.config`](../conf/biohpc_gen.config) which has been pre-configured with a setup suitable for the biohpc_gen cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Charliecloud container before execution of the pipeline.

> NB: You will need an account to use the LRZ Linux cluster as well as group access to the biohpc_gen cluster in order to run nf-core pipelines.

To correctly submit jobs into the `biohpc_gen` cluster the `SLURM_CLUSTERS` variable needs to be set:

```bash
export SLURM_CLUSTERS=biohpc_gen
```

Recent versions can be installed via `spack` and made available as a module.

Cluster specific instructions to load spack:

```bash
module load spack
module load user_spack
```

We recommend to use `charliecloud` >= 0.35.

```bash
spack install charliecloud@0.35
spack module tcl refresh charliecloud
module avail charliecloud
```

In addition we recommend using nextflow >= 24.04.2. This can be installed via `spack`:

```bash
spack install nextflow@24.04.2
spack module tcl refresh nextflow
module avail nextflow
```

These are then available as modules (please confirm the module name using module avail)

```bash
## Load Nextflow and Charliecloud environment modules
module load nextflow/24.04.2-gcc12 charliecloud/0.35-gcc12
```

> NB: bioHPC compute nodes are submit hosts. This means you can submit the nextflow head job via sbatch.

> NB: Sometimes you may want to have jobs submitted 'locally' in a large nextflow job. Details on this can be found here https://doku.lrz.de/nextflow-on-hpc-systems-test-operation-788693597.html
