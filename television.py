class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        '''
        Toggles the __status variable of the Television to True or False
        :return:
        '''
        self.__status = not self.__status

    def mute(self) -> None:
        '''
        Toggles the __muted variable of the Television to True or False if __status is true
        :return:
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        '''
        If __status is True, Increments __channel by 1, if __channel is at the MAX_CHANNEL value when channel_up is called __channel becomes the MIN_CHANNEL value
        :return:
        '''
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        If __status is True, Increments __channel by -1, if __channel is at the MIN_CHANNEL values when channel_down is called __channel becomes the MAX_CHANNEL value
        :return:
        '''
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        If __status is True, sets __muted to false and Increments __volume by 1 if __volume is not at the MAX_VOLUME value
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume != Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = Television.MAX_VOLUME

    def volume_down(self) -> None:
        '''
        If __status is True, sets __muted to false and Increments __volume by -1 if __volume is not at the MAX_VOLUME value
        :return:
        '''
        if self.__status:
            self.__muted = False
            if self.__volume != Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                self.__volume = Television.MIN_VOLUME

    def __str__(self) -> str:
        '''
        returns the attributes of the Television object inside a string and is called whenever the object is put inside a print function
        :return: Television object in string form
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {0}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
