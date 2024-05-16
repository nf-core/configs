# nf-core/configs: Pôle Scientifique de Modélisation Numérique (PSMN)

All nf-core pipelines have been successfully configured for use on the tars cluster at the Institut Pasteur.

To use, run the pipeline with `-profile psmn`. This will download and launch the [`psmn.config`](../conf/psmn.config) which has been pre-configured with a setup suitable for the PSMN cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

You can have more information on the cluster parition here:
[www.ens-lyon.fr/PSMN/Documentation/clusters_usage/computing_resources.html](https://www.ens-lyon.fr/PSMN/Documentation/clusters_usage/computing_resources.html)

## Running the workflow on the PSMN cluster

### Install [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html#) and [Charliecloud](https://hpc.github.io/charliecloud/index.html)

The Nextflow binary is available in the folder `/Xnfs/abc/nextflow_bin/`.
All the Charliecloud binaries are available in the folder `/Xnfs/abc/charliecloud_bin/`.

You can update your `$PATH` variable with the following command to have access to Nextflow and Charliecloud:

```sh
PATH=/Xnfs/abc/charliecloud_bin/:/Xnfs/abc/nextflow_bin/:$PATH
```

or add this line to your `~/.zshrc` or `~/.bashrc` configuration file.

### Install nf-core

nf-core is available on the PSMN as a Charliecloud container you can run the classical nf-core command by prefixing them with:

```sh
ch-run -b /scratch:/scratch /Xnfs/abc/charliecloud/img/nfcore%tools+2.6 -- nf-core
```

For exemple to download the `nf-core/rnaseq` pipeline you can use the command:

```sh
cd /Xnfs/abc/nf_scratch/<user_name>/
ch-run -b /scratch:/scratch -b /Xnfs:"" \
  /Xnfs/abc/charliecloud/img/nfcore%tools+2.6 -- nf-core \
  download rnaseq -r 3.9 --outdir nf-core-rnaseq
```

### Download and launch a nf-core pipeline

You can use the `nf-core download` command to download an nf-core pipeline and the configuration files for the PSMN:

```sh
cd /Xnfs/abc/nf_scratch/<user_name>/
ch-run -b /scratch:/scratch \
  /Xnfs/abc/charliecloud/img/nfcore%tools+2.6 -- nf-core \
  download rnaseq -r 3.9 --outdir <your scratch directory>/nf-core-rnaseq -x none -c none
```

### Download all the necessary image

By default the `psmn` profile will lookup charliecloud img in the `/Xnfs/abc/charliecloud/` folder.
To download all the images that are not already present in this folder you can use the following script

```sh
cd nf-core-rnaseq
pull_ch_images_locally.sh
```

### Launch the pipeline

Then you can launch this pipeline with the PSMN profile

```sh
tmux
cd nf-core-rnaseq
nextflow run workflow -profile test,psmn --outdir results/
```
