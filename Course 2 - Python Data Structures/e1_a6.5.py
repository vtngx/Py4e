text = "X-DSPAM-Confidence:    0.8475"
textSliced = text[(text.find(':') +1) : len(text)].strip()
textToNum = float(textSliced)

print(textSliced)
