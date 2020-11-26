# nf-core/configs: UPPMAX Configuration

All nf-core pipelines have been successfully configured for use on the Swedish UPPMAX clusters.

## Getting help

We have a Slack channel dedicated to UPPMAX users on the nf-core Slack: [https://nfcore.slack.com/channels/uppmax](https://nfcore.slack.com/channels/uppmax)

## Using the UPPMAX config profile

To use, run the pipeline with `-profile uppmax` (one hyphen).
This will download and launch the [`uppmax.config`](../conf/uppmax.config) which has been pre-configured with a setup suitable for the UPPMAX servers.
Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

In addition to this config profile, you will also need to specify an UPPMAX project id.
You can do this with the `--project` flag (two hyphens) when launching nextflow. For example:

```bash
nextflow run nf-core/PIPELINE -profile uppmax --project snic2018-1-234 # ..rest of pipeline flags
```

> NB: If you're not sure what your UPPMAX project ID is, try running `groups` or checking SUPR.

Before running the pipeline you will need to either install Nextflow or load it using the environment module system.

This config enables Nextflow to manage the pipeline jobs via the Slurm job scheduler and using Singularity for software management.

Just run Nextflow on a login node and it will handle everything else.

Remember to use `-bg` to launch Nextflow in the background, so that the pipeline doesn't exit if you leave your terminal session.

## Using iGenomes references

A local copy of the iGenomes resource has been made available on all UPPMAX clusters so you should be able to run the pipeline against any reference available in the `igenomes.config`.
You can do this by simply using the `--genome <GENOME_ID>` parameter.

## Getting more memory

If your nf-core pipeline run is running out of memory, you can run on a fat node with more memory using the following nextflow flags:

```bash
--clusterOptions "-C mem256GB" --max_memory "256GB"
```

This raises the ceiling of available memory from the default of `128.GB` to `256.GB`.
Rackham has nodes with 128GB, 256GB and 1TB memory available.

Note that each job will still start with the same request as normal, but restarted attempts with larger requests will be able to request greater amounts of memory.

All jobs will be submitted to fat nodes using this method, so it's only for use in extreme circumstances.

## Different UPPMAX clusters

The UPPMAX nf-core configuration profile uses the `hostname` of the active environment to automatically apply the following resource limits:

* `bianca`
  * cpus available: 16 cpus
  * memory available: 109 GB
* `irma`
  * cpus available: 16 cpus
  * memory available: 250 GB
* `rackham`
  * cpus available: 20 cpus
  * memory available: 125 GB

## Development config

If doing pipeline development work on UPPMAX, the `devel` profile allows for faster testing.

Applied after main UPPMAX config, it overwrites certain parts of the config and submits jobs to the `devcore` queue, which has much faster queue times.

All jobs are limited to 1 hour to be eligible for this queue and only one job allowed at a time.
It is not suitable for use with real data.

To use it, submit with `-profile uppmax,devel`.


## Running on Bianca

For security reasons, there is no internet access on Bianca so you can't download from or upload files to the cluster directly. Before running a nf-core pipeline on bianca you will first have to download the pipeline and singularity images needed elsewhere and transfer them via the wharf area to your bianca project. 

You can follow the guide for downloading pipelines [for offline use](https://nf-co.re/tools#downloading-pipelines-for-offline-use) Note that you will have to download the singularity images as well. 


After transffering the pipeline and the singularity images to your project. Before running the pipeline you will have to indicate to nextflow where the singularity images are located by setting `NXF_SINGULARITY_CACHEDIR` :

`export NXF_SINGULARITY_CACHEDIR=Your_Location_For_The_Singularity_directory/.`

You should now be able to run your nf-core pipeline on bianca.
