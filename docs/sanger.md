# nf-core/configs: Wellcome Sanger Institute Configuration

To use, run the pipeline with `-profile sanger`. This will download and launch the [`sanger.config`](https://github.com/nf-core/configs/blob/master/conf/sanger.config) which has been
pre-configured with a setup suitable for the Wellcome Sanger Institute LSF cluster.

## Running the workflow on the Wellcome Sanger Institute cluster

Nextflow is installed centrally by IDS. Type `module load nextflow-` and press <key>TAB</key> to see the list of versions available, e.g.:

```console
$ module load nextflow-[TAB]
nextflow-23.10.0  nextflow-26.04.6
```

Then `module load nextflow-26.04.6` to load Nextflow.

If you need a different version, raise a ticket at <https://sanger.freshservice.com/>.

If asking Nextflow to use Singularity or Apptainer to run the individual jobs,
you should make sure that you enable the right module by adding one of these lines to your `.bashrc` file

```bash
module load ISG/apptainer
module load ISG/singularity
module load ISG/experimental/sp39/singularityce
```

If you need a specific version, press <key>TAB</key> after the module name to see the list of versions available.

Nextflow shouldn't run directly on the submission node but on a compute node, via the `oversubscribed` queue.
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

## GPU access

GPUs on the `cub22` and `farm22` clusters need a cost code. Pass this to your pipeline via the `sanger_gpu_group` parameter.

