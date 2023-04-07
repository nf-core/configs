# University of Washington Hyak Profile for the Department of Pediatrics

1) You will need Hyak access, which can be requested from UW Peds IT (pedcomp@uw.edu)
2) Download and install Miniconda or preferably Mambaforge:
Miniconda
    `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
    `bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda3`
Mambaforge
    `wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh`
    `bash Mambaforge-Linux-x86_64.sh -b -p $HOME/mambaforge`
3) Create a nextflow environment
    `conda create -n nextflow -c conda-forge -c bioconda nextflow nf-core -y`
4) Activate the nextflow environment
    `conda activate nextflow`
5) Run any nf-core pipeline using the following profile flag:
    `-profile uw_hyak_pedslabs`
- By default, this profile will submit all jobs to the checkpoint queue on the first try, and then re-submit to the compute-hugemem queue if necessary
