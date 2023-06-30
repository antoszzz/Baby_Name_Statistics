

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

import sys
import os
import tkinter
from tkinter import filedialog
import ctypes

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  if not os.path.isfile(filename): 
    ctypes.windll.user32.MessageBoxW(0, 'The file was not found:\n' + filename, 'Error!', 0)
    sys.exit(1)

  with open(filename, 'r') as file:
    s = file.read()
  what = 'Popularity in '
  t = s.find(what)
  t = t + len(what)
  content_l = len(s)
  year = s[t:-(content_l - t - 4)]
  start = s.find('Female name')
  finish = s.find('</table>', start)
  rank = []
  m_name = []
  f_name = []
  while start < finish:
    if s.find('</td>', start) > finish: break
    for i in range(3):
      x1 = s.find('<td>', start)
      x2 = s.find('</td>', start)
      if i == 0:      rank.append(s[(x1 + 4):-(content_l - x2)])
      elif i == 1:      m_name.append(s[(x1 + 4):-(content_l - x2)])
      else:      f_name.append(s[(x1 + 4):-(content_l - x2)])
      start = x2 + 4
  f_rank = {};m_rank = {};j = 0
  for i in rank:
    f_rank[f_name[j]] = i
    m_rank[m_name[j]] = i
    j += 1
  stat_rank = m_rank
  stat_rank.update(f_rank)
  answ = [year]
  for i in sorted(stat_rank):
    answ.append(i + ' ' + stat_rank[i])
  #print(answ)
  return answ


def main():
  #This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    tkinter.Tk().withdraw()  # prevents and empty tkinter window from appearing
    d_f = filedialog.askopenfile(title='Step_1: Choose the data-file pls.', filetypes=[('Web files','*.html')])
    s_f = filedialog.askopenfile(title='Step_2: Choose the Summary-file pls.', filetypes=[('Text files','*.txt')])
    if d_f is None or s_f is None:
      ctypes.windll.user32.MessageBoxW(0,'Not all the files were provided!','Error',0)
      sys.exit()
    d_f=d_f.name
    s_f=s_f.name
  else:
    if len(args)==1: #'no_summary'
      print('Confirm that U don\'t need to save the results (Y/N):\n')
      s_f=input('Y/N:')
      i=0
      while i!=1:
        if s_f.upper() =='Y': 
          d_f=input('Type the address of data-file:\n')
          i=1
        elif s_f.upper() == 'N': sys.exit(1)
        else: print('Don\'t understand the answer. Repeat please.')
    elif len(args)==2:
      s_f = input('Type the address of summary-file:\n')
      d_f=input('Type the address of data-file:\n')
    else: flag='Expected only 2 arguments'
  if s_f == 'Y':
    print(f'Name statistics: \n{str(extract_names(d_f))}')
  else:
    #print(f'THE FILE NAME:{s_f.name}')
    with open(s_f,'a') as the_file:
      the_file.write(str(extract_names(d_f)))
      if not args: 
        ctypes.windll.user32.MessageBoxW(0, 'The Output was saved in to the:\n'+ s_f, 'Report', 0)
      else: 
        print(f'The Output was saved in to the: {s_f}')

if __name__ == '__main__':   main()
