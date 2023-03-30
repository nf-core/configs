# nf-core/configs: Rosalind UGE HPC Configuration

nf-core pipelines have been successfully configured for use on the Rosalind UGE cluster.

To use the Rosalind profile, run the pipeline with `-profile rosalind_uge`. This will download and apply ['rosalind_uge.config'](../conf/rosalind_uge.config) which has been configured for the Rosalind HPC cluster. This profile will allow all Nextflow processes to run within singularity containers, which will be downloaded and converted from docker containers, if needed.

> Note: This profile does not configure resources but does partition jobs based on runtime to make use of `short.q` and `all.q` nodes. If you require resources outside of the limits specified in the pipeline (ex. more memory, CPUS, or walltime), you will need to provide a custom config specifying needed resources.

Rosalind has Nextflow pre-installed on the HPC cluster, and can be accessed by running `module load nextflow` or `module load nextflow/<version>` prior to running your pipeline. Additional singularity variables may need to be configured, such as a scratch directory, temp directory, cache directory, etc. If assistance is needed, please contact the Scientific Computing and Bioinformatics department (SciComp).
