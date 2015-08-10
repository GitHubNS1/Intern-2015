import urllib
import re 

problem_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
i = 0

while i < len(problem_number):
	url = "http://www.artofproblemsolving.com/wiki/index.php/2014_AMC_8_Problems"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	problem = re.findall("<p>(.*?)</p>", htmltext, re.DOTALL)

	i += 1
	print problem
