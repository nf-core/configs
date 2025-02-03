# nf-core/configs: NCI Gadi proteinfold specific configuration

Extra specific configuration for proteinfold pipeline

## Usage

To use, run the pipeline with `-profile nci_gadi`.

This will download and launch the proteinfold specific [`nci_gadi.config`](../../../conf/pipeline/proteinfold/nci_gadi.config) which has been pre-configured with a setup suitable for the  NCI Gadi HPC cluster.

Example: `nextflow run nf-core/proteinfold -profile nci_gadi`

## proteinfold specific configurations for NCI Gadi

Specific configurations for NCI Gadi has been made for proteinfold.

### Project accounting

As described [here](https://github.com/nf-core/configs/blob/master/docs/nci_gadi.md#project-accounting) the config uses the PBS environmental variable `$PROJECT` to assign a project code to all task job submissions for billing purposes. If you are a member of multiple Gadi projects, you should confirm which project will be charged for your pipeline execution. You can do this using:

```bash
echo $PROJECT
```

The version of Nextflow installed on Gadi has been modified to make it easier to specify resource options for jobs submitted to the cluster. See NCI's [Gadi user guide](https://opus.nci.org.au/display/DAE/Nextflow) for more details. You can manually override the `$PROJECT` specification by editing your local copy of the `nci_gadi.config` and replacing `$PROJECT` with your project code. For example:

```nextflow
process {
    project = '<abc>'
    storage'scratch/<abc>+gdata/<abc>'
    ...
}
```
or export specification manually
```
export $PROJECT = '<abc>'
```

### Storage considerations 

When running proteinfold on NCI Gadi it is expected that all your data will be contained within the projects `/scratch` and `/g/data` directories, as specified in `$PROJECT` . However, if you are working across multiple project codes, you will need to manually edit this line in the `nci_gadi.config` to reflect this:

```bash
storage = "scratch/<abc>+gdata/<def>"
``` 

Alternatively, you can use the `--storage_account "scratch/abc+gdata/def"` parameter to specify access to storage as required.

### ⚠️ Expected Warnings  

When running the pipeline, you may encounter the following warnings:  

```
WARN: The following invalid input values have been detected:

* --storage_account: scratch/abc+gdata/def
* --project: abc
```

These warnings can be safely ignored. The parameters are required for job allocations and billing purposes on NCI Gadi, but they do not affect execution.
