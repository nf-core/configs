# nf-core/configs: biowulf Configuration

nf-core pipelines such as sarek have been successfully tested on the [Biowulf](https://hpc.nih.gov) cluster at the NIH.

To use, run the pipeline with `-profile biowulf`, this will pull the [`biowulf.config`](../conf/biowulf.config) from github which has been pre-configured with a setup suitable for running slurm executor on the Biowulf cluster. By default, Nextflow will download Singularity containers to a cache directory setted by the config file.

```bash
nextflow run <pipeline> -profile biowulf <Add your other parameters>

```

Before running the pipeline you will need to load Nextflow using the environment module system on Biowulf compute node through sinteractive session or a sbatch job. You can do this by issuing the commands below:

```bash
## Load Nextflow which will also load Singularity modules
module purge
module load nextflow

```

The Illumina iGenomes resource is available on Biowulf. However it is different from the s3-hosted nf-core iGenomes. There are some structural differences of note. A local copy of the AWS-iGenomes resource is under consideration. In particular, if using BWA, the igenomes.conf should be modified to specify the BWA version folder, otherwise the BWA module will fail to find an appropriate index. To date, this is the only issue, however functionality has not been extensively tested with iGenomes on Biowulf. Nonetheless, you should, in theory, be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline.

You can do this by simply using the `--genome <GENOME_ID>` parameter, if `--genome` is supported by a given pipeline.

> NB: You will need an account to use the HPC cluster on Biowulf in order to run the pipeline. If in doubt contact staff@hpc.nih.gov.
> NB: Nextflow will need to submit the jobs via the job scheduler to the HPC cluster. The master process submitting jobs should be run either as a batch job or on an interactive node - not on the biowulf login node. If in doubt contact Biowulf staff.
