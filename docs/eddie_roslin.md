# nf-core/configs: Eddie Configuration

nf-core pipelines sarek, rnaseq, atacseq, and viralrecon have all been tested on the University of Edinburgh Eddie HPC. All except atacseq have pipeline-specific config files; atacseq does not yet support this.

## Getting help

There is a Teams group dedicated to nextflow users: [Netxtflow Teams](https://teams.microsoft.com/l/team/19%3A7e957d32ce1345b8989af14564547690%40thread.tacv2/conversations?groupId=446c509d-b8fd-466c-a66f-52122f0a2fcc&tenantId=2e9f06b0-1669-4589-8789-10a06934dc61)

## Using the Eddie config profile

To use, run the pipeline with `-profile eddie_roslin` (one hyphen).
This will download and launch the [`eddie_roslin.config`](../conf/eddie_roslin.config) which has been pre-configured with a setup suitable for the [University of Edinburgh Eddie HPC](https://www.ed.ac.uk/information-services/research-support/research-computing/ecdf/high-performance-computing).

The configuration file supports running nf-core pipelines with Docker containers running under Singularity by default. Conda is not currently supported.

```bash
nextflow run nf-core/PIPELINE -profile eddie_roslin # ...rest of pipeline flags
```

Before running the pipeline you will need to load Nextflow from the module system or activate youir Nextflow conda envronment. Generally the most recent version will be the one you want.

To list versions:

```bash
module avail|grep nextflow
```

To load the most recent version (08/08/2024):

```bash
module load igmm/bac/nextflow/24.04.2
```

This config enables Nextflow to manage the pipeline jobs via the SGE job scheduler and using Singularity for software management.

## Singularity set-up

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
If your eddie terminal disconnects your Nextflow job will stop. You can run qlogin in a screen session to prevent this.

Start a new screen session.

```bash
screen -S <session_name>
```

Start an interactive job with qlogin. 

```bash
qlogin -l h_vmem=8G
```

You can leave our screen session by typing Ctrl + A, then d.

To list existing screen sessions, use:

```bash
screen -ls
```

To reconnect to an existing screen session, use:

```bash
screen -r <session_name>
```


### On the wild west node

Wild West node have relaxed restriction compared to regular nodes, which allows the execution of Nextflow. 
The access to Wild West node must be requested to Andy Law (alaw3@ed.ac.uk) and IS. 
Similarly to qlogin option, it is advised to run Nextflow within a screen session. 


## Using iGenomes references

A local copy of the iGenomes resource has been made available on the Eddie HPC for those with access to `/exports/igmm/eddie/BioinformaticsResources` so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

