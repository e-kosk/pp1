class TV:
    
    def __init__(self):
        self.is_on = False
        self.channel_no = '1'
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        print(f'TV is {"on, channel no: " + self.channel_no if self.is_on else "off"}')
    
    def set_channel(self, new_channel):
        self.channel_no = new_channel
        

tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.set_channel('5')
tv1.show_status()
tv1.off()
tv1.show_status()


