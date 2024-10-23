# nf-core/configs: GIGA Cluster Configuration

This configuration provides sensible default parameters to run nf-core pipelines (and nf-core compatible pipelines) on the [GIGA cluster](https://giga-bioinfo.gitlabpages.uliege.be/docs/mass-storage-and-cluster/cluster/overview.html).
To use it, add `-profile giga` when running a pipeline.
This will automatically download the [`giga.config`](../conf/giga.config).

The configuraiton sets `slurm` as the default executor and enables `singularity` as container runner.

## Loading the required modules

Before running a pipeline, one should load `slurm`, `nextflow` and `singularity` using the environment module system.
This can be achieved with:

```bash
# Clear loaded modules
module purge

# Add GIGA bioinformatics modules to modules path
module use '/resources/GIGA/PUBLIC/tools/modules/containerised/modulefiles'
module use '/resources/GIGA/PUBLIC/tools/modules/uncontainerised/modulefiles'

# Load modules
module load 'slurm'
module load 'singularity/giga'
module load 'nextflow/24.04.4'
```

---
*Built with* ❤️ *by the [GIGA Bioinformatics Team](https://www.gigabioinformatics.uliege.be/cms/c_8464757/en/gigabioinformatics)*
