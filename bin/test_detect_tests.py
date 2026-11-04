import unittest

from detect_tests import select_tests

PROFILES = {"alpha", "sanger", "czbiohub_aws"}
PIPELINES = {
    "rnaseq": [("alpha", "pipeline/rnaseq/alpha"), ("beta", "pipeline/rnaseq/beta")],
    "viralrecon": [
        (None, "pipeline/viralrecon/genomes"),
        ("alpha", "pipeline/viralrecon/alpha"),
    ],
}
ALPHA = [("alpha", ""), ("alpha", "rnaseq"), ("alpha", "viralrecon")]


class SelectTests(unittest.TestCase):
    def check(self, changed, expected):
        self.assertEqual(select_tests(changed, PROFILES, PIPELINES), expected)

    def test_no_range_tests_every_testable_profile(self):
        self.check(None, ALPHA + [("sanger", "")])

    def test_files_outside_profiles_need_no_test(self):
        self.check(["docs/alpha.md", "bin/cchecker.py", "nfcore_custom.config"], [])
        self.check([], [])

    def test_profile_config_also_tests_its_pipelines(self):
        self.check(["conf/alpha.config"], ALPHA)

    def test_profile_subdirectory(self):
        self.check(["conf/sanger/farm22.config"], [("sanger", "")])

    def test_unregistered_and_untestable_configs_are_skipped(self):
        self.check(["conf/wcm.config", "conf/czbiohub_aws.config"], [])

    def test_pipeline_profile_config(self):
        self.check(["conf/pipeline/rnaseq/beta.config"], [("beta", "rnaseq")])

    def test_top_level_pipeline_include_tests_every_profile_of_the_pipeline(self):
        self.check(
            ["conf/pipeline/viralrecon/genomes.config"], [("alpha", "viralrecon")]
        )

    def test_pipeline_registry(self):
        self.check(
            ["pipeline/rnaseq.config"], [("alpha", "rnaseq"), ("beta", "rnaseq")]
        )

    def test_unreferenced_pipeline_config_is_skipped(self):
        self.check(
            ["conf/pipeline/rnaseq/kaust.config", "conf/pipeline/absent/x.config"], []
        )
