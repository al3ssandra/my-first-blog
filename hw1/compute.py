import os, time, glob
import numpy
import control
from scipy import signal
from control.matlab import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def compute(R, L, Km, b, J, P):

    print os.getcwd()
    A = numpy.matrix([[-b/J, Km/J], [-Km/L, -R/L]])
    B = numpy.matrix([[0, 1/J], [1/L, 0]])
    C = numpy.matrix([1.0, 0])
    D = numpy.matrix([0.0, 0.0])
    Aa = numpy.concatenate((numpy.column_stack((A, numpy.zeros((2, 1)))), numpy.column_stack((-C, 0))))
    Ba = numpy.concatenate((B, numpy.zeros((1, 2))))
    K = signal.place_poles(Aa, Ba, P)
    K = K.gain_matrix
    Acont = Aa - Ba*K
    Bcont = numpy.array([0, 0, 1.0])
    Bcont.shape = (3, 1)
    Ccont = [1.0, 0, 0]
    dcm_cont = ss(Acont, Bcont, Ccont, 0)
    T, yout = control.step_response(dcm_cont, T=None)
    fig = Figure()
    FigureCanvas(fig)
    ax = fig.add_subplot(1, 1, 1)

    ax.plot(T.T, yout.T)
    #if not os.path.isdir('static'):
        #os.mkdir('static')
    #else:
    for filename in glob.glob(os.path.join('C:\Users\Alessandra\Desktop\dcmotor\dcmotor\static', '*.png')):
            os.remove(filename)

    plotfile = os.path.join('C:\Users\Alessandra\Desktop\dcmotor\dcmotor\static', str(time.time()) + '.png')
    fig.savefig(plotfile)
    return plotfile

if __name__ == '__main__':
    print compute(1, 0.5, 0.01, 0.1, 0.01, [-1, -2, -3])