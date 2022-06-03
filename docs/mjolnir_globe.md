# nf-core/configs: Section for Hologenomics at GLOBE, University of Copenhagen (Mjolnir server) Configuration

> **NB:** You will need an account on Mjolnir to run the pipeline. If in doubt contact IT.

Prior to running the pipeline for the first time with the `mjolnir_globe.config` (../conf/mjolnir_globe.config), users **must** create a hidden directory called `.tmp_nfcore` in their data/project directory on Mjolnir where the temp files from nf-core pipelines will be re-directed by the `NXF_TEMP` command (see below).

The contents of the `.tmp_nfcore` directory should be periodically deleted manually to save on space.
If the `NXF_TEMP` command is not used to properly re-direct temp files the `/tmp` directory on the compute nodes will be used and quickly filled up, which blocks anyone from working on these nodes until the offending user removes their files.

The following lines **must** be added by users to their `~/.bash_profile`:

```bash
#re-direct tmp files away from /tmp directories on compute nodes or the headnode
export NXF_TEMP=/maps/projects/mjolnir1/people/$USER/.tmp_nfcore

# nextflow - limiting memory of virtual java machine
NXF_OPTS='-Xms1g -Xmx4g'
```

Once you have created the `.tmp_nfcore` directory and added the above lines of code to your `.bash_profile` you can run an nf-core pipeline.

Before running a pipeline you will need to load Java, Miniconda, Singularity and Nextflow. You can do this by including the commands below in your SLURM/sbatch script:

```bash
## Load Java and Nextflow environment modules
module purge
module load jdk/1.8.0_291 miniconda singularity/3.8.0 nextflow/21.04.1.5556
```

All of the intermediate output files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
The `mjolnir_globe` config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completeed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space.
