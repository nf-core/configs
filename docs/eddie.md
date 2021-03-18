# nf-core/configs: Eddie Configuration

nf-core pipelines sarek, rnaseq, and atacseq have all been tested on the University of Edinburgh Eddie HPC.

## Getting help

There is a Slack channel dedicated to eddie users on the MRC IGMM Slack: [https://igmm.slack.com/channels/eddie3](https://igmm.slack.com/channels/eddie3)

## Using the Eddie config profile

To use, run the pipeline with `-profile eddie` (one hyphen).
This will download and launch the [`eddie.config`](../conf/eddie.config) which has been pre-configured with a setup suitable for the [University of Edinburgh Eddie HPC](https://www.ed.ac.uk/information-services/research-support/research-computing/ecdf/high-performance-computing).

The configuration file supports running nf-core pipelines with Docker containers running under Singularity. Support for Conda will follow.

```bash
nextflow run nf-core/PIPELINE -profile eddie,singularity  # ..rest of pipeline flags
```

Before running the pipeline you will need to install Nextflow or load it from the module system. Generally the most recent version will be the one you want.

To list versions:

```bash
module avail igmm/apps/nextflow
```

To load the most recent version:
```bash
module load igmm/apps/nextflow
```

This config enables Nextflow to manage the pipeline jobs via the SGE job scheduler and using Conda or Singularity for software management.

To set up Nextflow on a login node ... TODO

## Singularity set-up

Load Singularity from the module system and set the Singularity cache directory to the NextGenResources path for the pipeline and version you want to run. If this does not exist, please contact the [IGMM Data Manager](data.manager@igmm.ed.ac.uk) to have it added.

```
module load singularity
export NXF_SINGULARITY_CACHEDIR="/exports/igmm/eddie/NextGenResources/nextflow/singularity/nf-core-rnaseq_v3.0"
```

## Using iGenomes references

A local copy of the iGenomes resource has been made available on the Eddie HPC so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Adjusting maximum resources

This config is set for IGMM standard nodes which have 32 cores and 384GB memory. If you are a non-IGMM user, please see the [ECDF specification](https://www.wiki.ed.ac.uk/display/ResearchServices/Memory+Specification) and adjust the `--clusterOptions` flag appropriately, e.g.

```bash
--clusterOptions "-C mem256GB" --max_memory "256GB"
```
