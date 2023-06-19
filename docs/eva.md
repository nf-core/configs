# nf-core/configs: EVA Configuration

All nf-core pipelines have been successfully configured for use on the Department of Genetics and Archaeogenetic's clusters at the [Max Planck Institute for Evolutionary Anthropology (MPI-EVA)](http://eva.mpg.de).

To use, run the pipeline with `-profile eva`. You can further with optimise submissions by specifying which cluster queue you are using e,g, `-profile eva,archgen`. This will download and launch the [`eva.config`](../conf/eva.config) which has been pre-configured with a setup suitable for the `all.q` queue. The number of parallel jobs that run is currently limited to 8.

Using this profile, a docker image containing all of the required software will be downloaded, and converted to a `singularity` image before execution of the pipeline.

Institute-specific pipeline profiles exists for:

- eager
- mag
- sarek
- taxprofiler

## Additional Profiles

We currently also offer profiles for the different department's specific nodes.

### archgen

If you specify `-profile eva,archgen` you will be able to use the nodes available on the `archgen.q` queue.

Note the following characteristics of this profile:

- By default, job resources are assigned a maximum number of CPUs of 32, 256 GB maximum memory and 365 day maximum wall time.
- Using this profile will currently store singularity images in a cache under `/mnt/archgen/users/singularity_scratch/cache/`. All archgen users currently have read/write access to this directory, however this will likely change to a read-only directory in the future that will be managed by the IT team.
- Intermediate files will be _automatically_ cleaned up (see `debug` below if you don't want this to happen) on successful run completion.
- Jobs submitted with >700.GB will automatically be submitted to the dynamic `bigmem.q`.

> NB: You will need an account and VPN access to use the cluster at MPI-EVA in order to run the pipeline. If in doubt contact the IT team.
> NB: Nextflow will need to submit the jobs via SGE to the clusters and as such the commands above will have to be executed on one of the head nodes. If in doubt contact IT.

### debug

This simple profile just turns off automatic clean up of intermediate files. This can be useful for debugging. Specify e.g. with `-profile eva,archgen`.
