class University():

    def __init__(self):
        self.name = 'UEK'
    
    def print_name(self):
        print(self.name)
    
    def set_name(self, new_name):
        self.name = new_name
        
uek = University()
uek.print_name()
uek.set_name('AGH')
uek.print_name()
