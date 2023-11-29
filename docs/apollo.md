# nf-core/configs: City of Hope Apollo Configuration

All nf-core pipelines have been successfully configured for use on the [HPRCC](http://hprcc.coh.org) Apollo cluster at City of Hope.

To use, run the pipeline with `-profile apollo`. This will download and launch the [`apollo.config`](../conf/apollo.config) which has been pre-configured with a setup suitable for the Apollo cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Getting set up

First off, you'll need an [HPRCC account](http://hprcc.coh.org/clusters/account/).

Before running a pipeline, Nextflow and Singularity should be loaded using the environment module system on Apollo. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load nextflow
module load singularity
```

Alternately, add this line to your `.bashrc` file so that the modules are automatically loaded each time you log in.

```bash
echo "module load nextflow singularity" >> ~/.bashrc
```

> Nextflow needs to submit jobs via the job scheduler to the HPC cluster and as such the commands should be executed on one of the login nodes. If in doubt contact the HPRCC Helpdesk.

## Reference genomes

A local copy of the iGenomes resource has been made available on Apollo so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline. You can do this by simply using the `--genome <GENOME_ID>` parameter.

Additional genomes are available at `/ref_genome`

## Cleanup after a run

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. This config contains a `cleanup` command that'll remove the `work/` directory automatically if the pipeline completes successfully. To prevent this, run the pipeline with the `debug` profile. For example, using the RNA-seq pipeline:

```bash
nextflow run nf-core/rnaseq -profile apollo,debug --outdir results/
```
