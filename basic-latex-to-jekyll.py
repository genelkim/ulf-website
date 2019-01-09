"""
Super rough-and-ready script for mapping LaTeX to Jekyll Markdown.
This is really based on my usage of LaTeX and not general coverage of
functionality.

This isn't meant to be perfect, but just speed up some of the process of
converting LaTeX files to webpage format.
"""

import argparse
import os
import re

GROUP_SEP = os.linesep + os.linesep

RE_PAIRS = [
    (r"\\textit\{([^\{]*?)\}", r"_\1_"), # italics
    (r"\\textbf\{([^\{]*?)\}", r"**\1**"), # bold
    (r"\\underline\{([^\{]*?)\}", r"__**\1**__"), # underline
    (r"\\section\{([^\{]*?)\}", r"# \1"), # section/h1
    (r"\\subsection\{([^\{]*?)\}", r"## \1"), # subsection/h2
    (r"\\subsubsection\{([^\{]*?)\}", r"### \1"), # subsubsection/h3
    (r"\\ulf\{([^\{]*?)\}", r"`\1`"), # monospace
    (r"\\texttt\{([^\{]*?)\}", r"`\1`"), # monospace
    (r"\\mono\{([^\{]*?)\}", r"`\1`"), # monospace
    (r"\\cite{([^\{]*?)\}", r"{% cite \1 %}"), # citation (doesn't handle multiple citations).
    (r"\\noindent", r""),
    (r"``(.+?)''", r'"\1"'), # quote
    (r"``(.+?)\"", r'"\1"'), # quote
    (r"\{\\sc ([^\{]*?)\}", r"*\1*{:.sc}") # small caps 
    ] 


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('--infile', type=str, required=True, help="Path to input file.")
  parser.add_argument('--outfile', type=str, required=True, help="Path to output file.")

  args = parser.parse_args()

  fstr = open(args.infile, 'r').read()

  # Split by multiple newlines.
  fgroups = fstr.split(GROUP_SEP)
  fgroups = [fg.strip() for fg in fgroups if fg.strip() != ""]
  fgroups = [fg.replace(os.linesep, " ") for fg in fgroups]
  
  ngroups = []
  for fg in fgroups:
    curfg = fg
    for pat, rep in RE_PAIRS:
      curfg = re.sub(pat, rep, curfg)
    ngroups.append(curfg)

  out = open(args.outfile, 'w')
  out.write(GROUP_SEP.join(ngroups))
  out.close()

