class phone : 
    price = 10000
    color = "white"
    brand = "google"
    features = ["camera", "speaker", "calling", "internet"]

    def func(self):
        print("just nothing")
        return "it worked"
    
    def sms(self, phone_id, message):
        text = f"sending sms to {phone_id} and the message is \"{message}\""
        return text

obj = phone()
print(obj.price)
print(obj.features)
print(obj.func())
text_recieved = obj.sms(1234, "hey gorib")
print(text_recieved)

