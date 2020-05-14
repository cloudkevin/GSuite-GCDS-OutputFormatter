import re, csv
inputfile = open('<FILE_NAME>', encoding = "ISO-8859-1")
outputfile = open('gcdsCleanedOutput.csv', 'w')
regex = re.compile('"([^"]*)"')
text = inputfile.readlines()

print('\n[+] Opening csv file...')

writer = csv.writer(outputfile, delimiter=' ')
for line in text:
	line = line.replace('\x00', '')
	line = line.replace('\n', '')
	if len(line) > 0:
		if 'New' in line:
			value = re.findall(r'"([^"]*)"', line)[0]
			if value.startswith('[') and value.endswith(']'):
				value = value[1:len(value)-1]
			writer.writerow([value])

print('\n[+] Finished Processing\n')
