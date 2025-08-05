# nf-core/configs: UPPMAX Configuration

All nf-core pipelines have been successfully configured for use on the Swedish UPPMAX clusters.

## Getting help

We have a Slack channel dedicated to assist Swedish HPC users on the nf-core
Slack: [https://nfcore.slack.com/channels/helpdesk-hpc-sweden](https://nfcore.slack.com/channels/helpdesk-hpc-sweden)

## Using the UPPMAX config profile

The recommended way to activate `Nextflow`, `nf-core`, and any pipeline
available in `nf-core` on UPPMAX is to use the [module system](https://www.uppmax.uu.se/resources/software/module-system/):

```bash
# Log in to the desired cluster
ssh <USER>@{rackham,miarka,bianca,pelle}.uppmax.uu.se

# Activate the modules, you can also choose to use a specific version with e.g. `Nextflow/21.10`.
module load bioinfo-tools Nextflow nf-core nf-core-pipelines
```

To use, run the pipeline with `-profile uppmax` (one hyphen).
This will download and launch the [`uppmax.config`](../conf/uppmax.config) which has been pre-configured with a setup suitable for the UPPMAX servers.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler.
Using this profile, `Singularity` images will be downloaded for each process. If a `Singularity` image is not available, `Docker` image(s) containing required software(s) will be downloaded, and converted to `Singularity` image(s) if needed before execution of the pipeline. Images are converted and stored in the singularity cache. If you run out of disk space converting images set `SINGULARITY_CACHEDIR` environment variable to a location with more space.

`Nextflow` also supports the environment variable `NXF_SINGULARITY_CACHEDIR` which can be used to store and supply images for repeated executions.
The equivalent `Nextflow` config setting is `singularity.cacheDir`.

In addition to this config profile, you will also need to specify an UPPMAX project id.
You can do this with the `--project` flag (two hyphens) when launching `Nextflow`.
For example:

```bash
# Launch a nf-core pipeline with the uppmax profile for the project id snic2018-1-234
$ nextflow run nf-core/<PIPELINE> -profile uppmax --project snic2018-1-234 [...]
```

> NB: If you're not sure what your UPPMAX project ID is, try running `groups` or checking SUPR.

Run `Nextflow` on a login node in a `screen` or a `tmux` session and it will handle everything else.

## Using AWS iGenomes references

A local copy of the `AWS iGenomes` resource has been made available on all UPPMAX clusters so you should be able to run the pipeline against any reference available in the `conf/igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Getting more memory

If a task in your `nf-core` pipeline runs out of memory (exit code 137), you increase the memory request for that task by using a local config.

```nextflow
// nextflow.config in your launch directory ( the directory where you run `nextflow run` )
process {
    withName: '<PROCESS_NAME>' {
        memory = 256.GB
    }
}
```

Time (exit code 140), and cpu allocations can be increased in the same way.

The maximum allowed cpu, memory, and time allocations are determined by the `process.resourceLimits` directive. If you request more resources than the maximum they will be reduced to the limit set by this directive. We have implemented a node auto-selection system that will automatically select the best node for your job based on the resources you request.

## Development config

If doing pipeline development work on UPPMAX, the `devel` profile allows for faster testing.

Applied after main UPPMAX config, it overwrites certain parts of the config and submits jobs to the `devcore` queue, which has much faster queue times.

All jobs are limited to 1 hour to be eligible for this queue and only one job allowed at a time.
It is not suitable for use with real data.

To use it, submit with `-profile uppmax,devel`.

## Running on Bianca

> :warning: For more information, please follow the following guides:
>
> - [UPPMAX `bianca` user guide](https://docs.uppmax.uu.se/cluster_guides/bianca/).
> - [nf-core guide for running offline](https://nf-co.re/usage/offline)
> - [nf-core `tools` guide for downloading pipelines for offline use](https://nf-co.re/docs/nf-core-tools/pipelines/download).
> - [UPPMAX `Singularity` guide](https://docs.uppmax.uu.se/software/singularity/).

For security reasons, there is no internet access on `bianca` so you can't download from or upload files to the cluster directly.
Before running a nf-core pipeline on `bianca` you will first have to download the pipeline and singularity images needed elsewhere and transfer them via the `wharf` area to your own `bianca` project.

In this guide, we use `rackham` to download and transfer files to the `wharf` area, but it can also be done on your own computer.
If you use `rackham` to download the pipeline and the singularity containers, we recommend using an interactive session (cf [interactive guide](https://docs.uppmax.uu.se/cluster_guides/interactive_more/)), which is what we do in the following guide.

It is recommended to activate `Nextflow`, `nf-core` and your `nf-core`
pipeline through the module system (see **Using the UPPMAX config profile**
above). In case you need a specific version of any of these tools you can
follow the guide below.

### Download and install Nextflow

```bash
# Connect to rackham
$ ssh -X <USER>@rackham.uppmax.uu.se
# Or stay in your terminal

# Download the nextflow-all bundle
$ wget https://github.com/nextflow-io/nextflow/releases/download/v<NEXTFLOW_VERSION>/nextflow-<NEXTFLOW_VERSION>-all

# Connect to the wharf area using sftp
$ sftp <USER>-<BIANCA_PROJECT>@bianca-sftp.uppmax.uu.se:<USER>-<BIANCA_PROJECT>

# Transfer nextflow to the wharf area
sftp> put nextflow-<NEXTFLOW_VERSION>-all .

# Exit sftp
$ exit

# Connect to bianca
$ ssh -A <USER>-<BIANCA_PROJECT>@bianca.uppmax.uu.se

# Go to your project
$ cd /castor/project/proj_nobackup

# Make folder for Nextflow
$ mkdir tools
$ mkdir tools/nextflow

# Move Nextflow from the wharf area to its directory
$ mv /castor/project/proj_nobackup/wharf/<USER>/<USER>-<BIANCA_PROJECT>/nextflow-<NEXTFLOW_VERSION>-all /castor/project/proj_nobackup/tools/nextflow

# Establish permission
$ chmod a+x /castor/project/proj_nobackup/tools/nextflow/nextflow-<NEXTFLOW_VERSION>-all

# If you want other people to use it
# Be sure that your group has rights to the directory as well
$ chown -R .<BIANCA_PROJECT> /castor/project/proj_nobackup/tools/nextflow/nextflow-<NEXTFLOW_VERSION>-all

# Make a link to it
$ ln -s /castor/project/proj_nobackup/tools/nextflow/nextflow-<NEXTFLOW_VERSION>-all /castor/project/proj_nobackup/tools/nextflow/nextflow

# And every time you're launching Nextflow, don't forget to export the following ENV variables
# Or add them to your .bashrc file
$ export NXF_HOME=/castor/project/proj/nobackup/tools/nextflow/
$ export PATH=${NXF_HOME}:${PATH}
$ export NXF_TEMP=$SNIC_TMP
$ export NXF_LAUNCHER=$SNIC_TMP
$ export NXF_SINGULARITY_CACHEDIR=/castor/project/proj_nobackup/singularity-images
```

### Install nf-core tools

```bash
# Connect to rackham
$ ssh -X <USER>@rackham.uppmax.uu.se
# Or stay in your terminal

# Install the latest pip version
$ pip3 install --upgrade --force-reinstall git+https://github.com/nf-core/tools.git@dev --user
```

### Download and transfer a nf-core pipeline

```bash
# Connect to rackham
$ ssh -X <USER>@rackham.uppmax.uu.se
# Or stay in your terminal

# Open an interactive session (if you are on rackham)
$ interactive <rackham_project>

# Download a pipeline with the singularity images
$ nf-core download <PIPELINE> -r <PIPELINE_VERSION> -s --compress none

# If necessary, extra singularity images can be download separately
# For example, if you downloaded nf-core/sarek, you will need extra images for annotation
# Here we download the nf-core/sarek GRCh38 specific images
$ singularity pull --name nfcore-sareksnpeff-2.7.GRCh38.img docker://nfcore/sareksnpeff:2.7.GRCh38
$ singularity pull --name nfcore-sarekvep-2.7.GRCh38.img docker://nfcore/sarekvep:2.7.GRCh38

# Which can then be moved into the nf-core/sarek download folder
$ mv *.img nf-core-sarek-2.7/singularity-images/.

# Connect to the wharf area using sftp
$ sftp <USER>-<BIANCA_PROJECT>@bianca-sftp.uppmax.uu.se:<USER>-<BIANCA_PROJECT>

# Transfer <PIPELINE> folder from rackham to the wharf area
sftp> put -r nf-core-<PIPELINE>-<PIPELINE_VERSION> .

# The archives will be in the wharf folder in your user home on your bianca project

# Connect to bianca
$ ssh -A <USER>-<BIANCA_PROJECT>@bianca.uppmax.uu.se

# Go to your project
$ cd /castor/project/proj_nobackup

# Make and go into a nf-core directory (where you will store all nf-core pipelines')
$ mkdir nf-core
$ cd nf-core

# Move the folder from the wharf area to the project
$ cp /castor/project/proj_nobackup/wharf/<USER>/<USER>-<BIANCA_PROJECT>/nf-core-<PIPELINE>-<PIPELINE_VERSION> .

# If you want other people to use it,
# Be sure that your group has rights to the directory as well
$ chown -R .<BIANCA_PROJECT> nf-core-<PIPELINE>-<PIPELINE_VERSION>

# Make a symbolic link to the extracted repository
$ ln -s nf-core-<PIPELINE>-<PIPELINE_VERSION> nf-core-<PIPELINE>-default
```

The principle is to have every member of your project to be able to use the same `nf-core/<PIPELINE>` version at the same time.
So every member of the project who wants to use `nf-core/<PIPELINE>` will need to do:

```bash
# Connect to bianca
$ ssh -A <USER>-<BIANCA_PROJECT>@bianca.uppmax.uu.se

# Go to your user directory
$ cd /home/<USER>

# Make a symbolic link to the default nf-core/<PIPELINE>
$ ln -s /castor/project/proj_nobackup/nf-core/nf-core-<PIPELINE>-default nf-core-<PIPELINE>
```

And then `nf-core/<PIPELINE>` can be used with:

```bash
# run <PIPELINE> on bianca
$ nextflow run ~/<PIPELINE> -profile uppmax --project <BIANCA_PROJECT> --genome <GENOME_ASSEMBLY> ...
```

### Update a pipeline

To update, repeat the same steps as for installing and update the link.

```bash
# Connect to bianca (Connect to rackham first if needed)
$ ssh -A <USER>-<BIANCA_PROJECT>@bianca.uppmax.uu.se

# Go to the nf-core directory in your project
$ cd /castor/project/proj_nobackup/nf-core

# Remove link
$ unlink nf-core-<PIPELINE>-default

# Link to new nf-core/<PIPELINE> version
$ ln -s nf-core-<PIPELINE>-<PIPELINE_VERSION> nf-core-<PIPELINE>-default
```

You can for example keep a `nf-core-<PIPELINE>-default` version that you are sure is working, an make a link for a `nf-core-<PIPELINE>-testing` or `nf-core-<PIPELINE>-development`.
