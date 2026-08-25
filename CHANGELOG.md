## [0.1.0] - 2026-08-25

### 🚀 Features

- *(ci)* Adopt the platform's release-PR workflow family

### 🐛 Bug Fixes

- *(ci)* Add package import test so pytest stops exiting 5 on empty tests dir
- *(ci)* Migrate publish job to python-semantic-release v10
- *(ci)* Match develop under semantic-release's main release group
- *(ci)* Pin python-semantic-release action to v10.5.3
- *(ci)* Run semantic-release via pip instead of the Docker action
- *(ci)* Pin GitPython below 3.1.60 for semantic-release compat

### 🚜 Refactor

- Rename package from shelf-objects.py to game-room-objects.py

### ⚙️ Miscellaneous Tasks

- Initial commit
- Scaffold Python package structure for shelf-objects.py
- Run tests on pull requests, not just push to develop
- Add CHANGELOG.md
# Changelog

All notable changes to this project are documented in this file.
