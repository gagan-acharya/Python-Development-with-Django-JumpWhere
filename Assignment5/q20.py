def delete_consecutive_strings(s):
	i=0
	j=0
	new_elements=''
	while(j<len(s)):
		if( s[i]==s[j] ):
			j+=1
		elif((s[j]!=s[i]) or (j==len(s)-1)):
			new_elements+=s[i]
			i=j
			j+=1
	new_elements+=s[j-1]
	return new_elements
s='coffee keeps you awake'
print('Input :', s)
print('Output :',delete_consecutive_strings(s))
