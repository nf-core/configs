# How this repo is used currently

In each nf-core config or pipeline, these lines are included. So basically, nf-core custom.config and the pipeline rnaseq.config will get pulled in.

```nextflow
// Load nf-core custom profiles from different institutions

// If params.custom_config_base is set AND either the NXF_OFFLINE environment variable is not set or params.custom_config_base is a local path, the nfcore_custom.config file from the specified base path is included.
// Load nf-core/rnaseq custom profiles from different institutions.
includeConfig params.custom_config_base && (!System.getenv('NXF_OFFLINE') || !params.custom_config_base.startsWith('http')) ? "${params.custom_config_base}/nfcore_custom.config" : "/dev/null"

// Load nf-core/rnaseq custom profiles from different institutions.
includeConfig params.custom_config_base && (!System.getenv('NXF_OFFLINE') || !params.custom_config_base.startsWith('http')) ? "${params.custom_config_base}/pipeline/rnaseq.config" : "/dev/null"
```

# New Directory Structure (2024)

We've reorganized cluster configurations to improve maintainability and co-locate related files. The new structure follows this pattern:

## Structure Overview

```
conf/<cluster>/
├── nextflow.config                    # Main cluster configuration
├── README.md                         # Cluster documentation and usage
└── pipelines/                        # Pipeline-specific configurations
    ├── <pipeline1>/
    │   ├── nextflow.config           # Pipeline-specific config
    │   └── README.md                 # Pipeline-specific docs
    └── <pipeline2>/
        ├── nextflow.config
        └── README.md
```

## Examples

### UPPMAX (complex cluster with pipeline-specific configs)
```
conf/uppmax/
├── nextflow.config                    # Main UPPMAX configuration
├── README.md                         # UPPMAX usage guide
└── pipelines/
    ├── ampliseq/
    │   ├── nextflow.config           # AmplicSeq-specific UPPMAX config
    │   └── README.md                 # AmplicSeq on UPPMAX docs
    └── sarek/
        ├── nextflow.config           # Sarek-specific UPPMAX config
        └── README.md                 # Sarek on UPPMAX docs
```

### Sanger (simple cluster with just main config)
```
conf/sanger/
├── nextflow.config                    # Main Sanger configuration
└── README.md                         # Sanger usage guide (if exists)
```

## Migration Process

### Automated Migration
Use the provided automation script to reorganize existing clusters:

```bash
./bin/reorganize-cluster.sh <cluster_name>
```

This script:
1. Creates the cluster directory if it doesn't exist
2. Moves `conf/cluster.config` → `conf/cluster/nextflow.config`
3. Renames `pipeline/` → `pipelines/` (if exists)
4. Moves pipeline configs from `conf/pipeline/*/cluster.config`
5. Moves pipeline docs from `docs/pipeline/*/cluster.md`
6. Updates `nfcore_custom.config` with the new path
7. Cleans up duplicate files

### Manual Steps (if needed)
1. **Create directory**: `mkdir conf/<cluster>`
2. **Move main config**: `mv conf/<cluster>.config conf/<cluster>/nextflow.config`
3. **Move pipeline configs**: `mv conf/pipeline/<pipeline>/<cluster>.config conf/<cluster>/pipelines/<pipeline>/nextflow.config`
4. **Move documentation**: `mv docs/pipeline/<pipeline>/<cluster>.md conf/<cluster>/pipelines/<pipeline>/README.md`
5. **Update registry**: Edit `nfcore_custom.config` to point to `conf/<cluster>/nextflow.config`

## Benefits

- **Co-location**: All cluster-related files are in one place
- **Consistent naming**: `nextflow.config` and `README.md` everywhere
- **Better discoverability**: Easier for maintainers to find cluster-specific files
- **Reduced duplication**: Single source of truth for each cluster configuration
- **Improved maintainability**: Clear separation between general and pipeline-specific configs

## Registry Update Required

When moving cluster configs, always update `nfcore_custom.config`:

```diff
profiles {
    cluster_name {
-       includeConfig "${params.custom_config_base}/conf/cluster_name.config"
+       includeConfig "${params.custom_config_base}/conf/cluster_name/nextflow.config"
    }
}
```

This is automatically handled by the reorganization script.
