#coding:utf-8
#Last Change: 2013_11_15_12:42:13.

# -*- coding: utf-8 -*-
import pygame.midi
import pygame.mixer
import time
import pynoise


pygame.init()
pygame.midi.init()
input_id = pygame.midi.get_default_input_id()
print("input MIDI:%d" % input_id)
i = pygame.midi.Input(input_id)

print ("starting")
print ("full midi_events:[[[status,data1,data2,data3],timestamp],...]")

#piano_60 = pygame.mixer.Sound("piano_short/piano_60.wav")  # サウンドをロード

synth = pynoise.System(1)
synth.stop = False
synth.start()

while True:
    if i.poll():
        midi_events = i.read(10)
        print ('full midi_events' + str(midi_events))
        
        #print (midi_events[0][0][1])
        if midi_events[0][0][0]==144:
            #synth.removes()
            synth.settone(midi_events[0][0][1])
        elif midi_events[0][0][0]==128:
            synth.removes()

        '''
        if midi_events[0][0][1]==60:
            if midi_events[0][0][0]==144:
               #60番の鍵盤が押された
               print('60番の音を再生(鳴らし続ける)')
            elif midi_events[0][0][0]==128:
               #60番の鍵盤が押されなくなった（指が離れた）
               print('60番の音を止める')
        '''
i.close()
pygame.midi.quit()
pygame.quit()
exit()