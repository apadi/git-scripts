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
    project_status = subprocess.check_output(['git', 'status', '--porcelain']).rstrip().split('\n')
    if ignore_untracked:
        project_status = filter(lambda x: not x.startswith('?'), project_status)
    return [os.path.join(project_root, i[3:]) for i in project_status]
