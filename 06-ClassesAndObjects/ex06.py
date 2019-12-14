class Book:
    
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def change_title(self, new_title):
        self.title = new_title
        
    def make_promo(self, discount):
        self.price = self.price - (self.price * (discount/100))
        
    def make_giveaway(self):
        self.price = 0
        

harry = Book('Harry Potter', 'idk', 32.50)

print(harry.price)
harry.make_promo(10)
print(harry.price)
harry.make_giveaway()
print(harry.price)
print()


class PhoneCall:
    
    def __init__(self, incomming_number, outcomming_number, time):
        self.incomming_number = incomming_number
        self.outcomming_number = outcomming_number
        self.time = time
        
    def end_call(self):
        print(f'Ended phone call at {self.time}')
        
    def say_hi(self):
        print(f'{self.outcomming_number} said "Hi" to {self.incomming_number}')
    
    def make_call(self):
        print(f'Calling {self.outcomming_number}')


call1 = PhoneCall('123123123', '456456456', '14.12.2019 12:05')
call1.make_call()
call1.say_hi()
call1.end_call()
print()


class Group:
    
    def __init__(self, no_of_male, no_of_female, group_name):
        self.no_of_male = no_of_male
        self.no_of_female = no_of_female
        self.group_name = group_name
        
    def change_group_name(self, new_name):
        self.group_name = new_name

    def add_male(self, no_of_new_male):
        self.no_of_male += no_of_new_male
        
    def add_female(self, no_of_new_famale):
        self.no_of_female += no_of_new_famale
        

group1 = Group(10, 20, '1111')
print(group1.group_name)
group1.change_group_name('1112')
print(group1.group_name)
