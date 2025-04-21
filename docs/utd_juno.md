# nf-core/configs: UTD Juno Configuration

TBD: All nf-core pipelines have been successfully configured for use on the [Juno HPC cluster](https://docs.circ.utdallas.edu/user-guide/systems/juno.html) at [The Univeristy of Texas at Dallas](https://www.utdallas.edu/).

To use, run the pipeline with `-profile utd_juno`. This will download and launch the [`utd_juno.config`](../conf/utd_juno.config) which has been pre-configured with a setup suitable for Juno.

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

> [!NOTE]
> You will need an account to use the HPC cluster on Ganymede in order to run the pipeline.
> https://docs.circ.utdallas.edu/user-guide/accounts/index.html
> Nextflow will need to submit the jobs via SLURM to the HPC cluster and as such the commands above will have to be executed on the login node.
> If in doubt contact CIRC.

## Heterogenous/GPU jobs

Juno is a heterogenous compute cluster, which means it can accommodate pipelines that require GPUs.
The config file has a dispatch rule that will automatically assign a queue based on the accelerator directive. You can always override this by specifying a queue directly in the `queue` directive.

The supported accelerators considered by the profile are NVIDIA H100 and A30 GPUs, you can request them like this:

```groovy
process NVIDIA_SMI {
    publishDir "results", mode: 'copy'
    accelerator params.gpus, type: params.gpu_type

    input:
    val(gpu_id)

    output:
    path "nvidia_smi_${gpu_id}.out", emit: results

    script:
    """
    NVIDIA_SMI=\${NVIDIA_SMI:-nvidia-smi}
    \${NVIDIA_SMI} -i ${gpu_id} > nvidia_smi_${gpu_id}.out
    """
}
```

