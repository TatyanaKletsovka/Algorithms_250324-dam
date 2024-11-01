from collections import defaultdict


info = """
йцукен aaa, AAA, äÄÖÖÜÜ, ww, wew
"""
#
# print(ord('ä'))
# print(ord('ö'))
# print(ord('ü'))
# print(ord('ß'))

info = info.lower()
import string

ge = 'abcdefghijklmnopqrstuvwxyzäöüß'
eng = string.ascii_lowercase

if any(i in 'äöüß' for i in info):
  print('It\'s german alphabet:')
  alphabet = ge
else:
  print('It\'s english alphabet:')
  alphabet = eng

new = defaultdict(int)

for i in info:
  if i in alphabet:
    new[i] += 1


print(new)

