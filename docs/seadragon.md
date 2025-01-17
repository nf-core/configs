# nf-core/configs: Seadragon Configuration

To use, run a pipeline with `-profile seadragon`. This will download and launch the [`seadragon.config`](../conf/seadragon.config), which has been pre-configured with a setup suitable for the Seadragon HPC environment at The University of Texas MD Anderson Cancer Center. Using this profile, container images with all required software will be pulled and converted to Singularity images before job execution.

## Module Requirements

In order to run a pipeline on the Seadragon environment, you will need to load the following modules:

```bash
module load Nextflow
```

## iGenomes Resource

A local copy of the iGenomes resource is available on Seadragon `/rsrch3/scratch/reflib/REFLIB_data/AWS-iGenomes/` . You can reference it by using the `--genome <GENOME_ID>` parameter in your nf-core pipeline. This ensures that all genome-specific references are correctly configured and optimized for the cluster.


## Notes

- **Data Storage**: All intermediate files will be stored in the `work/` directory within the job's launch directory. These files can consume significant space, so it is recommended to delete this directory after the pipeline completes successfully.
- **User Access**: Ensure that you have an active account to use Seadragon. If unsure, contact the HPC support team at The University of Texas MD Anderson Cancer Center.
- **Job Submission**: Nextflow jobs must be submitted from the login nodes of Seadragon. If in doubt, refer to the cluster documentation or contact support.

## Example Command

```bash
nextflow run nf-core/rnaseq --reads '*_R{1,2}.fastq.gz' --genome GRCh38 -profile seadragon
```

## Further Information

For more details about seadragon cluster, visit the Seadragon HPC webpage: [https://hpcweb.mdanderson.edu/](https://hpcweb.mdanderson.edu/)
