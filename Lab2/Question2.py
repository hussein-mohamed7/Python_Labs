def divide_string(text1,text2):
    text1_mid = (len(text1) + 1) // 2
    text2_mid = (len(text2) + 1) // 2
    
    text1_front = text1[:text1_mid]
    text1_back = text1[text1_mid:]
    text2_front = text2[:text2_mid]
    text2_back = text2[text2_mid:]
    
    return text1_front + text2_front + text1_back + text2_back

text1 = input("enter text1 :")
text2 = input("enter text2 :")

result = divide_string(text1,text2)
print(result)