# nf-core/configs: UPPMAX Configuration

All nf-core pipelines have been successfully configured for use on the Swedish UPPMAX clusters.

## Getting help

We have a Slack channel dedicated to UPPMAX users on the nf-core Slack: [https://nfcore.slack.com/channels/uppmax](https://nfcore.slack.com/channels/uppmax)

## Using the UPPMAX config profile

The recommended way to activate `Nextflow`, `nf-core`, and any pipeline
available in `nf-core` on UPPMAX is to use the [module system](https://www.uppmax.uu.se/resources/software/module-system/):

```bash
# Log in to the desired cluster
ssh <USER>@{rackham,miarka,bianca}.uppmax.uu.se

# Activate the modules, you can also choose to use a specific version with e.g. `Nextflow/21.10`.
module load bioinfo-tools Nextflow nf-core nf-core-pipelines
```

To use, run the pipeline with `-profile uppmax` (one hyphen).
This will download and launch the [`uppmax.config`](../conf/uppmax.config) which has been pre-configured with a setup suitable for the UPPMAX servers.
It will enable `Nextflow` to manage the pipeline jobs via the `Slurm` job scheduler.
Using this profile, `Docker` image(s) containing required software(s) will be downloaded, and converted to `Singularity` image(s) if needed before execution of the pipeline.

Recent version of `Nextflow` also support the environment variable `NXF_SINGULARITY_CACHEDIR` which can be used to supply images.
Images for some `nf-core` pipelines are available under `/sw/data/ToolBox/nf-core/` and those can be used by `NXF_SINGULARITY_CACHEDIR=/sw/data/ToolBox/nf-core/; export NXF_SINGULARITY_CACHEDIR`.

In addition to this config profile, you will also need to specify an UPPMAX project id.
You can do this with the `--project` flag (two hyphens) when launching `Nextflow`.
For example:

```bash
# Launch a nf-core pipeline with the uppmax profile for the project id snic2018-1-234
$ nextflow run nf-core/<PIPELINE> -profile uppmax --project snic2018-1-234 [...]
```

> NB: If you're not sure what your UPPMAX project ID is, try running `groups` or checking SUPR.

Just run `Nextflow` on a login node and it will handle everything else.

Remember to use `-bg` to launch `Nextflow` in the background, so that the pipeline doesn't exit if you leave your terminal session.
Alternatively, you can also launch `Nextflow` in a `screen` or a `tmux` session.

## Using AWS iGenomes references

A local copy of the `AWS iGenomes` resource has been made available on all UPPMAX clusters so you should be able to run the pipeline against any reference available in the `conf/igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Getting more memory

If your `nf-core` pipeline run is running out of memory, you can run on a fat node with more memory using the following `Nextflow` flags:

```bash
--clusterOptions "-C mem256GB -p node" --max_memory "256GB"
```

This raises the ceiling of available memory from the default of `128.GB` to `256.GB`.
`rackham` has nodes with 128GB, 256GB and 1TB memory available.

Note that each job will still start with the same request as normal, but restarted attempts with larger requests will be able to request greater amounts of memory.

All jobs will be submitted to fat nodes using this method, so it's only for use in extreme circumstances.

## Different UPPMAX clusters

The UPPMAX nf-core configuration profile uses the `hostname` of the active environment to automatically apply the following resource limits:

- `rackham`
  - cpus available: 20 cpus
  - memory available: 125 GB
- `bianca`
  - cpus available: 16 cpus
  - memory available: 109 GB
- `miarka`
  - cpus available: 48 cpus
  - memory available: 357 GB

## Development config

If doing pipeline development work on UPPMAX, the `devel` profile allows for faster testing.

Applied after main UPPMAX config, it overwrites certain parts of the config and submits jobs to the `devcore` queue, which has much faster queue times.

All jobs are limited to 1 hour to be eligible for this queue and only one job allowed at a time.
It is not suitable for use with real data.

To use it, submit with `-profile uppmax,devel`.

## Running on bianca

> :warning: For more information, please follow the following guides:
>
> - [UPPMAX `bianca` user guide](http://uppmax.uu.se/support/user-guides/bianca-user-guide/).
> - [nf-core guide for running offline](https://nf-co.re/usage/offline)
> - [nf-core `tools` guide for downloading pipelines for offline use](https://nf-co.re/tools#downloading-pipelines-for-offline-use).
> - [UPPMAX `Singularity` guide](https://www.uppmax.uu.se/support-sv/user-guides/singularity-user-guide/).

For security reasons, there is no internet access on `bianca` so you can't download from or upload files to the cluster directly.
Before running a nf-core pipeline on `bianca` you will first have to download the pipeline and singularity images needed elsewhere and transfer them via the `wharf` area to your own `bianca` project.

In this guide, we use `rackham` to download and transfer files to the `wharf` area, but it can also be done on your own computer.
If you use `rackham` to download the pipeline and the singularity containers, we recommend using an interactive session (cf [interactive guide](https://www.uppmax.uu.se/support/faq/running-jobs-faq/how-can-i-run-interactively-on-a-compute-node/)), which is what we do in the following guide.

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
