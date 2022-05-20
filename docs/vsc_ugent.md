# nf-core/configs: University of Ghent High Performance Computing Infrastructure (VSC)

> **NB:** You will need an [account](https://www.ugent.be/hpc/en/access/faq/access) to use the HPC cluster to run the pipeline.

First you should go to the cluster you want to run the pipeline on. You can check what clusters have the most free space on this [link](https://shieldon.ugent.be:8083/pbsmon-web-users/). Use the following commands to easily switch between clusters:

```shell
module purge
module swap cluster/<CLUSTER>
```

Before running the pipeline you will need to create a PBS script to submit as a job.

```bash
#!/bin/bash

module load Nextflow

nextflow run <pipeline> -profile vsc_ugent,<CLUSTER> <Add your other parameters>
```

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large, and all of the main output files will be saved in the `results/` directory anyway.
The config contains a `cleanup` command that removes the `work/` directory automatically once the pipeline has completed successfully. If the run does not complete successfully then the `work/` dir should be removed manually to save storage space. The default work directory is set to `$VSC_SCRATCH_VO_USER/work` per this configuration

You can also add several TORQUE options to the PBS script. More about this on this [link](http://hpcugent.github.io/vsc_user_docs/pdf/intro-HPC-linux-gent.pdf#appendix.B).

To submit your job to the cluster by using the following command:

```shell
qsub <script name>.pbs
```

> **NB:** The profile only works for the clusters `skitty`, `swalot`, `victini`, `kirlia` and `doduo`.

> **NB:** The default directory where the `work/` and `singularity/` (cache directory for images) is located in `$VSC_SCRATCH_VO_USER`.
