# nf-core/configs: Institute of Cancer Research (Davros HPC) Configuration

Deployment and testing of nf-core pipelines at the Davros cluster is on-going.

To run an nf-core pipeline on Davros, run the pipeline with `-profile icr_davros`. This will download and launch the [`icr_davros.config`](../conf/icr_davros.config) which has been pre-configured with a setup suitable for the Davros HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

Before running the pipeline you will need to load Nextflow using the environment module system. You can do this by issuing the commands below:

```bash
## Load Nextflow environment modules
module load Nextflow/19.10.0
```

Singularity is installed on the compute nodes of Davros, but not the login nodes. There is no module for Singularity.

A subset of the [AWS-iGenomes](https://github.com/ewels/AWS-iGenomes) resource has been made available locally on Davros so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline you want to execute. You can do this by simply using the `--genome <GENOME_ID>` parameter. Some of the more exotic genomes may not have been downloaded onto Davros so have a look in the `igenomes_base` path specified in [`icr_davros.config`](../conf/icr_davros.config), and if your genome of interest isn't present please contact [Scientific Computing](mailto:schelpdesk@icr.ac.uk).

Alternatively, if you are running the pipeline regularly for genomes that arent available in the iGenomes resource, we recommend creating a config file with paths to your reference genome indices (see [`reference genomes documentation`](https://nf-co.re/usage/reference_genomes) for instructions).

All of the intermediate files required to run the pipeline will be stored in the `work/` directory. It is recommended to delete this directory after the pipeline has finished successfully because it can get quite large. All of the main output files will be saved in the `results/` directory.

> NB: Nextflow will need to submit the jobs via LSF to the HPC cluster. This can be done from an interactive or normal job. If in doubt contact Scientific Computing.
