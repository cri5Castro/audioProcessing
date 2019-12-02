import sys
import ast
import argparse
from collections import OrderedDict
from controller.plot import plotter
import controller.operators.math as op
import controller.operators.audio as audio


def plot(options):
    """plots signals from option.files

    Arguments:
        options.files {array} -- [contains the files where the signals comes from]
    """
    kwargs = {f'{i}': audio.read(i).data for i in options.files}
    plotter.plot(**kwargs)


def interpolate(options):
    """[interpolates a signal by a factor options.factor]

    Arguments:
        options.factor {string}  -- [factor of interpolation]
        options.ipath  {string}  -- [path to the input signal]
        options.opath  {string}  -- [path for the output signal]
        options.plot   {boolean} -- [option to plot the signals]
    """
    signal = audio.read(options.ipath)
    result = op.interpolate(signal.data, int(options.factor))
    audio.write(options.opath, result, signal.rate, sampwidth=1)
    if options.plot:
        plotter.plot(**{options.ipath: signal.data, options.opath: result})


def decimate(options):
    """[downsample a signal by a factor options.factor]

    Arguments:
        options.factor {string}  -- [factor of interpolation]
        options.ipath  {string}  -- [path to the input signal]
        options.opath  {string}  -- [path for the output signal]
        options.plot   {boolean} -- [option to plot the signals]
    """
    signal = audio.read(options.ipath)
    result = op.decimate(signal.data, int(options.factor))
    audio.write(options.opath, result, signal.rate, sampwidth=1)
    if options.plot:
        plotter.plot(**{options.ipath: signal.data, options.opath: result})


def shift(options):
    """[shift a signal in time ]

    Arguments:
        options.factor {string}  -- [factor of interpolation]
        options.ipath  {string}  -- [path to the input signal]
        options.opath  {string}  -- [path for the output signal]
        options.plot   {boolean} -- [option to plot the signals]
    """
    signal = audio.read(options.ipath)
    result = op.shift(signal.data, int(options.factor))
    audio.write(options.opath, result, signal.rate, sampwidth=1)
    if options.plot:
        plotter.plot(**{options.ipath: signal.data, options.opath: result})


def reflect(options):
    """[reflect the signal in time]

    Arguments:
        options.ipath  {string}  -- [path to the input signal]
        options.opath  {string}  -- [path for the output signal]
        options.plot   {boolean} -- [option to plot the signals]
    """
    signal = audio.read(options.ipath)
    result = op.reflect(signal.data)
    audio.write(options.opath, result, signal.rate, sampwidth=1)
    if options.plot:
        plotter.plot(**{options.ipath: signal.data, options.opath: result})


def mamplitude(options):
    """[modifies the amplitude of a signal]

    Arguments:
        options.factor {string}  -- [factor of interpolation]
        options.ipath  {string}  -- [path to the input signal]
        options.opath  {string}  -- [path for the output signal]
        options.plot   {boolean} -- [option to plot the signals]
    """
    signal = audio.read(options.ipath)
    result = op.mamplitude(signal.data, float(options.factor))
    audio.write(options.opath, result, signal.rate, sampwidth=1)
    if options.plot:
        plotter.plot(**{options.ipath: signal.data, options.opath: result})


def record(options):
    """records audio from computer's built in mic

    Keyword Arguments:
        options.secs {int} -- [seconds to record (segs)] (default: {4})
        options.opath {str} -- [output path] (default: {'record.wav'})
        options.plot   {boolean} -- [option to plot the signals]
    """
    signal = audio.record(rate=22050, secs=options.secs,
                          store=True, opath=options.opath)
    if options.plot:
        plotter.plot(**{options.opath: signal.data})


def guiMode(options):
    """[Launches a gui to perfom operations over audio signals]

    Arguments:
        options {[type]} -- [description]
    """
    pass


