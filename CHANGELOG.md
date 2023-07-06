# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]
## [1.4] - 2023-07-06
### Added
- `check_for_config` function
- `load_config` function
- `save_config` function
### Changed
- `README.md` modified
- Logo changed
- `codecov` removed from `dev-requirements.txt`
- Test system modified
- Error messages updated
## [1.3] - 2022-11-30
### Added
- Graphviz(DOT) format
### Changed
- [asciinema](https://asciinema.org) instruction video updated
- Test system modified
- `README.md` modified
- `Python 3.11` added to `test.yml`
- CLI mode updated
- `dev-requirements.txt` updated
- To-do list moved to `TODO.md`
## [1.2] - 2022-09-07
### Added
- Anaconda workflow
- Discord badge
### Changed
- Menu optimized
- Docstrings modified
- `branch_gen` function modified
- `edge_gen` function modified
- `precision` and `min_edge` parameters added to `branch_gen` function
- `random_edge` parameter removed from `branch_gen` function
- Test system modified
- `AUTHORS.md` updated
- License updated
- `README.md` modified
- `Python 3.10` added to `test.yml`
### Removed
- `sign_gen` function
- `random_edge_limits` function
## [1.1] - 2021-06-09
### Added
- `requirements-splitter.py`
- `is_weighted` function
- `_write_properties_to_json` function
- `PYRGG_TEST_MODE` parameter
### Changed
- Test system modified
- JSON, YAML and Pickle formats value changed from `string` to `number`
- `properties` section added to JSON, YAML and Pickle formats
- `_write_to_json` function renamed to `_write_data_to_json`
- `logger` function modified
- `time_convert` function modified
- `branch_gen` function modified
- References updated
## [1.0] - 2021-01-11
### Added
- Number of files option
### Changed
- All flags type changed to `bool`
- Menu optimized
- The `logger` function enhanced.
- Time format in the `logger` changed to `%Y-%m-%d %H:%M:%S`
- `dl_maker` function modified
- `tgf_maker` function modified
- `gdf_maker` function modified
- `run` function modified
## [0.9] - 2020-10-07
### Added
- GEXF format
- Float weight support
- `tox.ini`
### Changed
- Menu optimized
- `pyrgg.py` renamed to `graph_gen.py`
- Other functions moved to `functions.py`
- Test system modified
- `params.py` refactored
- `graph_gen.py` refactored
- `functions.py` refactored
- `weight_str_to_number` function renamed to `convert_str_to_number`
- `branch_gen` function bugs fixed
- `input_filter` function bug fixed
- `gl_maker` function bug fixed
- `CONTRIBUTING.md` updated
- `AUTHORS.md` updated
### Removed
- `print_test` function
- `left_justify` function
- `justify` function
- `zero_insert` function
## [0.8] - 2020-08-19
### Added
- GDF format
- GML format
### Changed
- CLI snapshots updated
- `AUTHORS.md` updated
## [0.7] - 2020-08-07
### Added
- Graph Line format
### Changed
- Menu optimized
## [0.6] - 2020-07-24
### Added
- Matrix Market format
### Changed
- `json_maker` function optimized
- `dl_maker` function optimized
- `tgf_maker` function optimized
- `lp_maker` function optimized
## [0.5] - 2020-07-01
### Added
- TSV format
- Multigraph control
### Changed
- `branch_gen` function modified
- Website changed to [https://www.pyrgg.ir](https://www.pyrgg.ir)
## [0.4] - 2020-06-17
### Added
- Self loop control
- Github action
### Changed
- `appveyor.yml` updated
## [0.3] - 2019-11-29
### Added
- `__version__` variable
- `CHANGELOG.md`
- `dev-requirements.txt`
- `requirements.txt`
- `CODE_OF_CONDUCT.md`
- `ISSUE_TEMPLATE.md`
- `PULL_REQUEST_TEMPLATE.md`
- `CONTRIBUTING.md`
- `version_check.py`
- `pyrgg_profile.py`
- Unweighted graph
- Undirected graph
- Exe version
### Changed
- Test system modified
- `README.md` modified
- Docstrings modified
- `get_input` function modified
- `edge_gen` function modified
- Parameters moved to `params.py`

## [0.2] - 2017-09-20
### Added
- CSV format
- YAML format
- Weighted edge list format (WEL)
- ASP format
- Trivial graph format (TGF)
- UCINET DL format
- Pickle format

## [0.1] - 2017-08-19
### Added
- DIMACS format
- JSON format
- README

[Unreleased]: https://github.com/sepandhaghighi/pyrgg/compare/v1.4...dev
[1.4]: https://github.com/sepandhaghighi/pyrgg/compare/v1.3...v1.4
[1.3]: https://github.com/sepandhaghighi/pyrgg/compare/v1.2...v1.3
[1.2]: https://github.com/sepandhaghighi/pyrgg/compare/v1.1...v1.2
[1.1]: https://github.com/sepandhaghighi/pyrgg/compare/v1.0...v1.1
[1.0]: https://github.com/sepandhaghighi/pyrgg/compare/v0.9...v1.0
[0.9]: https://github.com/sepandhaghighi/pyrgg/compare/v0.8...v0.9
[0.8]: https://github.com/sepandhaghighi/pyrgg/compare/v0.7...v0.8
[0.7]: https://github.com/sepandhaghighi/pyrgg/compare/v0.6...v0.7
[0.6]: https://github.com/sepandhaghighi/pyrgg/compare/v0.5...v0.6
[0.5]: https://github.com/sepandhaghighi/pyrgg/compare/v0.4...v0.5
[0.4]: https://github.com/sepandhaghighi/pyrgg/compare/v0.3...v0.4
[0.3]: https://github.com/sepandhaghighi/pyrgg/compare/v0.2...v0.3
[0.2]: https://github.com/sepandhaghighi/pyrgg/compare/v0.1...v0.2
[0.1]: https://github.com/sepandhaghighi/pyrgg/compare/1e238cd...v0.1



