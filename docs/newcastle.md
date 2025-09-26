# nf-core/configs: Newcastle HPC Configuration

Configuration for the Newcastle high performance computing (HPC) cluster.

## Setup

To install nextflow we first need to get the prequisite java from module avail:

`module load Java/17.0.6`

Then installing Nextflow using the standard install options:
https://www.nextflow.io/docs/latest/install.html

`curl -s https://get.nextflow.io | bash`

Make Nextflow executable:

`chmod +x nextflow`

Then move Nextflow into an executable path. For example:

`mkdir -p $HOME/bin/`
`mv nextflow $HOME/bin/`

To ensure this works every time you login to the cluster, put inside your `~/.bash_profile` the java install:

`nano ~/.bash_profile`

Then paste in the line for the java install:

```
#Java module add v17:
module load Java/17.0.6
```

Exit nano with, control-X, then y to save, then enter to confirm

## Run

To use this profile, simply pass Nextflow the -profile newcastle flag eg.

```bash
nextflow run nf-core/_pipeline_ -profile newcastle --outdir results
```

In case of issues, please feel free to reach out to one of the maintainers (Chris Wyatt or Fernando Duarte) at ecoflow.ucl@gmail.com . We are based at UCL, but helped set up this config, and are happy to help.
