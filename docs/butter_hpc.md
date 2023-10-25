# nf-core/configs: Butter Quantitative Proteomics (butter_hpc) Configuration

All nf-core pipelines have been successfully configured for use on the Butter Quantitative Proteomics (butter_hpc) cluster that is housed at the FLI Greifswald for research groups at institute.

To use, run the pipeline with -profile butter_hpc. This will download and launch the butter_hpc.config which has been pre-configured with a setup suitable for the butter_hpc cluster.
Before running the pipeline you will have to prepare a conda environment with Nextflow and nf-core installed:

## only at the first time application:

conda create -n nextflow_nf-core

conda activate nextflow_nf-core

conda install mamba -c conda-forge

mamba install -c bioconda nextflow

conda config --add channels bioconda

mamba install nf-core (choose newest, say yes to singularity download and make it install it into a folder for singularity images that you should prepare beforehand e.g. ${USER}/singularity_simgs/)

nf-core list

# Straight away usage

## Test

nextflow run nf-core/rnaseq -profile butter_hpc,test --outdir results

## Own data

nextflow run nf-core/rnaseq --input test_sample_sheet.csv --outdir results_rnaseq -profile BUTTER_HPC --fasta <path_to_unzipped_genome_fasta_file> --gtf <path_to_gtf_file_from same_source_as_genome>

# For offline

nf-core download nf-core/rnaseq
cd nf-core-rnaseq-3.10.1/workflow/

## Execute for testing:

nextflow run main.nf -profile butter_hpc,test --outdir results_test

### use -resume to resume a formerly failed run after adjusting parameters
