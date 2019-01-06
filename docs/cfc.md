# nf-core/configs: CFC Configuration

All nf-core pipelines have been successfully configured for use on the CFC cluster at the insert institution here.

To use, run the pipeline with `-profile cfc`. This will download and launch the [`cfc.config`](../conf/cfc.config) which has been pre-configured with a setup suitable for the CFC cluster. Using this profile, Nextflow will download a singularity image with all of the required software before execution of the pipeline.

Before running the pipeline you will need to load Nextflow and Singularity using the environment module system on CFC cluster. You can do this by issuing the commands below:

```bash
## Load Nextflow and Singularity environment modules
module purge
module load devel/java_jdk/1.8.0u121
module load qbic/singularity_slurm/3.0.1

## Example command for nf-core/atacseq
nextflow run nf-core/atacseq -profile PROFILE --genome GRCh37 --design /path/to/design.csv --email test.user@crick.ac.uk
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.

>NB: You will need an account to use the HPC cluster CFC in order to run the pipeline. If in doubt contact IT.

>NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
