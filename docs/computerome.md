# nf-core/configs: Computerome 2.0 Configuration

This is a first attempt at creating a profile for the Computerome 2.0 cluster.

To use, run the pipeline with `-profile computerome`. This will download and launch the [`computerome.config`](../conf/computerome.config) which has been pre-configured with a setup suitable for the Computerome cluster.

## Using the Computerome config profile

Before running the pipeline you will need to load `Nextflow` using the environment module system (this can be done with e.g. `module load tools Nextflow/<VERSION>` where `VERSION` is e.g. `20.10`).

To use, run the pipeline with `-profile computerome` (one hyphen).
This will download and launch the [`computerome.config`](../conf/computerome.config) which has been pre-configured with a setup suitable for the Computerome servers.
It will enable `Nextflow` to manage the pipeline jobs via the `Torque` job scheduler.
Using this profile, `Singularity` image(s) containing required software(s) will be downloaded before execution of the pipeline.

Recent version of `Nextflow` also support the environment variable `NXF_SINGULARITY_CACHEDIR` which can be used to supply images. The computerome configuration uses your project's scratch folder as the cachedir if not specified.

In addition to this config profile, you will also need to specify a Computerome project id.
You can do this with the `--project` flag (two hyphens) when launching `Nextflow`.
For example:

```bash
# Launch a nf-core pipeline with the computerome profile for the project id ab00002
$ nextflow run nf-core/<PIPELINE> -profile computerome --project ab00002 [...]
```

> NB: If you're not sure what your Computerome project ID is, try running `groups`.

Remember to use `-bg` to launch `Nextflow` in the background, so that the pipeline doesn't exit if you leave your terminal session.
Alternatively, you can also launch `Nextflow` in a `screen` or a `tmux` session.
