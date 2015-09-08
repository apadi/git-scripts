#!/usr/bin/env python

import os
import subprocess
import re


def filter_changes(regex, ignore_untracked=False):
    pattern = re.compile(regex)
    return filter(pattern.search, get_repo_changes(ignore_untracked))


def get_repo_changes(ignore_untracked=False):
    """
    Return a list of modified files within a git repository
    """
    project_root = subprocess.check_output(['git', 'root']).strip()

    proc = subprocess.Popen('git status --porcelain',
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    stdout, stderr = proc.communicate()
    if stderr.decode("utf-8") != "":
        print(stderr)
        raise RuntimeError
    else:
        # When the list of modified files is composed, the three first
        # characters of each line (which contain the file status marks)
        # are stripped out.
        # Additionally, any empty line (usually the stdout contains an
        # spurious empty line due to a training carry return) is stripped
        # out.
        # if requested (i.e. ignore_untracked arg == True) are stripped
        # too. The ignored files are denoted by the '??' marker in the
        # status report provided by git.
        modified_files = filter(None, stdout.decode("utf-8").split('\n'))
        if ignore_untracked:
            modified_files = filter(lambda x: not x.startswith('?'), modified_files)
        return [os.path.join(project_root, i[3:]) for i in modified_files]
