# nf-core/configs: Ilifu slurm cluster configuration

To use, run the pipeline with `-profile ilifu`. This will use the [`ilifu.config`](../conf/ilifu.config) which has been pre-configured
with a setup suitable for the Ilifu slurm cluster. In particular it configures the use of Singularity containers and chooses an
appropriate queue based on the memory required and the need (or lack of need) for a GPU (as specified using the
[`accelerator` attribute](https://www.nextflow.io/docs/latest/process.html#accelerator) of the Nextflow process).

## Running the workflow on the Ilifu slurm cluster

Mextflow is made available using the Environment Modules system. Load the Nextflow module with `module load nextflow`.

Do not run Nextflow directly on the login node, rather write a script that executes `module load nextflow` and then
runs the workflow with `nextflow -profile ilifu`.

Singularity containers are cached in the directory specified by `NXF_SINGULARITY_CACHEDIR`. Ensure that this directory exists and
that the environment variable is set to ensure that you re-use Singularity container images.

An example script illustrating the execution of a (fictional) workflow follows:

```bash
#!/bin/bash

#SBATCH -J my_pipeline

NXF_SINGULARITY_CACHEDIR=/projects/bio/sanbi/singularity_images
export NXF_SINGULARITY_CACHEDIR

module add nextflow

nextflow run nf-core/my_pipeline -profile ilifu \
    -w /path/to/some/dir/work \
    -resume
    --some_parameter

## clean up on exit 0 - delete this if you want to keep the work dir
status=$?
if [[ $status -eq 0 ]]; then
    rm -r /path/to/some/dir/work
fi

```

Memory, CPU and time limits can be imposed by providing `--max_memory`, `--max_cpus` and `--max_time` paramaters to the workflow run.

To check which versions of Nextflow are installed on the cluster and which is the default version, use the `module avail nextflow` command. If a
newer version is required, contact [Ilifu support](mailto:support@ilifu.ac.za).
