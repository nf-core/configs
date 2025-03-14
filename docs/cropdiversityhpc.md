# nf-core/configs: Crop Diversity HPC Configuration

Configuration for the Crop Diversity high perofrmance computing (HPC) cluster.

## Setup

Prior to using nextflow, please follow the instructions on the help pages for installing conda with intall-bioconda (<https://help.cropdiversity.ac.uk/bioconda.html>).

We advise either creating a conda environment containing nextflow, or installing nextflow in your base environment if this is not possible.

## Apptainer/Singularity and Conda

Apptainer/Singularity and Conda are both available on the HPC and are both enabled in this config. If you have a choice we recommend Apptainer/Singularity due to previously reported performance issues with Conda.

## Run

**DO NOT** run Nextflow pipelines on gruffalo. Instead use a batch script, or alternatively an interactive session within an uninterruptable window (screen or tmux). We recommend providing 4G of memory.

Please also keep in mind the time limits of various queues, medium is the default and has a 24 hour time limit. If your job running the core Nextflow process times out your run will fail.
If you are timed out, or have errors in your run, please use the `-resume` option to avoid unecessary repetition of tasks.

To use this profile, simply pass Nextflow the -profile cropdiversityhpc flag eg.

```bash
nextflow run nf-core/_pipeline_ -profile cropdiversityhpc --outdir results
```

In case of issues, please feel free to reach out to me (Thomas Adams [JHI]) on the Crop Diversity HPC Slack.
