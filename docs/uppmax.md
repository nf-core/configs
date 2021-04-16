# nf-core/configs: UPPMAX Configuration

All nf-core pipelines have been successfully configured for use on the Swedish UPPMAX clusters.

## Getting help

We have a Slack channel dedicated to UPPMAX users on the nf-core Slack: [https://nfcore.slack.com/channels/uppmax](https://nfcore.slack.com/channels/uppmax)

## Using the UPPMAX config profile

To use, run the pipeline with `-profile uppmax` (one hyphen).
This will download and launch the [`uppmax.config`](../conf/uppmax.config) which has been pre-configured with a setup suitable for the UPPMAX servers.
Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

In addition to this config profile, you will also need to specify an UPPMAX project id.
You can do this with the `--project` flag (two hyphens) when launching nextflow. For example:

```bash
nextflow run nf-core/PIPELINE -profile uppmax --project snic2018-1-234 # ..rest of pipeline flags
```

$ NB: If you're not sure what your UPPMAX project ID is, try running `groups` or checking SUPR.

Before running the pipeline you will need to either install Nextflow or load it using the environment module system.

This config enables Nextflow to manage the pipeline jobs via the Slurm job scheduler and using Singularity for software management.

Just run Nextflow on a login node and it will handle everything else.

Remember to use `-bg` to launch Nextflow in the background, so that the pipeline doesn't exit if you leave your terminal session.

## Using iGenomes references

A local copy of the iGenomes resource has been made available on all UPPMAX clusters so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Getting more memory

If your nf-core pipeline run is running out of memory, you can run on a fat node with more memory using the following nextflow flags:

```bash
--clusterOptions "-C mem256GB" --max_memory "256GB"
```

This raises the ceiling of available memory from the default of `128.GB` to `256.GB`.
`Rackham` has nodes with 128GB, 256GB and 1TB memory available.

Note that each job will still start with the same request as normal, but restarted attempts with larger requests will be able to request greater amounts of memory.

All jobs will be submitted to fat nodes using this method, so it's only for use in extreme circumstances.

## Different UPPMAX clusters

The UPPMAX nf-core configuration profile uses the `hostname` of the active environment to automatically apply the following resource limits:

* `bianca`
  * cpus available: 16 cpus
  * memory available: 109 GB
* `irma`
  * cpus available: 16 cpus
  * memory available: 250 GB
* `rackham`
  * cpus available: 20 cpus
  * memory available: 125 GB

## Development config

If doing pipeline development work on UPPMAX, the `devel` profile allows for faster testing.

Applied after main UPPMAX config, it overwrites certain parts of the config and submits jobs to the `devcore` queue, which has much faster queue times.

All jobs are limited to 1 hour to be eligible for this queue and only one job allowed at a time.
It is not suitable for use with real data.

To use it, submit with `-profile uppmax,devel`.

## Running on Bianca

$ :warning: For more information about `bianca`, follow the [UPPMAX `bianca` user guide](http://uppmax.uu.se/support/user-guides/bianca-user-guide/).
$ :warning: For more information, follow the [nf-core guide for running offline](https://nf-co.re/usage/offline) and the [nf-core `tools` guide for downloading pipelines for offline use](https://nf-co.re/tools#downloading-pipelines-for-offline-use).
 > :warning: For more information about using `Singularity` with UPPMAX, follow the [UPPMAX `Singularity` guide](https://www.uppmax.uu.se/support-sv/user-guides/singularity-user-guide/).

For security reasons, there is no internet access on `bianca` so you can't download from or upload files to the cluster directly.
Before running a nf-core pipeline on `bianca` you will first have to download the pipeline and singularity images needed elsewhere and transfer them via the wharf area to your own `bianca` project.

In this guide, we use `rackham` to download and transfer files to wharf, but it can also be done on your own computer.
If you use `rackham` to download the pipeline and the singularity containers, we recommend using an interactive session (cf [interactive guide](https://www.uppmax.uu.se/support/faq/running-jobs-faq/how-can-i-run-interactively-on-a-compute-node/)), which is what we do in the following guide.

### Download Nextflow

You can use the UPPMAX provided `module`, but if necessary, you can also download a more recent version.

```bash
# Connect to rackham
$ ssh -X <user>@rackham.uppmax.uu.se
# Or stay in your terminal

# Download the nextflow-all bundle
$ wget https://github.com/nextflow-io/nextflow/releases/download/v<nextflow_version>/nextflow-<nextflow_version>-all

# Connect to wharf using sftp
# For FileZilla follow the bianca user guide
$ sftp <user>-<bianca_project>@bianca-sftp.uppmax.uu.se:<user>-<bianca_project>

# Transfer nextflow to wharf
sftp> put nextflow-<nextflow_version>-all .

# Exit sftp
$ exit

# Connect to bianca
$ ssh -A <user>-<bianca_project>@bianca.uppmax.uu.se

# Go to your project
$ cd /castor/project/proj_nobackup

# Make folder for Nextflow
$ mkdir tools
$ mkdir tools/nextflow

# Move Nextflow from wharf to its directory
$ mv /castor/project/proj_nobackup/wharf/<user>/<user>-<bianca_project>/nextflow-<nextflow_version>-all /castor/project/proj_nobackup/tools/nextflow

# Establish permission
$ chmod a+x /castor/project/proj_nobackup/tools/nextflow/nextflow-<nextflow_version>-all

# If you want other people to use it
# Be sure that your group has rights to the directory as well

$ chown -R .<bianca_project> /castor/project/proj_nobackup/tools/nextflow/nextflow-<nextflow_version>-all

# Make a link to it
$ ln -s /castor/project/proj_nobackup/tools/nextflow/nextflow-<nextflow_version>-all /castor/project/proj_nobackup/tools/nextflow/nextflow

# And every time you're launching Nextflow, don't forget to export the following ENV variables
# Or add them to your .bashrc file
$ export NXF_HOME=/castor/project/proj/nobackup/tools/nextflow/
$ export PATH=${NXF_HOME}:${PATH}
$ export NXF_TEMP=$SNIC_TMP
$ export NXF_LAUNCHER=$SNIC_TMP
$ export NXF_SINGULARITY_CACHEDIR=/castor/project/proj_nobackup/singularity-images
```

### Download nf-core pipelines

```bash
# Connect to rackham
$ ssh -X <user>@rackham.uppmax.uu.se
# Or stay in your terminal

# Open an interactive session (if you are on rackham)
$ interactive <rackham_project>

# Install the latest pip version
$ pip3 install --upgrade --force-reinstall git+https://github.com/nf-core/tools.git@dev --user

# Download a pipeline (nf-core/rnaseq 3.0) with the singularity images
$ nf-core download rnaseq -r 3.0 -s -p 10 --compress none

# Download a pipeline (nf-core/sarek 2.7) with the singularity images
$ nf-core download sarek -r 2.7 -s -p 10 --compress none

# Download specific Singularity images
$ singularity pull --name nfcore-sareksnpeff-2.7.GRCh38.img docker://nfcore/sareksnpeff:2.7.GRCh38
$ singularity pull --name nfcore-sarekvep-2.7.GRCh38.img docker://nfcore/sarekvep:2.7.GRCh38

# Move specific Singularity images into nf-core download folder
$ mv *.img nf-core-sarek-2.7/singularity-images/.

# Connect to wharf using sftp
$ sftp <user>-<bianca_project>@bianca-sftp.uppmax.uu.se:<user>-<bianca_project>

# Transfer rnaseq folder from rackham to wharf
sftp> put -r nf-core-rnaseq-3.0 .
[...]

# Transfer sarek folder from rackham to wharf
sftp> put -r nf-core-sarek-2.7 .
[...]

# The archives will be in the wharf folder in your user home on your bianca project

# Connect to bianca
$ ssh -A <user>-<bianca_project>@bianca.uppmax.uu.se

# Go to your project
$ cd /castor/project/proj_nobackup

# Make and go into a nf-core/sarek directory (where you will store all nf-core/sarek versions)
$ mkdir sarek
$ cd sarek

# Copy the tar from wharf to the project
$ cp /castor/project/proj_nobackup/wharf/<user>/<user>-<bianca_project>/nf-core-sarek-2.7 /castor/project/proj_nobackup/sarek

# If you want other people to use it,
# Be sure that your group has rights to the directory as well
$ chown -R .<bianca_project> nf-core-sarek-2.7

# Make a symbolic link to the extracted repository
$ ln -s nf-core-sarek-2.7 default
```

The principle is to have every member of your project to be able to use the same nf-core/sarek version at the same time. So every member of the project who wants to use nf-core/sarek will need to do:

```bash
# Connect to bianca
$ ssh -A <user>-<bianca_project>@bianca.uppmax.uu.se

# Go to your user directory
$ cd /home/<user>

# Make a symbolic link to the default nf-core/sarek
$ ln -s /castor/project/proj_nobackup/sarek/default sarek
```

And then nf-core/sarek can be used with:

```bash
$ nextflow run ~/sarek -profile uppmax --project <bianca_project> --genome [GENOME ASSEMBLY] ...
```

This is an example of how to run sarek with the tool Manta and the genome assembly version GRCh38, which worked on `bianca` 20210416

```bash
$ nextflow run ~/sarek -profile uppmax --project <bianca_project> --tools Manta --input <input.tsv>
```

## Update nf-core/sarek

Repeat the same steps as for installing nf-core/sarek, and update the link.

```bash
# Connect to bianca (Connect to rackham first if needed)
$ ssh -A <user>-<bianca_project>@bianca.uppmax.uu.se

# Go to the sarek directory in your project
$ cd /castor/project/proj_nobackup/sarek

# Remove link
$ rm default

# Link to new nf-core/sarek version
$ ln -s nf-core-sarek-2.7 default
```

You can for example keep a `default` version that you are sure is working, an make a link for a `testing` or `development`
