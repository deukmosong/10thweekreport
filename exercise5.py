class TV:
    MIN_VOLUME=0
    MAX_VOLUME=20
    MIN_CHANNEL=0
    MAX_CHANNEL=200
    def __init__(self,volume=None,channel=None):
        if volume==None:
            self.__volume=5
        else :
            self.__volume=volume
        if channel==None:
            self.__channel=0
            self.__is_on=False
        else :
            self.__channel=channel
            self.__is_on=True



    def __str__(self):
        if self.__is_on==False:
            return 'TV가 꺼짐 상태 입니다'
        else:
            return '볼륨 ='+str(self.__volume)+',채널 ='+str(self.__channel)
    def toggle_power(self):
          if self.__is_on==False:
            self.__is_on=True
          else:
            self.__is_on=False
    def get_channel(self):
        return self.__channel
    def set_channel(self,channel):
        if channel>200 or channel<=0:
            print('채널오류')
        else:
            self.__channel=channel
    def get_volume(self):
        return self.__volume
    def set_volume(self,volume):
        if volume<0 or volume>20:
            print('볼륨 오류')
        else:
            self.__volume=volume
    def volume_up(self):
        self.__volume+=1
        if self.__volume>self.MAX_VOLUME:
            self.__volume=self.MAX_VOLUME
    def volume_down(self):
        self.__volume-=1
        if self.__volume<self.MAX_VOLUME:
            self.__volume=self.MAX_VOLUME
    def channel_up(self):
        self.__channel+=1
        if self.__channel>self.MAX_CHANNEL:
            self.__channel=0
    def channel_down(self):
        self.__channel-=1
        if self.__channel<self.MAX_CHANNEL:
            self.__channel=200

my_tv=TV()
print(my_tv)
my_tv.toggle_power()
print(my_tv)
my_tv.set_channel(200)
print(my_tv)
my_tv.volume_up()
my_tv.channel_up()
print(my_tv)