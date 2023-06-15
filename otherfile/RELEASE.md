# PyRGG Release Instructions

#### Last Update: 2023-06-15

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
4. Create a PR from `release` to `dev`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Wait for all CI pass
	6. Need review
	7. Squash and merge
	8. Delete `release` branch
5. Merge `dev` branch into `master`
	1. Checkout to `master`
	2. `git merge dev`
	3. `git push origin master`
	4. Wait for all CI pass
6. Build EXE file
	1. Use `Python 3.4.x`
	2. Run `build_exe.bat`
7. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
	6. Upload EXE file
8. Bump!!
9. Close this version issues
10. Close milestone
11. Update website
	1. `git checkout gh-pages`
	2. Update all version tags
	3. Update size of files