# nf-core/configs: MSSM Configuration

This nextflow profiles has been configured to be run with nf-core maintained pipelines for use on the **Minerva HPC** cluster at the **Icahn School of Medicine at Mount Sinai**. All testing has been done within pipelines that follow the DLS2 framework.

Run the pipeline with `-profile mssm`. This will download and launch the [`mssm.config`](../conf/mssm.config) which has been pre-configured with a setup suitable for the Minerva HPC cluster. Using this profile, a container image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline. While this is typically governed by the configuration and execution framework, some manual adjustments will be needed at times. See custom configurations to address this.

## Contact Information

**HPC Support:** hpchelp@hpc.mssm.edu
**Author:** Christopher Tastad - Judy Cho Lab
**Email:** christopher.tastad@mssm.edu

## Required Environment Setup

Before running any nf-core pipeline on Minerva, you **must set the MINERVA_ALLOCATION environment variable** in your submission script:

```bash
export MINERVA_ALLOCATION="acc_YOUR-PROJECT-NAME"
```

## Module Requirements

To run nf-core pipelines on Minerva, you need Nextflow and Singularity. Through experience, it has been found that the local nextflow module can produce some difficulties with execution, and the conda environment installation given by nf-core is preferred.

```bash
ml java
ml anaconda3
ml singularity-ce

# Activate Nextflow from conda environment
source /hpc/packages/minerva-centos7/anaconda3/2018.12/etc/profile.d/conda.sh
conda init bash
conda activate nextflow
```

## Proxy Configuration

Minerva requires proxy settings to download containers from remote sources:

```bash
export http_proxy=http://172.28.7.1:3128
export https_proxy=http://172.28.7.1:3128
export all_proxy=http://172.28.7.1:3128
export no_proxy=localhost,*.chimera.hpc.mssm.edu,172.28.0.0/16
```

## Configuration Details

This profile includes:

- **LSF executor** configuration optimized for Minerva
- **Dynamic queue selection** based on job requirements:
  - `express` queue for short jobs (≤12h, ≤8 CPUs)
  - `premium` queue for standard jobs
  - `long` queue for jobs >144h
  - `gpu` and `gpuexpress` queues for GPU workloads
- **Singularity container** support with proper cache directories
- **Error handling** strategies with automatic retries

## Example Submission Script

```bash
#!/bin/bash
#BSUB -J nfcore-pipeline-job
#BSUB -P acc_YOUR-PROJECT-NAME
#BSUB -W 48:00
#BSUB -q premium
#BSUB -n 2
#BSUB -R rusage[mem=8GB]
#BSUB -R span[hosts=1]
#BSUB -o output_%J.stdout
#BSUB -eo error_%J.stderr
#BSUB -L /bin/bash

PROJ_DIR=/path/to/project/
NFC_PIPE=nf-core/rnaseq
NFC_VER=3.18.0
NFC_PROFILE=mssm,singularity
SAMPLESHEET=$PROJ_DIR/samplesheet.csv
OUTDIR=$PROJ_DIR
GENOME=GRCh38

# Required environment variable
export MINERVA_ALLOCATION='acc_YOUR-PROJECT-NAME'

# Proxy settings
export http_proxy=http://172.28.7.1:3128
export https_proxy=http://172.28.7.1:3128
export all_proxy=http://172.28.7.1:3128
export no_proxy=localhost,*.chimera.hpc.mssm.edu,172.28.0.0/16

# Load modules
ml java
ml anaconda3
ml singularity-ce

# Set up Nextflow environment
source /hpc/packages/minerva-centos7/anaconda3/2018.12/etc/profile.d/conda.sh
conda init bash
conda activate nextflow

cd $PROJ_DIR

# Run pipeline
nextflow run $NFC_PIPE \
    -r $NFC_VER \
    -profile $NFC_PROFILE \
    -w /sc/arion/scratch/${USER}/work \
    -c $PROJ_DIR/custom.config \
    --input $SAMPLESHEET \
    --outdir $OUTDIR \
    --genome $GENOME
```

## Custom Configuration

Users can supplement the base configuration by creating a `custom.config` file. Many processes require minor modifications address specific parameters of a dataset or condition. Given the generalized nature of the main config profile and diversity of process requirements, needing this flexibility is common.

```nextflow
process {
  withName: 'PICARD_MARKDUPLICATES' {
    ext.suffix = 'bam'  // Explicitly set the suffix to avoid using getExtension()
  }

  withName: 'STRINGTIE_STRINGTIE' {
      memory = '24.GB'  // Increase to at least 2-3x the default
  }
}
```

## Troubleshooting

### Common Issues

- **Singularity cache errors**: If you encounter errors related to Singularity caching, check your scratch or work space allocation, and clean up the cache directory if needed. A common issue is related to the singularity `pullTimeout` argument. Large, remote images may exceed this and would benefit from being pulled into the cache manually.
- **Memory issues**: Some processes may require more memory than the default allocation. Use a custom config to increase memory for specific processes.
- **LSF job submission failures**: Ensure your MINERVA_ALLOCATION variable is set correctly and that you have sufficient allocation hours remaining.

## Tested Versions

This configuration has been tested with:

- Nextflow: 24.10.3
- Singularity-ce: 4.1.1
- nf-core pipelines: DSL2 compatible (2022-2025)

:::note
You will need an account and allocation on the Minerva HPC cluster to run nf-core pipelines. For accounts and allocation requests, contact your lab administrator or hpchelp@hpc.mssm.edu.
:::

:::note
All jobs will be submitted to the cluster via LSF scheduler. For technical assistance with the HPC environment, contact hpchelp@hpc.mssm.edu.
:::
