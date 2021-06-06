print("brute-calc v0.02")
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

#seconds
tr_s = n_key/speed_brute

#minutes
tr_min = tr_s/60

#hours
tr_hr = tr_min/60

#days
tr_d = tr_hr/24

#months
tr_m = tr_d/30

#years
tr_y = tr_d/365



#printing everthing
print("length of the keyword:",length,"characters")
print("number of characters in character set:",n_chars_in_charset)
print("number of keywords:",n_key,"keywords")
print("the speed of Bruteforce:",speed_brute,"k/s")
print("time required:",tr_s,"s ,",tr_min,"min ,",tr_hr,"hr ,",tr_d,"days ,",tr_m,"months ,",tr_y,"years")