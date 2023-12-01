# nf-core/configs: DaiSyBio


To use the DaiSyBio profile, run a nf-core pipeline with  `-profile DaiSyBio,<singularity/apptainer>`.

This will automatically download and apply ['daisybio.config'](../conf/daisybio.config) as a nextflow config file.

The config file will set slurm as a scheduler for the compute cluster, define max resources, and specify cache locations for singularity, apptainer, and iGenomes.
Pipeline specific parameters still need to be configured manually.
