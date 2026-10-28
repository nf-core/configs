# nf-core/configs: Palmetto HPC Configuration

Configuration profile for the Clemson University Palmetto HPC cluster.

This profile is maintained by the Research Computing and Data Engagment team at Clemson University.
Contact us at [ithelp@clemson.edu](mailto:ithelp@clemson.edu)
for questions or issues.

## Using the profile

To use this profile, specify it when running any nf-core pipeline:

```bash
## Load Nextflow module
module load nextflow
nextflow run nf-core/<pipeline-name> -profile palmetto
```

This will automatically apply all cluster-specific settings including executor,
resource limits, and container configurations.

### Sub-profiles

The following sub-profiles are available for specialized resources:

- `palmetto,cleanup`: Removes your pipeline's `work` directory after a successful run

Example:

```bash
nextflow run nf-core/<pipeline-name> -profile palmetto,cleanup
```

## Prerequisites

Before running pipelines with this profile:

1. Ensure you have access to the Clemson University HPC cluster
1. Load the Nextflow module: `module load nextflow`
1. Verify Singularity is available: `singularity --version`

### First-time setup

At least the first time you run a piepline, it may take several minutes
to download container images. If you would like to reuse these images, 
please set `$NXF_SINGULARITY_CACHEDIR` in your `~/.bashrc` to a folder
in your `/home` or `/project` folder.

## Cluster details

- **Scheduler**: SLURM
- **Default queue**: `work1`
- **Container engine**: Singularity
- **Resource limits**:
  - Maximum CPUs: 192 cores
  - Maximum memory: 750GB
  - Maximum walltime: 72 hours

## Reference genomes

This profile includes paths to local iGenomes reference genomes at
`/datasets/igenomes/`. Pipelines will automatically use local copies
instead of downloading references, saving time and bandwidth.

## Known issues

- Jobs requesting more than 24 hours may experience longer queue times
- The `/home` filesystem has a 250GB quota. Use `/scratch` for large datasets
- Container builds are not supported. Contact support if you need custom containers

## Troubleshooting

### Quota exceeded errors

Move your work directory to `/scratch` if you exceed `/home` quota:

```bash
cd /scratch/$USER
nextflow run nf-core/<pipeline-name> -profile palmetto
```

## Support

For issues related to this profile or the Clemson University HPC cluster:

- Email: [ithelp@clemson.edu](mailto:ithelp@clemson.edu)
- Documentation: https://docs.rcd.clemson.edu
- Submit tickets: https://docs.rcd.clemson.edu/support/category/submit-a-ticket/

For issues with nf-core pipelines, see the [nf-core website](https://nf-co.re).
