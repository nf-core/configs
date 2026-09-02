# nf-core/configs: SAGA-Sigma2 Configuration (Unofficial)

> [!WARNING]
> This is an **unofficial** project and is not supported by [National e-infrastructure services](https://www.sigma2.no/). Please do not contact the NRIS team for support with this config.

This document describes how to use the profile `saga_sigma2` on the Saga HPC system hosted by Sigma2 AS.

To use this profile, run the pipeline with `-profile saga_sigma2`. This will download and launch the [`saga_sigma2.config`](../conf/saga_sigma2.config) file, which has been pre-configured with settings suitable for the `Saga HPC` cluster. This profile only supports the `normal` job type. If you want to use another partition, modify the config file accordingly.

## Module Requirements

This configuration file assumes you are running the Nextflow pipeline as a `Slurm` job and extracts the necessary environment variables from the `Slurm` environment. To run any Nextflow pipeline with this configuration file, use the following `Slurm` script template:

```bash
#!/bin/bash
#SBATCH --job-name=nextflow
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err
#SBATCH --account=nn****k
#SBATCH --time=01:00:00
#SBATCH --mem=16G
#SBATCH --cpus-per-task=4


# Load required modules
module purge
module load Nextflow/26.04.6

# NF JVM options
export NXF_OPTS="-Xms4g -Xmx16g"

# Pipeline command
nextflow run nf-core/rnaseq \
        -r 3.26.0 \
        -profile apptainer \
        -c saga_sigma2.config \
        -params-file rnaseq_params.json

```
RNA-seq params file example:

```json
{
  "input": "samplesheet.csv",
  "outdir": "./rnaseq_results",

  "fasta": "reference.fa",
  "gtf": "reference.gtf",

  "aligner": "star_salmon",

  "ncpus": 40,
  "mem": "240.GB",
  "time": "6.h",
  "skip_qc": false,
  "email": "ola.nordmann@example.com"
}
```

## Additional information

The SAGA HPC system offers the option to use `$LOCALSCRATCH` instead of `$SCRATCH` for temporary files. For more details, see the [job work directory](https://documentation.sigma2.no/jobs/job_scripts/work_directory.html) documentation.