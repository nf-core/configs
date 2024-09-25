# nf-core/configs: St. Jude HPCF Configuration

All nf-core pipelines have been successfully configured for use on the High Performance Research Cluster (HPCF) at St. Jude Children's Research Hospital.
The HPCF cluster is using IBM Spectrum LSF for workload management and job scheduling.

To use, run the pipeline with `-profile stjude`. This will download and launch the [`stjude.config`](../conf/stjude.config) which has been pre-configured with a setup suitable for the St. Jude HPCF cluster. Using this profile, a Singularity image containing all of the required software will be used for execution of the pipeline.

## Running the Pipeline

Before running the pipeline, you will need to prepare a `NextFlow` runtime environment to launch the workflow.
You can do this by issuing the command below (not recommended):

```bash
## Load nextflow module
module load nextflow/23.10.0
```

You can also use the `NextFlow` installed in your own environment for better control of software version. `Nextflow` can be
easily installed via `conda` or `mamba` using the following command:

```bash
conda/mamba install nextflow={VERSION}
```


The `codna` or `mamba`  will automatically sets up the necessary environment for `Nextflow` execution.

## Resource Allocation

The St. Jude HPCF configuration includes the following resource limits:

- Max CPUs: 32
- Max Memory: 1024 GB
- Max Time: 240 hours (10 days)

## Queue Selection

The configuration automatically selects the appropriate queue based on your task requirements:

- GPU tasks: 'gpu'
- Short tasks (<30 min): 'short'
- High memory tasks (>512 GB): 'large_mem'
- Default: 'standard'

## GPU Usage

To use GPUs in your pipeline:

1. Set the `accelerator` option in your process directives.
2. Use the `--num_gpus` parameter when running your pipeline to specify the number of GPUs needed.
3. (Optional) If you want to use docker (unsupported) or singularity (supported) on HPCF, you need to add the following container options:

```bash
containerOptions = {
    workflow.containerEngine == "singularity" ? '--nv':
        ( workflow.containerEngine == "docker" ? '--gpus all': null )
}
```

## Singularity Configuration

Singularity is enabled by default with the following settings:

- Auto-mounts enabled
- Environment variables whitelist: SINGULARITY_TMPDIR, TMPDIR, CUDA_VISIBLE_DEVICES
- Pull timeout: 3 hours

> [!NOTE]
> You will need an account to use the HPC cluster at St. Jude Children's Research Hospital in order to run the pipeline. If in doubt, contact IT.

> [!NOTE]
> Nextflow will need to submit the jobs via the LSF job scheduler to the HPC cluster, and as such, the commands above will have to be executed on one of the login nodes. If in doubt, contact IT.

## Support

For any issues or questions, please contact:

**Profile Contact:** Haidong Yi (hyi@stjude.org)
