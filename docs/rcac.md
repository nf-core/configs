# nf-core/configs: Purdue RCAC Configuration

nf-core pipelines have been configured for use on the ACCESS Anvil and community clusters operated by Rosen Center for Advanced Computing (RCAC) at Purdue University.

To use RCAC's profile, run the pipeline with `-profile rcac`. 

Example: `nextflow run -profile rcac`

Users can also put the `nextflow ...` command into a batch script and submit the job to computing nodes by `sbatch` or launch interative jobs to computing nodes by `sinteractive`. Using this way, both nextflow manager processes and tasks will run on the allocated compute nodes using the `local` executor. It is recommended to use `-profile singularity`

Example: `nextflow run -profile singularity`



## Environment module

Before running the pipeline, you will need to load the Nextflow module by:


```bash
module purge ## Optional but recommended
module load nextflow
```

## Local copy of iGenomes 

A local copy of the iGenomes resource is available on Purdue RCAC community clusters as well as ACCESS Anvil. The locations of local iGenomes resource are different between RCAC community clusters and ACCESS Anvil. To use local iGenomes resource, you have to specify `--igenomes_base` path in your execution command. 

For ACCESS Anvil, please use the parameter like this `--igenomes_base /anvil/datasets/igenomes`.

For Purdue community clusters, please use `--igenomes_base /depot/itap/datasets/igenomes`.

