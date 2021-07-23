# nf-core/configs: Eddie Configuration

nf-core pipelines sarek, rnaseq, atacseq, and viralrecon have all been tested on the University of Edinburgh Eddie HPC. All except atacseq have pipeline-specific config files; atacseq does not yet support this.

## Getting help

There is a Slack channel dedicated to eddie users on the MRC IGC Slack: [https://igmm.slack.com/channels/eddie3](https://igmm.slack.com/channels/eddie3)

## Using the Eddie config profile

To use, run the pipeline with `-profile eddie` (one hyphen).
This will download and launch the [`eddie.config`](../conf/eddie.config) which has been pre-configured with a setup suitable for the [University of Edinburgh Eddie HPC](https://www.ed.ac.uk/information-services/research-support/research-computing/ecdf/high-performance-computing).

The configuration file supports running nf-core pipelines with Docker containers running under Singularity by default. Conda is not currently supported.

```bash
nextflow run nf-core/PIPELINE -profile eddie  # ...rest of pipeline flags
```

Before running the pipeline you will need to install Nextflow or load it from the module system. Generally the most recent version will be the one you want. If you want to run a Nextflow pipeline that is based on [DSL2](https://www.nextflow.io/docs/latest/dsl2.html), you will need a version that ends with '-edge'.

To list versions:

```bash
module avail igmm/apps/nextflow
```

To load the most recent version:

```bash
module load igmm/apps/nextflow
```

This config enables Nextflow to manage the pipeline jobs via the SGE job scheduler and using Singularity for software management.

## Singularity set-up

Load Singularity from the module system.

```bash
module load singularity
```

The eddie profile is set to use `/exports/igmm/eddie/BioinformaticsResources/nfcore/singularity-images` as the Singularity cache directory. If some containers for your pipeline run are not present, please contact the [IGC Data Manager](data.manager@igc.ed.ac.uk) to have them added. You can add these lines to the file `$HOME/.bashrc`, or you can run these commands before you run an nf-core pipeline.

If you do not have access to `/exports/igmm/eddie/BioinformaticsResources`, set the Singularity cache directory to somewhere sensible that is not in your `$HOME` area (which has limited space). It will take time to download all the Singularity containers, but you can use this again.

Singularity will by default create a directory `.singularity` in your `$HOME` directory on eddie. Space on `$HOME` is very limited, so it is a good idea to create a directory somewhere else with more room and link the locations.

```bash
cd $HOME
mkdir /exports/eddie/path/to/my/area/.singularity
ln -s /exports/eddie/path/to/my/area/.singularity .singularity
```

## Running Nextflow

### On a login node

You can use a qlogin to run Nextflow, if you request more than the default 2GB of memory. Unfortunately you can't submit the initial Nextflow run process as a job as you can't qsub within a qsub.

```bash
qlogin -l h_vmem=8G
```

If your eddie terminal disconnects your Nextflow job will stop. You can run Nextflow as a bash script on the command line using `nohup` to prevent this.

```bash
nohup ./nextflow_run.sh &
```

### On a wild west node - IGC only

Wild west nodes on eddie can be accessed via ssh (node2c15, node2c16, node3g22). To run Nextflow on one of these nodes, do it within a [screen session](https://linuxize.com/post/how-to-use-linux-screen/).

Start a new screen session.

```bash
screen -S <session_name>
```

List existing screen sessions

```bash
screen -ls
```

Reconnect to an existing screen session

```bash
screen -r <session_name>
```

## Using iGenomes references

A local copy of the iGenomes resource has been made available on the Eddie HPC for those with access to `/exports/igmm/eddie/BioinformaticsResources` so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Adjusting maximum resources

This config is set for IGC standard nodes which have 32 cores and 384GB memory. If you are a non-IGC user, please see the [ECDF specification](https://www.wiki.ed.ac.uk/display/ResearchServices/Memory+Specification) and adjust the `--clusterOptions` flag appropriately, e.g.

```bash
--clusterOptions "-C mem256GB" --max_memory "256GB"
```
