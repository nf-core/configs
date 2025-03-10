# nf-core/configs: Myriad Configuration

All nf-core pipelines have been successfully configured for use on UCL's myriad cluster [University College London](https://www.rc.ucl.ac.uk/docs/Clusters/Myriad/).

## Using Nextflow on Myriad

Before running an nf-core pipeline you will need to set up the requirements and install Nextflow.

### Requirements

You will need the java 11 or later to install and run Nextflow. Different java versions are available in the cluster. To avoid any compatibily issues, use the latest version of `java/temurin`. You can do this by placing the next line inside your `.bashrc`:

```bash
module load java/temurin-17/17.0.2_8

```

You can check for other java versions using the `module avail java` command, and load the corresponding version by including `module load java/your-version` inside your `.bashrc`.

### Install Nextflow

Download the latest release of nextflow. Warning: the self-update line should update to the latest version, but sometimes not, so please check which is the latest release (https://github.com/nextflow-io/nextflow/releases), you can then manually set this by entering (`NXF_VER=XX.XX.X`).

```bash
## Download Nextflow-all
curl -s https://get.nextflow.io | bash
NXF_VER=XX.XX.X
nextflow -self-update
chmod a+x nextflow
mv nextflow ~/bin/nextflow

```

Then make sure that your bin PATH is executable, by placing the following line in your `.bash_profile`:

```bash
export PATH=$PATH:$HOME/bin

```

## Running an nf-core pipeline

To run the pipeline, make sure to add `-profile ucl_myriad`. This will download and launch the [`ucl_myriad.config`](../conf/ucl_myriad.config) which has been pre-configured with a setup suitable for the myriad cluster, as well as use the correct container engine for myriad.

```bash
nextflow run nf-core/your-pipeline -profile ucl_myriad --outdir your/output/directory

```

You can check your set up is correct by using `-profile test` before running the pipeline with your own data.

```bash
nextflow run nf-core/your-pipeline -profile test,ucl_myriad --outdir your/output/directory

```
