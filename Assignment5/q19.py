str = "Solitary cloud, Shadow in the setting sun, Stirs the drifter's heart"
print("Original Strings : ",str)
word = ""
all_words = []
str = str + " "
for i in range(0, len(str)):
	if(str[i] != ' '):
		word = word + str[i]
	else:
		all_words.append(word) 
		word = ""
 
small = large = all_words[0]
  
for k in range(0, len(all_words)):
	if(len(small) > len(all_words[k])):
		small = all_words[k]
	if(len(large) < len(all_words[k])):
		large = all_words[k]
print("Smallest word: " + small)
print("Largest word: " + large)