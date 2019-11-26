# nf-core/configs: UPPMAX Configuration

All nf-core pipelines have been successfully configured for use on the Swedish UPPMAX clusters.

## Using the UPPMAX config profile

To use, run the pipeline with `-profile uppmax` (one hyphen). This will download and launch the [`uppmax.config`](../conf/uppmax.config) which has been pre-configured with a setup suitable for the UPPMAX servers. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

In addition to this config profile, you will also need to specify an UPPMAX project id.
You can do this with the `--project` flag (two hyphens) when launching nextflow. For example:

```bash
nextflow run nf-core/PIPELINE -profile uppmax --project SNIC 2018/1-234 # ..rest of pipeline flags
```

Before running the pipeline you will need to either install Nextflow or load it using the environment module system.

This config enables Nextflow to manage the pipeline jobs via the Slurm job scheduler.
Just run Nextflow on a login node and it will handle everything else.

## Using iGenomes references

A local copy of the iGenomes resource has been made available on all UPPMAX clusters so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Running offline with Bianca

If running on Bianca, you will have no internet connection and these configs will not be loaded.
Please use the nf-core helper tool on a different system to download the required pipeline files, and transfer them to bianca.
This helper tool bundles the config files in this repo together with the pipeline files, so the profile will still be available.

Note that Bianca only allocates 7 GB memory per core so the max memory needs to be limited:

```bash
--max_memory "112GB"
```

## Getting more memory

If your nf-core pipeline run is running out of memory, you can run on a fat node with more memory using the following nextflow flags:

```bash
--clusterOptions "-C mem256GB" --max_memory "256GB"
```

This raises the ceiling of available memory from the default of `128.GB` to `256.GB`.
Rackham has nodes with 128GB, 256GB and 1TB memory available.

Note that each job will still start with the same request as normal, but restarted attempts with larger requests will be able to request greater amounts of memory.

All jobs will be submitted to fat nodes using this method, so it's only for use in extreme circumstances.

## Uppmax-devel config

If doing pipeline development work on Uppmax, this profile allows for faster testing.

Applied after main UPPMAX config, it overwrites certain parts of the config and submits jobs to the `devcore` queue, which has much faster queue times.

All jobs are limited to 1 hour to be eligible for this queue and only one job allowed at a time.
It is not suitable for use with real data.

To use it, submit with `-profile uppmax-devel`.
