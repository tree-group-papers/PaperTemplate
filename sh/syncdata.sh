#!/bin/bash

# Notes:
#   * This file is run as a pre-push hook, it must be configured properly.
#   * Do not move or rename this file, or it will break the symlink in .git/hooks

repopath=$(git rev-parse --show-toplevel)
reponame=$(basename ${repopath})

ssh ${USER}@ssh.et.byu.edu "mkdir -pf ~/groups/softmatter/Papers/data/$reponame-data"
rsync -avz --progress data/ ${USER}@ssh.et.byu.edu:~/groups/softmatter/Papers/data/$reponame-data/

