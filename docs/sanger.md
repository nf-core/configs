# nf-core/configs: Wellcome Sanger Institute Configuration

To use, run the pipeline with `-profile sanger`. This will download and launch the [`sanger.config`](../conf/sanger.config) which has been
pre-configured with a setup suitable for the Wellcome Sanger Institute LSF cluster.
Using this profile, either a docker image containing all of the required software will be downloaded, and converted to a Singularity image or
a Singularity image downloaded directly before execution of the pipeline.

## Running the workflow on the Wellcome Sanger Institute cluster

The latest version of Nextflow is not installed by default on the cluster. You will need to install it into a directory you have write access to

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

A recommended place to move the `nextflow` executable to is `~/bin` so that it's in the `PATH`.

Nextflow manages each process as a separate job that is submitted to the cluster by using the `bsub` command.
Since the Nextflow pipeline will submit individual jobs for each process to the cluster and dependencies will be provided bu Singularity images you shoudl make sure that your account has access to the Singularity binary by adding these lines to your `.bashrc` file

```bash
[[ -f  /software/pathogen/farm5 ]] && module load ISG/singularity
```

Nextflow shouldn't run directly on the submission node but on a compute node.
To do so make a shell script with a similar structure to the following code and submit with `bsub < $PWD/my_script.sh`

```bash
#!/bin/bash
#BSUB -o /path/to/a/log/dir/%J.o
#BSUB -e /path/to/a/log/dir//%J.e
#BSUB -M 8000
#BSUB -q long
#BSUB -n 4

export HTTP_PROXY='http://wwwcache.sanger.ac.uk:3128'
export HTTPS_PROXY='http://wwwcache.sanger.ac.uk:3128'
export NXF_ANSI_LOG=false
export NXF_OPTS="-Xms8G -Xmx8G -Dnxf.pool.maxThreads=2000"
export NXF_VER=21.04.0-edge


nextflow run \
/path/to/nf-core/pipeline/main.nf \
-w /path/to/some/dir/work \
-profile sanger \
-c my_specific.config \
-qs 1000 \
-resume

## clean up on exit 0 - delete this if you want to keep the work dir
status=$?
if [[ $status -eq 0 ]]; then
  rm -r /path/to/some/dir/work
fi
```
