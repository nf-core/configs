# nf-core/configs: CRA HPC Configuration

nfcore pipeline sarek and rnaseq have been tested on the CRA HPC.

## Before running the pipeline

- You will need an account to use the CRA HPC cluster in order to run the pipeline.
- Make sure that Singularity and Nextflow are installed.
- Downlode pipeline singularity images to a HPC system using [nf-core tools](https://nf-co.re/tools/#downloading-pipelines-for-offline-use)

```
$ conda install nf-core
$ nf-core download
```

- You will need to specify a Singularity cache directory in your ~./bashrc. This will store your container images in this cache directory without repeatedly downloading them every time you run a pipeline. Since space on home directory is limited, using lustre file system is recommended.

```
export NXF_SINGULARITY_CACHEDIR = "/lustre/fs0/storage/yourCRAAccount/cache_dir"
```

- Download iGenome reference to be used as a local copy.

```
$ aws s3 --no-sign-request --region eu-west-1 sync s3://ngi-igenomes/igenomes/Homo_sapiens/GATK/GRCh38/ /lustre/fs0/storage/yourCRAAccount/references/Homo_sapiens/GATK/GRCh38/
```

## Running the pipeline using the adcra config profile

- Run the pipeline within a [screen](https://linuxize.com/post/how-to-use-linux-screen/) or [tmux](https://linuxize.com/post/getting-started-with-tmux/) session.
- Specify the config profile with `-profile adcra`.
- Using lustre file systems to store results (`--outdir`) and intermediate files (`-work-dir`) is recommended.

```
nextflow run /path/to/nf-core/<pipeline-name> -profile adcra \
--genome GRCh38 \
--igenomes_base /path/to/genome_references/ \
... # the rest of pipeline flags
```
