#Assignment 8
word = input("type a word ")
word_set = set(word)
right_hand = set("qazwsxedcrfvtgbQAZWSXEDCRFVTGB")
left_hand = set("yhnujmkolpYHNUJMKOLPI") #Assignment İngilizce olduğundan Türkçe karakterleri dahil etmedim.
isnot = int( not (int(bool(right_hand & word_set)) + int(bool(left_hand & word_set)) == 2))*"not "
print(f"{word} is {isnot} a comfortable word")