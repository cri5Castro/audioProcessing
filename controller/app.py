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
    pass
def shift(options):
    pass
def reflect(options):
    pass
def mamplitude(options):
    pass
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



    if len(sys.argv) <= 1:
        sys.argv.append('--help')
    options = parser.parse_args()
    options.func(options)
    