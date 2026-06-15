# nf-core/configs: NC State Hazel HPC Configuration

nf-core pipelines have been configured for use on the Hazel HPC at NC State University.

To use, run the pipeline with `-profile hazel`.

Example:

`nextflow run nf-core/<pipeline> -profile hazel`

Running this command will download the `hazel` config from the nf-core repository, and will submit nextflow processes as jobs to the `slurm` job scheduler. Therefore, the `nextflow run` command must be run from the `login node`. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. These images are cached in `/share/$GROUP/$USER/tmp` so they don't have to be re-downloaded on subsequent runs.

## Loading required environment modules

Before running the pipeline you will need to load Nextflow using the environment module system on hazel. Some of these modules are managed by the BRC, and are not in the default module path. See this resource for information about using these modules: https://hurwitzlab.github.io/COS_Compute_Handbook/chapters/14_loading_brc_modules.html

```bash
## Load Nextflow environment modules
module purge                    # Optional, unload any currently loaded modules.
module load nextflow/26.04.3    # Required
module load nf-core             # Optional, manages and downloads nf-core pipelines for common use. Requires singularity.
```

## Job submission partitions

By default, using this profile will submit jobs to the `compute` partition. To specify a different partition for submission, use `--partition <PARTITION NAME>` in the `nextflow run` command.

Nextflow processes with the `process_gpu` label will be submitted to the `gpu` partition by default; override with `--gpu_partition <PARTITION NAME>`. To request a different GPU type or multiple GPUs, use `--hazel_gpu 'gpu:<gpu-type>:<num-gpus>'` at runtime.


## Overriding Hazel config options

Nextflow-level options passed to your `nextflow run` command will override options contained in the Hazel institutional profile:

```bash
nextflow run nf-core/<pipeline> -profile hazel --max_memory 256.GB  # raise memory ceiling
nextflow run nf-core/<pipeline> -profile hazel --hazel_gpu 'gpu:a100:2'  # different GPU
```

For persistent overrides, use a local config file with `-c my_overrides.config`.

:::note
You will need an account to use the Hazel HPC in order to run the pipeline. If in doubt contact IT or your PI to get access.
:::

:::note
Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
:::
