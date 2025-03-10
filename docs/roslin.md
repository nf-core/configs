# nf-core/configs: Roslin Configuration

nf-core pipelines sarek, rnaseq, chipseq, mag, differentialabundance and isoseq have all been tested on the University of Edinburgh Eddie HPC with test profile.

## Getting help

There is a Teams group dedicated to Nextflow users: [Nextflow Teams](https://teams.microsoft.com/l/team/19%3A7e957d32ce1345b8989af14564547690%40thread.tacv2/conversations?groupId=446c509d-b8fd-466c-a66f-52122f0a2fcc&tenantId=2e9f06b0-1669-4589-8789-10a06934dc61)
Also, you can find at the coding club held each Wednesday: [Code Club Teams](https://teams.microsoft.com/l/channel/19%3A1bf9220112e445c382b6beb660ffb61a%40thread.tacv2/Coding%20Club?groupId=cc7a1113-38a1-48f6-9fc6-14700c8da27e&tenantId=2e9f06b0-1669-4589-8789-10a06934dc61)

## Using the Roslin config profile

To use, run the pipeline with `-profile roslin` (one hyphen).
This will download and launch the [`roslin.config`](../conf/roslin.config) file which has been pre-configured with a setup suitable for the [University of Edinburgh Eddie HPC](https://www.ed.ac.uk/information-services/research-support/research-computing/ecdf/high-performance-computing).

The configuration file supports running nf-core pipelines with Docker containers running under Singularity by default. Conda is not currently supported.

```bash
nextflow run nf-core/PIPELINE -profile roslin # ...rest of pipeline flags
```

Before running the pipeline, you will need to load Nextflow from the module system or activate your Nextflow conda environment. Generally, the most recent version will be the one you want.

To list versions:

```bash
module avail|grep nextflow
```

To load the most recent version (08/08/2024):

```bash
module load igmm/bac/nextflow/24.04.2
```

This config enables Nextflow to manage the pipeline jobs via the SGE job scheduler and using Singularity for software management.

## Singularity set up

The roslin profile is set to use `/exports/cmvm/eddie/eb/groups/alaw3_eb_singularity_cache` as the singularity cache directory. This directory is put at the disposition of roslin institute nextflow/nf-core users by the Roslin Bioinformatics group led by Andy Law. All new container will be cached in this directory writable by all. If you face any problem with singularity cache, please contact [Sébastien Guizard](sguizard@ed.ac.uk), [Donald Dunbar](donald.dunbar@ed.ac.uk) and [Andy Law](andy.law@roslin.ed.ac.uk) with the [Roslin Bioinformatics](roslin.bioinformatics@roslin.ed.ac.uk) group in CC.

Singularity will by default create a directory `.singularity` in your `$HOME` directory on eddie. Space on `$HOME` is very limited, so it is a good idea to create a directory somewhere else with more room and link the locations.

```bash
cd $HOME
mkdir /exports/eddie/path/to/my/area/.singularity
ln -s /exports/eddie/path/to/my/area/.singularity .singularity
```

## SGE project set up

By default, users’ jobs are started with the `uoe_baseline` project that gives access to free nodes. If you have a project code that gives you access to paid nodes, it can be used by jobs submitted by Nextflow. To do so, you need to set up an environment variable called `NFX_SGE_PROJECT`:

```bash
export NFX_SGE_PROJECT="<PROJECT_NAME_HERE>"
```

If you wish, you place this variable declaration in your `.bashrc` file located in your home directory to automatically set it up each time you log on Eddie.

**NB:** This will work only with the roslin profile.

## Nodes exclusion

The roslin profile excludes some specific nodes.
The superdome node is reserved for special applications, and the access must be requested.
Eddie's nodes are being migrated to Rocky Linux 9 and some of them are already online. These are not fully set up yet and jobs have troubles to run on them.
Until those nodes are stable, we exclude them.

## Running Nextflow

### On a login node

You can use a qlogin to run Nextflow, if you request more than the default 2 GB of memory. Unfortunately, you can't submit the initial Nextflow run process as a job as you can't qsub within a qsub.
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

Wild West node has relaxed restriction compared to regular nodes, which allows the execution of Nextflow.
The access to Wild West node must be requested to [Andy Law](andy.law@roslin.ed.ac.uk) and IS.
Similarly to the qlogin option, it is advised to run Nextflow within a screen session.

## Using iGenomes references

A local copy of the iGenomes resource has been made available on the Eddie HPC for those with access to `/exports/igmm/eddie/BioinformaticsResources` so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.
