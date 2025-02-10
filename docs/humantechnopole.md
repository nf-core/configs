# nf-core/configs: Human Technopole configuration

To use, run the pipeline with `-profile humantechnopole`. This will download and launch the [`humantechnopole.config`](../conf/humantechnopole.config) which has been pre-configured with a setup suitable for the Human Technopole SLURM cluster.

This configuration is tested for Nextflow 23.10 and above. 

## Before you use this profile

1. This profile automatically load Singularity module before the script using `beforeScript` directive. Hence, you should be able to use singulatiry containers without any additional configuration.
2. It is suggested to always use `/scratch` space for the working directory. Thus you should add something like `-workDir /scratch/$USER/your_work_dir` to set the working directory to some folder inside your scratch space in the HPC.
3. The `/localscratch` folder is automatically mounted in the container when using Singularity to ensure you have access to the `$TMPDIR` when running commands on the compute nodes

## Enable GPU support

You can use the `gpu` label in your process definition to enable GPU support. This will automatically trigger all the necessary settings.

You can use the [`accelerator` directive](https://www.nextflow.io/docs/latest/reference/process.html#accelerator) in your process to eventually request multiple GPUs. When this is absent the default is to request 1 GPU. 

For example to request 2 GPUs you can use something like this.

```nextflow
process GPU_PROCESS {
    label 'gpu'
    accelerator 2

    ...
}
```

## Running Nextflow workflow on the Human Technopole cluster

Various versions of Nextflow are available in the cluster as modules. You can see a list of available version using `module avail Nextflow` and then load your preferred Nextflow version using `module load`.

It is suggested to always use `/scratch` space for the working directory. Thus you should add something like `-workDir /scratch/$USER/your_work_dir` to set the working directory to some folder inside your scratch space in the HPC.

Nextflow shouldn't run directly on the submission node but on a compute node.
To do so make a shell script with a similar structure to the following code and submit with `sbatch my_script.sh`

```bash
#!/bin/bash
#SBATCH -J job_name 
#SBATCH -o /path/to/a/log/%x_%A.log
#SBATCH -c 1
#SBATCH --mem 8G
#SBATCH -p cpuq

module load Nextflow/24.10.4 #Change this to other version if needed

export NXF_ANSI_LOG=false
export NXF_OPTS="-Xms8G -Xmx8G -Dnxf.pool.maxThreads=2000"

# Eventually modify -workDir to a folder of your choice in your /scratch space
# Use -c to eventually add an additional configuration file
nextflow run \
/path/to/nf-core/pipeline/main.nf \
-w /path/to/some/dir/work \
-profile humantechnopole \
-workDir /scratch/$USER/nf-work \
-c my_specific.config 
```
