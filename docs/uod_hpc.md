# nf-core/configs: Dundee Configuration

The nf-core pipelines [rnaseq](https://nf-co.re/rnaseq) and [sarek](https://nf-co.re/sarek) have been successfully tested on the [University of Dundee compute cluster](https://uod-hpc.readthedocs.io/en/latest/).

To use, run the pipeline with `-profile uod_hpc`. This will download and launch the [`uod_hpc.config`](../conf/uod_hpc.config) which has been pre-configured with a setup suitable for the Dundee cluster.

## Using Nextflow on Dundee Cluster

Before running the pipeline you will need to install and configure Nextflow. You can do this by issuing the commands below:

```bash
# Create a Bioconda environment and install Nextflow
setup-miniconda-env /cluster/<group_name>/<your_directory>/nextflow-env
source "/cluster/<group_name>/<your_directory>/nextflow-env/bin/activate"
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install -c bioconda nextflow

# Specify a cache directory in your /cluster space for conda environments
export NXF_CONDA_CACHEDIR="/cluster/<group_name>/<your_directory>/nxf-conda-cachedir"
```

For convenience, append the `export NXF_CONDA_CACHEDIR` and conda activation commands to your `.bashrc` file to avoid having to run on each log-in:

```bash
echo export NXF_CONDA_CACHEDIR='"/cluster/<group_name>/<your_directory>/nxf-conda-cachedir"' >> ~/.bashrc
echo source '"/cluster/<group_name>/<your_directory>/nextflow-env/bin/activate"' >> ~/.bashrc
```

:::note
You will need an account to use the HPC cluster in order to run the pipeline. If in doubt raise a support request with University of Dundee service desk.
:::

:::note
Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt raise a support request with University of Dundee service desk.
:::
