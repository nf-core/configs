# nf-core/configs: DaiSyBio

To use the DaiSyBio profile, run a nf-core pipeline with `-profile daisybio,<singularity/apptainer>`.

This will automatically download and apply ['daisybio.config'](../conf/daisybio.config) as a nextflow config file.

The config file will set slurm as a scheduler for the compute cluster, define max resources, and specify cache locations for singularity, apptainer, and iGenomes.
Pipeline-specific parameters still need to be configured manually.

## Keep work directories

Work directories will be kept at `/nfs/scratch/nf-core_work/` in a directory named after the full path of the launch directory ("." separated). They are automatically removed after a successful pipeline run. To keep the intermediate files, e.g. for using the `-resume` function, add `keep_work` as a profile: `-profile daisybio,<singularity/apptainer>,keep_work`.

## GPU support

If you need GPU access, add `gpu` to the profile list: `-profile daisybio,<singularity/apptainer>,gpu`.
This will submit all processes labeled with `process_gpu` to our GPU queue.
If you are using an nf-core pipeline, processes with GPU support should be already labeled correctly.
If you are using a custom pipeline, you need to add the label to the process definition:

```
process YOURGPUPROCESS {
    label 'process_gpu'
    # ...
}
```
