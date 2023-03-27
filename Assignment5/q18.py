def Replace(str1):
	maketrans = str1.maketrans
	final = str1.translate(maketrans(',.', '.,', ' '))
	return final.replace(',', ", ")
string = "64.108,46"
print(Replace(string))