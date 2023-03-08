nf-core/configs: Butter Quantitative Proteomics (BUTTER_HPC) Configuration
All nf-core pipelines have been successfully configured for use on the Butter Quantitative Proteomics (BUTTER_HPC) cluster that is housed at the FLI Greifswald for research groups at institute.

To use, run the pipeline with -profile BUTTER_HPC. This will download and launch the BUTTER_HPC.config which has been pre-configured with a setup suitable for the BUTTER_HPC cluster. 
Before running the pipeline you will have to prepare a conda environment with Nextflow and nf-core installed:

## only at the first time application:
conda create -n nextflow_nf-core 

conda activate nextflow_nf-core 

conda install mamba -c conda-forge

mamba install -c bioconda nextflow

conda config --add channels bioconda

mamba install  nf-core (choose newest, say yes to singularity download and make it install it into a folder for singularity images that you should prepare beforehand e.g.  ~/singularity_simgs/) 

nf-core list
## Straight away usage
# Test
nextflow run nf-core/rnaseq -c /home/gast.rie19/data/make_nf-cor_config_profile/configs/conf/BUTTER_HPC.config -profile singularity,test --outdir results

# Own data
 nextflow run nf-core/rnaseq --input test_sample_sheet.csv --outdir /home/gast.rie19/data/nf-core_rnaseq_test/results_owndata -profile singularity -c ~/data/make_nf-cor_config_profile/configs/conf/BUTTER_HPC.config --fasta /home/gast.rie19/data/common_assemblies_annotations/homo-sapiens/ensembl/GRCh38/genomes/Homo_sapiens.GRCh38.dna.primary_assembly.fa --gtf /home/gast.rie19/data/common_assemblies_annotations/homo-sapiens/ensembl/GRCh38/annotation/Homo_sapiens.GRCh38.98.gtf

## For offline 
nf-core download nf-core/rnaseq
cd nf-core-rnaseq-3.10.1/workflow/
## Execute for testing:
nextflow run main.nf -c ~/data/make_nf-cor_config_profile/configs/conf/BUTTER_HPC.config -profile conda,test --outdir results-conda -resume
