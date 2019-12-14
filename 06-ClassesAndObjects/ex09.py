class University():

    def __init__(self):
        self.name = 'UEK'
        self.full_name = 'Uniwesytet Ekonomiczny w Krakowie')
    
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name
        
    def print_full_name(self):
        print(self.full_name)
        
    def set_full_name(self, new_full_name):
        self.full_name = new_full_name
        
uek = University()
uek.print_full_name()
uek.set_name('Cracow University of Economics')
uek.print_full_name

