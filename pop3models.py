"""
Define SNANA CCSN models for sncosmo, using registry.register_loader
to make them accessible for on-the-fly loading.
"""
__author__ = 'rodney'

import sys
import os
from astropy.utils.data import get_pkg_data_filename

from sncosmo import registry
from sncosmo import Source, TimeSeriesSource
from sncosmo import io

def load_timeseries_ascii_local(pkg_data_name, name=None, version=None):
    fname = get_pkg_data_filename(pkg_data_name)
    phase, wave, flux = io.read_griddata_ascii(fname)
    return TimeSeriesSource(phase, wave, flux, name=name, version=version)

# -----------------------------------------------------------------------
# POP III  CC SN models

ref = ('Whalen13', 'Whalen et al. 2013',
       '<http://adsabs.harvard.edu/abs/2013ApJ...768...95W>')
subclass = '`~sncosmo.TimeSeriesSource`'
note = "private communication (D.Whalen to S.Rodney), May 2014."

thisfile = sys.argv[0]
if 'ipython' in thisfile :
    thisfile = __file__
thisdir = os.path.dirname( thisfile )
sedroot = os.path.join( thisdir, 'data/models/' )


registry.register_loader(Source,'z15G',load_timeseries_ascii_local,
								args=[sedroot+'popIII-z15G.sed.restframe10pc.dat'],
                                version='1.0',
								meta={'snid':'z15G','type':'PopIII',
                                      'subclass':subclass,'reference':ref,
                                      'note':note})

registry.register_loader(Source,'z25G',load_timeseries_ascii_local,
								args=[sedroot+'popIII-z25G.sed.restframe10pc.dat'],
                                version='1.0',
								meta={'snid':'z25G','type':'PopIII',
                                      'subclass':subclass,'reference':ref,
                                      'note':note})


registry.register_loader(Source,'z40G',load_timeseries_ascii_local,
								args=[sedroot+'popIII-z40G.sed.restframe10pc.dat'],
                                version='1.0',
								meta={'snid':'z40G','type':'PopIII',
                                      'subclass':subclass,'reference':ref,
                                      'note':note})
