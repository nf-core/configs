#!/bin/bash

# migrate-all-clusters.sh
# Mass migration script to reorganize all cluster configurations
# to the new directory structure using the existing reorganize-cluster.sh script

set -euo pipefail

# Script configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
REORGANIZE_SCRIPT="$SCRIPT_DIR/reorganize-cluster.sh"

# Counters
TOTAL_CLUSTERS=0
SUCCESSFUL_MIGRATIONS=0
FAILED_MIGRATIONS=0
SKIPPED_CLUSTERS=0

# Arrays to track results
SUCCESSFUL_CLUSTERS=()
FAILED_CLUSTERS=()
SKIPPED_CLUSTERS_LIST=()

# Usage function
usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Mass migration tool to reorganize all cluster configurations."
    echo ""
    echo "Options:"
    echo "  --dry-run     Show what would be migrated without making changes"
    echo "  --test-only   Only migrate first 3 clusters for testing"
    echo "  --help        Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 --dry-run              # Preview what would be migrated"
    echo "  $0 --test-only            # Test migration on first 3 clusters"
    echo "  $0                        # Migrate all remaining clusters"
    echo ""
    exit 1
}

# Parse command line arguments
DRY_RUN=false
TEST_ONLY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --test-only)
            TEST_ONLY=true
            shift
            ;;
        --help)
            usage
            ;;
        *)
            echo "Unknown option: $1"
            usage
            ;;
    esac
done

# Change to repository root
cd "$REPO_ROOT"

# Validate reorganize script exists
if [[ ! -x "$REORGANIZE_SCRIPT" ]]; then
    echo "❌ Error: reorganize-cluster.sh script not found or not executable at $REORGANIZE_SCRIPT"
    exit 1
fi

echo "🔄 Mass Cluster Configuration Migration"
echo "======================================="

# Find all remaining .config files that need migration
echo "🔍 Discovering clusters to migrate..."
CLUSTER_CONFIGS=($(find conf/ -maxdepth 1 -name "*.config" -type f | sort))
TOTAL_CLUSTERS=${#CLUSTER_CONFIGS[@]}

if [[ $TOTAL_CLUSTERS -eq 0 ]]; then
    echo "✅ No clusters found that need migration!"
    exit 0
fi

# Apply test-only limit if requested
if [[ "$TEST_ONLY" == true ]]; then
    if [[ $TOTAL_CLUSTERS -gt 3 ]]; then
        CLUSTER_CONFIGS=("${CLUSTER_CONFIGS[@]:0:3}")
        echo "🧪 TEST MODE: Only processing first 3 clusters"
    fi
fi

echo "📊 Found ${#CLUSTER_CONFIGS[@]} clusters to process (${TOTAL_CLUSTERS} total remaining)"

# Show what would be migrated in dry-run mode
if [[ "$DRY_RUN" == true ]]; then
    echo ""
    echo "🔍 DRY RUN - Clusters that would be migrated:"
    echo "=============================================="
    for config_file in "${CLUSTER_CONFIGS[@]}"; do
        cluster_name=$(basename "$config_file" .config)
        echo "  • $cluster_name (from $config_file)"
    done
    echo ""
    echo "Total clusters to migrate: ${#CLUSTER_CONFIGS[@]}"
    echo ""
    echo "To perform the actual migration, run without --dry-run"
    exit 0
fi

echo ""
echo "🚀 Starting migration process..."
echo ""

# Process each cluster
for config_file in "${CLUSTER_CONFIGS[@]}"; do
    cluster_name=$(basename "$config_file" .config)
    echo "📁 Processing cluster: $cluster_name"
    
    # Check if cluster already has a directory (shouldn't happen but be safe)
    if [[ -d "conf/$cluster_name" ]]; then
        echo "  ⚠️  Cluster directory already exists, skipping..."
        SKIPPED_CLUSTERS_LIST+=("$cluster_name")
        ((SKIPPED_CLUSTERS++))
        echo ""
        continue
    fi
    
    # Run the reorganization script
    if "$REORGANIZE_SCRIPT" "$cluster_name" >/dev/null 2>&1; then
        echo "  ✅ Migration successful"
        SUCCESSFUL_CLUSTERS+=("$cluster_name")
        ((SUCCESSFUL_MIGRATIONS++))
    else
        echo "  ❌ Migration failed"
        FAILED_CLUSTERS+=("$cluster_name")
        ((FAILED_MIGRATIONS++))
    fi
    
    echo ""
done

# Generate summary report
echo "🎉 Migration Summary"
echo "==================="
echo "Total clusters processed: ${#CLUSTER_CONFIGS[@]}"
echo "✅ Successful migrations: $SUCCESSFUL_MIGRATIONS"
echo "❌ Failed migrations: $FAILED_MIGRATIONS"
echo "⚠️  Skipped clusters: $SKIPPED_CLUSTERS"
echo ""

# Show detailed results
if [[ $SUCCESSFUL_MIGRATIONS -gt 0 ]]; then
    echo "✅ Successfully migrated clusters:"
    printf '   • %s\n' "${SUCCESSFUL_CLUSTERS[@]}"
    echo ""
fi

if [[ $FAILED_MIGRATIONS -gt 0 ]]; then
    echo "❌ Failed migrations (may need manual attention):"
    printf '   • %s\n' "${FAILED_CLUSTERS[@]}"
    echo ""
fi

if [[ $SKIPPED_CLUSTERS -gt 0 ]]; then
    echo "⚠️  Skipped clusters (already migrated):"
    printf '   • %s\n' "${SKIPPED_CLUSTERS_LIST[@]}"
    echo ""
fi

# Show git status
if [[ $SUCCESSFUL_MIGRATIONS -gt 0 ]]; then
    echo "📝 Git Status:"
    echo "=============="
    if git status --porcelain | head -5; then
        echo ""
        echo "📋 Next steps:"
        echo "1. Review the changes: git status"
        echo "2. Test a few profiles: nextflow config -show-profiles ."
        echo "3. Commit the changes: git add . && git commit -m 'refactor: migrate all clusters to new directory structure'"
        echo ""
    fi
fi

# Exit with error code if any migrations failed
if [[ $FAILED_MIGRATIONS -gt 0 ]]; then
    echo "⚠️  Some migrations failed. Please check the failed clusters manually."
    exit 1
fi

echo "🎊 All migrations completed successfully!"