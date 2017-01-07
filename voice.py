from pocketsphinx import LiveSpeech, get_model_path, get_data_path
modeldir = 'models/'
datadir = get_data_path()
includedir = 'include/'
SOUND_DIR = 'sounds/'
CONFIG_FILE = 'config.conf'

import sys, os
sys.path.append(os.path.join(includedir))
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
import pyaudio
from include.WindowsInput import *

def setup():
    global config, conf_speak
    config = Decoder.default_config()
    config.set_string('-hmm', os.path.join(modeldir, 'en-us'))
    config.set_string('-dict', os.path.join(modeldir, 'cmudict-en-us.dict'))
    config.set_string('-kws', 'numbers.conf')
    config.set_string('-logfn', 'nul')
    #config.set_string('-keyphrase', 'r')
    #config.set_float('-kws_threshold', 1e-10)
    conf_speak = True
    try:
        conf = open(CONFIG_FILE, 'r')
        conf_speak = True if conf.readline().split("=")[1].replace(" ","") == "true" else False  # speak
    except IOError:
        print "'{}' does not exist. Using default setting".format(CONFIG_FILE)
    

def start_recognition():
    print "starting up environment for recognition. Please wait."
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()
    # Process audio chunk by chunk. On keyword detected perform action and restart search
    decoder = Decoder(config)

    print "program loaded."
    playsound(SOUND_DIR + 'alert.wav', False)
    print "starting voice recognition. say: [one, two, three, four, five, ignite]"
    decoder.start_utt()
    while True:
        buf = stream.read(1024)
        if buf:
             decoder.process_raw(buf, False, False)
        else:
             break
        if decoder.hyp() != None:
            res = [(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()]
            #print res
            processVoice(res[0][0])
            decoder.end_utt()
            decoder.start_utt()

def processVoice(key):
    print key
    pressed = key.replace(" ", "")
    pressthis = DIK_Q
    
    if pressed == "one":
        pressthis = DIK_Q
    elif pressed == "two":
        pressthis = DIK_W
    elif pressed == "three":
        pressthis = DIK_E
    elif pressed == "four":
        pressthis = DIK_R
    elif pressed == "five":
        pressthis = DIK_D
    elif pressed == "ignite":
        pressthis = DIK_F
    else:
        print "something else other than expected words was recognized. word: {}".format(pressed)
    time.sleep(0.001)
    pressKey(pressthis)
    time.sleep(0.005)
    releaseKey(pressthis)
    if conf_speak:
        playSound(pressthis)

def playSound(key):
    if key == DIK_Q:
        playsound(SOUND_DIR + 'q.mp3', False)
    if key == DIK_W:
        playsound(SOUND_DIR + 'w.mp3', False)
    if key == DIK_E:
        playsound(SOUND_DIR + 'e.mp3', False)
    if key == DIK_R:
        playsound(SOUND_DIR + 'r.mp3', False)
    if key == DIK_D:
        playsound(SOUND_DIR + 'd.mp3', False)
    if key == DIK_F:
        playsound(SOUND_DIR + 'f.mp3', False)

if __name__ == "__main__":
    setup()
    start_recognition()
