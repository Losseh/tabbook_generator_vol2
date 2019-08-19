# util script to transform standard format of chords(upper verse)+lyrics(lower) song to supported *ly format
#
# * Example input in file dummy.lyb
#
#    Am    C     
# I am a dummy song
#     Am            E        E7
# And I really like to shake my ass
#
# * command to run:
# python transform.py path/to/dummy.lyb
#
# * Output (standard output)
#
# I am a dummy song \textbf{Am C}\\
# And I really like to shake my ass \textbf{Am E E7}\\
#
#
# * In order to save the output as a file please use ">" operator to redirect the output stream to a file.
# This was done on purpose for an intended usage to first see the output and be able to make needed changes
# and only after the output has eventually become satisfactory, save the output to the *ly formatted file.

#!/usr/bin/python
import sys
import re

CHORDS = "chords"
TEXT = "text"
EMPTY = "empty"
FORMATTED = "formatted"

CHORDS_THRESHOLD = 4.01
NOTES = "ABHCDEFG"


class stream:
  def __init__(self, data):
    self.data = data
    self.operations = []

  def pipe(self, operation):
    self.operations.append(operation)

  def get(self):
    result = self.data
    for op in self.operations:
      result = filter(lambda x: x is not None, map(op, result))

    return result


def get_line_type(s):
  if is_empty_line(s):
    return EMPTY
  if is_formatted(s):
    return FORMATTED
  if is_chords(s):
    return CHORDS

  return TEXT

def is_chords(s):
  words = s.split()
  return mean_words_length(words) < CHORDS_THRESHOLD and matches_chords_patterns(words)

def matches_chords_patterns(words):
  for w in words:
    if w[0] not in NOTES:
      return False

  return True

def is_formatted(s):
  return s[0] == '\\'

def is_empty_line(s):
  return s == ''

def is_lyrics(s):
  return not is_chords(s) and true

def mean_words_length(words):
  v = map(lambda x: (x, 1), map(len, words))
  count = reduce(sum_each, v, (0, 0))
  return float(count[0])/count[1] if count[1] is not 0 else 0

def sum_each(x, y):
  assert(len(x) == len(y))
  return (x[0] + y[0], x[1] + y[1])

def format_chords(line):
  t = line[1]
  result = re.sub('\ +', ' ', line[0])
  return ('\\textbf{' + result.replace("#", "\\texttt{\\#}") + '}' if t == CHORDS else result, t)

# after this we might have 2 types of lines: TEXT and FORMATTED
def reformat_chords_to_lineends(s):
  result = []
  s.reverse()
  
  def check_types(l, type1, type2):
    return l[1] == type1 and s and s[-1][1] == type2
  
  while s:
    line = s.pop()
    if check_types(line, CHORDS, TEXT):
      new_line = "{} {}".format(s[-1][0], line[0])
      result.append((new_line, TEXT))
      s.pop()
    elif check_types(line, EMPTY, EMPTY):
      result.append((line[0], TEXT))
      s.pop()
    else:
      result.append((line[0], TEXT if line[1] is not FORMATTED else FORMATTED))

  return result

def add_no_page_breaks(s):
  return ["\\begin{absolutelynopagebreak}"] + s + ["\\end{absolutelynopagebreak}", "\\newpage"]


assert(len(sys.argv) == 2)
fname = sys.argv[1]

with open(fname) as f:
    content = f.readlines()

tf = stream(content)
tf.pipe(lambda x: re.sub('\ *\n', '', x))
tf.pipe(lambda x: (x, get_line_type(x)))
tf.pipe(format_chords)

reformatted = reformat_chords_to_lineends(tf.get())

tf2 = stream(reformatted)
tf2.pipe(lambda x: "{}\\\\".format(x[0]) if x[1] == TEXT else x[0])
#tf2.pipe(lambda x: re.sub('\[', '', x))
#tf2.pipe(lambda x: re.sub('\]', '', x))
tf2.pipe(lambda x: re.sub('\[(.*)\]', '\\\\textit{\\1}', x))
tf2.pipe(lambda x: re.sub('\{ ', '{', x))

for line in add_no_page_breaks(tf2.get()):
  print line
