import re
# User input is obtained by [raw_input('prompt: )] in python 2.x
# x2 = raw_input('input x2')
# print(x2)
# x3 = raw_input('input x3')
# print(x3)

# global x

# x = "i3on34g/10"
# cutoff = x[:-2]
# new = cutoff + "9"
# print(new)

# x.append("9")

# url = 'https://e-hentai.org/g/1103211/9444ca87d5/'
url = 'https://e-hentai.org/g/1103211/9444ca87d5/?p=33'

x = int(re.findall("[^\D]*$", url)[0])
y = x - 1
print(y)