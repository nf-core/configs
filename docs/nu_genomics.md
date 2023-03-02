# nf-core/configs: NU_Genomics Configuration

All nf-core pipelines have been successfully configured for use on the Quest Genomics Nodes at Northwestern University. Note that, at present, this config has only been tested with nf-core/RNA-seq, but should function similarly for other nf-core pipelines. If you would like to test other pipelines and share on the genomics-rcs Slack, we would be very much obliged.

To use, run the pipeline with `-profile nu_genomics`. This will download and launch the [`nu_genomics.config`](../conf/nu_genomics.config) which has been pre-configured with a setup suitable for the Quest Genomics Nodes. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Before running the pipeline

There are several important steps to take before this pipeline will run successfully on Quest. First, you must have an active Quest allocation. If you do not, please apply [here](https://www.it.northwestern.edu/secure/forms/research/allocation-request-forms.html). You will also need access to the Genomics Nodes. If you do not already have access, please apply [here](https://app.smartsheet.com/b/form/f6e96bd561114be8a33dc778bc00b919). As of 2023, we now have a dedicated nextflow module, which we recommend using. However if you need an edge version of nextflow, you will need to perform a local installation of Nextflow and add it to your path. Please follow the basic installation instructions shown [here](https://www.nextflow.io/), or install in your home directory as shown below. If you already have a bin directory in your path, you will not need to create the directory or append to your path.

```bash
cd ~
mkdir bin
cd bin
curl -s https://get.nextflow.io | bash
export PATH=~/bin:$PATH
```

Note that you may need to install an "edge" version of Nextflow, depending on which pipeline you use. Please read the documentation carefully to see if this is the case, or you may see an error when running the pipeline. If this is the case, you need to explicitly set the version when installing, e.g.:

```bash
curl -s https://github.com/nextflow-io/nextflow/releases/download/v20.11.0-edge/nextflow-20.11.0-edge-all | bash
```

If you are using the nextflow module, you can simply load the module as follows:

```bash
module purge
module load nextflow/22.10.5 #or newest version
```

If you are using your own installation, note that while the config does explicitly load the necessary modules, you will often need to load them manually anyway. Please do so before each run as follows, or you may run into errors:

```bash
module purge
module load singularity/latest
module load graphviz/2.40.1
module load java/jdk11.0.10
```

## Use of iGenomes

A local copy of the iGenomes resource with all commonly used genomes has been made available for all of Quest so you should be able to run the pipeline against any reference available in the `igenomes.config` specific to the nf-core pipeline. These files can be found at `/projects/genomicsshare/AWS_iGenomes`. You can do this by simply using the `--genome <GENOME_ID>` parameter. While you can technically "stream" genomes from iGenomes directly using the pipeline, this is a substantial use of bandwidth and resources on both ends, and potentially poses reproducibility issues later on. Please use the local copies unless absolutely necessary, and save your custom genomes to your personal allocation where necessary.
