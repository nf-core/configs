# nf-core/configs: ARCC Configuration

The [Advanced Research Computing Center (ARCC)](http://www.uwyo.edu/arcc/) for the University
of Wyoming (UW) has been set up to allow its users to utilize Nextflow with Singularity.

## Getting Started

First, you will need an account on ARCC, if you already have an account, skip ahead, otherwise
please continue. To get an account, you will need to be a Principal Investigator (PI) or student
at UW, or be sponsored by a UW PI. To learn more please visit [ARCC - HPC Account Requests](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1913684148/Accounts+Access+and+Security).

With an account in hand, you are ready to proceed.

## Running Nextflow

Please consider making use of [screen or tmux](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1617494076/Screen+and+Tmux+Commands)
before launching your Interactive Job. This will allow you to resume it later.

When using Nextflow on ARCC it is recommended you launch Nextflow as an Interactive Jobs on one of the
compute nodes, instead of the login nodes. To do this you will use the `salloc` command to launch an
[Interactive Job](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1599078403/Start+Processing#Interactive-Jobs).

Once you are on a compute node, you can then use the `module` command to load Conda and/or
Singularity.

### Creating a Nextflow environment

As an ARCC user you may have noticed there is already a module for Nextflow. However, it
may be out of date or limited to a single version. All nf-core pipelines have minimum Nextflow
version requirements, so its easier to create a Nextflow environment, as it will ensure you
have the latest available Nextflow version.

```{bash}
module load miniforge
conda create -n nextflow -c conda-forge -c bioconda nextflow
```

### Environment Variables

When using Nextflow on ARCC, you will need to set a few environment variables.

#### `NXF_SINGULARITY_CACHEDIR`

This is a Nextflow specific environment variable that will let Nextflow know where you have
or would like downloaded Singularity images to be downloaded.

```{bash}
export NXF_SINGULARITY_CACHEDIR="/path/to/your/singularity/image/cache"

# Example for 'healthdatasci'
export NXF_SINGULARITY_CACHEDIR="/project/healthdatasci/singularity"
```

#### `SBATCH_ACCOUNT`

The `SBATCH_ACCOUNT` environment variable will be used by Nextflow to inform SLURM which
account the job should be submitted under.

```{bash}
export SBATCH_ACCOUNT=<YOUR_ARCC_ACCOUNT>

# Example for 'healthdatasci'
export SBATCH_ACCOUNT=heatlhdatasci
```

### Available Paritions

At the moment, only the CPU based partitions are available from this config. In the event
a GPU partition is needed, please reach out. The GPU partitions require additional arguements
that will need to be added.

The available partitions include:

- `beartooth`
- `beartooth-bigmem`
- `beartooth-hugemem`
- `moran`
- `moran-bigmem`
- `moran-hugemem`
- `teton`
- `teton-cascade`
- `teton-hugemem`
- `teton-massmem`
- `teton-knl`

Please see [Beartooth Hardware Summary Table](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1721139201/Beartooth+Hardware+Summary+Table)
for the full list of partitions.

#### Specifying a Partition

Each partition is provided as a separate Nextflow profile, so you will need to pick a
specific partition to submit jobs to. Using the available partitions, you will replace
the `-` (dash) with an underscore.

For example, to use `beartooth`, you would provide the following:

```{bash}
-profile arcc,beartooth
```

To use `beartooth-bigmem``, you would provide:

```{bash}
-profile arcc,beartooth_bigmem
```

## Example: Running nf-core/fetchngs

```{bash}
# Start a screen
screen -S test-fetchngs

# Start an interactive job
salloc --account=healthdatasci --time=12:00:00 --mem=32G

# Load modules
module load singularity
module load miniforge
conda activate nextflow

# Export NXF_SINGULARITY_CACHEDIR (consider adding to your .bashrc)
export NXF_SINGULARITY_CACHEDIR=/gscratch/rpetit/singularity

# Export SBATCH_ACCOUNT to specificy which account to use
export SBATCH_ACCOUNT="healthdatasci"

# Run the fetchngs test profile with Singularity
nextflow run nf-core/fetchngs \
    -profile test,arcc,<ARCC_PARTITION> \
    --outdir test-fetchngs \
```

If everything is successful, you will be met with:

```{bash}
-[nf-core/fetchngs] Pipeline completed successfully-
WARN: =============================================================================
  Please double-check the samplesheet that has been auto-created by the pipeline.

  Public databases don't reliably hold information such as strandedness
  information, controls etc

  All of the sample metadata obtained from the ENA has been appended
  as additional columns to help you manually curate the samplesheet before
  running nf-core/other pipelines.
===================================================================================
Completed at: 30-Jan-2024 14:36:24
Duration    : 1m 28s
CPU hours   : (a few seconds)
Succeeded   : 18
```
