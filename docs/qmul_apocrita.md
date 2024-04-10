# nf-core/configs: Apocrita Configuration

All nf-core pipelines have been successfully configured for use on QMUL's Apocrita cluster [Queen Mary University of London](https://docs.hpc.qmul.ac.uk/).

To use, run the pipeline with `-profile qmul_apocrita`. This will download and launch the [`qmul_apocrita.config`](../conf/qmul_apocrita.config) which has been pre-configured with a setup suitable for Apocrita.

## Using Nextflow on Apocrita

Before running the pipeline you will need to configure Apptainer and install+configure Nextflow.

### Singularity

Set the correct configuration of the cache directories, where <YOUR_ID> is replaced with you credentials which you can find by entering `whoami` into the terminal once you are logged into Apocrita. Once you have added your credentials save these lines into your `.bash_profile` file in your home directory (e.g. `/data/home/<YOUR_ID>/.bash_profile`):

```bash
# Set all the Apptainer environment variables
export APPTAINER_CACHEDIR=/data/scratch/<YOUR_ID>/.apptainer/
export APPTAINER_TMPDIR=/data/scratch/<YOUR_ID>/.apptainer/tmp
export APPTAINER_LOCALCACHEDIR=/data/scratch/<YOUR_ID>/.apptainer/localcache
export APPTAINER_PULLFOLDER=/data/scratch/<YOUR_ID>/.apptainer/pull
```

### Nextflow

Download the latest release of nextflow. _Warning:_ the `self-update` line should update to the latest version, but sometimes not, so please check which is the latest release (https://github.com/nextflow-io/nextflow/releases), you can then manually set this by entering (`NXF_VER=XX.XX.X`).

```bash
## Download Nextflow-all
curl -s https://get.nextflow.io | bash
nextflow -self-update
NXF_VER=XX.XX.X
chmod a+x nextflow
mv nextflow ~/bin/nextflow
```

Then make sure that your bin PATH is executable, by placing the following line in your `.bash_profile`:

```bash
export PATH=$PATH:/data/home/<YOUR_ID>/bin
```
