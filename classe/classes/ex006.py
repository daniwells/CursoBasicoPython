class tv:
    def __init__(self, channel, volume):
        if 0 < channel < 401:
            self.channel = channel
        else:
            raise Exception('ERROR! This channel does not exist.')

        if 0 < volume < 101:
            self.volume = volume
        else:
            raise Exception("ERROR! The volume don't arrives beyond this it.")

    def change_channel(self, new_channel):
        if 0 < new_channel < 401:
            self.channel = new_channel
        else:
            print('ERROR! This channel does not exist.')
            exit()

    def increase_volume(self, new_volume):
        if 0 < new_volume < 101:
            result = self.volume + new_volume
            if result > 100:
                self.volume = 100
            else:
                self.volume = result
        else:
            self.volume = 100

    def decrease_volume(self, new_volume):
        if 0 < new_volume < 101:
            result = self.volume - new_volume
            if result < 1:
                self.volume = 0
            else:
                self.volume = result
        else:
            self.volume = 0


viewer = tv(1, 100)
print(f'Start channel: {viewer.channel}')
print(f'Start volume: {viewer.volume}')

viewer.change_channel(344)
print(f'Changing of channel for: {viewer.channel}')
viewer.increase_volume(102)
print(f'Increasing volume for: {viewer.volume}')
viewer.decrease_volume(66)
print(f'decreasing volume for: {viewer.volume}')