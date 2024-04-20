# PyRGG Release Instructions

#### Last Update: 2024-04-19

1. Create the `release` branch under `dev`
2. Update all version tags
	1. `setup.py`
	2. `README.md`
	3. `PYRGG.spec`
	4. `otherfile/version_check.py`
	5. `otherfile/meta.yaml`
	6. `otherfile/Version.rc`
	7. `pyrgg/params.py`
3. Update `CHANGELOG.md`
	1. Add a new header under `Unreleased` section (Example: `## [0.1] - 2022-08-17`)
	2. Add a new compare link to the end of the file (Example: `[0.2]: https://github.com/sepandhaghighi/pyrgg/compare/v0.1...v0.2`)
	3. Update `dev` compare link (Example: `[Unreleased]: https://github.com/sepandhaghighi/pyrgg/compare/v0.2...dev`)
4. Update `.github/ISSUE_TEMPLATE/bug_report.yml`
   1. Add new version tag to `PyRGG version` dropbox options
5. Create a PR from `release` to `dev`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Wait for all CI pass
	6. Need review (**1** reviewer)
	7. Squash and merge
	8. Delete `release` branch
6. Merge `dev` branch into `master`
	1. Checkout to `master`
	2. `git merge dev`
	3. `git push origin master`
	4. Wait for all CI pass
7. Build EXE file
	1. Run `build_exe.bat` (Use `Python 3.4.x`)
8. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
	6. Upload EXE file
9. Bump!!
10. Close this version issues
11. Close milestone
12. Update website
	1. `git checkout gh-pages`
	2. Update all version tags
		1. `index.html`
	3. Update size of files
		1. `index.html`