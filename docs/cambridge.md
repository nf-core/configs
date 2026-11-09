# nf-core/configs: Cambridge HPC Configuration

All nf-core pipelines can be run on the [Cambridge HPC cluster](https://docs.hpc.cam.ac.uk/hpc/index.html) at the University of Cambridge using `-profile cambridge`.
This will download and use the [`cambridge.config`](../conf/cambridge.config)
institutional profile, which is configured for running pipelines on CSD3 with
Singularity containers.

### Install Nextflow

The latest version of Nextflow is not installed by default on CSD3.

The recommended option is the standard Nextflow self-installing package:

```
# Check that Java 17+ is available
java -version

# Download Nextflow
curl -s https://get.nextflow.io | bash

# Make it executable
chmod +x nextflow

# Move it to a personal bin directory in hpc-work
mkdir -p $HOME/rds/hpc-work/bin
mv nextflow $HOME/rds/hpc-work/bin/

# Add that directory to your PATH if needed
export PATH="$HOME/rds/hpc-work/bin:$PATH"

# Confirm the installation
nextflow info
```

To make the `PATH` change persistent across sessions, add the `export PATH=...`
line to your `~/.bashrc` or equivalent shell startup file.

See the official installation guide for the latest details and Java
requirements:

- [nf-core / Nextflow installation guide](https://nf-co.re/docs/usage/getting_started/installation)

If you prefer a user-managed package manager, a simple option is to install
`micromamba` and then follow the nf-core conda-style instructions for creating
an environment with `nextflow`:

- [micromamba installation guide](https://mamba.readthedocs.io/en/stable/installation/micromamba-installation.html)
- [nf-core conda installation instructions](https://nf-co.re/docs/usage/getting_started/installation#conda-installation)

`pixi` may also work well for personal environment management; see the
[pixi documentation](https://pixi.prefix.dev/latest/). However, this profile
does not currently provide tested `pixi` instructions, so `micromamba` is the
more conservative recommendation here.

### Set up Singularity cache

Singularity allows the use of containers and will use a caching strategy. First,
you might want to set the `NXF_SINGULARITY_CACHEDIR` bash environment variable,
pointing at a directory with sufficient space. If not, it will be
automatically assigned to the current directory.

```
# do this once per login, or add this line to .bashrc
export NXF_SINGULARITY_CACHEDIR=$HOME/rds/hpc-work/nxf-singularity-cache
```

On CSD3, Singularity is available by default, so no additional module loading
should be required.

### Run Nextflow

Here is an example with the nf-core pipeline sarek ([read documentation here](https://nf-co.re/sarek/3.3.2)).
The profile defaults to the `icelake` partition, but users can switch to
`icelake-himem` or `sapphire` with `--partition`. The user should also provide
their SLURM project / account with `--project`.

#### Choosing a partition

As a rough guide, `icelake` is the default general-purpose choice for most
workflows. `icelake-himem` is the better option when processes need more memory
per CPU, for example memory-hungry tasks or jobs using only a small number of
CPUs but requiring substantial RAM. `sapphire` provides newer Sapphire Rapids
nodes with 112 CPUs and about 4.5 GiB RAM per CPU (512 GB per node), so it may
be a better fit for higher-CPU jobs than `icelake`.

#### Example

```
# Launch the nf-core pipeline for a test database
# with the Cambridge profile
nextflow run nf-core/sarek -profile test,cambridge --partition icelake --project NAME-SL2-CPU --outdir nf-sarek-test
```

If the project name contains `-SL3-`, the profile applies a 12 h walltime cap.
Otherwise it assumes the standard SL1 / SL2 36 h limit.

#### Running Nextflow on CSD3

We recommend starting Nextflow inside a `screen` or `tmux`
session so that the Nextflow manager process keeps running after you disconnect
your SSH session.

```
# Start a tmux session
tmux new -s nextflow

# Or start a screen session
screen -S nextflow

# Re-attach later if needed
tmux attach -t nextflow
screen -r nextflow
```

Detaching from `tmux` leaves the workflow running in the background with
`Ctrl-b` then `d`. For `screen`, use `Ctrl-a` then `d`.

You can then logout of the HPC and reattach to the session later.
Before logging out, make sure to **note the node you’re on**.
Suppose your login node was called `login-p-3`, you can later log back into this specific node as follows:

```bash
ssh username@login-p-3.hpc.cam.ac.uk
```

Then, you can re-attach to the `tmux`/`screen` session:

```bash
tmux attach -t nextflow
screen -r nextflow
```

#### Limit Nextflow JVM memory (recommended)

If needed, you can limit the memory used by the Nextflow manager process by
setting:

```bash
export NXF_JVM_ARGS='-Xms2g -Xmx4g'
```

This is a conservative example that should work for most runs. If the Nextflow
manager process still runs into memory errors, increase `-Xmx` accordingly.
This must be set **before** launching `nextflow run ...`. If you want to use
this setting by default, you can add the export line to your `~/.bashrc`.

#### Large runs

For large runs, for example workflows with many samples or many tasks, the
Nextflow manager process can itself use substantial memory. In those cases, it
is better to launch `nextflow run ...` inside an interactive `srun` session or
submit it via `sbatch`, rather than running it directly on a login node.

#### `work` directory

All of the intermediate files required to run the pipeline will be stored in
the `work/` directory. It is recommended to **delete** this directory after the
pipeline has finished successfully because it can get quite large, and all of
the main output files will be saved in the `--outdir` directory anyway.

> NB: You will need an account to use the Cambridge HPC cluster in order to run the pipeline. If in doubt contact IT.
> NB: Nextflow will need to submit the jobs via SLURM to the Cambridge HPC cluster and as such the commands above will have to be executed on one of the login nodes. If in doubt contact IT.
