import sys
if len(sys.argv) < 3:
 print('Error: args less than 2,\nusage: python3 "Kanami-English convert.py" <0-english>kanami/1-kanami>english> <"words">')
 sys.exit()
for item in sys.argv:
 print(item)
if sys.argv[1] == "0":
 exec(open("./WordsLists/Kanami.config").read())
elif sys.argv[1] == "1":
 exec(open("./WordsLists/English.config").read())
startfrom = 0
for item in sys.argv:
 if startfrom > 1:
  line = item + "\n"
 startfrom += 1
temp = ""
data = ""
startfrom = 0
for char in line:
 if char in "!@#$%^&*()_+-=0987654321{}[]|\\:\";'><,.?/\n" and temp in "!@#$%^&*()_+-=0987654321{}[]|\\:\";'><,.?/\n":
  sys.stdout.write(char)
  data = str(data) + char
  temp = ""
 elif startfrom != len(line) and char in " !@#$%^&*()_+-=0987654321{}[]|\\:\";'><,.?/\n":
  #print(type(words[temp.lower()]))
  try:
   if type(words[temp]) == str:
    print(data + words[temp])
    data = str(data) + words[temp] + char
    startfrom += 1
   else:
    sys.stdout.write(data)
    info = int(input(str(words[temp]) + "indexId:"))-1
    data = str(data) + words[temp][info] + char
   temp = ""
   startfrom = 0
  except KeyError:
   print("can't find word")
   sys.stdout.write(char)
   data = str(data) + temp + char
   temp = ""
   startfrom = 0
 else:
  startfrom += 1
  temp = str(temp) + char.lower()
print("------------------------------------")
print(data)
