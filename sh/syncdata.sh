#!/bin/bash

# Notes:
#   * This file is run as a pre-push hook, it must be configured properly.
#   * Do not move or rename this file, or it will break the symlink in .git/hooks
#   * Files in data/ are not part of the repo (they are ignored via .gitignore), 
#     This means updating these files will not trigger a need to run a git commit.
#     However, when a push is done, they will be backed up.

repopath=$(git rev-parse --show-toplevel)
reponame=$(basename ${repopath})

ssh ${USER}@ssh.et.byu.edu "mkdir -p ~/groups/softmatter/Papers/data/$reponame-data"
rsync -avz --progress data/ ${USER}@ssh.et.byu.edu:~/groups/softmatter/Papers/data/$reponame-data/

