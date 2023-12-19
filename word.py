def hasWord(string,word):
  spl = string.split(' ')
  for i in range(len(spl)):
    if spl[i] == word:
      return True
  return False
