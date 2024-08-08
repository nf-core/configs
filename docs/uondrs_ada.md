# nf-core/configs: Ada HPC Configuration

nfcore pipeline rnaseq have been tested on the Ada HPC.

## Before running the pipeline

- You will need an account to use the Ada HPC cluster in order to run the pipeline.
- Make sure that Singularity and Nextflow are installed.
- Downlode pipeline singularity images to a HPC system using [nf-core tools](https://nf-co.re/tools/#downloading-pipelines-for-offline-use)

```
$ conda install nf-core
$ nf-core download
```




## Running the pipeline using the adcra config profile

- Run the pipeline within a [screen](https://linuxize.com/post/how-to-use-linux-screen/) or [tmux](https://linuxize.com/post/getting-started-with-tmux/) session.
- Specify the config profile with `-profile uondrs_ada`.

```
nextflow run /path/to/nf-core/rnaseq -profile uondrs_ada \
--genome GRCh38 \
--igenomes_base /path/to/genome_references/ \
... # the rest of pipeline flags
```