#!/bin/bash

repopath=$(git rev-parse --show-toplevel)
reponame=$(basename ${repopath})

rsync -avz --progress ${USER}@ssh.et.byu.edu:~/groups/softmatter/Papers/data/$reponame-data/ data/

