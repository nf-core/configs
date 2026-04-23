# nf-core/configs: NCI Gadi HPC Configuration

nf-core pipelines have been successfully configured for use on the [Gadi HPC](https://opus.nci.org.au/display/Help/Gadi+User+Guide) at the National Computational Infrastructure (NCI), Canberra, Australia.

To run an nf-core pipeline at NCI Gadi, run the pipeline with `-profile singularity,nci_gadi`. This will download and launch the [`nci_gadi.config`](https://github.com/nf-core/configs/blob/master/conf/nci_gadi.config) which has been pre-configured with a setup suitable for the NCI Gadi HPC cluster.

## Access to NCI Gadi

Please be aware that you will need to have a user account, be a member of an Gadi project, and have a service unit allocation to your project in order to use this infrastructure. See the [NCI user guide](https://opus.nci.org.au/display/Help/Getting+Started+at+NCI) for details on getting access to Gadi.

## Launch an nf-core pipeline on Gadi

Before running the pipeline, you will need to load Nextflow and Singularity, both of which are globally installed modules on Gadi (under `/apps`). You can do this by running the commands below:

```bash
module purge
module load nextflow
module load singularity
```

You can then run the pipeline using:

```bash
nextflow run <nf-core_pipeline>/main.nf \
    -profile singularity,nci_gadi \
    <additional flags>
```

### Cluster considerations

#### External network access

Please be aware that NCI Gadi HPC compute nodes **do not** have external network access. This means you will not be able to pull the workflow codebase or containers if you submit your `nextflow run` command as a job on any of the standard job queues (see the [nf-core documentation](https://nf-co.re/docs/usage/offline) for instructions on running pipelines offline). NCI currently recommends you run your Nextflow head job either in a GNU screen or tmux session within a [persistent session](https://opus.nci.org.au/spaces/Help/pages/241926895/Persistent+Sessions), or submit it as a job to the [copyq](https://opus.nci.org.au/display/Help/Queue+Structure). 

For example, to run Nextflow in a GNU screen session within a persistent session:

```bash
persistent-sessions start -p <project> <ps_name>
ssh <ps_name>.<user>.<project>.ps.gadi.nci.org.au
screen -S <screen_name>
nextflow run ...
```

You can detach from the screen session using Ctrl+A, then D, and log out of the persistent session while the pipeline continues to run. Later, you can reconnect to the persistent session using the same `ssh` command and reattach to the screen session with: `screen -r <screen_name>`.

#### Downloading containers

This config requires Nextflow to use [Singularity](https://www.nextflow.io/docs/latest/container.html#singularity) to execute processes. Before any process can be executed, the nf-core pipeline will first download the required container image to a local cache. This cache location can be specified using either `$NXF_SINGULARITY_CACHEDIR` environment variable or the `singularity.cacheDir` setting in the Nextflow config file. `nci_gadi.config` specifies the download and storage location with:

```
singularity.cacheDir = "/scratch/${params.project}/${System.getenv('USER')}/nxf_singularity_cache"
```

See the [project accounting](#project-accounting) section below for details on `params.project`.

Furthermore, Singularity uses the `$SINGULARITY_CACHEDIR` directory to store intermediate image layers and files during pulls (note that this cache is only used when the required container is not already available in Nextflow's own Singularity cache, specified by `$NXF_SINGULARITY_CACHEDIR` or `singularity.cacheDir`). By default, `$SINGULARITY_CACHEDIR` is set to `$HOME/.singularity/cache`. For pipelines involving a large number and/or large size of first-time container downloads, we recommend setting this environment variable to a scratch location to avoid exceeding your home filesystem quota. For example, before running your nextflow run command, you can set the environment variable to a location in the scratch filesystem with:

```
export SINGULARITY_CACHEDIR=/scratch/$PROJECT/$USER/singularity_cache
```

#### Gadi queues and job submission

This config currently determines which Gadi queue to submit your task jobs to based on the amount of memory required. For the sake of resource and cost (service unit) efficiency, the following rules are applied by this config:

- Tasks requesting **less than 128 Gb** will be submitted to the normalbw queue
- Tasks requesting **more than 128 Gb and less than 190 Gb** will be submitted to the normal queue
- Tasks requesting **more than 190 Gb and less than 1020 Gb** will be submitted to the hugemembw queue

Note that these are only baseline queue settings and may be adjusted depending on the goals of your pipeline run and the most efficient use of the HPC. You can make a local copy of the `nci_gadi.config` and modify the queue assignments as needed for specific processes or process groups. See the NCI Gadi [queue limit documentation](https://opus.nci.org.au/display/Help/Queue+Limits) for more information on the available queues and their associated charge rates.

### Project accounting

This config uses `params.project` to assign a project code to all task job submissions for billing purposes. By default, this is set to the environment variable `$PROJECT`. If you are a member of multiple Gadi projects, you can choose which project will be charged for your pipeline execution by setting `params.project` (`--project` on the command line) to the desired project code.

Similarly, `params.storage` (`--storage` on the command line) is used to specify the storage locations that the pipeline needs to access. By default, this is set to `gdata/${params.project}+scratch/${params.project}`.

Note: The version of Nextflow installed on Gadi has been modified to make it easier to specify resource options for jobs submitted to the cluster through the Nextflow process block (see NCI's [Gadi user guide](https://opus.nci.org.au/display/DAE/Nextflow) for more details). The values specified through the parameters above are passed into the process block in the `nci_gadi.config`.

## Resource usage

To help monitor the service unit (SU) cost of running workflows on Gadi, a plugin has been developed to generate a report in CSV or JSON format upon workflow completion. The `nf-gadi` plugin is available via the Nextflow plugin registry and can be enabled by adding `-plugins nf-gadi` to your Nextflow run command. See the [plugin project repository](https://github.com/AustralianBioCommons/nf-gadi) for more details.

Additionally, Sydney Informatics Hub also provides a script to collect per-task SU costs. Upon workflow completion, you can run the [gadi_nfcore_report.sh](https://github.com/Sydney-Informatics-Hub/HPC_usage_reports/blob/master/Scripts/gadi_nfcore_report.sh) in your workflow execution directory to collect resources from the PBS log files printed to each task's `.command.log`. Resource requests and usage for each process are summarised in the output `gadi-nf-core-joblogs.tsv` file. To run it, execute the following in your workflow execution directory:

```bash
bash gadi_nfcore_report.sh
```