# nf-core/configs: Dundee Configuration

The nf-core pipelines [rnaseq](https://nf-co.re/rnaseq) and [sarek](https://nf-co.re/sarek) have been successfully tested on the [University of Dundee compute cluster](https://uod-hpc.readthedocs.io/en/latest/).

To use, run the pipeline with `-profile uod_hpc`. This will download and launch the [`uod_hpc.config`](../conf/uod_hpc.config) which has been pre-configured with a setup suitable for the Dundee cluster.

## Using Nextflow on Dundee Cluster

### Installation

Before running the pipeline you will need to install and configure Nextflow. You can do this by issuing the commands below:

```bash
# Create a Bioconda environment and install Nextflow
setup-miniconda-env /cluster/<group_name>/<your_directory>/nextflow-env
source "/cluster/<group_name>/<your_directory>/nextflow-env/bin/activate"
conda install -c bioconda nextflow

# Specify a cache directory in your /cluster space for Singularity containers
export NXF_SINGULARITY_CACHEDIR="/cluster/<group_name>/<your_directory>/nxf-singularity-cache"
```

For convenience, append the `export NXF_SINGULARITY_CACHEDIR` and conda activation commands to your `.bashrc` file to avoid having to run both on each log-in or include both in every job script:

```bash
echo export NXF_SINGULARITY_CACHEDIR='"/cluster/<group_name>/<your_directory>/nxf-singularity-cache"' >> ~/.bashrc
echo source '"/cluster/<group_name>/<your_directory>/nextflow-env/bin/activate"' >> ~/.bashrc
```

### Usage

Create a job script containing your desired Nextflow command, always including `-profile uod_hpc` to ensure the correct cluster configuration is applied. For example:

```bash
nano myjobscript.sh
```

with contents:

```bash
# NOTE: The following two lines should be omitted if they are already appended to your .bashrc
export NXF_SINGULARITY_CACHEDIR="/cluster/<group_name>/<your_directory>/nxf-singularity-cache"
source "/cluster/<group_name>/<your_directory>/nextflow-env/bin/activate"

nextflow run nf-core/sarek -profile uod_hpc -r 3.3.2 --input ./samplesheet.csv --outdir ./results ...<further parameters as required>...
```

Submit the script using `qsub`:

```bash
qsub -cwd myjobscript.sh
```

Standard and error output for the job will be produced in `.o` and `.e` files, such as `myjobscript.sh.o1400340` and `myjobscript.sh.e1400340`, as it runs.

:::note
You will need an account to use the HPC cluster in order to run the pipeline. If in doubt raise a support request with University of Dundee service desk.
:::

:::note
Nextflow will need to submit the jobs via the job scheduler to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt raise a support request with University of Dundee service desk.
:::
