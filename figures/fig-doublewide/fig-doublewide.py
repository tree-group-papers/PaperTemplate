#!/usr/bin/env python

import os
import subprocess

basename = os.path.splitext(__file__)[0]

f1 = open(basename+'.tex', 'w')
f1.writelines("""\
\\documentclass[10pt]{article}

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

#  \\put(2.375,2.30){(b)}
#  \\put(4.050,2.30){(c)}
#  \\put(5.675,2.30){(d)}

subprocess.run(['latex', basename+'.tex'])
subprocess.run(['pdflatex', basename+'.tex'])
subprocess.run(['dvips', '-t', 'unknown', basename+'.dvi', '-E', '-o', basename+'.eps'])
subprocess.run(['rm', basename+'.tex', basename+'.aux', basename+'.log', basename+'.dvi'])

#pdflatex $name.tex
#rm $name.tex $name.aux $name.log
#

