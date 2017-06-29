# -*- coding:utf-8 -*-
import threading
import time
import pyaudio
import math
import array
import random

class System(threading.Thread):
    def __init__(self,channels,pine = 3.14):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.tempo = 0.5
        self.sounds = []
        self.que = []
        self.channels = channels
        self.pine = pine
        p = pyaudio.PyAudio()
        self.stream = p.open(rate=44100,channels=self.channels,format=pyaudio.paFloat32,output=True)

        #音の止めるとか
        self.stop = True
    def run(self):
        while True:
            if self.stop:
                continue
            if len(self.sounds) == 0:
                continue
            if len(self.sounds) == 1:
                self.play(self.sounds[0])
                #self.play_tone
                continue
            if len(self.sounds) > 1:
                for sound in self.sounds:
                    self.play(sound)

    def soundset(self,x,y = 1):
        self.sounds.append([y,x])

    def settone(self,x):
        if x==60:
            self.sounds.append([1,100])
        elif x==61:
            self.sounds.append([1,108])
        elif x==62:
            self.sounds.append([1,116])
        elif x==63:
            self.sounds.append([1,124])
        elif x==64:
            self.sounds.append([1,132])
        elif x==65:
            self.sounds.append([1,140])
        elif x==66:
            self.sounds.append([1,148])
        elif x==67:
            self.sounds.append([1,156])
        elif x==68:
            self.sounds.append([1,164])
        elif x==69:
            self.sounds.append([1,172])
        elif x==70:
            self.sounds.append([1,180])
        elif x==71:
            self.sounds.append([1,188])
        elif x==72:
            self.sounds.append([1,196])
    def removes(self):
        self.sounds = []

    def sine(frequency, length, rate):
        length = int(length * rate)
        factor = float(frequency) * (math.pi * 2) / rate
        return numpy.sin(numpy.arange(length) * factor)

    #オーディオ鳴らす
    def play_tone(self, frequency=440, length=1, rate=44100):
        chunks = []
        chunks.append(self.sine(frequency, length, rate))
        chunk = numpy.concatenate(chunks) * 0.25
        self.stream.write(chunk.astype(numpy.float32).tostring())





    def play(self,sound):
        self.stream.write(self.tone(sound[0],sound[1],sec=self.tempo))

    def tone(self,val,freq,sec=0.01,velocity=.2,rate=44100):
        w = rate / freq
        def gen():
            if val == 0:
                time.sleep(freq * self.tempo)
            for  i in range(int(rate * sec)):
                if val == 1 : yield math.sin(float(i % w) / w * 10. * self.pine) * velocity
                if val == 2 : yield math.tan(float(i % w) / w * 10. * self.pine) * velocity
                if val == 3 : yield math.log(float(i % w) / w * 10. * self.pine + 0.1) * velocity
                if val == 4 : yield random.uniform(0,float(i % w) /w * 10. * self.pine) * velocity
        return array.array('f',gen()).tostring()