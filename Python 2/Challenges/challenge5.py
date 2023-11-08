stringsFile = open(r"Python 2/Challenges/strings.txt", "rt")
outputFile = open(r"Python 2/Challenges/string_output.txt", "wt")
result = ""

for line in stringsFile:
  word = line.strip()
  if word == "I" or word == "Almdrasa":
    word = word.capitalize()
  else:
    word = word.lower()
  result += f"{word} "
  # print(word)
print(result, len(result.strip())) # terminal
print(result.strip(), file= outputFile)
outputFile.close()