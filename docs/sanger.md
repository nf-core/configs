# nf-core/configs: Wellcome Sanger Institute Configuration

To use, run the pipeline with `-profile sanger`. This will download and launch the [`sanger.config`](../conf/sanger.config) which has been
pre-configured with a setup suitable for the Wellcome Sanger Institute LSF cluster.

## Running the workflow on the Wellcome Sanger Institute cluster

The latest version of Nextflow is not installed by default on the cluster. You will need to install it into a directory you have write access to

- Install Nextflow : [here](https://www.nextflow.io/docs/latest/getstarted.html#)

A recommended place to move the `nextflow` executable to is `~/bin` so that it's in the `PATH`.

Nextflow manages each process as a separate job that is submitted to the cluster by using the `bsub` command.

If asking Nextflow to use Singularity to run the individual jobs,
you should make sure that your account has access to the Singularity binary by adding these lines to your `.bashrc` file

```bash
[[ -f /software/modules/ISG/singularity ]] && module load ISG/singularity
```

Nextflow shouldn't run directly on the submission node but on a compute node.
To do so make a shell script with a similar structure to the following code and submit with `bsub < $PWD/my_script.sh`

```bash
#!/bin/bash
#BSUB -o /path/to/a/log/dir/%J.o
#BSUB -e /path/to/a/log/dir/%J.e
#BSUB -M 8000
#BSUB -q oversubscribed
#BSUB -n 2

export HTTP_PROXY='http://wwwcache.sanger.ac.uk:3128'
export HTTPS_PROXY='http://wwwcache.sanger.ac.uk:3128'
export NXF_ANSI_LOG=false
export NXF_OPTS="-Xms8G -Xmx8G -Dnxf.pool.maxThreads=2000"
export NXF_VER=22.04.0-5697


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
