---
name: New Config
about: A new cluster config
---

Please follow these steps before submitting your PR:

- [ ] If your PR is a work in progress, include `[WIP]` in its title
- [ ] Your PR targets the `master` branch
- [ ] You've included links to relevant issues, if any

Steps for adding a new config profile:

- [ ] Add your custom config file to the `conf/` directory
- [ ] Add your documentation file to the `docs/` directory
- [ ] Add your custom profile to the `nfcore_custom.config` file in the top-level directory
- [ ] Add your custom profile to the `README.md` file in the top-level directory
- [ ] Add your profile name to the `profile:` scope in `.github/workflows/main.yml`

<!--
If you require/still waiting for a review, please feel free to request from @nf-core/configs-team

Please see uploading to`nf-core/configs` for more details:
https://github.com/nf-core/configs#uploading-to-nf-coreconfigs

Thank you for contributing to nf-core!
-->
