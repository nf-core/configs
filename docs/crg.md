# nf-core/configs: CRG Configuration

All nf-core pipelines have been successfully configured for use on the CRG HPC cluster at the [Centre for Genomic Regulation](https://www.crg.eu/).

## Using the CRG config profile

In order to avoid overloading the CRG login nodes, a specific VM to run Nextflow pipelines is provided. This VM can submit jobs to the HPC scheduler, thus using the computing nodes in the cluster. You just need to connect to it via SSH (replacing <username> with your username):

```bash
## Log in to the node
ssh <username>@nextflow.linux.crg.es
```

Before running the pipeline you will need to download Nextflow and load Singularity using the environment module system on CRG cluster. Please check the main README of the pipeline to make sure that the version of Nextflow is compatible with that required to run the pipeline. At the time of writing, the VM has an old version of Java installed. Thus, you need to make sure you load the Java 11 module for running Nextflow. You can do all this by issuing the commands below:

```bash
## Download Nextflow
wget -qO- https://get.nextflow.io | bash
```

For your convenience, you can move the `nextflow` launcher to a directory included in your `PATH` environment variable.

```bash
## Load Singularity environment modules
module use /software/as/el7.2/EasyBuild/CRG/modules/all
module load Singularity/3.7.0
module load Java/11.0.2
```

Adding the previous lines to your `.bash_profile` or `.bashrc` file is an option to avoid having to load the modules each time you start a session.

To use, run the pipeline with `-profile crg`. This will download and launch the [`crg.config`](../conf/crg.config) which has been pre-configured with a setup suitable for the CRG HPC cluster, with the queues definitions. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

```bash
# Launch a nf-core pipeline with the crg profile
$ nextflow run nf-core/<PIPELINE> -profile crg [...]
```

Remember to use `-bg` to launch `Nextflow` in the background, so that the pipeline doesn't exit if you leave your terminal session.
Alternatively, you can also launch `Nextflow` in a `screen` or a `tmux` session.

> NB: You will need an account to use the HPC cluster on CRG in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via SGE to the HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.

## Redirecting the `work` directory

It is highly recommended to place the `work` directory within the `scratch` volume.

> If your group has no space on the scratch volume, please open a ticket to SIT for receiving support.

You might create a work folder in the CRG scratch volume and run the nextflow pipeline specifying that folder as the work directory using the parameter `-w`

```bash
# Launch a nf-core pipeline with the crg profile redirecting the work dir to the scratch volume
$ nextflow run nf-core/<PIPELINE> -profile crg -w /nfs/scratch01/<YOUR_GROUP_NAME>/<YOUR_WORK_DIR>
```

Alternatively, you can set the `NXF_WORK` environmental variable to set the Nextflow work directory to the scratch volume permanently.

## Reducing the amout of RAM

In case of big pipelines Nextflow can use a non trivial amount of RAM. You can reduce it by setting a special nextflow environmental variable that define the Java VM heap memory allocation limits:

```bash
# Reduce the amount of RAM before launching a pipeline
$ export NXF_OPTS="-Xms250m -Xmx2000m"
```
