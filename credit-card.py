class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = None
        self.valid = None

# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        if (self.card_number[0] == "4"):
            self.card_type = "VISA"
            return True
        # elif (self.card_number[0] == "5") && (card_number[1] == "1" ||  "2" || "3" || "4" || "5")
        elif (self.card_number [0:2] in ["51", "52", "53", "54", "55"]):
            self.card_type = "Mastercard"
            return True
        elif (self.card_number [0:2] in ["34", "37"]):
            self.card_type = "AMEX"
            return True
        elif (self.card_number [0:4] == "6011"):
            self.card_type = "Discover"
            return True
        else:
            return "This is not a valid card type" 
            self.card_type = "INVALID"
            return False

# Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        if (self.card_type == "AMEX"):
            if len(self.card_number) == 15:
                print ("This is a long enough card with 15 digits")
                return True
        elif len(self.card_number) == 16:
            print ("This is a long enough card with 16 digits")
            return True
        else: 
            print ("This card number is not long enough")
            return False

# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        numbers = []
        length = len(self.card_number)
        #print ("length", length)

        # puts the cc numbers in a list
        for i in range (0,length):
            numbers.append (self.card_number[i])
            numbers[i]=int(numbers[i])

        # doubling every other number
        for i in range(0,length):
            if i%2 == 0:
                numbers[i] *= 2

        # put list of numbers back into string 
        for i in range (0,length):
            numbers[i]=str(numbers[i])

        #print ("list of numbers doubled", numbers)    
        
        # changes all the numbers in the list to one joined string
        new_numbers = "".join(numbers)

        #print("new numbers string", new_numbers)

        total_sum = 0 
        doubled_numbers = []
        length2 = len(new_numbers)

        for i in range (0,length2): 
            doubled_numbers.append (new_numbers[i])
            doubled_numbers[i]=int(doubled_numbers[i])

        # print ("This is a list of all the doubled split numbers", doubled_numbers)    

        total_sum = sum (doubled_numbers)
        # print ("Total sum", total_sum)

        if (total_sum%10 == 0):
            print ("This is a valid card")
            return True
        else:
            print ("This is an invalid card number")
            return False


cc = CreditCard (card_number = "5466506001288674")
cc.determine_card_type()
cc.check_length()
cc.validate()

print ("This is a card type", cc.card_type)
print (cc.check_length)
print (cc.validate)


# do not modify assert statements

"""
cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
"""
