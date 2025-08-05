# nf-core/configs: Crop Diversity HPC Configuration

Configuration for the Crop Diversity high performance computing (HPC) cluster.

## Setup

Prior to using nextflow, please follow the instructions on the [help pages for installing conda with intall-bioconda](https://help.cropdiversity.ac.uk/bioconda.html).

We advise either creating a conda environment containing nextflow, or installing nextflow in your base environment if this is not possible.

## Software sources

We recommend using the config as default to use Singularity. However, if you wish to override Singularity and use the conda, use the `-profile cropdiversityhpc,conda` flag.

## Run

**DO NOT** run Nextflow pipelines on gruffalo. Instead use a batch script, or alternatively an interactive session within an uninterruptable window (screen or tmux). We recommend providing 4G of memory.

Please also keep in mind the time limits of various queues, medium is the default and has a 24 hour time limit. If your job running the core Nextflow process times out your run will fail.
If you are timed out, or have errors in your run, please use the `-resume` option to avoid unecessary repetition of tasks.

To use this profile, simply pass Nextflow the -profile cropdiversityhpc flag eg.

```bash
nextflow run nf-core/_pipeline_ -profile cropdiversityhpc --outdir results
```

In case of issues, please feel free to reach out to one of the maintainers (Thomas Adams, Moray Smith and Miriam Schreiber) on the Crop Diversity HPC Slack.
