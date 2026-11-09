# nf-core/configs: NIC5 CÉCI Cluster Configuration

This configuration provides sensible default parameters to run nf-core pipelines (and nf-core compatible pipelines) on the [CÉCI NIC5 cluster](https://www.ceci-hpc.be/clusters.html#nic5).
To use it, add `-profile ceci_nic5` when running a pipeline.
This will automatically download the [`ceci_nic5.config`](../conf/ceci_nic5.config).

The configuration sets `slurm` as the default executor and enables `singularity` as container runner.

## Loading the required modules

Before running a pipeline, one should load `nextflow` using the environment module system.
This can be achieved with:

```bash
# Load modules
module load 'Nextflow/21.08.0'
```

---

_Built with_ ❤️ _by the [GIGA Bioinformatics Team](https://www.gigabioinformatics.uliege.be/cms/c_8464757/en/gigabioinformatics)_
