# Changelog

All notable changes to this project will be documented in this file.

## [1.3]
### Added
- Added the ability to genrate random connected graphs

## [1.2]
### Added
- Added the ability to save graphs to text files with `save_graph`.
- Added the ability to load graphs from text files with `load_graph`.
- Added a `CHANGELOG.md` file to document changes.

### Changed
- Updated the README with examples for saving and loading graphs.

### Fixed
- Fixed a bug in `draw_graph` where paths with three nodes were not fully highlighted.

## [1.1]

### Fixed
- Fixed an issue in the calculation of the edges in the path inside th `draw_graph` function

## [1.0]
### Added
- Initial release with basic weighted graph creation and Dijkstra's algorithm for shortest path calculation.
- Graph visualization using `matplotlib` and `networkx`