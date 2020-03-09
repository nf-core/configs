# nf-core/configs: EBC Configuration

All nf-core pipelines have been successfully configured for use on the [Estonian Biocentre (EBC)](https://genomics.ut.ee/en/about-us/estonian-biocentre) cluster at the [High Performance Computing Center](https://hpc.ut.ee/en) of the the University of Tartu.
To use, run the pipeline with `-profile ebc`. This will download and launch the [`ebc.config`](../conf/ebc.config) which has been pre-configured with a setup suitable for the EBC cluster. Using this profile, currently, a conda environment containing all of the required software will be downloaded and stored in a central location.

> :warning: You must install your own [conda binary](conda.io) to run nf-core pipelines in a conda environment. Running with singularity will be added soon.

The profile will put a maximum job limit of 12 GB, 20 CPUs and a maximum wall time of 120 hours.

NB: You will need an account to use the HPC cluster on EBC cluster in order to run the pipeline. If in doubt contact IT.
NB: Nextflow will need to submit the jobs via the SLURM scheduler to the HPC cluster and as such the commands above will have to be executed on one of the head nodes. If in doubt contact IT.
