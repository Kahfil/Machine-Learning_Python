text = "X-DSPAM-Confidence:    0.8475"
search=text.find("0")
number=text[search : ]
result=float(number)
print(result)
