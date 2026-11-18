#!/usr/bin/env python
"""Parse the nf-core/configs profile registry and check every conf/*.config is in it."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# In conf/, but not registered in nfcore_custom.config
UNREGISTERED_CONFIGS = {"azurebatchdev", "wcm"}

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


if __name__ == "__main__":
    configs = {config.stem for config in (ROOT / "conf").glob("*.config")}
    unregistered = configs - registered_profiles() - UNREGISTERED_CONFIGS
    if unregistered:
        sys.exit(f"Not registered in nfcore_custom.config: {sorted(unregistered)}")
    print("Profile registry is consistent.")
