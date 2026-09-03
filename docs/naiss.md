# nf-core/configs: NAISS Configuration

This profile provides configuration for running nf-core pipelines on NAISS
resources. Currently supported resources are

- arrhenius

## Getting help

We have a Slack channel dedicated to assist Swedish HPC users on the nf-core
Slack: [https://nfcore.slack.com/channels/helpdesk-hpc-sweden](https://nfcore.slack.com/channels/helpdesk-hpc-sweden)

## Using the NAISS config profile

To use, run the pipeline with `-profile naiss` (one hyphen).
This will download and launch the [`naiss.config`](../conf/naiss.config) which will provide general
configuration and defer to more specific configurations per cluster that will be loaded automatically.

### Cluster-specific configurations

#### arrhenius

The configuration will submit pipeline jobs via the `Slurm` job scheduler. Tasks
providing a container image will be run using `apptainer`. Images can be native (usually called
`singularity` for historic reasons) or provided through `OCI`/`Docker` images.

Images are downloaded and stored in a cache (usually in the `work` directory in the
directory where you start Nextflow). If the image provided is non-native (`Docker`), it
needs to be converted before storing. If you run out of disk space converting images set
`APPTAINER_CACHEDIR` environment variable to a location with more space.

`Nextflow` also supports the environment variable `NXF_APPTAINER_CACHEDIR` which can be used to
store and supply images for repeated executions. The equivalent `Nextflow` config setting is
`apptainer.cacheDir`.

In addition to this config profile, you will also need to specify an NAISS project id.
You can do this with the `--project` flag (two hyphens) when launching `Nextflow`.
For example:

```bash
# Launch a nf-core pipeline with the naiss profile for the project id naiss2026-1-234
$ nextflow run nf-core/<PIPELINE> -profile naiss --project naiss2026-1-234 [...]
```

> NB: If you're not sure what your NAISS project ID is, try running `groups` or checking SUPR.

You can run `Nextflow` on a login node in a `screen` or a `tmux` session or in a job
(batch or interactive) and it will handle everything else. The nextflow main/monitoring
process uses very little resources.

##### GPU on arrhenius

GPUs are offerend on arrhenius through GH200 "superchip" nodes, which uses
another CPU architecture than the CPUs on normal arrhenius nodes. Since the
actual GPU work is initiated and controlled by the CPUs, which causes a problem.

So far, we haven't come up with a good solution for this. In the meantime,
you can tell nextflow to use specific container images for the tasks requiring
GPU resources.

Recent releases of nf-core pipelines should have a file
`conf/containers_singularity_https_arm64.config` which you can use to find the
Nextflow processes you need to run on GPU resources and copy those clauses to
a file `nextflow.config` in the directory you run nextflow from (which will make
it used without you asking, see
[Seqera documentation](https://docs.seqera.io/nextflow/config)) for other options.

But from e.g. https://github.com/nf-core/funcprofiler/blob/dev/conf/containers_singularity_https_arm64.config, you can
copy the line

```nextflow
process { withName: 'MULTIQC' { container = 'https://community-cr-prod.seqera.io/docker/registry/v2/blobs/sha256/e4/e48aa28aebc881254a499b24c3e1ce77b8df1b85a5432699ed6f72eb17ac7fb5/data' } }
```

to your own configuration to make nextflow use a compatible container image
when running on GPU resources.

## Getting more memory

If a task in your `nf-core` pipeline runs out of memory (exit code 137), you
can increase the memory request for that task by using a local config.

```nextflow
// nextflow.config in your launch directory ( the directory where you run `nextflow run` )
process {
    withName: '<PROCESS_NAME>' {
        memory = 256.GB
    }
}
```

Time (exit code 140), and cpu allocations can be increased in the same way.

The maximum allowed cpu, memory, and time allocations are determined by the
`process.resourceLimits` directive. If you request more resources than the
maximum they will be reduced to the limit set by this directive. We have
implemented a node auto-selection system that will automatically select the
best node for your job based on the resources you request.

## Local execution

For specific processes with very short runtimes, the induced latency by submitting
the task to the scheduler and waiting for them to go through the queue may be
non-productive. If they are light enough, you can instead have nextflow start
them on the node where the main Nextflow process runs. The `naiss` profile
enforces limits on such processes so they don't consume too many resources. You
should still be aware and restrictive with local execution.

To configure local execution for a process, add

```nextflow
// nextflow.config in your launch directory ( the directory where you run `nextflow run` )
process {
    withName: '<PROCESS_NAME>' {
        executor 'local'
    }
}
```
