#!ipython --pylab=auto
# encoding: utf-8

from misc import make_scatter_plot

if __name__ == '__main__':
    y = [0.0,
         61.4297108491, 72.1442781861,
         100.915187162, 109.379857035,
         106.270953816, 153.977321788,
         118.491363082, 194.919935486,
         215.845575586, 238.882391304]
    x = [0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

    make_scatter_plot(u'椒盐噪声参数', x,
                      u'与原图的距离', y,
                      '../images/speckle_gs0.png')


