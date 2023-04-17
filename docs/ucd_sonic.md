# nf-core/configs: UCD Sonic Configuration

The nf-core pipeline [sarek](https://nf-co.re/sarek) has been successfully tested on [Sonic HPC] (https://www.ucd.ie/itservices/ourservices/researchit/researchcomputing/sonichpc) using this config.

This Sonic config offers very minimal options to users but should allow the use of all nf-core pipelines.

## sabtch_nxf_creator
To run a pipeline, you should use the [sbatch_nxf_creator](https://github.com/brucemoran/sbatch_nxf_creator) method.

This requires you to write a small YAML file including all of your sample names that you want to process individually, as well as your basic Nextflow command and where the output should be written.

There is some weirdness on Sonic via SLURM (maybe it's just me!) which required me to write this method, maybe you can bypass it.

The `sbatch_nxf_creator.sh` script takes you YAML and makes an `sbatch` file that can be submitted to the scheduler via a simple `sbatch my_file.sbatch` command.

Practically, it means appending `srun` to the command and appending `-with-mpi`, as well as a few other vaguaries like specifying output and loading `Nextflow` and `Singularity`.  

Even more practical is that as new samples arrive to you, you can add them to your YAML and then create new sbatch files, which I think is good.
