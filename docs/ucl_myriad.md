# nf-core/configs: Myriad Configuration

All nf-core pipelines have been successfully configured for use on UCL's myriad cluster [University College London](https://www.rc.ucl.ac.uk/docs/Clusters/Myriad/).

To use, run the pipeline with `-profile ucl_myriad`. This will download and launch the [`ucl_myriad.config`](../conf/ucl_myriad.config) which has been pre-configured with a setup suitable for the myriad cluster.

## Using Nextflow on Myriad

Before running the pipeline you will need to configure Apptainer and install+configure Nextflow.

### Apptainer

This can be done with the following commands:

Set the correct configuration of the cache directories, where <YOUR_ID> is replaced with you credentials which you can find by entering `whoami` into the terminal once you are logged into Myriad. Once you have added your credentials save these lines into your `.bash_profile` file in your home directory (e.g. `/home/<YOUR_ID>/.bash_profile`):

```bash
# Set all the Apptainer environment variables
export APPTAINER_CACHEDIR=/home/<YOUR_ID>/Scratch/.apptainer/
export APPTAINER_TMPDIR=/home/<YOUR_ID>/Scratch/.apptainer/tmp
export APPTAINER_LOCALCACHEDIR=/home/<YOUR_ID>/Scratch/.apptainer/localcache
export APPTAINER_PULLFOLDER=/home/<YOUR_ID>/Scratch/.apptainer/pull
```

**Warning**: You may need to outcomment any singularity environmental variables you have set previously.

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

### Common troubleshooting issues:

1. If your job gets terminated by SIGHUP, you should then submit your nextflow script within a job:

`qsub -l h_rt=48:00:00 -l mem_free=40G -pe smp 1 -b y nextflow run`

2. If a job fails due to apptainer requiring too much cpu/memory, from the `mksquashfs` process.
   
Then make a sge qsub script to pull the container using apptainer, then point to the location of the resultant SIF files. 

e.g. 

```bash
#!/bin/bash -l
#$ -l h_rt=3:0:0
#$ -l mem=50G
#$ -N Apptainer_pull
#$ -wd /home/<YOUR_ID>/Scratch/
#$ -e /home/<YOUR_ID>/Scratch/

# Pull a container.
apptainer pull docker://kanghu/hite:3.2.0
```
