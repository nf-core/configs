# nf-core/configs: University of Tuebingen APG group Configuration

All nf-core pipelines have been successfully configured for use on the APG group's clusters at the [University of Tuebingen](https://uni-tuebingen.de/fakultaeten/mathematisch-naturwissenschaftliche-fakultaet/fachbereiche/geowissenschaften/arbeitsgruppen/urgeschichte-naturwissenschaftliche-archaeologie/ina/archaeo-and-palaeogenetik/).

To use, run the pipeline with `-profile tubingen_apg`. This will download and launch the [`tubingen_apg.config`](../conf/tubingen_apg.config) which has been pre-configured with a setup suitable for the APG cluster. The number of parallel jobs that run is currently limited to 8.

This configuration will automatically choose the correct SLURM queue (short, medium, long) depending on the time and memory required by each process.

When using this profile, a docker image containing all of the required software will be downloaded and converted to a singularity container before execution of the pipeline. The image will be stored in the cache directory:

```
/opt/container_tmp/apptainer/nextflow
```

> NB: Nextflow will need to submit the jobs via SLURM to the clusters and as such the commands above will have to be executed on one of the head nodes. If in doubt contact IT.

## Additional Profiles

We currently also offer profiles for deactivating the cleanup of intermediate files.

### debug

This simple profile just turns off automatic clean up of intermediate files. This can be useful for debugging. Specify e.g. with `-profile tubingen_apg,debug`.
