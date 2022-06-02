# nf-core/configs: Section for Hologenomics at GLOBE, Univeristy of Copenhagen (Mjolnir server) Configuration

> **NB:** You will need an account on Mjolnir to run the pipeline. If in doubt contact IT.

Prior to runing the pipeline for the first time, users **must** create a hidden directory called .tmp_eager in their user/work directory where the tmp files from nf-core/eager will be re-directed by the NXF_TEMP command (see below).

```bash
#navigate into correct directory
cd /maps/projects/mjolnir1/people/$USER

#create .tmp_eager directory. This is a hidden directory.
mkdir .tmp_eager
```

The contents of the .tmp_eager directory should be periodically deleted to save on space. 
If the NXF_TEMP command is not used to properly re-direct tmp files the /tmp directory on the compute nodes will be used and quickly filled up, which will make it so that noone can work on these nodes until the files are removed.

The following lines **must** be added by users to their .bash_profile:

```bash
#re-direct tmp files away from /tmp directories on compute nodes or the headnode
export NXF_TEMP=/maps/projects/mjolnir1/people/$USER/.tmp_eager

# nextflow - limiting memory of virtual java machine
NXF_OPTS='-Xms1g -Xmx4g'
```


The profile is configured to run with Singularity

Before running the pipeline you will need to load Java, Miniconda, Singularity and Nextflow. You can do this by including the commands below in your SLURM/sbatch script:

```bash
## Load Java and Nextflow environment modules
module purge
module load jdk/1.8.0_291 miniconda/4.9.2 singularity/3.8.0 nextflow/21.04.1.5556
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
The config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completeed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space.



This configuration will automatically choose the correct SLURM queue (short,medium,long) depending on the time and memory required by each process.

> **NB:** Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be submitted from one of the login nodes.
