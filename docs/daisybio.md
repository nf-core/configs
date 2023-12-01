# nf-core/configs: DaiSyBio

To use the DaiSyBio profile, run a nf-core pipeline with `-profile daisybio,<singularity/apptainer>`.

This will automatically download and apply ['daisybio.config'](../conf/daisybio.config) as a nextflow config file.

The config file will set slurm as a scheduler for the compute cluster, define max resources, and specify cache locations for singularity, apptainer, and iGenomes.
Pipeline specific parameters still need to be configured manually.

Singularity and apptainer are currently only installed on the exbio nodes. In order to use them, you can either install singularity/apptainer in a conda environment and execute nextflow inside the environment, or limit the queue to exbio nodes with `-process.queue exbio-cpu`
