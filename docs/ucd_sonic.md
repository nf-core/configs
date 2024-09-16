# nf-core/configs: UCD Sonic Configuration

The nf-core pipeline [sarek](https://nf-co.re/sarek) has been successfully tested on [Sonic HPC] (https://www.ucd.ie/itservices/ourservices/researchit/researchcomputing/sonichpc) using this config.

This Sonic config offers very minimal options to users but should allow the use of all nf-core pipelines.

## sbatch_nxf_creator

To run a pipeline, you can optionally use the [sbatch_nxf_creator](https://github.com/brucemoran/sbatch_nxf_creator) method.

This allows you to write a YAML file including all of your sample names that you want to process individually, as well as your basic Nextflow command and where the output should be written.

There are some additional requirements on Sonic based on its use of SLURM which are resolved using this write this method.

The `sbatch_nxf_creator.sh` parses your YAML and makes an `sbatch` file that can be submitted to the scheduler via a simple `sbatch my_file.sbatch` command.

Practically, it means appending `srun` to the command and appending `-with-mpi`, as well as a few other vaguaries like specifying output and loading `Nextflow` and `Singularity`.
