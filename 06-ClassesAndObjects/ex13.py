class TV:
    
    def __init__(self):
        self.is_on = False
        self.channel_no = '1'
        self.channels = []
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        print(f'TV is {"on, channel no: " + self.channel_no if self.is_on else "off"}')
    
    def set_channel(self, new_channel):
        self.channel_no = new_channel
    
    def set_channels(self, channels_list):
        self.channels = channels_list
        
    def show_channels(self):
        print(self.channels)
        

TV_CHANNELS = [
    'TVP1',
    'TVP2',
    'Polsat',
    'TVN',
    'Filmbox'
]

tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.show_channels()
tv1.set_channels(TV_CHANNELS)
tv1.show_channels()
tv1.show_status()
tv1.off()
