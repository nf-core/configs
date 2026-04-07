# nf-core/configs: NYU HPC Configuration

All nf-core pipelines have been successfully configured for use on the HPC Cluster at New York University.

To use, run the pipeline with `-profile nyu_hpc`. This will download and launch the [`nyu_hpc.config`](../conf/nyu_hpc.config) which has been pre-configured with a setup suitable for the NYU HPC cluster.

Before running the pipeline you will need to load Nextflow using the environment module system on NYU HPC.

```bash
## See available nextflow versions
$ module avail nextflow
--- /share/apps/modulefiles ----
  nextflow/25.04.7    nextflow/25.10.2

## Load desired nextflow
$ module load nextflow/25.10.2
```
