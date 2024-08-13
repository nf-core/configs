# nf-core/configs: CalcUA - UAntwerp Tier-2 High Performance Computing Infrastructure (VSC)

> **NB:** You will need an [account](https://docs.vscentrum.be/access/vsc_account.html) to use the CalcUA VSC HPC to run the pipeline.

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Quick start](#quick-start)
  - [Slurm-scheduled pipeline run](#slurm-scheduled-pipeline-run)
  - [Single node pipeline run](#single-node-pipeline-run)
- [Step-by-step instructions](#step-by-step-instructions)
- [Location of output and work directory](#location-of-output-and-work-directory)
  - [Debug mode](#debug-mode)
- [Availability of Nextflow](#availability-of-nextflow)
- [Overview of partitions and resources](#overview-of-partitions-and-resources)
- [Schedule Nextflow pipeline tasks using Slurm](#schedule-nextflow-pipeline-tasks-using-slurm)
- [Local Nextflow run on a single (interactive) node](#local-nextflow-run-on-a-single-interactive-node)
- [Apptainer / Singularity and Nextflow environment variables for cache and tmp directories](#apptainer--singularity-and-nextflow-environment-variables-for-cache-and-tmp-directories)
- [Troubleshooting](#troubleshooting)
  - [Failed to pull singularity image](#failed-to-pull-singularity-image)

<!-- /code_chunk_output -->

## Quick start

To get started with running nf-core pipelines on CalcUA, you can use one of the example templates below. For more detailed info, see the extended explanations further below.

### Slurm-scheduled pipeline run

Example `job_script.slurm` to run the pipeline using the Slurm job scheduler to queue the individual tasks making up the pipeline. Note that the head Nextflow process used to launch the pipeline does not need to request many resources, 1 CPU and 4 GB should be adequate. The wall clock should be set so that it is long enough for all pipeline tasks to complete.

```bash
#!/bin/bash -l
#SBATCH --partition=broadwell          # choose partition to run the nextflow head process on
#SBATCH --job-name=nextflow            # create a short name for your job
#SBATCH --nodes=1                      # node count
#SBATCH --cpus-per-task=1              # only 1 cpu cores is needed to run the nextflow head process
#SBATCH --mem-per-cpu=4G               # memory per cpu (4G is default for most partitions)
#SBATCH --time=00:05:00                # total run time limit (HH:MM:SS)
#SBATCH --account=<project-account>    # set project account

# Load the available Nextflow module.
module load Nextflow

# Or, if using a locally installed version of Nextflow, make Java available.
# module load Java

# Set Apptainer/Singularity environment variables to define caching and tmp
# directories. These are used during the conversion of Docker images to
# Apptainer/Singularity ones.
# These lines can be omitted if the variables are already set in your `~/.bashrc` file.
export APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/cache"
export APPTAINER_TMPDIR="${VSC_SCRATCH}/apptainer/tmp"
# optional - set by default in the config already
# export NXF_APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/nextflow_cache"

# Launch Nextflow head process.
# Provide the vsc_calcua profile to use this config and let Nextflow schedule tasks
# using the Slurm job scheduler. For local execution on a single node, see below.
# Note that multiple profiles can be stacked, and here we use the built-in test profile
# of the nf-core/rnaseq pipeline for demonstration purposes.
nextflow run nf-core/rnaseq \
  -profile test,vsc_calcua \
  -with-report report.html \
  --outdir test_output
```

### Single node pipeline run

Example `job_script.slurm` to run the pipeline on a single node in local execution mode, only making use of the resources allocated by `sbatch`, instead of submitting each Nextflow task as a new Slurm job. Note that in this case we need to request as many resources as are necessary for the pipeline.

```bash
#!/bin/bash -l
#SBATCH --partition=broadwell          # choose partition to run the nextflow head process on
#SBATCH --job-name=nextflow            # create a short name for your job
#SBATCH --nodes=1                      # node count
#SBATCH --cpus-per-task=28             # request a full node for local execution (broadwell nodes have 28 cpus)
#SBATCH --mem=112G                     # total memory (e.g., 112G max for broadwell) - can be omitted to use default (= max / # cores)
#SBATCH --time=00:05:00                # total run time limit (HH:MM:SS)
#SBATCH --account=<project-account>    # set project account

# Load the available Nextflow module.
module load Nextflow

# Or, if using a locally installed version of Nextflow, make Java available.
# module load Java

# Set Apptainer/Singularity environment variables to define caching and tmp
# directories. These are used during the conversion of Docker images to
# Apptainer/Singularity ones.
# These lines can be omitted if the variables are already set in your `~/.bashrc` file.
export APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/cache"
export APPTAINER_TMPDIR="${VSC_SCRATCH}/apptainer/tmp"
# optional - set by default in the config already
# export NXF_APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/nextflow_cache"

# Launch Nextflow head process that will run on the same node as the pipeline tasks.
# Append the single_node profile after the vsc_calcua one, to make Nextflow schedule
# all jobs on the same local node. Note: don't do this on the login nodes!
nextflow run nf-core/rnaseq \
  -profile test,vsc_calcua,single_node \
  -with-report report.html \
  --outdir test_output
```

## Step-by-step instructions

1.  Set the `APPTAINER_CACHEDIR`, `APPTAINER_TMPDIR` and `NXF_APPTAINER_CACHEDIR` environment variables by adding the following lines to your `.bashrc` file (or simply add them to your Slurm job script):

    ```
    export APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/cache"
    export APPTAINER_TMPDIR="${VSC_SCRATCH}/apptainer/tmp"
    # optional - set by default in the config already
    # export NXF_APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/nextflow_cache"
    ```

    When using the `~/.bashrc` method, you can ensure that the environment variables are available in your jobs by starting your scripts with the line `#! /bin/bash -l`, although this does not always seem to be required (initial testing: required to propagate PATH, but not for other env vars?). See [below](#apptainer--singularity-and-nextflow-environment-variables-for-cache-and-tmp-directories) for more info.

2.  Load Nextflow in your job script via the command: `module load Nextflow/23.04.2`. Alternatively, when using [your own version of Nextflow](#availability-of-nextflow), use `module load Java`.

3.  Choose whether you want to use the [Slurm job scheduler to queue individual pipeline tasks](#schedule-nextflow-pipeline-using-slurm) (default mode) or if you prefer [local execution on a single node](#local-nextflow-run-on-a-single-interactive-node).

    - For Slurm scheduling, you only need to specify the `vsc_calcua` profile. E.g., `nextflow run pipeline -profile vsc_calcua`. Nextflow tasks will be scheduled as Slurm jobs to your current partition (or the one defined via `sbatch --partion=<partition-name>`).
    - For local execution mode on a single node, you need to append an additional sub-profile. E.g., `nextflow run pipeline -profile vsc_calcua,single_node`.

    Note that the `-profile` option can take multiple values, the first one always being `vsc_calcua` and the second `single_node` one being optional.

4.  Specify the _partition_ that you want to run the pipeline on using the [`sbatch` command's `--partition=<name>` option](https://docs.vscentrum.be/jobs/job_submission.html#specifying-a-partition) and how many _resources_ should be allocated. See the [overview of partitions and their resources](#overview-of-partitions-and-resources) below, or refer to [the CalcUA documentation](https://docs.vscentrum.be/antwerp/tier2_hardware.html) for more info.

    - For the default Slurm scheduling, the partition on which the head process runs has no effect on the resources allocated to the actual pipeline tasks; these will instead be requested by Nextflow depending on the particular process' requirements and limited by the maximum thresholds set for each partition in this config.
    - For local execution mode on a single node, it is probably convenient to simply request a full node (e.g., `--cpus-per-task=28` and `--mem=112G` for broadwell), but if fewer resources are requested, these limits will be passed on the Nextflow too.
    - Omitting `--mem-per-cpu` or `--mem` will [allocate the default memory value](https://docs.vscentrum.be/jobs/job_submission.html#requesting-memory), which is the total available memory divided by the number of cores, e.g., `28 * 4 GB = 112 GB` for broadwell (`128 GB - 16 GB buffer`).

> **NB:** The head process only requires minimal resources (e.g., 1 CPU and 4 GB RAM).

5.  Submit the job script containing your full `nextflow run` command via `sbatch` or from an an interactive `srun` session launched via `screen` or `tmux` (to avoid the process from stopping when you disconnect your SSH session).

> For more background info on how Slurm and Nextflow interact, you can read more in the [Nextflow training docs](https://training.nextflow.io/basic_training/executors/#submit-nextflow-as-a-job) and in this [Nextflow blog post](https://www.nextflow.io/blog/2023/best-practices-deploying-pipelines-with-hpc-workload-managers.html).

---

## Location of output and work directory

> **NB:** The Nextflow `work` directory is located in `$VSC_SCRATCH/work` by default, but this can be changed by using the `-work-dir` in your `nextflow run` command.

By default, Nextflow stores all of the intermediate files required to run the pipeline in the `work` directory. The default work directory is set to `$VSC_SCRATCH/work` in this config.

It is generally recommended to delete this directory after the pipeline has finished successfully, because it can grow quite large, and all of the main output files will be saved in the `results/` directory anyway. That's why this config contains a `cleanup` command that removes the `work` directory automatically once the pipeline has completed successfully.

If the run does not complete successfully, then the `work` directory is not deleted and pipelines can be re-submitted using the `-resume` flag to re-use any cached files. If runs are abandoned, the directory should be cleaned manually to save storage space.

You can also use the [`nextflow clean` command](https://www.nextflow.io/docs/latest/cli.html#clean) to clean up all files related to a specific run (including not just the `work` directory, but also log files and the `.nextflow` cache directory).

### Debug mode

> **NB:** The work directory is cleaned automatically after a successful pipeline run to avoid going over the storage quotas, but the `debug` profile can be provided to retain them in case you need to inspect any intermediate files (e.g., `-profile vsc_calcua,debug`).

Debug mode can be enabled to always retain the `work` directory instead of cleaning it. To use it, pass `debug` as an additional value to the `-profile` option (the order is important, later entries overwrite earlier ones!):

`nextflow run <pipeline> -profile vsc_calcua,debug`

Note that this is a core config provided by nf-core pipelines, not something built into the VSC CalcUA config directly.

## Availability of Nextflow

Nextflow has been made available on CalcUA as a module. You can find out which versions are available by using `module av nextflow`.

If you need to use a specific or more recent version of Nextflow that is not available, you can of course manually install it to your home directory and add the executable to your `PATH`:

```
curl -s https://get.nextflow.io | bash
mkdir -p ~/.local/bin/ && mv nextflow ~/.local/bin/
```

Before it can be used, you will still need to load the Java module in your job scripts: `module load Java`. Also make sure that you pass your PATH to your job scripts by starting them with `#!/bin/bash -l` or use the full path to the Nextflow binary instead of just calling `nextflow`.

## Overview of partitions and resources

The CalcUA config is built to work with the following partitions:

| Partition     | Cluster                   | Profiles               | Type                        | Max memory               | Max CPU              | Max wall time | Example usage                                   |
|---------------|---------------------------|------------------------|-----------------------------|--------------------------|----------------------|---------------|-------------------------------------------------|
| zen2          | Vaughan                   | vsc_calcua             | Slurm scheduler             | 240 GB (per task)        | 64 (per task)        | 3 days        | `nextflow run  -profile vsc_calcua`             |
| zen2          | Vaughan                   | vsc_calcua,single_node | Single node local execution | 240 GB (or as requested) | 64 (or as requested) | 3 days        | `nextflow run  -profile vsc_calcua,single_node` |
| zen3          | Vaughan                   | vsc_calcua             | Slurm scheduler             | 240 GB (per task)        | 64 (per task)        | 3 days        | `nextflow run  -profile vsc_calcua`             |
| zen3          | Vaughan                   | vsc_calcua,single_node | Single node local execution | 240 GB (or as requested) | 64 (or as requested) | 3 days        | `nextflow run  -profile vsc_calcua,single_node` |
| zen3_512      | Vaughan                   | vsc_calcua             | Slurm scheduler             | 496 GB (per task)        | 64 (per task)        | 3 days        | `nextflow run  -profile vsc_calcua`             |
| zen3_512      | Vaughan                   | vsc_calcua,single_node | Single node local execution | 496 GB (or as requested) | 64 (or as requested) | 3 days        | `nextflow run  -profile vsc_calcua,single_node` |
| broadwell     | Leibniz                   | vsc_calcua             | Slurm scheduler             | 112 GB (per task)        | 28 (per task)        | 3 days        | `nextflow run  -profile vsc_calcua`             |
| broadwell     | Leibniz                   | vsc_calcua,single_node | Single node local execution | 112 GB (or as requested) | 28 (or as requested) | 3 days        | `nextflow run  -profile vsc_calcua,single_node` |
| broadwell_256 | Leibniz                   | vsc_calcua             | Slurm scheduler             | 240 GB (per task)        | 28 (per task)        | 3 days        | `nextflow run  -profile vsc_calcua`             |
| broadwell_256 | Leibniz                   | vsc_calcua,single_node | Single node local execution | 240 GB (or as requested) | 28 (or as requested) | 3 days        | `nextflow run  -profile vsc_calcua,single_node` |
| skylake       | Breniac (formerly Hopper) | vsc_calcua             | Slurm scheduler             | 176 GB (per task)        | 28 (per task)        | 7 days        | `nextflow run  -profile vsc_calcua`             |
| skylake       | Breniac (formerly Hopper) | vsc_calcua,single_node | Single node local execution | 176 GB (or as requested) | 28 (or as requested) | 7 days        | `nextflow run  -profile vsc_calcua,single_node` |

For more information on the difference between the [Slurm scheduling](#schedule-nextflow-pipeline-tasks-using-slurm) and [Single node local execution mode](#local-nextflow-run-on-a-single-interactive-node), see below. Briefly,

- The default `vsc_calcua` profile submits each pipeline task to the Slurm job scheduler using the current partition (where the job was launched or the value supplied to `sbatch --partition=<name>`).
- The optional `single_node` profile runs pipeline tasks on the same single local node, using only the resource that were requested by `sbatch` (or `srun` in interactive mode).

The max memory for the Slurm partitions is set to the [available amount of memory for each partition](https://docs.vscentrum.be/antwerp/tier2_hardware.html) minus 16 GB (which is the amount reserved for the OS and file system buffers, [see slide 63 of this CalcUA introduction course](https://calcua.uantwerpen.be/courses/hpc-intro/IntroductionHPC-20240226.pdf)). For the local profiles the resources are set dynamically based on those requested by `sbatch`.

More information on the hardware differences between the partitions can be found on [the CalcUA website](https://www.uantwerpen.be/en/research-facilities/calcua/infrastructure/) and in the [VSC documentation](https://docs.vscentrum.be/antwerp/tier2_hardware.html). You can also use the `sinfo  -o "%12P %.10A %.11l %D %c %m"` command to see the available partitions yourself.

> **NB:** Do not launch nextflow jobs directly from a login node. Not only will this occupy considerable resources on the login nodes (the nextflow master process/head job can still use considerable amounts of RAM, see [https://nextflow.io/blog/2024/optimizing-nextflow-for-hpc-and-cloud-at-scale.html](https://nextflow.io/blog/2024/optimizing-nextflow-for-hpc-and-cloud-at-scale.html)), but the command might get cancelled (since there is a wall time for the login nodes too).

## Schedule Nextflow pipeline tasks using Slurm

The default behaviour of the `vsc_calcua` profile allows Nextflow to use the Slurm job scheduler to queue each pipeline task as a separate job. The main job that you manually submit using `sbatch` will run the head Nextflow process (`nextflow run ...`), which acts as a governor and monitoring job, and spawn new Slurm jobs for the different tasks in the pipeline. Each task will request the appropriate amount of resources defined by the pipeline (up to a threshold set per partition in this config) and will be run as an individual Slurm job. This means that each task will be placed in the scheduling queue individually and [all the standard priority rules](https://docs.vscentrum.be/jobs/why_doesn_t_my_job_start.html#why-doesn-t-my-job-start) will apply to each of them.

The `nextflow run ...` command that launches the head process, can be invoked either via `sbatch` or from an an interactive `srun` session launched via `screen` or `tmux` (to avoid the process from stopping when you disconnect your SSH session), but it **does NOT need to request the total amount of resources that would be required by the full pipeline!**

> **NB:** When using the default `vsc_calcua` profile, the initial job that launches the master nextflow process does not need many resources to run. Therefore, use the #SBATCH options to limit its requested to a small sensible amount (e.g., 1-2 CPUs and 4 GB RAM), regardless of how computationally intensive the actual pipeline is.

> **NB:** The wall time of the Nextflow head process will ultimately determine how long the pipeline can run for.

## Local Nextflow run on a single (interactive) node

By adding the `single_node` profile, Nextflow will run in _local execution mode_, which means that it will not make use of the Slurm job scheduler. Instead, the head Nextflow process (`nextflow run ...`) will run on the allocated compute node and spawn all sub-processes for the individual tasks in the pipeline on that same node (i.e., similar to running a pipeline on your own machine). The available resources are determined by the [`#SBATCH` options passed to Slurm](https://docs.vscentrum.be/jobs/job_submission.html#requesting-compute-resources) as usual and are shared among all tasks. The thresholds for the amount of resources that can be requested are automatically set to those that were requested during job submission (and will otherwise default to those of the partition).

The `nextflow run ...` command that launches the head process, can be invoked either via `sbatch` or from an an interactive `srun` session launched via `screen` or `tmux` (to avoid the process from stopping when you disconnect your SSH session) and it **DOES need to request the total amount of resources that are required by the full pipeline!**

> **NB:** `-profile vsc_calcua,single_node` **does not** automatically set the pipeline's CPU/RAM resource limits to those of a full node, but instead dynamically set them based on those allocated by Slurm, i.e. those requested via the `sbatch`. However, in many cases, it likely is a good idea to simply request a full node.

## Apptainer / Singularity and Nextflow environment variables for cache and tmp directories

> **NB:** The default directory where Nextflow will cache container images is set to `$VSC_SCRATCH/apptainer/nextflow_cache` for this config.

> **NB:** The recommended directories for apptainer/singularity's cache and tmp directories are `$VSC_SCRATCH/apptainer/cache` (cache directory for images layers) and `$VSC_SCRATCH/apptainer/tmp` (temporary directory used during build or docker conversion) respectively, to avoid filling up your home storage and/or job node's SSDs (since the default locations when unset are `$HOME/.apptainer/cache` and `/tmp` respectively). These environment variables cannot be set automatically by the config, so warnings will be displayed when launching runs without them being set.

[Apptainer](https://apptainer.org/) is an open-source fork of [Singularity](https://sylabs.io/singularity/), which is an alternative container runtime to Docker. It is more suitable to usage on HPCs because it can be run without root privileges and does not use a dedicated daemon process. More info on the usage of Apptainer/Singularity on the VSC HPC can be found [here](https://docs.vscentrum.be/software/singularity.html).

When executing Nextflow pipelines using Apptainer/Singularity, the container image files will by default be cached inside the pipeline work directory. The CalcUA config profile instead sets the [singularity.cacheDir setting](https://www.nextflow.io/docs/latest/singularity.html#singularity-docker-hub) to a central location on your scratch space (`$VSC_SCRATCH/apptainer/nextflow_cache`), in order to reuse them between different pipelines even when cleaning the work directory. If the `NXF_APPTAINER_CACHEDIR`/`NXF_SINGULARITY_CACHEDIR` environment variables are set manually, they will take precedence over this default setting.

Apptainer/Singularity makes use of two additional environment variables, `APPTAINER_CACHEDIR`/`SINGULARITY_CACHEDIR` and `APPTAINER_TMPDIR`/`SINGULARITY_TMPDIR`. As recommended by the [VSC documentation on containers](https://docs.vscentrum.be/software/singularity.html#building-on-vsc-infrastructure), these should be set to a location on the scratch system, to avoid exceeding the quota on your home directory file system.

> **NB:** The cachedir and tmpdir are only used when new images are built or converted from existing docker images. For most nf-core pipelines this does not happen, since they will instead try to directly pull pre-built singularity images from [Galaxy Depot](https://depot.galaxyproject.org/singularity/)

- The [cache directory](https://apptainer.org/docs/user/main/build_env.html#cache-folders) `APPTAINER_CACHEDIR`/`SINGULARITY_CACHEDIR` is used to store files and layers used during image creation (or conversion of Docker/OCI images). Its default location is `$HOME/.apptainer/cache`, but we recommended changing it to `$VSC_SCRATCH/apptainer/cache` (or another location in scratch) on the CalcUA HPC instead, to avoid exceeding the quota in the home file system.
- The [temporary directory](https://apptainer.org/docs/user/main/build_env.html#temporary-folders) `APPTAINER_TMPDIR`/`SINGULARITY_TMPDIR` is used to store temporary files when building an image (or converting a Docker/OCI source). The directory must have enough free space to hold the entire uncompressed image during all steps of the build process. Its default location is `/tmp` (or more accurately, `$TMPDIR` in the environment of the nextflow head process), but we recommended changing it to `$VSC_SCRATCH/apptainer/tmp` (or another location in scratch) on the CalcUA HPC instead. The reason being that the default `/tmp` would refer to a directory on the the compute node running the nextflow head process, which are [small SSDs on CalcUA](https://docs.vscentrum.be/antwerp/tier2_hardware/uantwerp_storage.html) that could get filled up otherwise.

  > **NB:** The tmp directory needs to be created manually beforehand, otherwise pipelines that need to pull in and convert docker images, or the manual building of images yourself, will fail.

Currently, Apptainer respects environment variables with either an `APPTAINER` or `SINGULARITY` prefix, but because [support for the latter might be dropped in the future](https://apptainer.org/docs/user/main/singularity_compatibility.html#singularity-prefixed-environment-variable-support), the former variant is recommended.

These two variables can be set in several different ways:

- Specified in your `~/.bashrc` file (e.g., `echo "export APPTAINER_CACHEDIR=${VSC_SCRATCH}/apptainer/cache APPTAINER_TMPDIR=${VSC_SCRATCH}/apptainer/tmp" >> ~/.bashrc`) - recommended.
- Passed to `sbatch` as a parameter or on a `#SBATCH` line in the job script (e.g., `--export=APPTAINER_CACHEDIR=${VSC_SCRATCH}/apptainer/cache,APPTAINER_TMPDIR=${VSC_SCRATCH}/apptainer/tmp`).
- Directly in your job script (e.g., `export APPTAINER_CACHEDIR=${VSC_SCRATCH}/apptainer/cache APPTAINER_TMPDIR=${VSC_SCRATCH}/apptainer/tmp`).

However, note that for the `.bashrc` option to work, the environment need to be passed on to the slurm jobs. Currently, this seems to happen by default (i.e., variables defined in `~/.bashrc` are propagated, as per [the VSC docs](https://docs.vscentrum.be/leuven/slurm_specifics.html#environment-propagation)), but there also exist methods to enforce this more strictly. E.g., job scripts that start with `#!/bin/bash -l`, will ensure that jobs [launch using your login environment](https://docs.vscentrum.be/leuven/slurm_specifics.html#job-shell). Similarly, the `sbatch` options [`--get-user-env`](https://slurm.schedmd.com/sbatch.html#OPT_get-user-env) or [`--export=`](https://slurm.schedmd.com/sbatch.html#OPT_export) can be used. Also [see the CalcUA-specific](https://docs.vscentrum.be/jobs/slurm_pbs_comparison.html#main-differences-between-slurm-and-torque) and the [general VSC documentation for more info](https://docs.vscentrum.be/jobs/job_submission.html#the-job-environment).

Lastly, note that this config file currently uses the Singularity engine rather than the Apptainer one (see [`singularity` directive: `enabled = true`](https://www.nextflow.io/docs/latest/config.html#scope-singularity)). The reason is that, for the time being, using the apptainer engine in nf-core pipelines will result in docker images being pulled and converted to apptainer ones, rather than making use of pre-built singularity images (see [nf-core documentation](https://nf-co.re/docs/usage/installation#pipeline-software)). Conversely, when making use of the singularity engine, pre-built images are downloaded and Apptainer will still be used in the background for running these, since the installation of `apptainer` will by default create an alias for `singularity` (and this is also the case on CalcUA).

## Troubleshooting

For general errors regarding the pulling of images, try clearing out the existing caches located in `$VSC_SCRATCH/apptainer`.

### Failed to pull singularity image

```
FATAL: While making image from oci registry: error fetching image to cache: while building SIF from
layers: conveyor failed to get: while getting config: no descriptor found for reference
"139610e0c1955f333b61f10e6681e6c70c94357105e2ec6f486659dc61152a21"
```

Errors similar to the one above can be avoided by first downloading all required container images manually before running the pipeline. It seems like they could be caused by parallel downloads overwhelming the image repository (see [issue](https://github.com/apptainer/singularity/issues/5020)).

To download a pipeline's required images, use `nf-core download <pipeline> --container-system singularity`. See the [nf-core docs](https://nf-co.re/tools#downloading-pipelines-for-offline-use) for more info.
