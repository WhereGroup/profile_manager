# CHANGELOG

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

<!--

Unreleased

## version_tag - YYYY-DD-mm

### Added

### Changed

### Removed

-->

## 0.6.0 - 2025-04-03
### Bugs fixes 🐛
* fix(qdt profile): plugin_id should be an int by @jmkerloch in https://github.com/WhereGroup/profile_manager/pull/49
* fix(docstrings): escape chars in sample ini files to allow code introspection by @Guts in https://github.com/WhereGroup/profile_manager/pull/51
### Features and enhancements 🎉
* Big refactoring number 2 by @kannes in https://github.com/WhereGroup/profile_manager/pull/34
* Fix wrong enum by @kannes in https://github.com/WhereGroup/profile_manager/pull/41
* UI improvements by @kannes in https://github.com/WhereGroup/profile_manager/pull/45
* Misc improvements by @kannes in https://github.com/WhereGroup/profile_manager/pull/44
* Documentation: complete contributing guide and publish to GitHub Pages using GitHub Actions by @Guts in https://github.com/WhereGroup/profile_manager/pull/52
* Tooling: add script to update translation by @Guts in https://github.com/WhereGroup/profile_manager/pull/54
### Tooling 🔧
* update(tooling): add a proposed VS Code configuration to match contributing guidelines by @Guts in https://github.com/WhereGroup/profile_manager/pull/53
* add(tooling): dependabot configuration to track on dependencies update by @Guts in https://github.com/WhereGroup/profile_manager/pull/58
* Check Qt6 support flag by @kannes in https://github.com/WhereGroup/profile_manager/pull/57
### Documentation 📖
* Adjust URLs to new profile directory name by @kannes in https://github.com/WhereGroup/profile_manager/pull/40
### Other Changes
* change(license): use GPLv2 instead of MIT to comply with upstream licenses (Qt/QGIS) by @Guts in https://github.com/WhereGroup/profile_manager/pull/18
* Drop experimental flag by @kannes in https://github.com/WhereGroup/profile_manager/pull/55

## 0.5.0-beta2 - 2024-11-05

- First version after plugin's folder renaming under the hood (`profile-manager` --> `profile_manager` to comply with Python guidelines)
- Fix parameter order (broken import/removal of data sources) by @kannes in <https://github.com/WhereGroup/profile_manager/pull/33>
- Switch dialog tabs to back sensible defaults by @kannes in <https://github.com/WhereGroup/profile_manager/pull/32>
- update(ci): rm deprecated `set-output` command by @Guts in <https://github.com/WhereGroup/profile_manager/pull/31>

## 0.5.0-beta1 - 2024-10-09

- add tab to export profile ready for [QGIS Deployment Toolbelt](https://github.com/Guts/qgis-deployment-cli/) - See related [issue](https://github.com/WhereGroup/profile_manager/issues/10)
- add modern plugin's packaging using [QGIS Plugin CI](https://github.com/opengisch/qgis-plugin-ci/)
- apply Python coding rules to whole codebase (PEP8)
- remove dead code and every Plugin builder related files
- add Git hooks (pre-commit) and quality tooling
- ships the big refactoring started in 2023

## 0.4 - 2023-06-29

- Fairly big refactoring and cleanup
- Better and more verbose error handling
- Improve performance
- Reduce backup size, change backup directory
- Improve dialogs and messages
- Add support for Vector Tiles connections
- Fix a crash (thanks Ivano Giuliano!)

## 0.31 - 2022-07-31

- Update metadata

## 0.3 - 2022-07-13

- Fix scanning for bookmarks, favourites, exp functions, styles

## 0.21 - 2022-01-18

- Add support for BSD and other Unixes (thanks Loïc Bartoletti!)
- Add Italy - German translation (thanks Salvatore Fiandaca!)

## 0.2 - 2022-01-12

- First public release
