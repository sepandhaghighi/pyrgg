# -*- coding: utf-8 -*-
"""Version-check script."""
import os
import sys
import codecs
Failed = 0
VERSION = "1.3"

VERSION_1 = VERSION.split(".")[0]
VERSION_2 = str(int(float(VERSION) * 10 - int(VERSION_1) * 10))
VERSION_3 = str(int(float(VERSION) * 100 - int(VERSION_1)
                    * 100 - int(VERSION_2) * 10))
VERSION_4 = "0"

SETUP_ITEMS = [
    "version='{0}'",
    'https://github.com/sepandhaghighi/pyrgg/tarball/v{0}']
README_ITEMS = [
    "[Version {0}](https://github.com/sepandhaghighi/pyrgg/archive/v{0}.zip)",
    "[Exe-Version {0}](https://github.com/sepandhaghighi/pyrgg/releases/download/v{0}/PYRGG-{0}.exe)",
    "Run `PYRGG-{0}.exe`",
    "pip install pyrgg=={0}",
    "pip3 install pyrgg=={0}"]
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/sepandhaghighi/pyrgg/compare/v{0}...dev",
    "[{0}]:"]
RC_ITEMS = [
    "filevers=({0}, {1}, {2}, {3})",
    "prodvers=({0}, {1}, {2}, {3})",
    "(u'FileVersion', u'{0}.{1}.{2}.{3}'),",
    "(u'ProductVersion', u'{0}, {1}, {2}, {3}')"]
PARAMS_ITEMS = ['PYRGG_VERSION = "{0}"']
META_ITEMS = ['% set version = "{0}" %']

FILES = {
    "setup.py": SETUP_ITEMS,
    "README.md": README_ITEMS,
    "CHANGELOG.md": CHANGELOG_ITEMS,
    os.path.join(
        "pyrgg",
        "params.py"): PARAMS_ITEMS,
    os.path.join(
        "otherfile",
        "meta.yaml"): META_ITEMS
}

TEST_NUMBER = len(FILES.keys()) + 1


def print_result(failed=False):
    """
    Print final result.

    :param failed: failed flag
    :type failed: bool
    :return: None
    """
    message = "Version tag tests "
    if not failed:
        print("\n" + message + "passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER - Failed) + "/" + str(TEST_NUMBER))


if __name__ == "__main__":
    for file_name in FILES.keys():
        try:
            file_content = codecs.open(
                file_name, "r", "utf-8", 'ignore').read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(VERSION)) == -1:
                    print("Incorrect version tag in " + file_name)
                    Failed += 1
                    break
        except Exception as e:
            Failed += 1
            print("Error in " + file_name + "\n" + "Message : " + str(e))
    try:
        file_content = codecs.open(
            os.path.join(
                "otherfile",
                "Version.rc"),
            "r",
            "utf-8",
            'ignore').read()
        for test_item in RC_ITEMS:
            if file_content.find(
                test_item.format(
                    VERSION_1,
                    VERSION_2,
                    VERSION_3,
                    VERSION_4)) == -1:
                print("Incorrect version tag in " + "Version.rc")
                Failed += 1
                break
    except Exception as e:
        Failed += 1
        print("Error in Version.rc" + "\n" + "Message : " + str(e))

    if Failed == 0:
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)
