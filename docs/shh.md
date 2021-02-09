# nf-core/configs: SHH Configuration

All nf-core pipelines have been successfully configured for use on the Department of Archaeogenetic's SDAG/CDAG clusters at the [Max Planck Institute for the Science of Human History (MPI-SHH)](http://shh.mpg.de).

To use, run the pipeline with `-profile shh`. You can further with optimise submissions by specifying which cluster you are using with `-profile shh,sdag` or `-profile shh,cdag`. This will download and launch the [`shh.config`](../conf/shh.config) which has been pre-configured with a setup suitable for the SDAG and CDAG clusters respectively. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. The image will currently be centrally stored here:

```bash
/projects1/singularity_scratch/cache/
```

however this will likely change to a read-only directory in the future that will be managed by the IT team.

This configuration will automatically choose the correct SLURM queue (`short`,`medium`,`long`) depending on the time and memory required by each process. `-profile shh,sdag` additionally allows for submission of jobs to the `supercruncher` queue when a job's requested memory exceeds 756GB.

>NB: You will need an account and VPN access to use the cluster at MPI-SHH in order to run the pipeline. If in doubt contact the IT team.
>NB: Nextflow will need to submit the jobs via SLURM to the clusters and as such the commands above will have to be executed on one of the head nodes. If in doubt contact IT.
