#!/usr/bin/env python

#######################################################################
#######################################################################
## Created on November 26 to check pipeline configs for nf-core/configs
#######################################################################
#######################################################################

import sys
import argparse
import re
import os
import glob

############################################
############################################
## PARSE ARGUMENTS
############################################
############################################

Description = "Check consistency between custom config files and the registry"
Epilog = """Example usage: python cchecker.py <nfcore_custom.config>"""

argParser = argparse.ArgumentParser(description=Description, epilog=Epilog)
## REQUIRED PARAMETERS
argParser.add_argument("CUSTOM_CONFIG", help="Input nfcore_custom.config.")

args = argParser.parse_args()

############################################
############################################
## MAIN FUNCTION
############################################
############################################


def check_config(Config):
    """Check that all profiles in nfcore_custom.config have a matching config file."""
    regex = "includeConfig*"
    missing_files = []

    with open(Config, "r") as cfg:
        config_dir = os.path.dirname(Config)
        for line in cfg:
            if re.search(regex, line):
                # Extract the profile name from: includeConfig "${params.custom_config_base}/conf/<name>.config"
                profile = line.split("/")[2].split(".")[0]
                config_path = os.path.join(config_dir, "conf", f"{profile}.config")
                if not os.path.exists(config_path):
                    missing_files.append(profile)

    if missing_files:
        print(
            f"ERROR: The following profiles in {Config} are missing their config files:\n"
        )
        for p in missing_files:
            print(f"  - {p}")
        sys.exit(1)
    else:
        print("All profiles in nfcore_custom.config have matching config files.")


def check_config_files(Config):
    """Check that all config files in conf/ are referenced in nfcore_custom.config."""
    custom_config_dir = os.path.dirname(Config)
    conf_dir = os.path.join(custom_config_dir, "conf")

    # Known config files that are not registered as profiles
    ignore = {"azurebatchdev", "wcm"}

    # Get all referenced profiles from nfcore_custom.config
    referenced = set()
    with open(Config, "r") as cfg:
        for line in cfg:
            if re.search(r"includeConfig\s*\"", line):
                profile = line.split("/")[2].split(".")[0]
                referenced.add(profile)

    # Check all .config files in conf/ (excluding pipeline/ subdirectory)
    orphaned = []
    for config_file in glob.glob(os.path.join(conf_dir, "*.config")):
        profile = os.path.splitext(os.path.basename(config_file))[0]
        if profile not in referenced and profile not in ignore:
            orphaned.append(profile)

    if orphaned:
        print(
            f"ERROR: The following config files in {conf_dir} are not referenced in {Config}:\n"
        )
        for p in orphaned:
            print(f"  - {p}")
        sys.exit(1)
    else:
        print("All config files in conf/ are referenced in nfcore_custom.config.")


def check_pipeline_configs(Config):
    """Check that pipeline-specific configs have matching entries in pipeline/*.config."""
    custom_config_dir = os.path.dirname(Config)
    pipeline_conf_dir = os.path.join(custom_config_dir, "conf", "pipeline")
    pipeline_dir = os.path.join(custom_config_dir, "pipeline")

    # Known pipeline config files that exist but are not yet referenced
    ignore = {
        "methylseq/ku_sund_danhead",
        "rnaseq/kaust",
        "rnaseq/ku_sund_dangpu",
        "seqinspector/hasta",
    }

    if not os.path.exists(pipeline_conf_dir):
        return

    orphaned_configs = []

    for pipeline_name in os.listdir(pipeline_conf_dir):
        pipeline_config_path = os.path.join(pipeline_dir, f"{pipeline_name}.config")
        pipeline_dir_path = os.path.join(pipeline_conf_dir, pipeline_name)

        if not os.path.isdir(pipeline_dir_path):
            continue

        if not os.path.exists(pipeline_config_path):
            print(
                f"WARNING: Pipeline config directory 'conf/pipeline/{pipeline_name}' exists but no 'pipeline/{pipeline_name}.config' file found."
            )
            continue

        # Get all referenced config files from pipeline config
        referenced = set()
        with open(pipeline_config_path, "r") as f:
            for line in f:
                if re.search(r"includeConfig\s*\"", line):
                    match = re.search(r"conf/pipeline/[^/]+/(.+)\.config\"", line)
                    if match:
                        referenced.add(match.group(1))

        # Check all config files in the pipeline directory
        for config_file in glob.glob(os.path.join(pipeline_dir_path, "*.config")):
            profile = os.path.splitext(os.path.basename(config_file))[0]
            key = f"{pipeline_name}/{profile}"
            if profile not in referenced and key not in ignore:
                orphaned_configs.append(key)

    if orphaned_configs:
        print(
            "ERROR: The following pipeline config files are not referenced in their pipeline config:\n"
        )
        for p in orphaned_configs:
            print(f"  - {p}")
        sys.exit(1)


check_config(Config=args.CUSTOM_CONFIG)
check_config_files(Config=args.CUSTOM_CONFIG)
check_pipeline_configs(Config=args.CUSTOM_CONFIG)
