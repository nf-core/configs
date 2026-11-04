#!/usr/bin/env python
"""Parse the nf-core/configs profile registry and check it is consistent."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Registered, but CI cannot write to its private S3 work directory
UNTESTABLE_PROFILES = {"czbiohub_aws"}
# In conf/, but not registered in nfcore_custom.config
UNREGISTERED_CONFIGS = {"azurebatchdev", "wcm"}
# In conf/pipeline/, but not included by the matching pipeline/<pipeline>.config
UNREFERENCED_PIPELINE_CONFIGS = {
    "methylseq/ku_sund_danhead",
    "rnaseq/kaust",
    "rnaseq/ku_sund_dangpu",
    "seqinspector/hasta",
}

PROFILE = re.compile(r"\s+(\w+)\s*\{")
INCLUDE = re.compile(
    r'\s*includeConfig\s+"\$\{params\.custom_config_base\}/conf/(.+)\.config"'
)


# shortcut: an include after a profile block counts for that profile, track blocks if a pipeline needs one
def includes(config):
    """Yield (profile, path below conf/) per include, with profile None before the first profile."""
    profile = None
    for line in config.read_text().splitlines():
        if match := PROFILE.match(line):
            profile = match[1]
        elif match := INCLUDE.match(line):
            yield profile, match[1]


def registered_profiles():
    return {profile for profile, _ in includes(ROOT / "nfcore_custom.config")}


def pipeline_includes():
    return {
        config.stem: list(includes(config))
        for config in (ROOT / "pipeline").glob("*.config")
    }


def find_problems():
    problems = []

    registered = {path for _, path in includes(ROOT / "nfcore_custom.config")}
    for path in sorted(registered):
        if not (ROOT / "conf" / f"{path}.config").exists():
            problems.append(
                f"nfcore_custom.config includes missing file conf/{path}.config"
            )
    for config in sorted((ROOT / "conf").glob("*.config")):
        if config.stem not in registered | UNREGISTERED_CONFIGS:
            problems.append(
                f"{config.relative_to(ROOT)} is not registered in nfcore_custom.config"
            )

    pipelines = pipeline_includes()
    for config in sorted((ROOT / "conf" / "pipeline").glob("*/*.config")):
        pipeline = config.parent.name
        key = f"{pipeline}/{config.stem}"
        included = {path for _, path in pipelines.get(pipeline, [])}
        if (
            f"pipeline/{key}" not in included
            and key not in UNREFERENCED_PIPELINE_CONFIGS
        ):
            problems.append(
                f"{config.relative_to(ROOT)} is not included by pipeline/{pipeline}.config"
            )

    return problems


if __name__ == "__main__":
    problems = find_problems()
    if problems:
        sys.exit("\n".join(problems))
    print("Profile registry is consistent.")
