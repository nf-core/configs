# nf-core/configs: Mahuika HPC Configuration

nf-core pipelines have been successfully run on the [Mahuika HPC](https://docs.nesi.org.nz/).

To run an nf-core pipeline on Mahuika, run the pipeline with `-profile mahuika`. This will download and launch the [`mahuika.config`](../conf/mahuika.config) which has been pre-configured with a setup suitable for Mahuika. Using this profile, a Docker image containing all of the required software will be downloaded, and converted to an Apptainer image before execution of the pipeline.

## Access to Mahuika

Please be aware that you will need to have a user account and be a member of an active project on Mahuika in order to use this infrastructure. See documentation for details regarding [creating an account](https://docs.nesi.org.nz/Getting_Started/Creating_an_Account/) and [applying for a project](https://docs.nesi.org.nz/Getting_Started/Projects/Applying_for_a_New_Project/) on Mahuika.

## Launch an nf-core pipeline on Mahuika

### Prerequisites

Before running the pipeline you will need to load Nextflow, which is a globally installed module on Mahuika. You can do this by running the commands below:

```bash
#See what versions are available
module avail Nextflow
#Load one of the versions
module load Nextflow/<version>
```

### Execution command

```bash
module load Nextflow/<version>

nextflow run <nf-core_pipeline>/main.nf \
  -profile mahuika \
  <additional flags>
```

### Specifying a partition

By default the `mahuika` profile will use both the Genoa and Milan partitions.
To specify a partition you can add its name as an additional profile.
For example, to run exclusively on the Genoa partition `-profile mahuika,genoa`.

### Additional information

More information about running Nextflow on Mahuika can be found on the [Nextflow page in the documentation](https://docs.nesi.org.nz/Software/Available_Applications/Nextflow).
