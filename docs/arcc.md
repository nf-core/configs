# nf-core/configs: ARCC Configuration

The [Advanced Research Computing Center (ARCC)](http://www.uwyo.edu/arcc/) for the University
of Wyoming (UW) has been set up to allow its users to utilize Nextflow with Singularity.

## Getting Started

First, you will need an account on ARCC, if you already have an account, skip ahead, otherwise
please continue. To get an account, you will need to be a Principal Investigator (PI) or student
at UW, or be sponsored by a UW PI. To learn more please visit [ARCC - HPC Account Requests](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1913684148/Accounts+Access+and+Security).

With an account in hand, you are ready to proceed.

## Running Nextflow

When using Nextflow on ARCC it is recommended you launch Nextflow on one of the compute nodes,
instead of the login nodes. To do this you will use the `salloc` command to launch an
[Interactive Job](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1599078403/Start+Processing#Interactive-Jobs).

Alongside `salloc`, please consider making use of [screen or tmux](https://arccwiki.atlassian.net/wiki/spaces/DOCUMENTAT/pages/1617494076/Screen+and+Tmux+Commands)
in order to not lose your Interactive Job.

Once you are on a compute node, you can then use the `module` command to load Conda and
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

## Parameters of Interest

#### `--slurm_account`

You will want to use `--slurm_account` to the Project group you would like to submit jobs under.
This is the name you typically provide with `--account` in your sbatch scripts.

#### `--slurm_opts`

`--slurm_opts` allows you to pass any additional options that might be required for your
analysis.

#### `--slurm_queue`

By default the `teton` and `moran` partitions are used to submit jobs to. However, if you need
additional partitions are totally different partitiions, make use of `--slurm_queue`. Be sure
to separate the partitions by a comma if you would like to include more than one (e.g.
`--slurm_queue teton,moran`).

### `--slurm_use_scratch`

Finally you can adjust the usage of temporary scratch space with `--slurm_use_scratch`. If
enabled, you may lose access to the `work` directory files on job completion.

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

# Run the fetchngs test profile with Singularity
nextflow run nf-core/fetchngs \
    -profile test,arcc \
    --outdir test-fetchngs \
    --slurm_account healthdatasci
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
