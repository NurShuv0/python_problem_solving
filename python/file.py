with open("message.txt",'w') as file:
    file.write("nur you are a gorib motherfucker \n")

with open("message.txt",'a') as file: #append
    file.write("nur you are a gorib motherfucker \n")

with open("message.txt",'r') as file : 
    text = file.read()
    print(text)
