import wavio
import sounddevice as sd


class Struct(object):
    pass


def write(opath, data, rate, sampwidth=1):
    wavio.write(opath, data, rate, sampwidth=sampwidth)


def read(ipath):
    return wavio.read(ipath)


def record(rate=22050, secs=4, store=True, opath='record.wav'):
    recording = Struct()
    recording.data = sd.rec(int(secs * rate), samplerate=rate, channels=2)
    recording.rate = rate
    sd.wait()  # Wait until recording is finished
    if store:
        write(opath, recording.data, rate, sampwidth=2)
    return recording


def play(ipath=None, signal=None):
    if ipath:
        signal = read(ipath)
        sd.play(signal.data, signal.rate)
    elif signal:
        sd.play(signal.data, signal.rate)
