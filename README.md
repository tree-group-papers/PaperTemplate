# PaperTemplate
A "fork-able" template for writing a paper via LaTeX

## How to Use this Repo to Write a Paper

## Directories

### codes
This directory should store the code or codes used to generate the raw data.
Typically this will be a copy of the simulation software you used, e.g. PFPD or MCPC.
Analysis and plotting scripts will not normally be stored here.

### data
This directory should store (i) **raw** data and (ii) the post-processed data and accompanying analysis scripts.
Do not store "garbage" data in this directory.
If you discover that the data is bad or that the runs failed, please delete the data.

Typically, your data should be organized into "experiments" that were performed on a certain date (or range of dates).
For example, suppose that you are running the Monte Carlo Polymer Crystallization (MCPC) code written by Pierre, and you are calculating the internal energy as a function of temperature using the parallel/CUDA code.
You would store do your runs and then store your data in a directory named `E_versus_T_parallel.2019-04-23`.
The data would be stored in a sub-directory named `raw_data`.
Any analysis you perform should then be stored in another sub-directory named `analysis`.
This could include Excel sheets, python scripts, preliminary plots, etc. that you are using to understand the data.

Because this directory can hold a large amount of data, it will be ignored by the git repository.
More information about this directory and how it is backed up is detaled below.

### figures
This directory stores the figures that will be in your paper or supplementary information.
This directory should not include analysis scripts or raw data, but rather should only include the data necessary to make plots.
Unlike the data directory, the figures directory **will** be stored in the git repository, so care should be taken about the size of files used here.

Each figure should be stored in a separate sub-directory (e.g. fig-placeholder) inside figures.
I typically name all of my figures with a prefix "fig-", as shown in the example.
I do this so that my directory name, figure file-name and LaTeX reference are all the same, so I can easily keep track of the figures when I write.

Inside each figure sub-director (e.g. fig-placeholder), you should have a fig-data sub-directory where you put the files you are using to plot your data.
Typically, these files will be copied from the analysis subdirectory of one of the experiments in your data directory.
You should make a note of where these files come from in a file named data\_paths.txt, so someone else (including you at a later date) can easily find the source location later.

You should make your files in a plotting tool that can draw publication quality figures.
Python, gnuplot and Matlab can all do this, but **Excel cannot**.
You should save your files in a vector format like .eps or .pdf.
Most journals prefer the .eps format.

If you need to draw something, i.e. make a schematic, you should use a vector drawing program like Inkscape or Adobe Illustrator.
This will allow you to save the figure in a vector format.
Do not use a bitmap drawing program like Gimp or Adobe Photoshop.

### manuscript
This directory should contain:
- The manuscript LaTeX file: manuscript.tex
- The supplemental information LaTeX file: suppinfo.tex
- The references .bib file: refs.bib
- A copy of all of the figures in .eps format

When you run pdfLaTeX on the manuscript.tex file (either on your machine or in Overleaf) you will generate a manuscript.pdf file with your figures.
A number of other files (e.g. mauscript.log, manuscript.bbl) will also be generated.
These latter files tell help LaTeX run or tell you what it did.
You can delete these if you want.

### notes
This directory is a place for you to store any notes, files or scripts that you want tracked in the repository but that don't fit elsewhere in the directory structure.

#### revisions
This directory is a place to track different stages of the revision process, including correspondence with co-authors and with journals.
For example, you typically need to write a cover letter to the editor of the journal when you submit the paper.
This directory is useful for storing these types of things.

### sh
This directory stores some shell scripts that are useful when writing the paper.
It currently includes:
- maketex.sh: a script for rendering your LaTeX files
- cleantex.sh: a script for deleting the "extra" files generated when pdflatex runs
- makediff.sh: a script that creates a .pdf file highlighting what was changed from the last version of the document.
- syncdata.sh: a script for syncing the data directory to the CAEDM group drive
- getdata.sh: a script for syncing the CAEDM group drive to your data directory

## Storing Data

Every paper has raw data associated with it.
It is a good practice to store the raw data alongside the paper in a data/ directory.
Unfortunately, git isn't a very useful tool for storing data.
Every time you commit a replace a data file with a new one, it makes a copy, and this can end up generating huge repositories.
This is bad, because it then takes forever to clone, commit, push and pull from repos, and we end up having to pay GitHub to store our data.
We definitely don't want to do this, since we typically generate GBs (and sometimes TBs) of data!
To avoid this, follow this rule: **Do not store your raw data in a directory that is tracked via git**.

To help you keep this rule, I have set up a "data/" directory inside the paper template repository, but its contents are not included when you commit or push your repository.
This is done via the .gitignore file inside the repository's main directory.
This ensures that you can store your data locally along with your paper, but keep it out of the git repository.

However, you still probably want your data to be backed up and shared with others.
To facilitate this, I have added a "hook" that runs every time you push your commits back to the repo.
The hook is a bash script that syncs your data directory to the CAEDM ssh server.
This way your data stays backed up, and you can easily access it anytime you need to.
Additionally, others in the group who are working on the paper should have access to your data and vice versa.
Anytime you clone or pull from the repo, you can also sync your local data folder with the CAEDM server to your local machine.

### Setting up Data Storage
* Set up ssh keys to the CAEDM ssh server
* Make sure you have access to the "softmatter" CAEDM group

### Pushing your data to CAEDM SSH
Notes: 
* This copies data from your local machine to the CAEDM server.
If the files are large, this can take a long time.  
* Because the files in data are not part of the repo (i.e. they are ignored via .gitignore), 
updating these files will change the repo.
In other words, you will not see a change to the git status when you change files inside data.

* Automatically: make a commit and then run a git push. (*Only works when you have changes to the other files in the repository.*)
* Manually: run sh/syncdata.sh from the main directory of the repository. (*Works anytime.*)

### Getting your data from CAEDM SSH
Notes: 
* This copies data from your local machine to the CAEDM server.
If the files are large, this can take a long time.  
* Retrieving data from the external server can only be done manually.
This is to avoid possibly long retrival times the first time you clone the repo.

* Manually: run sh/getdata.sh from the main directory of the repository.

