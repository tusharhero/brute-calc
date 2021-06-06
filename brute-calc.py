print("brute-calc v0.01")
#made bt Tushar Maharana

#asking for the length of the keyword and converting it to integer
length = input("enter the length of the keyword:")
length = int(length)

#asking for the number of characters in character set and converting it to integer
n_chars_in_charset = input("enter the number of characters in character set:")
n_chars_in_charset = int(n_chars_in_charset)

#calculating number of keywords
n_key = n_chars_in_charset ** length

#asking for the speed of bruteforce in k/s and converting it to float
speed_brute = input("enter the speed of Bruteforce in k/s:")
speed_brute = float(speed_brute)

#calculating the time required
tr = n_key/speed_brute

#printing everthing
print("length of the keyword:",length,"characters")
print("number of characters in character set:",n_chars_in_charset)
print("number of keywords:",n_key,"keywords")
print("the speed of Bruteforce:",speed_brute,"k/s")
print("time required:",tr,"s")
