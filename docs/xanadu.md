# nf-core/configs: UConn HPC profile Configuration

nf-core pipelines have been successfully configured for use on the UConn HPC cluster at [Xanadu](https://bioinformatics.uconn.edu/).

To use the xanadu profile, run the pipeline with `-profile xanadu`. This will download and apply [`xanadu.config`](../conf/xanadu.config) which has been pre-configured for the UConn HPC cluster "Xanadu". Using this profile, all Nextflow processes will be run within singularity containers, which can download and convert from docker containers when necesary.

A Nextflow module is available on the Xanadu HPC cluster, to use run `module load nextflow` or `module load nextflow/<version>` prior to running your pipeline. If you are expecting the NextFlow pipeline to consume more space than is available, you can set the work directory to `/scratch/<userid>` which can handle `84.TB` with `export NXF_WORK=/scratch/<userid>`. **CAUTION** make sure to remove items from this directoy, it is not intended for long-term storage.
