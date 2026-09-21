# nf-core/configs: Newcastle University (UK, Comet) HPC Configuration

Configuration for the University of Newcastle upon Tyne HPC cluster (Slurm scheduler).

Check out the docs [here](https://hpc.researchcomputing.ncl.ac.uk/calc/resources/)

## ⚠️ Important usage note

**Do not run Nextflow on the login/head node.**

All nf-core pipelines must be launched **from within a Slurm job** using `sbatch`. Running on the login node can overload shared resources and may result in your job being terminated. See Submit the Job section.

## Setup

### 1. Load Java

Nextflow requires Java. On Newcastle HPC:

    module load Java/17.0.6

To make this persistent, add it to your `~/.bash_profile`:

    # Load Java for Nextflow
    module load Java/17.0.6

### 2. Install Nextflow

Install Nextflow using the official method:

    curl -s https://get.nextflow.io | bash
    chmod +x nextflow

Move it to a directory in your `$PATH`:

    mkdir -p $HOME/bin
    mv nextflow $HOME/bin/

Ensure `$HOME/bin` is in your `PATH` (add to `~/.bash_profile` if needed):

    export PATH="$HOME/bin:$PATH"

### 3. Container system (Apptainer)

nf-core pipelines use containers for reproducibility.

On comet, **Apptainer (formerly Singularity)** is already installed. Check with:

    module avail apptainer

Then load it (example):

    module load Apptainer

## Running pipelines

### 1. Create a Slurm submission script

Create a file, e.g. `run_nfcore.sh`:

    #!/bin/bash
    #SBATCH --job-name=nfcore_run
    #SBATCH --account=YOUR_ACCOUNT
    #SBATCH --time=24:00:00
    #SBATCH --cpus-per-task=4
    #SBATCH --mem=8G

    module load Java/17.0.6
    module load Apptainer

    nextflow run nf-core/_pipeline_ \
      -profile newcastle \
      --account YOUR_ACCOUNT \
      --outdir results \
      -resume

### 2. Submit the job

    sbatch run_nfcore.sh

## Configuration options

### `--account`

You **must** provide a Slurm account when running:

    --account YOUR_PROJECT_CODE

This is passed to Slurm as:

    #SBATCH --account=YOUR_PROJECT_CODE

## Example command to test nextflow is working (run this command, it should work!)

Inside your Slurm script:

    nextflow run  nf-core/fetchngs \
      -profile newcastle,test \
      --account bioinf_project \
      --outdir results \
      -resume

## Example "real" command (will not work, just for demonstration)

    nextflow run  nf-core/rnaseq \
      -profile newcastle \
      --account bioinf_project \
      --input input_samplesheet.csv \
      --aligner hisat2 \
      --fasta mygenome.fasta \
      --gtf myannotation.gtf \
      --outdir results \
      -resume

## Troubleshooting

- Jobs fail immediately → check `--account` is valid  
- Nextflow not found → ensure `$HOME/bin` is in your `PATH`  
- Container errors → ensure Apptainer module is loaded  
- Jobs not starting → check Slurm queue limits (`squeue`, `sacct`)  

## Support

For issues with this configuration, please contact:

- Chris Wyatt (@chriswyatt1)  Email: ecoflow.ucl@gmail.com  
