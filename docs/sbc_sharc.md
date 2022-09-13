# nf-core/configs: Sheffield Bioinformatics Core Facility ShARC Configuration

The following nf-core pipelines have been successfully configured for use on the the [University of Sheffield ShARC cluster](https://docs.hpc.shef.ac.uk/en/latest/index.html):

- [nf-co.re/atacseq](https://nf-co.re/atacseq)
- [nf-co.re/chipseq](https://nf-co.re/chipseq)
- [nf-co.re/rnaseq](https://nf-co.re/rnaseq)
- [nf-co.re/sarek](https://nf-co.re/sarek)

When using [`sbc_sharc.config`](../conf/sbc_sharc.config) with the pipelines listed above, the appropriate configuration file from the list below will be loaded automatically:

- [atacseq sbc_sharc.config](../conf/pipeline/atacseq/sbc_sharc.config)
- [chipseq sbc_sharc.config](../conf/pipeline/chipseq/sbc_sharc.config)
- [rnaseq sbc_sharc.config](../conf/pipeline/rnaseq/sbc_sharc.config)
- [sarek sbc_sharc.config](../conf/pipeline/sarek/sbc_sharc.config)

The [`sbc_sharc.config`](../conf/sbc_sharc.config) configuration file might work with other nf-core pipelines as it stands but we cannot guarantee they will run without issue. We will be continuing to create, test and optimise configurations for new pipelines in the future.


## Using the SBC_ShARC Institutional Configuration Profile

To use [`sbc_sharc.config`](../conf/sbc_sharc.config), run nextflow with an nf-core pipeline using `-profile sbc_sharc` (note the single hyphen). This will download and launch [`sbc_sharc.config`](../conf/sbc_sharc.config) which has been pre-configured with a setup suitable for the ShARC cluster and will automatically load the appropriate pipeline-specific configuration file.

For a full guide on how to setup and run Nextflow using nf-core pipelines on ShARC, see the **Running Nextflow with nf-core Pipelines on ShARC** section below.


## A Note on Singularity Containers

The [`sbc_sharc.config`](../conf/sbc_sharc.config) configuration file supports running nf-core pipelines with Singularity containers; Singularity images will be downloaded automatically before execution of the pipeline.

Please read the **Configure Singularity for use with Nextflow and nf-core** sub-section below.


## Running Nextflow with nf-core Pipelines on ShARC

Nextflow is not currently available on ShARC as an environmental software module. The most simple solution to this issue is to install Nextflow and nf-core using a personal install of miniconda. This guide will describe the main steps, which are to:

1. Install miniconda as a personal software module
2. Load and configure conda
3. Install Nextflow and nf-core within a conda environment
4. Configure Singularity for use with Nextflow and nf-core
5. Setup your project directory and configure your run
6. Submit your run to the SGE scheduler


### 1. Install Miniconda as a Personal Software Module

Connect to ShARC via SSH and login to a worker node via an interactive session.

```shell
# login
ssh -X username@sharc.shef.ac.uk

# request a command line only interactive session - some extra resources prevent issues building conda env later
qrsh -l rmem=4G -pe smp 2
```

Navigate your folder within the data area of the file store.

```shell
cd /data/$USER
```

Download and run the miniconda installer by running the following series of commands:

```shell
# download the latest installer file
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# check the hashes match
sha256sum Miniconda3-latest-Linux-x86_64.sh

# make the file executable
chmod +x Miniconda3-latest-Linux-x86_64.sh

# run the installer
bash Miniconda3-latest-Linux-x86_64.sh
```

The miniconda installer will now run and walk you through the install process. There are two **IMPORTANT** things you must take note of at this point:

1. You will have to overwrite the default install path when prompted by the miniconda installer to check the install path - the directory to which the install is attempted should be `/data/$USER/miniconda`.

```
Miniconda3 will now be installed into this location:
/<path>/<to>/miniconda3

  - Press ENTER to confirm the location
  - Press CTRL-C to abort the installation
  - Or specify a different location below

[/<path>/<to>/miniconda3] >>> /data/$USER/miniconda
```

2. **DO NOT** initialize miniconda at the end of the install process when prompted as shown here:

```
Do you wish the installer to initialize Miniconda3
by running conda init? [yes|no]
[yes] >>> no
```

Once the installer has run, delete the installation script.

```shell
rm Miniconda3-latest-Linux-x86_64.sh
```

Now make a modules folder and module file.

```shell
# modules folder
mkdir /home/$USER/modules

# module file
nano /home/$USER/modules/miniconda
```

Paste the below into the nano editor that opens upon running the final command. Note that this file is in Tcl not BASh, so environmental variable handing is different from the normal `$USER` for username.

```
#%Module10.2#####################################################################
##
## User Data Directory Miniconda module file
##
################################################################################

proc ModulesHelp { } {
        global version

        puts stderr "Makes a user's personal install of Miniconda available."
}

module-whatis   "Makes a user's personal install of Miniconda available."

# module variables

set MINICONDA_DIR     /data/$env(USER)/miniconda/bin

prepend-path PATH $MINICONDA_DIR
```

Now run the following line to make your personal modules available for loading whenever you login.

```shell
echo "module use /home/$USER/modules" >> ~/.bashrc
```

The last thing to note here is that you should not load the anaconda environmental module available to all HPC users and the personal miniconda module you have just made at the same time.

For further information on making software available via a custom module file visit:

[Making software available via a custom module file](https://docs.hpc.shef.ac.uk/en/latest/referenceinfo/environment-modules/creating-custom-modulefiles.html)


## 2. Load and Configure Conda

Run the following commands in order and follow any prompts as appropriate:

```shell
# load the miniconda module - if not already loaded
module load miniconda

# disable base environment auto-activation
conda config --set auto_activate_base false

# add the bioconda and conda-forge channels to conda configuration
conda config --add channels bioconda
conda config --add channels conda-forge

# set channel_priority to "strict"
conda config --set channel_priority strict

# ensure conda is up-to-date
conda update conda
```


## 3. Install Nextflow and nf-core within a Conda Environment

Run the following commands in order and follow any prompts as appropriate:

```shell
# make the "nf_env" environment (in /home/$USER/.conda/envs/nf_env)
conda create --name nf_env nextflow nf-core

# activate the environment
source activate nf_env

# ensure all packages are up-to-date
conda update --all
```

You can now test the install has worked by running the following:

```shell
# test the environment is working
nextflow info

# test functionality
nextflow run hello
```

When you are finished, you can deactivate your conda environment using the command `conda deactivate`.

Although you should not yet do this, should you wish to unload your personal miniconda module you can do so by running `module unload miniconda`.

Step 5. describes the process of running an nf-core pipeline using Nextflow. You do not have to have a conda environment active for this part of the process as it will be loaded as part of your submission script, but you should not unload the miniconda module at this point.


## 4. Configure Singularity for use with Nextflow and nf-core

When you run nextflow for the first time, Singularity will create a hidden directory `.singularity` in your `$HOME` directory `/home/$USER` which has very very limited (10GB) space available. It is therefore a good idea to create a directory somewhere else (e.g., `/data/$USER`) with more room and link the locations. To do this, run the following series of commands:

```shell
# change directory to $HOME
cd $HOME

# make the directory that will be linked to
mkdir /data/$USER/.singularity

# link the new directory with the existing one
ln -s /data/$USER/.singularity .singularity
```


## 5. Setup your Project and Configure your Run

Whichever file store you decide to locate your project root directory in, the assumed project sub-directory structure within this guide is as follows:

```
/filestore/$USER/
│
└── project_root/
    │
    ├── config
    ├── params
    ├── sample_sheet
    └── script
```

There are three things you will require to run an nf-core pipeline:

1. A sample sheet
2. A pipeline launcher parameter configuration file
3. A submission script

You can find nf-core pipelines by visiting [https://nf-co.re/pipelines](https://nf-co.re/pipelines). Each pipeline page has more information on how to use the pipeline as well as a full description of sample sheet requirements and formatting.

Your sample sheet should be located inside your `sample_sheet` sub-directory.

The general launch command in the script template below assumes you have configured your specific run using an nf-core pipeline launcher. For example, the launcher for the nf-core/rnaseq pipeline that can be found [here](https://nf-co.re/launch?pipeline=rnaseq). The parameters specified for your run using the launcher should be saved in a file named `nf-params.json` within the `params` sub-directory of your project root.

To create your run script, navigate to the `script` sub-directory and run the following:

```shell
nano nf_submission.sh
```

Paste the below into the editor ensuring to change the generic information for your own where indicated in the comment lines:

```shell
#!/bin/bash

## SGE scheduler flags

# job name  >>> edit "pipeline_name" for the name of the pipeline you are running e.g. rnaseq <<<
#$ -N nf-pipeline_name

# specify queue and project for the nextflow driver job  >>> keep and edit if using a priority queue else delete both <<<
#$ -q queue_name.q
#$ -P queue_name

# request resources for the nextflow driver job
#$ -pe smp 1
#$ -l rmem=2G

# export environmental variables in current shell environment to job
#$ -V

# send email >>> edit "username" <<<
#$ -M username@sheffield.ac.uk
#$ -m beas

# merge standard error stream into the standard output stream
#$ -j y

# output log file
#$ -o nextflow.log


## load miniconda module and activate analysis environment

module load miniconda
source activate nf_env


## define and export variables

# prevent java vm requesting too much memory and killing run
export NXF_OPTS="-Xms1g -Xmx2g"

# path to singularity cache
export NXF_SINGULARITY_CACHEDIR="/home/$USER/.singularity"

# project name  >>> edit "project_name" so that it is the name of your project root directory <<<
PROJECT="project_name"

# project directories  >>> edit the name of the "filestore" e.g. fastdata <<<
PARAM_DIR="/filestore/$USER/$PROJECT/params"
CONFIG_DIR="/filestore/$USER/$PROJECT/config"


## run command  >>> edit "pipeline" and "version" <<<

nextflow run nf-core/pipeline \
-r version \
-profile sbc_sharc \
-resume \
-params-file ${PARAM_DIR}/nf-params.json

```

Now save and exit by typing "Ctrl + O" then "Return" then "Ctrl + X".

**OPTIONAL:** If you have specified a priority access queue in your submission script, you will need a personal configuration to send your jobs and not just your driver script to the appropriate queue. Navigate to the `config` sub-directory of your project folder and run the following:

```shell
nano personal.config
```

Then paste the following into the editor, ensuring you enter the correct queue name:

```
process {
  queue = 'queue-name.q'
  clusterOptions = { "-P queue-name -l rmem=${task.memory.toGiga()}G" }
}
```

Save and exit by typing "Ctrl + O" then "Return" then "Ctrl + X".

Now append `-c ${CONFIG_DIR}/personal.config` to the `nextflow run` command on a new line in your submission script.


## 6. Submit your Run to the SGE Scheduler

Once you have fulfilled all of the requirements above, you should be ready to submit your batch job to the SGE scheduler on ShARC. From the project root, type the following:

```bash
qsub ./scripts/nf_submission.sh
```

Your pipeline run should start momentarily. Good Luck!

