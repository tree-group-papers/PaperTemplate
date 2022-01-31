#!/usr/bin/env python

## ------------------------------------------------------------------------
## This script can be useful for combining subfigures into a single figure.
## It creates a latex file and then compiles it to either a pdf or eps.
## 
## Some notes:
## * Preamble geometry sets the size of the overall figure (in inches).
##   - Most journals have figures that are 3.25 inches wide for a single column
##     and 6.5 inches for a double column.
##   - I typically use a 4x3 image aspect ratio: 3.25 in wide and 2.44 in tall
##   - This makes a double-wide figure: 6.5in x 2.44 and a double tall figure: 
##     3.25in x 4.88 in.
## * Picture command and "put" commands are used to place subfigures
##   - Must make sure the argument of the picture command matches the geometry
##     call in the preamble.
## * Can add text labels like (a), (b), etc. using a put command, see below
## * Uses a sans serif font
## * Compile with pdflatex for a pdf; Compile with latex for an eps file.
## * Creates a figure that is named the same as the script.
## ------------------------------------------------------------------------

import os
import subprocess

basename = os.path.splitext(__file__)[0]

f1 = open(basename+'.tex', 'w')
f1.writelines("""\
\\documentclass[11pt]{article}

%Preamble
\\usepackage[margin=0in,paperwidth=6.5in,paperheight=2.44in]{geometry}
\\usepackage{graphicx}

%Font
\\usepackage{DejaVuSans}
\\renewcommand*\\familydefault{\sfdefault}
\\usepackage[T1]{fontenc}
 
%Document
\\begin{document}
\\setlength{\\unitlength}{1.0in}
\\centering
\\begin{picture}(6.5,2.44)
  \\put(0.00,0.00){\\includegraphics[width=3.25in]{{{subfig-placeholder}}} }
  \\put(0.00,2.35){\scriptsize(a)}
  \\put(3.25,0.00){\\includegraphics[width=3.25in]{{{subfig-placeholder}}} }
  \\put(3.25,2.35){\scriptsize(b)}
\\end{picture}
\\end{document}
"""
)
f1.close();

# for eps
#subprocess.run(['latex', basename+'.tex'])
#subprocess.run(['dvips', '-t', 'unknown', basename+'.dvi', '-E', '-o', basename+'.eps'])
#subprocess.run(['rm', basename+'.tex', basename+'.aux', basename+'.log', basename+'.dvi'])

# for pdf
subprocess.run(['pdflatex', basename+'.tex'])
subprocess.run(['rm', basename+'.tex', basename+'.aux', basename+'.log'])

