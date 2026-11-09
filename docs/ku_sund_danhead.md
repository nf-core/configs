# nf-core/configs: ku_sund_danhead configuration

All nf-core pipelines have been successfully configured for use on the DanHead server
at the Novo Nordisk Foundation Center for Stem Cell Medicine (reNEW) at the University of Copenhagen.
The server consists of two computing nodes and one GPU node.

To use the institution profile, run the pipeline with `-profile ku_sund_danhead`.
This will download and launch the [`ku_sund_danhead.config`](../conf/ku_sund_danhead.config)
which has been pre-configured with a setup suitable for the DAN System.

## Environment variables

The main environment variables for nextflow are specified in `/projects/dan1/apps/etc/bashrc`.

## How to run a pipeline with institution profile

To download and test a pipeline for the first time, use the `-profile test` and
specify `--outdir`. It is a good practice to use the pipeline version with
specifying `-r` each time you run a pipeline. `-r` refers to a revision version
and is useful to ensure reproducibility when rerunning the pipeline. You can read
more on nf-core pipeline reproducibility [here](https://nf-co.re/rnaseq/3.10.1/docs/usage#reproducibility).

For example to run `nf-core/rnaseq` on **dancmpn01fl**:

```bash
#!/bin/bash

#SBATCH --job-name=test
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=NONE
#SBATCH -c 1
#SBATCH --mem=2gb
#SBATCH --time=1-00:00:00
#SBATCH --output=test.log
#SBATCH -w dancmpn01fl

module load openjdk/20.0.0 nextflow/23.04.1.5866 singularity/3.8.0

nextflow run nf-core/rnaseq \
  -profile test,ku_sund_danhead,dancmpn01fl \
  --input <name-of-input-csv-file> \
  --outdir <name-of-output-directory>

```

To run it on **dancmpn02fl** change `#SBATCH -w dancmpn02fl` and
`-profile test,ku_sund_danhead,dancmpn02fl`
