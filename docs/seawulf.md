# nf-core/configs: SeaWulf Configuration

The nf-core pipelines [rnaseq](https://nf-co.re/rnaseq) and 
[sarek](https://nf-co.re/sarek) have been successfully tested on the SeaWulf 
cluster at [Stony Brook University's Institute for Advanced Computational Science](https://www.stonybrook.edu/commcms/iacs/index.php). 



The SeaWulf config comes with two different profiles that will provide access to our 40-core and 96-core nodes, respectively. 
To run the pipeline with the 40-core nodes, use the `-profile seawulf,40-core` flag. Alternatively, to run your pipeline on the 96 core nodes, 
use the `-profile seawulf,96-core` flag.


The SeaWulf config  will use singularity to download and run all the containers necessary to execute the pipeline.  No module needs to be loaded to access singularity, however it is recommended that you load the following modules before running your pipeline

```bash
## get the latest version of Nextflow and a reasonably new Java version 
module load openjdk
module load nextflow/latest
```
