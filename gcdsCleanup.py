import re, csv
inputfile = open('<FILE_NAME>', encoding = "ISO-8859-1")
outputfile = open('gcdsCleanedOutput.csv', 'w')
regex = re.compile('"([^"]*)"')
text = inputfile.readlines()
writer = csv.writer(outputfile, delimiter=' ')

print('\n[+] Opening csv file...')

for line in text:
	line = line.replace('\x00', '').replace('\n', '')
	if len(line) > 0 and 'New' in line:
		value = re.findall(r'"([^"]*)"', line)[0]
		if value.startswith('[') and value.endswith(']'):
			value = value[1:len(value)-1]
		writer.writerow([value])

print('\n[+] Finished Processing\n')
