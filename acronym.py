user_input = str(input("Enter the Word :"))
text = user_input.split()
a = ""
for i in text:
  a = a + str(i[0]).upper()

print(a)