def run(args):
    """[parse arguments from shell to perfom the desired operations]

    Arguments:
        args -- [arguments]
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
    # create a plot subcommand
    parser_plot = subparsers.add_parser('plot', aliases=["plt", "p"],
                                        help='plot a set of discrete signals')
    parser_plot.add_argument(
        'files', nargs='+', help='audio files to be plotted requiers >=1')
    parser_plot.set_defaults(func=plot)

    # create a interpolation subcommand
    parser_interpolation = subparsers.add_parser('interpolate', aliases=["inp", "interp"],
                                                 help='interpolate a signal by a factor a')
    parser_interpolation.add_argument(
        'ipath', help='path of the file which contains the signal')
    parser_interpolation.add_argument('factor', help='factor of interpolation')
    parser_interpolation.add_argument(
        '-opath', '-o', help="Path to store the resulted signal", default='output.wav')
    parser_interpolation.add_argument(
        '-plot', '-p', help="plot the resulting signal", default=False)
    parser_interpolation.set_defaults(func=interpolate)

    # create a decimation subcommand
    parser_decimation = subparsers.add_parser('decimate', aliases=["dec", "d"],
                                              help='downsample a signal by a factor a')
    parser_decimation.add_argument(
        'ipath', help='path of the file which contains the signal')
    parser_decimation.add_argument('factor', help='factor of downsampling')
    parser_decimation.add_argument(
        '-opath', '-o', help="Path to store the resulted signal", default='output.wav')
    parser_decimation.add_argument(
        '-plot', '-p', help="plot the resulting signal", default=False)
    parser_decimation.set_defaults(func=decimate)

    # create a shift subcommand
    parser_shift = subparsers.add_parser('shift', aliases=["s", "sh"],
                                         help='shifts a signal n times in time')
    parser_shift.add_argument(
        'ipath', help='path of the file which contains the signal')
    parser_shift.add_argument('factor', help='shift amount')
    parser_shift.add_argument(
        '-opath', '-o', help="Path to store the resulted signal", default='output.wav')
    parser_shift.add_argument(
        '-plot', '-p', help="plot the resulting signal", default=False)
    parser_shift.set_defaults(func=shift)

    # create a reflect subcommand
    parser_reflect = subparsers.add_parser('reflect', aliases=["r", "rf"],
                                           help='reflecrts a signal  in time')
    parser_reflect.add_argument(
        'ipath', help='path of the file which contains the signal')
    parser_reflect.add_argument(
        '-opath', '-o', help="Path to store the resulted signal", default='output.wav')
    parser_reflect.add_argument(
        '-plot', '-p', help="plot the resulting signal", default=False)
    parser_reflect.set_defaults(func=reflect)

    # create a mamplitude subcommand
    parser_mamplitude = subparsers.add_parser('mamplitude', aliases=["ma", "mamp"],
                                              help='modifies the amplitude of a signal')
    parser_mamplitude.add_argument(
        'ipath', help='path of the file which contains the signal')
    parser_mamplitude.add_argument('factor', help='amplitude amount')
    parser_mamplitude.add_argument(
        '-opath', '-o', help="Path to store the resulted signal", default='output.wav')
    parser_mamplitude.add_argument(
        '-plot', '-p', help="plot the resulting signal", default=False)
    parser_mamplitude.set_defaults(func=mamplitude)

    # create a record subcommand
    parser_record = subparsers.add_parser('record', aliases=["rec", "r"],
                                          help='records audio from computer\'s built in mic')
    parser_record.add_argument(
        '-opath', '-o', help="Path to store the resulted signal", default='record.wav')
    parser_record.add_argument(
        '-secs', '-s', help="seconds of audio to be recorded", default=4)
    parser_record.add_argument(
        '-plot', '-p', help="plot the resulting signal", default=False)
    parser_record.set_defaults(func=record)

    # create a gui subcommand
    parser_gui = subparsers.add_parser('gui', aliases=["g", "interface"],
                                       help='launches the program in gui mode')
    parser_gui.set_defaults(func=guiMode)

    # parse arguments from shell
    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
