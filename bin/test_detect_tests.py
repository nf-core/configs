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
EVERY_PROFILE = [("alpha", ""), ("sanger", "")]


class SelectTests(unittest.TestCase):
    def check(self, changed, expected):
        self.assertEqual(select_tests(changed, PROFILES, PIPELINES), expected)

    def test_no_range_tests_every_testable_profile(self):
        self.check(None, EVERY_PROFILE)

    def test_core_files_test_every_profile(self):
        for path in (
            "bin/cchecker.py",
            "configtest.nf",
            "nfcore_custom.config",
            ".github/workflows/main.yml",
        ):
            self.check([path], EVERY_PROFILE)

    def test_docs_and_nothing_changed_need_no_test(self):
        self.check(["docs/alpha.md", "README.md", ".github/CODEOWNERS"], [])
        self.check([], [])

    def test_profile_config(self):
        self.check(["conf/alpha.config"], [("alpha", "")])

    def test_profile_subdirectory(self):
        self.check(["conf/sanger/farm22.config"], [("sanger", "")])

    def test_unregistered_and_untestable_configs_are_skipped(self):
        self.check(["conf/wcm.config", "conf/czbiohub_aws.config"], [])

    def test_unsafe_file_name_is_not_a_profile(self):
        self.check(["conf/$(curl evil).config"], [])

    def test_pipeline_profile_config(self):
        self.check(["conf/pipeline/rnaseq/beta.config"], [("beta", "rnaseq")])

    def test_pipeline_profile_data_file(self):
        self.check(["conf/pipeline/rnaseq/beta/params.yaml"], [("beta", "rnaseq")])

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


if __name__ == "__main__":
    unittest.main()
