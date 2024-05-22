# nf-core/configs: CalcUA - UAntwerp Tier-2 High Performance Computing Infrastructure (VSC)

> **NB:** You will need an [account](https://docs.vscentrum.be/access/vsc_account.html) to use the CalcUA VSC HPC cluster to run the pipeline.

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Quickstart](#quickstart)
  - [Slurm-scheduled pipeline](#slurm-scheduled-pipeline)
  - [Running pipeline in a single Slurm job](#running-pipeline-in-a-single-slurm-job)
- [Step-by-step instructions](#step-by-step-instructions)
- [Location of output and work directory](#location-of-output-and-work-directory)
  - [Debug mode](#debug-mode)
- [Availability of Nextflow](#availability-of-nextflow)
- [Overview of partition profiles and resources](#overview-of-partition-profiles-and-resources)
- [Schedule Nextflow pipeline using Slurm](#schedule-nextflow-pipeline-using-slurm)
- [Local Nextflow run on a single (interactive) node](#local-nextflow-run-on-a-single-interactive-node)
- [Apptainer / Singularity environment variables for cache and tmp directories](#apptainer--singularity-environment-variables-for-cache-and-tmp-directories)
- [Troubleshooting](#troubleshooting)
  - [Failed to pull singularity image](#failed-to-pull-singularity-image)

<!-- /code_chunk_output -->

## Quickstart

To get started with running nf-core pipelines on CalcUA, you can use one of the example templates below. For more detailed info, see the extended explanations further below.

### Slurm-scheduled pipeline

Example `job_script.slurm` to run the pipeline using the Slurm job scheduler to queue the individual tasks making up the pipeline. Note that the head nextflow process used to launch the pipeline does not need to request many resources.

```bash
#!/bin/bash -l
#SBATCH --partition=broadwell          # choose partition to run the nextflow head process on
#SBATCH --job-name=nextflow            # create a short name for your job
#SBATCH --nodes=1                      # node count
#SBATCH --cpus-per-task=1              # only 1 cpu cores is needed to run the nextflow head process
#SBATCH --mem-per-cpu=4G               # memory per cpu (4G is default for most partitions)
#SBATCH --time=00:02:00                # total run time limit (HH:MM:SS)
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

# Launch Nextflow head process.
# Provide a partition profile name to choose a particular partition queue, which
# will determine the available resources for each individual task in the pipeline.
# Note that the profile name ends with a `*_slurm` suffix, which indicates
# that this pipeline will submit each task to the Slurm job scheduler.
nextflow run nf-core/rnaseq \
  -profile test,vsc_calcua,broadwell_slurm \
  -with-report report.html \
  --outdir test_output

# Alternatively, use the generic slurm profile to let Nextflow submit tasks
# to different partitions, depending on their requirements.
nextflow run nf-core/rnaseq \
  -profile test,vsc_calcua,slurm \
  -with-report report.html \
  --outdir test_output
```

### Running pipeline in a single Slurm job

Example `job_script.slurm` to run the pipeline on a single node in local execution mode, only making use of the resources allocated by `sbatch`.

```bash
#!/bin/bash -l
#SBATCH --partition=broadwell          # choose partition to run the nextflow head process on
#SBATCH --job-name=nextflow            # create a short name for your job
#SBATCH --nodes=1                      # node count
#SBATCH --cpus-per-task=28             # request a full node for local execution (broadwell nodes have 28 cpus)
#SBATCH --mem=112G                     # total memory (e.g., 112G max for broadwell) - can be omitted to use default (= max / # cores)
#SBATCH --time=00:02:00                # total run time limit (HH:MM:SS)
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

# Launch Nextflow head process.
# Provide a partition profile name to choose a particular partition queue, which
# will determine the available resources for each individual task in the pipeline.
# Note that the profile name ends with a `*_local` suffix, which indicates
# that this pipeline will run in local execution mode on the submitted node.
nextflow run nf-core/rnaseq \
  -profile test,vsc_calcua,broadwell_local \
  -with-report report.html \
  --outdir test_output
```

## Step-by-step instructions

1.  Set the `APPTAINER_CACHEDIR` and `APPTAINER_TMPDIR` environment variables by adding the following lines to your `.bashrc` file (or simply add them to your Slurm job script):

        ```
        export APPTAINER_CACHEDIR="${VSC_SCRATCH}/apptainer/cache"
        export APPTAINER_TMPDIR="${VSC_SCRATCH}/apptainer/tmp"
        ```

    When using the `~/.bashrc` method, you can ensure that the environment variables are available in your jobs by starting your scripts with the line `#! /bin/bash -l`, although this does not seem to be required (see [below](#apptainer--singularity-environment-variables-for-cache-and-tmp-directories) for more info).

2.  Load Nextflow in your job script via the command: `module load Nextflow/23.04.2`. Alternatively, when using [your own version of Nextflow](#availability-of-nextflow), use `module load Java`.

3.  Choose whether you want to run in [local execution mode on a single node](#local-nextflow-run-on-a-single-interactive-node) or make use of the [Slurm job scheduler to queue individual pipeline tasks](#schedule-nextflow-pipeline-using-slurm).

    - For Slurm scheduling, choose a partition profile ending in `*_slurm`. E.g., `nextflow run pipeline -profile vsc_calcua,broadwell_slurm`.
    - For local execution mode on a single node, choose a partition profile ending in `*_local`. E.g., `nextflow run pipeline -profile vsc_calcua,broadwell_local`.

    Note that the `-profile` option can take multiple values, the first one always being `vsc_calcua` and the second one a partition plus execution mode.

4.  Specify the _partition_ that you want to run the pipeline on using the [`sbatch` command's `--partition=<name>` option](https://docs.vscentrum.be/jobs/job_submission.html#specifying-a-partition) and how many _resources_ should be allocated. See the [overview of partitions and their resources](#overview-of-partition-profiles-and-resources) below, or refer to [the CalcUA documentation](https://docs.vscentrum.be/antwerp/tier2_hardware.html) for more info.

    - For Slurm scheduling, the partition on which the head process runs has no effect on the resources allocated to the actual pipeline tasks. The head process only requires minimal resources (e.g., 1 CPU and 4 GB RAM).
    - For local execution mode on a single node, the partition selected via `sbatch` must match the one selected with nextflow's `-profile` option, otherwise the pipeline will not launch. It is probably convenient to simply request a full node (e.g., `--cpus-per-task=28` and `--mem=112G` for broadwell). Omitting `--mem-per-cpu` or `--mem` will [allocate the default memory value](https://docs.vscentrum.be/jobs/job_submission.html#requesting-memory), which is the total available memory divided by the number of cores, e.g., `28 * 4 GB = 112 GB` for broadwell (`128 GB - 16 GB buffer`).

5.  Submit the job script containing your full `nextflow run` command via `sbatch` or from an an interactive `srun` session launched via `screen` or `tmux` (to avoid the process from stopping when you disconnect your SSH session).

---

## Location of output and work directory

By default, Nextflow stores all of the intermediate files required to run the pipeline in the `work` directory. It is generally recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway. That's why this config contains a `cleanup` command that removes the `work` directory automatically once the pipeline has completed successfully.

If the run does not complete successfully then the `work` directory should be removed manually to save storage space. The default work directory is set to `$VSC_SCRATCH/work` per this configuration. You can also use the [`nextflow clean` command](https://www.nextflow.io/docs/latest/cli.html#clean) to clean up all files related to a specific run (including not just the `work` directory, but also log files and the `.nextflow` cache directory).

> **NB:** The Nextflow `work` directory for any pipeline is located in `$VSC_SCRATCH` by default and is cleaned automatically after a success pipeline run, unless the `debug` profile is provided.

### Debug mode

Debug mode can be enabled to always retain the `work` directory instead of cleaning it. To use it, pass `debug` as an additional value to the `-profile` option:

`nextflow run <pipeline> -profile vsc_calcua,broadwell_local,debug`

Note that this is a core config provided by nf-core pipelines, not something built into the VSC CalcUA config.

## Availability of Nextflow

Nextflow has been made available on CalcUA as a module. You can find out which versions are available by using `module av nextflow`.

If you need to use a specific version of Nextflow that is not available, you can of course manually install it to your home directory and add the executable to your `PATH`:

```
curl -s https://get.nextflow.io | bash
mkdir -p ~/.local/bin/ && mv nextflow ~/.local/bin/
```

Before it can be used, you will still need to load the Java module in your job scripts: `module load Java`.

## Overview of partition profiles and resources

> **NB:** Aside from the profiles defined in the table below, one additional profile is available, named `slurm`. It automatically lets Nextflow choose the most appropriate Slurm partition to submit each pipeline task to based on the task's requirements (CPU, memory and run time).
> Example usage: `nextflow run -profile vsc_calcua,slurm`.

The CalcUA config defines two types of profiles for each of the following partitions:

| Partition     | Cluster                   | Profile name        | Type                 | Max memory               | Max CPU              | Max wall time | Example usage                                                     |
| ------------- | ------------------------- | ------------------- | -------------------- | ------------------------ | -------------------- | ------------- | ----------------------------------------------------------------- |
| zen2          | Vaughan                   | zen2_slurm          | Slurm scheduler      | 240 GB (per task)        | 64 (per task)        | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,zen2_slurm`          |
| zen2          | Vaughan                   | zen2_local          | Local node execution | 240 GB (or as requested) | 64 (or as requested) | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,zen2_local`          |
| zen3          | Vaughan                   | zen3_slurm          | Slurm scheduler      | 240 GB (per task)        | 64 (per task)        | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,zen3_slurm`          |
| zen3          | Vaughan                   | zen3_local          | Local node execution | 240 GB (or as requested) | 64 (or as requested) | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,zen3_local`          |
| zen3_512      | Vaughan                   | zen3_512_slurm      | Slurm scheduler      | 496 GB (per task)        | 64 (per task)        | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,zen3_512_slurm`      |
| zen3_512      | Vaughan                   | zen3_512_local      | Local node execution | 496 GB (or as requested) | 64 (or as requested) | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,zen3_512_local`      |
| broadwell     | Leibniz                   | broadwell_slurm     | Slurm scheduler      | 112 GB (per task)        | 28 (per task)        | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,broadwell_slurm`     |
| broadwell     | Leibniz                   | broadwell_local     | Local node execution | 112 GB (or as requested) | 28 (or as requested) | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,broadwell_local`     |
| broadwell_256 | Leibniz                   | broadwell_256_slurm | Slurm scheduler      | 240 GB (per task)        | 28 (per task)        | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,broadwell_256_slurm` |
| broadwell_256 | Leibniz                   | broadwell_256_local | Local node execution | 240 GB (or as requested) | 28 (or as requested) | 3 days        | `nextflow run <pipeline> -profile vsc_calcua,broadwell_256_local` |
| skylake       | Breniac (formerly Hopper) | skylake_slurm       | Slurm scheduler      | 176 GB (per task)        | 28 (per task)        | 7 days        | `nextflow run <pipeline> -profile vsc_calcua,skylake_slurm`       |
| skylake       | Breniac (formerly Hopper) | skylake_local       | Local node execution | 176 GB (or as requested) | 28 (or as requested) | 7 days        | `nextflow run <pipeline> -profile vsc_calcua,skylake_local`       |
| all           | /                         | slurm               | Slurm scheduler      | /                        | /                    | /             | `nextflow run <pipeline> -profile vsc_calcua,slurm`               |

For more information on the difference between the [\*\_slurm-type](#schedule-nextflow-pipeline-using-slurm) and [\*\_local-type](#local-nextflow-run-on-a-single-interactive-node) profiles, see below. Briefly,

- Slurm profiles submit each pipeline task to the Slurm job scheduler using a particular partition.
  - The generic `slurm` profile also submits jobs to the Slurm job scheduler, but it can stage them across different partitions simultaneously depending on the tasks' requirements.
- Local profiles run pipeline tasks on the local node, using only the resource that were requested by `sbatch` (or `srun` in interactive mode).

The max memory for the Slurm partitions is set to the [available amount of memory for each partition](https://docs.vscentrum.be/antwerp/tier2_hardware.html) minus 16 GB (which is the amount reserved for the OS and file system buffers, [see slide 63 of this CalcUA introduction course](https://calcua.uantwerpen.be/courses/hpc-intro/IntroductionHPC-20240226.pdf)). For the local profiles the resources are set dynamically based on those requested by `sbatch`.

More information on the hardware differences between the partitions can be found on [the CalcUA website](https://www.uantwerpen.be/en/research-facilities/calcua/infrastructure/) and in the [VSC documentation](https://docs.vscentrum.be/antwerp/tier2_hardware.html). You can also use the `sinfo  -o "%12P %.10A %.11l %D %c %m"` command to see the available partitions yourself.

> **NB:** Do not launch nextflow jobs directly from a login node. Not only will this occupy considerable resources on the login nodes (the nextflow master process/head job can still use considerable amounts of RAM, see [https://nextflow.io/blog/2024/optimizing-nextflow-for-hpc-and-cloud-at-scale.html](https://nextflow.io/blog/2024/optimizing-nextflow-for-hpc-and-cloud-at-scale.html)), but the command might get cancelled (since there is a wall time for the login nodes too).

## Schedule Nextflow pipeline using Slurm

The `*_slurm` (and `slurm`) profiles allow Nextflow to use the Slurm job scheduler to queue each pipeline task as a separate job. The main job that you manually submit using `sbatch` will run the head Nextflow process (`nextflow run ...`), which acts as a governor and monitoring job, and spawn new Slurm jobs for the different tasks in the pipeline. Each task will request the appropriate amount of resources defined by the pipeline (up to a threshold set in the given partition's profile) and will be run as an individual Slurm job. This means that each task will be placed in the scheduling queue individually and [all the standard priority rules](https://docs.vscentrum.be/jobs/why_doesn_t_my_job_start.html#why-doesn-t-my-job-start) will apply to each of them.

The `nextflow run ...` command that launches the head process, can be invoked either via `sbatch` or from an an interactive `srun` session launched via `screen` or `tmux` (to avoid the process from stopping when you disconnect your SSH session), but it **does NOT need to request the total amount of resources that would be required for the full pipeline!**

> **NB:** When using the slurm-type profiles, the initial job that launches the master nextflow process does not need many resources to run. Therefore, use the #SBATCH options to limit its requested to a small sensible amount (e.g., 2 CPUs and 4 GB RAM), regardless of how computationally intensive the actual pipeline is.

> **NB:** The wall time of the Nextflow head process will ultimately determine how long the pipeline can run for.

## Local Nextflow run on a single (interactive) node

In contrast to the `*_slurm` profiles, the `*_local` profiles instead run in Nextflow's _local execution mode_, which means that they do not make use of the Slurm job scheduler. Instead, the head Nextflow process (`nextflow run ...`) will run on the allocated compute node and spawn all of sub-processes for the individual tasks in the pipeline on that same node (i.e., similar to running a pipeline on your own machine). The available resources are determined by the [`#SBATCH` options passed to Slurm](https://docs.vscentrum.be/jobs/job_submission.html#requesting-compute-resources) as usual and are shared among all tasks.

The `nextflow run ...` command that launches the head process, can be invoked either via `sbatch` or from an an interactive `srun` session launched via `screen` or `tmux` (to avoid the process from stopping when you disconnect your SSH session) and it **DOES need to request the total amount of resources that are required by the full pipeline!**

> **NB:** When using one of the single node profiles, make sure that you launch the job on the same partition as the one specified by the `-profile vsc_calcua,<partition>` option of your `nextflow run` command, either by launching it from the matching login node or by using the `sbatch` option `--partition=<partition>`. E.g., a job script containing the following nextflow command:
> `nextflow run <pipeline> -profile vsc_calcua,broadwell_local`
> should be launched from a [Leibniz login node](https://docs.vscentrum.be/antwerp/tier2_hardware/leibniz_hardware.html#login-infrastructure) or via the following `sbatch` command:
> `sbatch --account <project_account> --partition broadwell script.slurm`

> **NB:** The single node profiles **do not** automatically set the pipeline's CPU/RAM resource limits to those of a full node, but instead dynamically set them based on those allocated by Slurm, i.e. those requested via the `sbatch`. However, in many cases, it likely is a good idea to simply request a full node.

## Apptainer / Singularity environment variables for cache and tmp directories

> **NB:** The default directory where Nextflow will cache container images is `$VSC_SCRATCH/apptainer/nextflow_cache`.

> **NB:** The recommended directories for apptainer/singularity's cache and tmp directories are `$VSC_SCRATCH/apptainer/cache` (cache directory for images layers) and `$VSC_SCRATCH/apptainer/tmp` (temporary directory used during build or docker conversion) respectively, to avoid filling up your home storage and/or job node's SSDs (since the default locations when unset are `$HOME/.apptainer/cache` and `/tmp` respectively).

[Apptainer](https://apptainer.org/) is an open-source fork of [Singularity](https://sylabs.io/singularity/), which is an alternative container runtime to Docker. It is more suitable to usage on HPCs because it can be run without root privileges and does not use a dedicated daemon process. More info on the usage of Apptainer/Singularity on the VSC HPC can be found [here](https://docs.vscentrum.be/software/singularity.html).

When executing Nextflow pipelines using Apptainer/Singularity, the container image files will by default be cached inside the pipeline work directory. The CalcUA config profile instead sets the [singularity.cacheDir setting](https://www.nextflow.io/docs/latest/singularity.html#singularity-docker-hub) to a central location on your scratch space (`$VSC_SCRATCH/apptainer/nextflow_cache`), in order to reuse them between different pipelines. This is equivalent to setting the `NXF_APPTAINER_CACHEDIR`/`NXF_SINGULARITY_CACHEDIR` environment variables manually (but note that the `cacheDir` defined in the config file takes precedence and cannot be overwritten by setting the environment variable).

Apptainer/Singularity makes use of two additional environment variables, `APPTAINER_CACHEDIR`/`SINGULARITY_CACHEDIR` and `APPTAINER_TMPDIR`/`SINGULARITY_TMPDIR`. As recommended by the [VSC documentation on containers](https://docs.vscentrum.be/software/singularity.html#building-on-vsc-infrastructure), these should be set to a location on the scratch system, to avoid exceeding the quota on your home directory file system.

> **NB:** The cachedir and tmpdir are only used when new images are built or converted from existing docker images. For most nf-core pipelines this does not happen, since they will instead try to directly pull pre-built singularity images from [Galaxy Depot](https://depot.galaxyproject.org/singularity/)

- The [cache directory](https://apptainer.org/docs/user/main/build_env.html#cache-folders) `APPTAINER_CACHEDIR`/`SINGULARITY_CACHEDIR` is used to store files and layers used during image creation (or conversion of Docker/OCI images). Its default location is `$HOME/.apptainer/cache`, but it is recommended to change this to `$VSC_SCRATCH/apptainer/cache` on the CalcUA HPC instead.
- The [temporary directory](https://apptainer.org/docs/user/main/build_env.html#temporary-folders) `APPTAINER_TMPDIR`/`SINGULARITY_TMPDIR` is used to store temporary files when building an image (or converting a Docker/OCI source). The directory must have enough free space to hold the entire uncompressed image during all steps of the build process. Its default location is `/tmp`, but it is recommended to change this to `$VSC_SCRATCH/apptainer/tmp` on the CalcUA HPC instead. The reason being that the default `/tmp` would refer to a directory on the the compute node running the master nextflow process, which are [small SSDs on CalcUA](https://docs.vscentrum.be/antwerp/tier2_hardware/uantwerp_storage.html).

  > **NB:** The tmp directory needs to be created manually beforehand, otherwise pipelines that need to pull in and convert docker images, or the manual building of images yourself, will fail.

Currently, Apptainer respects environment variables with either an `APPTAINER` or `SINGULARITY` prefix, but because [support for the latter might be dropped in the future](https://apptainer.org/docs/user/main/singularity_compatibility.html#singularity-prefixed-environment-variable-support), the former variant is recommended.

These two variables can be set in several different ways:

- Specified in your `~/.bashrc` file (e.g., `echo "export APPTAINER_CACHEDIR=${VSC_SCRATCH}/apptainer/cache APPTAINER_TMPDIR=${VSC_SCRATCH}/apptainer/tmp" >> ~/.bashrc`) - recommended.
- Passed to `sbatch` as a parameter or on a `#SBATCH` line in the job script (e.g., `--export=APPTAINER_CACHEDIR=${VSC_SCRATCH}/apptainer/cache,APPTAINER_TMPDIR=${VSC_SCRATCH}/apptainer/tmp`).
- Directly in your job script (e.g., `export APPTAINER_CACHEDIR=${VSC_SCRATCH}/apptainer/cache APPTAINER_TMPDIR=${VSC_SCRATCH}/apptainer/tmp`).

However, note that for the `.bashrc` option to work, the environment need to be passed on to the slurm jobs. Currently, this seems to happen by default (i.e., variables defined in `~/.bashrc` are propagated), but there exist methods to enforce this more strictly. E.g., job scripts that start with `#!/bin/bash -l`, will ensure that jobs [launch using your login environment](https://docs.vscentrum.be/leuven/slurm_specifics.html#job-shell). Similarly, the `sbatch` options `[--get-user-env`](https://slurm.schedmd.com/sbatch.html#OPT_get-user-env) or [`--export=`](https://slurm.schedmd.com/sbatch.html#OPT_export) can be used. Also [see the CalcUA-specific](https://docs.vscentrum.be/jobs/slurm_pbs_comparison.html#main-differences-between-slurm-and-torque) and the [general VSC documentation for more info](https://docs.vscentrum.be/jobs/job_submission.html#the-job-environment).

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
