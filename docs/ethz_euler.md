# nf-core/configs: ETH Zurich Euler cluster configuration

Configuration file to run nf-core pipelines on the Euler cluster of [ETH Zurich](https://ethz.ch/).

To use the ETH Zurich Euler cluster configuration, run the pipeline with `-profile ethz_euler`. This will download and launch the [`ethz_euler.config`](../conf/ethz_euler.config), which has been pre-configured with a setup suitable for the Euler cluster. Using this profile, a docker image containing all of the required software will be downloaded and converted to a Singularity container before the execution of the pipeline.

## Before running the pipeline

Currently, Nextflow is not installed by default on the Euler cluster. You have to install Nextflow version **>= 23.07.0-edge** on your custom modules.

> **Important:** Previous Nextflow versions will fail to run the job, since the executor option '**perCpuMemAllocation**' is only available since **23.07.0-edge**. This option specifies memory allocations for SLURM jobs as --mem-per-cpu <task.memory / task.cpus> instead of --mem <task.memory>.

To run Nextflow on Euler, you will need to load the following modules:

`openjdk` - a free and opensource java implementation; <br />
`eth_proxy` - for the compute nodes communicate with the Internet through the ETH Zurich proxy server;<br />
`nextflow` - enables scalable and reproducible scientific workflows using software containers _(this module can have a user-defined name since was a custom installation)_.

```bash
module load openjdk eth_proxy nextflow
```

Finally, you will also need to specify the Singularity cache directory with the environmental variable `NXF_SINGULARITY_CACHEDIR`. _(https://www.nextflow.io/docs/latest/singularity.html)_

## Genomes

In `/cluster/project/igenomes`, the Euler cluster provides a set of reference genomes and annotations (illumina igenomes) for a selection of model organism. The genomes and annotations were downloaded from: https://support.illumina.com/sequencing/sequencing_software/igenome.html

The path for the _igenomes_ saved in the Euler cluster is already assigned to the parameter variable `igenomes_base` and the parameter variable `igenomes_ignore` is set to `false` so that it loads the igenomes.config when running the pipeline. These default values can be overwritten when running the Nextflow command.

```
igenomes_base   = '/cluster/project/igenomes'
igenomes_ignore = false
```

_(For more information : https://scicomp.ethz.ch/wiki/Reference_genomes)_
