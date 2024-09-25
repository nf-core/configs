# nf-core/configs: Myriad Configuration

All nf-core pipelines have been successfully configured for use on UCL's myriad cluster [University College London](https://www.rc.ucl.ac.uk/docs/Clusters/Myriad/).

## Using Nextflow on Myriad

Before running an nf-core pipeline you will need to configure the container engine (Apptainer/Singularity) environmental variables and install Nextflow.

### Apptainer/Singularity

Set the correct configuration of the cache directories. Save the following lines into your `.bash_profile` file in your home directory (e.g. `/home/<YOUR_ID>/.bash_profile`):

```bash
# Set all the Apptainer environment variables
export APPTAINER_CACHEDIR=$HOME/Scratch/.apptainer/
export APPTAINER_TMPDIR=$HOME/Scratch/.apptainer/tmp
export APPTAINER_LOCALCACHEDIR=$HOME/Scratch/.apptainer/localcache
export APPTAINER_PULLFOLDER=$HOME/Scratch/.apptainer/pull
```

Plus:

```bash

# Set all Singularity environmental variables
export SINGULARITY_CACHEDIR=$HOME/Scratch/.singularity/
export SINGULARITY_TMPDIR=$HOME/Scratch/.singularity/tmp
export SINGULARITY_LOCALCACHEDIR=$HOME/Scratch/.singularity/localcache
export SINGULARITY_PULLFOLDER=$HOME/Scratch/.singularity/pull
export NXF_SINGULARITY_CACHEDIR=$HOME/Scratch/.singularity/
export SINGULARITY_BINDPATH=/scratch/scratch/$USER,/tmpdir,$SINGULARITY_BINDPATH
```

### Nextflow

Download the latest release of nextflow. Warning: the self-update line should update to the latest version, but sometimes not, so please check which is the latest release (https://github.com/nextflow-io/nextflow/releases), you can then manually set this by entering (`NXF_VER=XX.XX.X`).

```bash
## Download Nextflow-all
curl -s https://get.nextflow.io | bash
NXF_VER=XX.XX.X
nextflow -self-update
chmod a+x nextflow
mv nextflow ~/bin/nextflow
```

Then make sure that your bin PATH is executable, by placing the following line in your `.bash_profile`:

```bash
export PATH=$PATH:/home/<YOUR_ID>/bin
```

## Running an nf-core pipeline

To run the pipeline, make sure to add `-profile ucl_myriad,singularity`. This will download and launch the [`ucl_myriad.config`](../conf/ucl_myriad.config) which has been pre-configured with a setup suitable for the myriad cluster, as well as use the correct container engine for myriad.

Singularity points to a copy of Apptainer, but you should always tell nextflow to run with `-profile singularity`.

```bash
/usr/bin/singularity -> apptainer
```
