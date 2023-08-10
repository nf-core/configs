# nf-core/configs: NCI Gadi HPC Configuration

nf-core pipelines have been successfully configured for use on the [Gadi HPC](https://opus.nci.org.au/display/Help/Gadi+User+Guide) at the National Computational Infrastructure (NCI), Canberra, Australia.

To run an nf-core pipeline at NCI Gadi, run the pipeline with `-profile singularity,nci_gadi`. This will download and launch the [`nci_gadi.config`](../conf/nci_gadi.config) which has been pre-configured with a setup suitable for the NCI Gadi HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Access to NCI Gadi

Please be aware that you will need to have a user account, be a member of an Gadi project, and have a service unit allocation to your project in order to use this infrastructure. See the [NCI user guide](https://opus.nci.org.au/display/Help/Getting+Started+at+NCI) for details on getting access to Gadi.

## Launch an nf-core pipeline on Gadi

### Prerequisites

Before running the pipeline you will need to load Nextflow and Singularity, both of which are globally installed modules on Gadi. You can do this by running the commands below:

```bash
module purge
module load nextflow singularity
```

### Execution command

```bash
module load nextflow
module load singularity

nextflow run <nf-core_pipeline>/main.nf \
    -profile singularity,nci_gadi \
    <additional flags>
```

### Cluster considerations

Please be aware that as of July 2023, NCI Gadi HPC queues **do not** have external network access. This means you will not be able to pull the workflow code base or containers if you submit your `nextflow run` command as a job on any of the standard job queues. NCI currently recommends you run your Nextflow head job either in a GNU screen or tmux session from the login node or submit it as a job to the [copyq](https://opus.nci.org.au/display/Help/Queue+Structure). See the [nf-core documentation](https://nf-co.re/docs/usage/offline) for instructions on running pipelines offline.

This config currently determines which Gadi queue to submit your task jobs to based on the amount of memory required. For the sake of resource and cost (service unit) efficiency, the following rules are applied by this config:

- Tasks requesting **less than 128 Gb** will be submitted to the normalbw queue
- Tasks requesting **more than 128 Gb and less than 190 Gb** will be submitted to the normal queue
- Tasks requesting **more than 190 Gb and less than 1020 Gb** will be submitted to the hugemembw queue

See the NCI Gadi [queue limit documentation](https://opus.nci.org.au/display/Help/Queue+Limits) for details on charge rates for each queue.

### Project accounting

This config uses the PBS environmental variable `$PROJECT` to assign a project code to all task job submissions for billing purposes. If you are a member of multiple Gadi projects, you should confirm which project will be charged for your pipeline execution. You can do this using:

```bash
echo $PROJECT
```

The version of Nextflow installed on Gadi has been modified to make it easier to specify resource options for jobs submitted to the cluster. See NCI's [Gadi user guide](https://opus.nci.org.au/display/DAE/Nextflow) for more details. You can manually override the $PROJECT specification by editing your local copy of the `nci_gadi.config` and replacing $PROJECT with your project code. For example:

```nextflow
process {
    executor = 'pbspro'
    project = 'aa00'
    storage = 'scratch/aa00+gdata/aa00'
    ...
}
```

## Resource usage

The NCI Gadi config summarises resource usage in a custom trace file that will be saved to your execution directory. However, for accounting or resource benchmarking purposes you may need to collect per-task service unit (SU) charges. Upon workflow completion, you can run the Sydney Informatics Hub's [gadi_nfcore_report.sh](https://github.com/Sydney-Informatics-Hub/HPC_usage_reports/blob/master/Scripts/gadi_nfcore_report.sh) script in your workflow execution directory with:

```bash
bash gadi_nfcore_report.sh
```

This script will collect resources from the PBS log files printed to each task's `.command.log`. Resource requests and usage for each process is summarised in the output `gadi-nf-core-joblogs.tsv` file. This is useful for resource benchmarking and SU accounting.
