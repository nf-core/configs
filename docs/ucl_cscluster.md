# nf-core/configs: CS cluster Configuration

All nf-core pipelines have been successfully configured for use on UCL's CS cluster [University College London](https://hpc.cs.ucl.ac.uk/).

To use, run the pipeline with `-profile ucl_cscluster`. This will download and launch the [`ucl_cscluster.config`](../conf/ucl_cscluster.config) which has been pre-configured with a setup suitable for the CS cluster.

## Using Nextflow on CS cluster

Before running the pipeline you will need to configure Singularity and install+configure Nextflow.

### Singularity

Set the correct configuration of the cache directories, where <YOUR_ID> is replaced with you credentials which you can find by entering `whoami` into the terminal once you are logged into CS cluster. Once you have added your credentials save these lines into your `.bash_profile` file in your home directory (e.g. `/home/<YOUR_ID>/.bash_profile`):

```bash
# Set all the Singularity environment variables
export SINGULARITY_CACHEDIR=/home/<YOUR_ID>/.singularity/
export SINGULARITY_TMPDIR=/home/<YOUR_ID>/.singularity/tmp
export SINGULARITY_LOCALCACHEDIR=/home/<YOUR_ID>/.singularity/localcache
export SINGULARITY_PULLFOLDER=/home/<YOUR_ID>/.singularity/pull
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
export PATH=$PATH:/home/<YOUR_ID>/bin
```

### CS specific information

Finally, we have been asked on this cluster to run nextflow on a special login node. So once you are logged into CS cluster, do,

```bash
ssh askey
```

And run your nextflow jobs from there using of course: `-profile ucl_cscluster` in you command.
