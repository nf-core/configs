# nf-core/configs: Myriad Configuration

All nf-core pipelines have been successfully configured for use on UCL's myriad cluster [University College London](https://www.rc.ucl.ac.uk/docs/Clusters/Myriad/).

To use, run the pipeline with `-profile ucl_myriad`. This will download and launch the [`ucl_myriad.config`](../conf/ucl_myriad.config) which has been pre-configured with a setup suitable for the myriad cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Using Nextflow on Myriad

Before running the pipeline you will need to install and configure Nextflow and Singularity.

### Singularity

This can be done with the following commands:

```bash
## Load Singularity environment modules - these commands can be placed in your ~/.bashrc also
module add java/openjdk-11/11.0.1
module add singularity-env/1.0.0
```

Then set the correct configuration of the cache directories, where <YOUR_ID> is replaced with you credentials which you can find by entering `whoami` into the terminal once you are logged into myriad. Once you have added your credentials save these lines into your .bashrc file in the base directory (e.g. /home/<YOUR_ID>/.bashrc):

```bash
# Set all the Singularity cache dirs to Scratch
export SINGULARITY_CACHEDIR=/home/<YOUR_ID>/Scratch/.singularity/
export SINGULARITY_TMPDIR=/home/<YOUR_ID>/Scratch/.singularity/tmp
export SINGULARITY_LOCALCACHEDIR=/home/<YOUR_ID>/Scratch/.singularity/localcache
export SINGULARITY_PULLFOLDER=/home/<YOUR_ID>/Scratch/.singularity/pull

# Bind your Scratch directory so it is accessible from inside the container
export SINGULARITY_BINDPATH=/scratch/scratch/<YOUR_ID>
```

### Nextflow

Download the latest release of nextflow. Warning: the self-update line should update to the latest version, but sometimes not, so please check which is the latest release (https://github.com/nextflow-io/nextflow/releases), you can then manually set this by entering (`NXF_VER=XX.XX.X`).

```bash
## Download Nextflow-all
curl -s https://get.nextflow.io | bash
NXF_VER=22.10.0
nextflow -self-update
chmod a+x nextflow
mv nextflow ~/bin/nextflow
```

Then make sure that your bin PATH is executable, by placing the following line in your .bashrc:

```bash
export PATH=$PATH:/home/<YOUR_ID>/bin
```
