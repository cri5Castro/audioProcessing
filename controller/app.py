import sys
import ast
import argparse
import wavio
from collections import OrderedDict
from controller.plot import plotter
from controller import operators

def plot(options):
    kwargs={f'{i}': wavio.read(i).data for i in options.files}
    plotter.plot(**kwargs)
    
def interpolate(options):
    signal=wavio.read(options.ipath)
    result=operators.interpolate(signal.data,int(options.factor))
    plotter.plot(**{options.ipath:signal.data,options.opath:result})
    wavio.write(options.opath, result, signal.rate, sampwidth=1)

def decimate(options):
    signal=wavio.read(options.ipath)
    result=operators.decimate(signal.data,int(options.factor))
    plotter.plot(**{options.ipath:signal.data,options.opath:result})
    wavio.write(options.opath, result, signal.rate, sampwidth=1)

def shift(options):
    signal=wavio.read(options.ipath)
    result=operators.shift(signal.data,int(options.factor))
    plotter.plot(**{options.ipath:signal.data,options.opath:result})
    wavio.write(options.opath, result, signal.rate, sampwidth=1)

def reflect(options):
    signal=wavio.read(options.ipath)
    result=operators.reflect(signal.data)
    plotter.plot(**{options.ipath:signal.data,options.opath:result})
    wavio.write(options.opath, result, signal.rate, sampwidth=1)
    
def mamplitude(options):
    signal=wavio.read(options.ipath)
    result=operators.mamplitude(signal.data,float(options.factor))
    plotter.plot(**{options.ipath:signal.data,options.opath:result})
    wavio.write(options.opath, result, signal.rate, sampwidth=1)

def run(args):
    #X = {-2:10,-1:-1,0:4,1:2,2:-3,3:6,4:9}
    #X = dict(enumerate(np.sin(range(-10,10))))
    #Y = {-2:2,-1:-4,0:-5} 
    
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()    
    #create a downloa subcommand
    parser_plot = subparsers.add_parser('plot',aliases=["plt","p"],
                                            help='plot a set of discrete signals')
    parser_plot.add_argument('files',nargs='+',help='audio files to be plotted requiers >=1')
    parser_plot.set_defaults(func=plot)
    
    parser_interpolation = subparsers.add_parser('interpolate',aliases=["inp","interp"],
                                            help='interpolate a signal by a factor a')
    parser_interpolation.add_argument('ipath',help='path of the file which contains the signal')
    parser_interpolation.add_argument('factor',help='factor of interpolation')
    parser_interpolation.add_argument('-opath', '-o', help="Path to store the resulted signal",default='output.wav')
    parser_interpolation.add_argument('-plot', '-p', help="plot the resulting signal",default=False)
    parser_interpolation.set_defaults(func=interpolate)


    parser_decimation = subparsers.add_parser('decimate',aliases=["dec","d"],
                                            help='downsample a signal by a factor a')
    parser_decimation.add_argument('ipath',help='path of the file which contains the signal')
    parser_decimation.add_argument('factor',help='factor of downsampling')
    parser_decimation.add_argument('-opath', '-o', help="Path to store the resulted signal",default='output.wav')
    parser_decimation.add_argument('-plot', '-p', help="plot the resulting signal",default=False)
    parser_decimation.set_defaults(func=decimate)

    parser_shift = subparsers.add_parser('shift',aliases=["s","sh"],
                                            help='shifts a signal n times in time')
    parser_shift.add_argument('ipath',help='path of the file which contains the signal')
    parser_shift.add_argument('factor',help='shift amount')
    parser_shift.add_argument('-opath', '-o', help="Path to store the resulted signal",default='output.wav')
    parser_shift.add_argument('-plot', '-p', help="plot the resulting signal",default=False)
    parser_shift.set_defaults(func=shift)
    
    parser_reflect = subparsers.add_parser('reflect',aliases=["r","rf"],
                                            help='reflecrts a signal  in time')
    parser_reflect.add_argument('ipath',help='path of the file which contains the signal')
    parser_reflect.add_argument('-opath', '-o', help="Path to store the resulted signal",default='output.wav')
    parser_reflect.add_argument('-plot', '-p', help="plot the resulting signal",default=False)
    parser_reflect.set_defaults(func=reflect)
    
    parser_mamplitude = subparsers.add_parser('mamplitude',aliases=["ma","mamp"],
                                            help='modifies the amplitude of a signal')
    parser_mamplitude.add_argument('ipath',help='path of the file which contains the signal')
    parser_mamplitude.add_argument('factor',help='amplitude amount')
    parser_mamplitude.add_argument('-opath', '-o', help="Path to store the resulted signal",default='output.wav')
    parser_mamplitude.add_argument('-plot', '-p', help="plot the resulting signal",default=False)
    parser_mamplitude.set_defaults(func=mamplitude)
    


    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
    