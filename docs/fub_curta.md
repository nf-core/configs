# nf-core/configs: Freie Universiät Berlin High-Performance Computer (Curta) Configuration

> **NB:** In order to run pipelines using this HPC cluster, you must first apply for access [here](https://ssl2.cms.fu-berlin.de/fu-berlin/en/sites/high-performance-computing/PM_Zugang-beantragen/index.html).

This profile is configured to run with Singularity version `1.1.9-1.el7`, which does not need to be loaded.

Nextflow should be loaded before use. Nextflow version `22.10.6.5844` is used. The following should be added to your sbatch/SLURM script:

```
module load Nextflow
```

Using `-profile fub_curta` will download [`fub_curta.config`](../conf/fub_curta.config), which has been pre-configured with a setup suitable for the Curta cluster.

## Additional Profiles

A profile for deactivating the cleanup of intermediate files is also offered.

### debug

This simply turns off automatic clean up of intermediate files, which can be useful for debugging. It is specified with `-profile fub_curta,debug`.
