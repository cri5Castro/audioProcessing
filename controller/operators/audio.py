import wavio
import sounddevice as sd


class Struct(object):
    """[helper object to give structure for a signal]
    """
    pass


def write(opath, data, rate, sampwidth=1):
    """writes a signal into a wav file

    Arguments:
        opath {str} -- [desired output path]
        data {numpy array} -- [discrete signal]
        rate {int} -- [rate of sampling]

    Keyword Arguments:
        sampwidth {int} -- [the sample witdth in bytes of the output file] (default: {1})
    """
    wavio.write(opath, data, rate, sampwidth=sampwidth)


def read(ipath):
    """[reads a discrete signal from a file]

    Arguments:
        ipath {str} -- [input path]

    Returns:
        discrete signal
    """
    return wavio.read(ipath)


def record(rate=22050, secs=4, store=True, opath='record.wav'):
    """records audio from computer's built in mic

    Keyword Arguments:
        rate {int} -- [rate of sampling] (default: {22050})
        secs {int} -- [seconds to record (segs)] (default: {4})
        store {bool} -- [option to store the audio in a file] (default: {True})
        opath {str} -- [output path] (default: {'record.wav'})

    Returns:
        [discrete signal]
    """
    recording = Struct()
    recording.data = sd.rec(int(secs * rate), samplerate=rate, channels=1)
    recording.rate = rate
    sd.wait()  # Wait until recording is finished
    if store:
        write(opath, recording.data, rate, sampwidth=2)
    return recording


def play(ipath=None, signal=None):
    """[plays a signal]

    Keyword Arguments:
        ipath {[str]} -- [input path in case to play from file] (default: {None})
        signal -- [discrete signal] (default: {None})
    """
    if ipath:
        signal = read(ipath)
        sd.play(signal.data, signal.rate)
        sd.wait()
    elif signal:
        sd.play(signal.data, signal.rate)
        sd.wait()
