# nf-core/configs: Janelia Research Campus Configuration

To use, run the pipeline with `-profile janelia`. This will download and launch the [`janelia.config`](../conf/janlia.config) which has been pre-configured with a setup suitable for the Janelia Research Campus LSF cluster.

## Running workflows on the Janelia Research Campus cluster

The latest version of Nextflow is not installed by default on the cluster. You will need to install it into your cluster account by following the installation instructions:

- [Install Nextflow](https://www.nextflow.io/docs/latest/getstarted.html#)

Remember to move the `nextflow` executable to `~/bin` or otherwise ensure that it's in your `PATH`.

Nextflow manages each process as a separate job that is submitted to the cluster by using the `bsub` command. Janelia's cluster has Singularity installed on all login and compute nodes, and the profile specifies that Singularity will be used to execute processes.

Nextflow should never be run directly on a login node. You can run it via an interactive cluster session (`bsub -Is /bin/bash`), or make a wrapper shell script like the example below, and submit with `bsub < $PWD/my_script.sh`

```bash
#!/bin/bash
#BSUB -o /path/to/a/log/dir/%J.o
#BSUB -e /path/to/a/log/dir/%J.e
#BSUB -n 2

export NXF_ANSI_LOG=false
export NXF_VER=22.10.7-5853
export NXF_JAVA_HOME=/misc/sc/jdks/zulu17
export NXF_SINGULARITY_CACHEDIR=$HOME/.singularity_cache

nextflow run \
/path/to/nf-core/pipeline/main.nf \
-w /path/to/some/dir/work \
-profile janelia \
-params-file my_params.json
```

## Using Nextflow Tower (web UI) to launch and monitor workflows

You can use Janelia's [internal Nextflow Tower instance](https://nextflow.int.janelia.org) to run workflows on the cluster. Additional instructions for using this resource can be found on the [Janelia Wiki](https://wikis.janelia.org/display/SCSW/Using+Nextflow+Tower).
