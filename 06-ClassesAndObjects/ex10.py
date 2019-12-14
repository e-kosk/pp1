class TV:
    
    def __init__(self):
        self.is_on = False
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        print(f'TV is {"on" if self.is_on else "off"}')
        

tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.off()
tv1.show_status()
