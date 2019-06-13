import fileinput

file_path = 'sample.html'
for line in fileinput.FileInput(file_path, inplace=1):
    if "</body>" in line:
        line = line.replace(line, "NEW_TEXT\n"+line)
    print (line)
