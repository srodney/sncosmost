"""
Quick test function, checking my version of the SNANA models
against the Sako 2011 versions already used in sncosmo.
"""
__author__ = 'rodney'

import numpy as np
import sncosmo
from . import ccsnmodels
from . import hstbandpasses

def mkmodels( z = 0.5, band='f160w' ):
    snmodel = sncosmo.Model(source='s11-2004hx')
    snmodel.set(z=z,t0=19)
    snmodel.set_source_peakabsmag( -18, 'bessellr', 'vega')

    mymodel = sncosmo.Model(source='iip.01')
    mymodel.set(z=z,t0=0)
    mymodel.set_source_peakabsmag( -18, 'bessellr', 'vega')


    mjdlist = np.arange(-20,80,5)

    snmaglist = snmodel.bandmag( band, 'ab', mjdlist )
    mymaglist = mymodel.bandmag( band, 'ab', mjdlist )
    return( mjdlist, snmaglist, mymaglist )


def mkplot( z=0.5 ):
    from matplotlib import pyplot as pl
    pl.clf()
    for band, color in zip( ['f225w','f475w','f105w','f160w'], ['cyan','green','darkorange','darkred']) :
        mjd, sn, my = mkmodels(z=z, band=band)

        pl.plot( mjd, sn, color=color, marker='o', ls='-', ms=12 )
        pl.plot( mjd, my, color=color, marker='d', ls='-', ms=8 )

        ax = pl.gca()
    ax.set_xlabel('MJD rel to peak')
    ax.set_ylabel('AB mag')
    ax.invert_yaxis()

