# nf-core/configs: Janelia Research Campus Configuration

To use, run the pipeline with `-profile janelia`. This will download and launch the [`janelia.config`](../conf/janlia.config) which has been pre-configured with a setup suitable for the Janelia Research Campus LSF cluster.

## Running the workflow on the Janelia Research Campus cluster

The latest version of Nextflow is not installed by default on the cluster. You will need to install it into your cluster account.

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

A recommended place to move the `nextflow` executable to is `~/bin` so that it's in the `PATH`.

Nextflow manages each process as a separate job that is submitted to the cluster by using the `bsub` command.

Janelia's cluster has Singularity installed on all login and compute nodes, and the profile specifies that Singularity will be used to execute processes.

Nextflow shouldn't run directly on the submission node but on a compute node.

To do so make a shell script with a similar structure to the following code and submit with `bsub < $PWD/my_script.sh`

```bash
#!/bin/bash
#BSUB -o /path/to/a/log/dir/%J.o
#BSUB -e /path/to/a/log/dir/%J.e
#BSUB -M 8000
#BSUB -q oversubscribed
#BSUB -n 2

export NXF_ANSI_LOG=false
export NXF_VER=22.04.0-5697
export NXF_JAVA_HOME=/misc/sc/jdks/zulu17
export NXF_SINGULARITY_CACHEDIR=$HOME/.singularity_cache

nextflow run \
/path/to/nf-core/pipeline/main.nf \
-w /path/to/some/dir/work \
-profile janelia \
-c my_specific.config \
-resume

## clean up on exit 0 - delete this if you want to keep the work dir
status=$?
if [[ $status -eq 0 ]]; then
  rm -r /path/to/some/dir/work
fi
```

You can also use the [internal Nextflow Tower instance](https://nextflow.int.janelia.org) to run workflows on the cluster. Additional instructions for using this resource can be found on the [Janelia Wiki](https://wikis.janelia.org/display/SCSW/Using+Nextflow+Tower).

