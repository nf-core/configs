# nf-core/configs: SeaWulf Configuration

The nf-core pipelines [rnaseq](https://nf-co.re/rnaseq) and
[sarek](https://nf-co.re/sarek) have been successfully tested on the SeaWulf
cluster at [Stony Brook University's Institute for Advanced Computational Science](https://www.stonybrook.edu/commcms/iacs/index.php).

The SeaWulf config offers access to our 40-core and 96-core nodes.
To run the pipeline, use the `-profile seawulf` flag.

The SeaWulf config will use singularity to download and run all the containers necessary to execute the pipeline. No module needs to be loaded to access singularity, however it is recommended that you load the following modules before running your pipeline

```bash
## get the latest version of Nextflow and a reasonably new Java version
module load openjdk
module load nextflow/latest
```

# Access to SeaWulf

The SeaWulf cluster is available to researchers at Stony Brook University.
Please see our [FAQ Page](https://it.stonybrook.edu/services/high-performance-computing)
for instructions on getting access.
