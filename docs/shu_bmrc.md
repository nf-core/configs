# nf-core/configs: Sheffield Hallam University BMRC Cluster Configuration

This document provides guidelines for using nf-core pipelines on Sheffield Hallam University's BMRC High-Performance Computing (HPC) cluster. The custom configuration file for this cluster enables optimised resource usage and workflow compatibility within the BMRC HPC environment, facilitating efficient execution of nf-core workflows.

---

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Configuration Details](#configuration-details)
4. [Usage](#usage)
5. [Troubleshooting](#troubleshooting)
6. [Support and Contact](#support-and-contact)

---

## Introduction

This configuration file is specifically designed for running nf-core workflows on the BMRC HPC cluster at **Sheffield Hallam University**. The configuration integrates optimal resource parameters and scheduling policies to ensure efficient job execution on the cluster, aligning with internal HPC policies and specifications.

The cluster configuration:

- **Location**: BMRC HPC Cluster at Sheffield Hallam University
- **Contact**: Dr Lewis A Quayle ([l.quayle@shu.ac.uk](mailto:l.quayle@shu.ac.uk))
- **Documentation**: [BMRC HPC Documentation](https://bmrc-hpc-documentation.readthedocs.io/en/latest/)

## Requirements

To use this configuration, you must have:

- **Access to BMRC HPC**: Ensure your user account is enabled for HPC access at Sheffield Hallam University. The **GlobalProtect VPN** is required for remote access. For setup instructions, refer to [SHU VPN Guide](https://www.shu.ac.uk/digital-skills/programs-and-applications/virtual-private-network-vpn).
- **Nextflow**: Version 20.10.0 or later is recommended for optimal compatibility.

For a detailed guide to setting up Nextflow and running nf-core pipelines on the BMRC cluster, refer to [Running nf-core Pipelines on SHU BMRC Cluster](https://bmrc-hpc-documentation.readthedocs.io/en/latest/nfcore/index.html).

## Configuration Details

The configuration has been tailored for the BMRC HPC, providing preset values for CPUs, memory, and scheduling to align with HPC policies.

### Core Configuration

- **Cluster Scheduler**: `slurm`
- **Max Retries**: 2 (automatically reattempts failed jobs)
- **Queue Size**: 50 jobs
- **Submit Rate Limit**: 1 job per second

### Resource Allocation

Each nf-core workflows will automatically receive the following default resource maxima:

| Resource | Setting   |
| -------- | --------- |
| CPUs     | 64        |
| Memory   | 1007 GB   |
| Time     | 999 hours |

### Container Support

The configuration supports Apptainer for containerised workflows, with automatic mounting enabled, allowing seamless access to necessary filesystems within containers.

### Cleanup

Intermediate files from successful runs will be automatically deleted to free up storage.

## Usage

To launch an nf-core pipeline on the BMRC cluster using the `shu_bmrc` profile:

```bash
nextflow run nf-core/<pipeline_name> -profile shu_bmrc
```

## Troubleshooting

If you encounter issues, ensure you have:

- Followed the user guide on the BMRC HPC documentation site (see below).
- Specified the correct profile (`shu_bmrc`) for the cluster.
- Checked for sufficient permissions on the BMRC HPC cluster.
- Verified that Apptainer is enabled and accessible within your environment.

## Support and Contact

For support or questions, contact:

- **Primary Contact**: Dr Lewis A Quayle ([l.quayle@shu.ac.uk](mailto:l.quayle@shu.ac.uk))
- **BMRC HPC Documentation**: [Link](https://bmrc-hpc-documentation.readthedocs.io/en/latest/)
