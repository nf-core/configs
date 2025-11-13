# nf-core/configs: IRIS Configuration

All nf-core pipelines have been successfully configured for use on the IRIS cluster at [Memorial Sloan Kettering Cancer Center (MSKCC)](https://www.mskcc.org/).

To use, run the pipeline with `-profile iris`. This will download and launch the [`iris.config`](../conf/iris.config) which has been pre-configured with a setup suitable for the IRIS cluster. Using this profile, Singularity images containing all required software will be pulled from our local library or downloaded and cached before execution of the pipeline.

## Before running the pipeline

Before running a pipeline for the first time, you will need to ensure that right version of Java, Nextflow and Singularity are available on the cluster. The IRIS cluster uses the SLURM job scheduler, and Nextflow will automatically submit jobs via SLURM.

### Load Java and Singularity

```bash
module load java/23.0.1
```

Singularity 4.1 should be loaded by default at `/usr/bin/singularity`

### Install Nextflow

You can install nextflow by running:

```bash
curl -s https://get.nextflow.io | bash
chmod +x nextflow
```

## Running the pipeline

A typical command to run an nf-core pipeline on IRIS would look like:

```bash
nextflow run nf-core/<PIPELINE> -profile iris [additional pipeline parameters]
```

### Optional Parameters

The IRIS config provides several optional parameters to customize job submission and paths:

- `--group`: Your IRIS group name (e.g., `core006`). When specified, sets the default working directory to `/scratch/<YOUR_GROUP>/work`. If not specified, the working directory defaults to `./work` in your current directory.
- `--partition`: Specify a SLURM partition (default: uses `$NXF_SLURM_PARTITION` environment variable or `cpu`)
- `--qos`: Set Quality of Service specification for SLURM jobs (e.g., `priority`)
- `--preemptable`: Set to `true` to use preemptable queues for faster job submission (default: `false`)
- `--isolated`: Set to `true` to restrict jobs to only the specified partition (default: `false`)

### Example Commands

Basic usage:

```bash
nextflow run nf-core/rnaseq -profile iris --input samplesheet.csv --genome GRCh38
```

Using the group parameter to set default working directory:

```bash
nextflow run nf-core/rnaseq -profile iris --group mygroup --input samplesheet.csv --genome GRCh38
```

Explicitly setting work and output directories:

```bash
nextflow run nf-core/rnaseq -profile iris \
  -work-dir /scratch/mygroup/work \
  --outdir /data1/mygroup/results \
  --input samplesheet.csv --genome GRCh38
```

Using preemptable queue for faster submission:

```bash
nextflow run nf-core/rnaseq -profile iris --preemptable true --input samplesheet.csv --genome GRCh38
```

Using a QoS for priority:

```bash
nextflow run nf-core/rnaseq -profile iris --partition cpu --qos priority --input samplesheet.csv --genome GRCh38
```

## Cluster Details

### Resource Limits

The IRIS config sets the following maximum resource limits:

- **CPUs**: 52 cores per job
- **Memory**: 550 GB per job
- **Time**: 7 days per job

### Queue Selection

The config automatically selects appropriate SLURM queues based on job requirements:

- **cpushort**: Jobs with runtime ≤ 2 hours (CPU only)
- **gpushort**: GPU jobs with runtime ≤ 2 hours
- **gpu**: Regular GPU jobs
- **cpu_highmem**: Jobs requiring ≥ 512 GB memory or ≥ 50 GB per CPU
- **preemptable**: First-attempt jobs when `--preemptable true` is set
- **cpu**: Default queue for standard CPU jobs

### GPU Support

The config includes support for GPU jobs. Processes labeled with `process_gpu` or `process_gpu_low` will automatically:

- Request GPU resources via SLURM (`--gres=gpu:1`)
- Use appropriate GPU queues (`gpu` or `gpushort`)
- Enable GPU support in Singularity containers (`--nv` flag)

## Automatic Resource Management

The IRIS config includes intelligent retry logic that automatically adjusts resources when jobs fail:

### Retry Strategy

- Jobs are automatically retried up to 3 times on failure
- Resources are dynamically increased based on the failure type:
  - **Out of Memory** (exit codes 125, 137): Memory increased by 10 GB
  - **Out of Time** (exit codes 15, 140): Time increased by 12 hours, memory by 4 GB
  - **Near resource limits**: Proactive increases to prevent future failures
  - **CPU starvation**: Additional CPUs allocated

### Process Labels

The config defines several process labels with default resources that scale automatically:

| Label                 | CPUs | Memory | Time |
| --------------------- | ---- | ------ | ---- |
| `process_single`      | 1    | 1 GB   | 4 h  |
| `process_low`         | 2    | 12 GB  | 2 h  |
| `process_medium`      | 6    | 36 GB  | 8 h  |
| `process_high`        | 12   | 72 GB  | 16 h |
| `process_long`        | 2    | 12 GB  | 20 h |
| `process_high_memory` | 6    | 200 GB | 8 h  |
| `process_gpu`         | 6    | 25 GB  | 8 h  |
| `process_gpu_low`     | 6    | 25 GB  | 2 h  |

These are starting values that will be automatically increased on retry if needed.

## Singularity Configuration

The config uses Singularity for containerization with the following settings:

- **Cache Directory**: Automatically set based on working directory or `$NXF_SINGULARITY_CACHEDIR`
- **Library Directory**: Uses the shared library, `/data1/core006/resources/singularity_image_library` (or `$NXF_SINGULARITY_LIBRARYDIR`)
- **Auto-mounting**: Enabled for seamless file access
- **Scratch Space**: Uses `/localscratch` when available

## Working Directory

- If the working directory is not set it is automatically configured based on your group (via --group <YOUR_GROUP>).
- Otherwise, the work directory is `./work` in your current directory
- Automatic cleanup is enabled when using `/scratch` to save space

## Getting Help

If you have any questions or issues running nf-core pipelines on IRIS, please contact:

- **IRIS Support**: Nikhil Kumar (kumarn1@mskcc.org)
- **nf-core Slack**: [https://nfcore.slack.com](https://nfcore.slack.com)

## Notes

> **Note**: You will need an account on the IRIS cluster at MSKCC to use this profile.

> **Note**: Nextflow should be run from a compute node (via `srun` or `sbatch`), not from the login node, to avoid overloading the login infrastructure.

> **Note**: The config automatically enables trace reports to help monitor pipeline execution and resource usage.
