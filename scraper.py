import urllib
import re 

problem_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
i = 0

while i < len(problem_number):
	url = "http://www.artofproblemsolving.com/wiki/index.php/2014_AMC_8_Problems"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()

	regex = '<h2><span class="mw-headline" id="Problem_' + problem_number[i] + '">Problem ' + problem_number[i] + '</span></h2><p>(.+?)</p>'
	pattern = re.compile(regex)
	problem = re.findall(pattern, htmltext)

	i += 1
	print problem
