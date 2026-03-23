# nf-core/configs: Apocrita Configuration

> [!WARNING]
> This is an **unofficial** project and not officially supported by [QMUL ITS Research](https://docs.hpc.qmul.ac.uk/). Please do not approach the ITSR team for support with this config.

> [!WARNING]
> Make sure that you are fully aware of the options this config submits to Apocrita, particularly the `highmem` flag, to avoid abusing nodes on the Apocrita cluster.

All nf-core pipelines have been successfully configured for use on QMUL's Apocrita cluster [Queen Mary University of London](https://docs.hpc.qmul.ac.uk/).

To use, run the pipeline with `-profile qmul_apocrita`. This will download and launch the [`qmul_apocrita.config`](../conf/qmul_apocrita.config) which has been pre-configured with a setup suitable for Apocrita.

## Using Nextflow on Apocrita

Before running the pipeline you will need to configure Apptainer and install+configure Nextflow.

### Singularity

Set the correct configuration of the cache directories, where <YOUR_ID> is replaced with you credentials which you can find by entering `whoami` into the terminal once you are logged into Apocrita. Run these lines in all job scripts or interactive sessions (or create a [Private Module](https://docs.hpc.qmul.ac.uk/using/UsingModules/#private-modules) to set them):

```bash
# Set all the Apptainer environment variables
export APPTAINER_CACHEDIR=/data/scratch/<YOUR_ID>/.apptainer/
export APPTAINER_TMPDIR=/data/scratch/<YOUR_ID>/.apptainer/tmp
export APPTAINER_LOCALCACHEDIR=/data/scratch/<YOUR_ID>/.apptainer/localcache
export APPTAINER_PULLFOLDER=/data/scratch/<YOUR_ID>/.apptainer/pull
```

> [!WARNING]
> You need to make sure that all these folders actually exist before running for the first time.

### Nextflow

#### Module

https://docs.hpc.qmul.ac.uk/apps/bio/nextflow/

#### Conda

Install Nextflow in a [Conda Environment](https://docs.hpc.qmul.ac.uk/apps/languages/miniforge/#environments) from the [Bioconda channel](https://anaconda.org/bioconda/nextflow).

#### Manual installation

> [!WARNING]
> Do not pipe `curl` to `bash` as per the offical [Quick start](https://github.com/nextflow-io/nextflow?tab=readme-ov-file#quick-start) guide, follow the instructions below.

Download the latest release of nextflow. _Warning:_ the `self-update` line should update to the latest version, but sometimes not, so please check which is the latest release (https://github.com/nextflow-io/nextflow/releases), you can then manually set this by entering (`NXF_VER=XX.XX.X`).

```bash
## Load OpenJDK module
module load openjdk
## Download Nextflow install script
curl -s https://get.nextflow.io -o nextflow
## Inspect the contents, then make it executable
chmod +x nextflow
## Check it runs
./nextflow
## Check it is up to date
./nextflow -self-update
NXF_VER=XX.XX.X
```

You can then move the `nextflow` executable to wherever you wish, for example:

```bash
mv nextflow ~/bin/nextflow
```

Then make sure that this location is in your `$PATH`, by creating a [Private Module](https://docs.hpc.qmul.ac.uk/using/UsingModules/#private-modules), which should load the OpenJDK module as well as add the location of the executable to `$PATH`.
