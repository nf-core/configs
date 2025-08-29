#!/bin/bash

# reorganize-cluster.sh
# Automates the reorganization of cluster configuration directories
# to follow the new nf-core/configs structure pattern

set -euo pipefail

# Usage function
usage() {
    echo "Usage: $0 <cluster_name>"
    echo ""
    echo "Reorganizes cluster configuration files to the new structure:"
    echo "  conf/<cluster>/"
    echo "  ├── nextflow.config              # Main cluster config"
    echo "  ├── README.md                   # Main cluster documentation"
    echo "  └── pipelines/                  # Pipeline-specific configs"
    echo "      ├── <pipeline1>/"
    echo "      │   ├── nextflow.config     # Pipeline-specific config"
    echo "      │   └── README.md           # Pipeline-specific docs"
    echo "      └── <pipeline2>/"
    echo "          ├── nextflow.config"
    echo "          └── README.md"
    echo ""
    echo "Examples:"
    echo "  $0 uppmax"
    echo "  $0 sanger"
    echo ""
    exit 1
}

# Check arguments
if [ $# -ne 1 ]; then
    usage
fi

CLUSTER_NAME="$1"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to repository root
cd "$REPO_ROOT"

# Check if cluster config exists (either as directory or single file)
if [ ! -d "conf/${CLUSTER_NAME}" ] && [ ! -f "conf/${CLUSTER_NAME}.config" ]; then
    echo "Error: Neither conf/${CLUSTER_NAME}/ directory nor conf/${CLUSTER_NAME}.config file exists"
    exit 1
fi

# Create cluster directory if it doesn't exist
if [ ! -d "conf/${CLUSTER_NAME}" ]; then
    echo "  📁 Creating conf/${CLUSTER_NAME}/ directory"
    mkdir -p "conf/${CLUSTER_NAME}"
    
    # Move the single config file into the directory
    if [ -f "conf/${CLUSTER_NAME}.config" ]; then
        echo "  ✅ Moving conf/${CLUSTER_NAME}.config → conf/${CLUSTER_NAME}/nextflow.config"
        mv "conf/${CLUSTER_NAME}.config" "conf/${CLUSTER_NAME}/nextflow.config"
    fi
fi

echo "🔄 Reorganizing ${CLUSTER_NAME} cluster configuration..."

# Step 1: Rename main config file if it exists
if [ -f "conf/${CLUSTER_NAME}/${CLUSTER_NAME}.config" ]; then
    echo "  ✅ Renaming conf/${CLUSTER_NAME}/${CLUSTER_NAME}.config → conf/${CLUSTER_NAME}/nextflow.config"
    mv "conf/${CLUSTER_NAME}/${CLUSTER_NAME}.config" "conf/${CLUSTER_NAME}/nextflow.config"
fi

# Step 2: Rename pipeline directory if it exists
if [ -d "conf/${CLUSTER_NAME}/pipeline" ]; then
    echo "  ✅ Renaming conf/${CLUSTER_NAME}/pipeline/ → conf/${CLUSTER_NAME}/pipelines/"
    mv "conf/${CLUSTER_NAME}/pipeline" "conf/${CLUSTER_NAME}/pipelines"
fi

# Step 3: Handle pipeline-specific configs from conf/pipeline/*/
echo "  🔍 Looking for pipeline-specific configs in conf/pipeline/*/${CLUSTER_NAME}.config..."
for pipeline_config in conf/pipeline/*/"${CLUSTER_NAME}.config"; do
    if [ -f "$pipeline_config" ]; then
        pipeline=$(basename "$(dirname "$pipeline_config")")
        echo "    📁 Found config for pipeline: $pipeline"
        
        # Create pipeline directory
        mkdir -p "conf/${CLUSTER_NAME}/pipelines/${pipeline}"
        
        # Move and rename config
        echo "    ✅ Moving $pipeline_config → conf/${CLUSTER_NAME}/pipelines/${pipeline}/nextflow.config"
        mv "$pipeline_config" "conf/${CLUSTER_NAME}/pipelines/${pipeline}/nextflow.config"
    fi
done

# Step 4: Handle pipeline-specific docs from docs/pipeline/*/
echo "  🔍 Looking for pipeline-specific docs in docs/pipeline/*/${CLUSTER_NAME}.md..."
for pipeline_doc in docs/pipeline/*/"${CLUSTER_NAME}.md"; do
    if [ -f "$pipeline_doc" ]; then
        pipeline=$(basename "$(dirname "$pipeline_doc")")
        echo "    📄 Found docs for pipeline: $pipeline"
        
        # Create pipeline directory if it doesn't exist
        mkdir -p "conf/${CLUSTER_NAME}/pipelines/${pipeline}"
        
        # Move and rename docs
        echo "    ✅ Moving $pipeline_doc → conf/${CLUSTER_NAME}/pipelines/${pipeline}/README.md"
        mv "$pipeline_doc" "conf/${CLUSTER_NAME}/pipelines/${pipeline}/README.md"
    fi
done

# Step 5: Clean up any loose files in the cluster's pipelines directory
if [ -d "conf/${CLUSTER_NAME}/pipelines" ]; then
    echo "  🧹 Cleaning up loose files in conf/${CLUSTER_NAME}/pipelines/"
    
    # Move any .config files to their own directories
    for config_file in "conf/${CLUSTER_NAME}/pipelines"/*.config; do
        if [ -f "$config_file" ]; then
            pipeline=$(basename "$config_file" .config)
            echo "    📁 Creating directory for $pipeline"
            mkdir -p "conf/${CLUSTER_NAME}/pipelines/${pipeline}"
            echo "    ✅ Moving $config_file → conf/${CLUSTER_NAME}/pipelines/${pipeline}/nextflow.config"
            mv "$config_file" "conf/${CLUSTER_NAME}/pipelines/${pipeline}/nextflow.config"
        fi
    done
    
    # Move any .md files to their own directories
    for md_file in "conf/${CLUSTER_NAME}/pipelines"/*.md; do
        if [ -f "$md_file" ]; then
            pipeline=$(basename "$md_file" .md)
            echo "    📁 Creating directory for $pipeline (if needed)"
            mkdir -p "conf/${CLUSTER_NAME}/pipelines/${pipeline}"
            echo "    ✅ Moving $md_file → conf/${CLUSTER_NAME}/pipelines/${pipeline}/README.md"
            mv "$md_file" "conf/${CLUSTER_NAME}/pipelines/${pipeline}/README.md"
        fi
    done
fi

# Step 6: Update nfcore_custom.config
echo "  🔧 Updating nfcore_custom.config..."
if grep -q "conf/${CLUSTER_NAME}.config" nfcore_custom.config; then
    echo "    ✅ Updating path: conf/${CLUSTER_NAME}.config → conf/${CLUSTER_NAME}/nextflow.config"
    sed -i.bak "s|conf/${CLUSTER_NAME}.config|conf/${CLUSTER_NAME}/nextflow.config|g" nfcore_custom.config
    rm nfcore_custom.config.bak
elif grep -q "conf/${CLUSTER_NAME}/nextflow.config" nfcore_custom.config; then
    echo "    ✅ Path already correct in nfcore_custom.config"
else
    echo "    ⚠️  Warning: No ${CLUSTER_NAME} profile found in nfcore_custom.config"
fi

# Step 7: Display final structure
echo ""
echo "🎉 Reorganization complete! Final structure:"
echo ""
if [ -d "conf/${CLUSTER_NAME}" ]; then
    tree "conf/${CLUSTER_NAME}" 2>/dev/null || {
        echo "conf/${CLUSTER_NAME}/"
        find "conf/${CLUSTER_NAME}" -type f | sort | sed 's/^/  /'
    }
fi

echo ""
echo "📝 Next steps:"
echo "  1. Review the changes: git status"
echo "  2. Test the profile: nextflow config -show-profiles ."
echo "  3. Commit the changes: git add . && git commit -m 'refactor(${CLUSTER_NAME}): reorganize directory structure'"
echo ""
echo "✨ Don't forget to update any documentation that references the old paths!"