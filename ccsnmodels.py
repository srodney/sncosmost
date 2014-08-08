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
# SNANA CC SN models

ref = ('SNANA', 'Kessler et al. 2009',
       '<http://adsabs.harvard.edu/abs/2009PASP..121.1028K>')
website = 'http://das.sdss2.org/ge/sample/sdsssn/SNANA-PUBLIC/'
subclass = '`~sncosmo.TimeSeriesSource`'
note = "extracted from SNANA's SNDATA_ROOT on 5 August 2014."

thisfile = sys.argv[0]
if 'ipython' in thisfile :
    thisfile = __file__
thisdir = os.path.dirname( thisfile )
sedroot = os.path.join( thisdir, 'data/models/' )


registry.register_loader(Source,'Ic.01',load_timeseries_ascii_local,
								args=[sedroot+'CSP-2004fe.SED'],version='1.0',
								meta={'url':website,'snid':'CSP-2004fe','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.02',load_timeseries_ascii_local,
								args=[sedroot+'CSP-2004gq.SED'],version='1.0',
								meta={'url':website,'snid':'CSP-2004gq','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.03',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-004012.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-004012','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.04',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-013195.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-013195','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.05',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-014475.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-014475','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.06',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-015475.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-015475','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.07',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-017548.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-017548','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.08',load_timeseries_ascii_local,
								args=[sedroot+'SNLS-04D1la.SED'],version='1.0',
								meta={'url':website,'snid':'SNLS-04D1la','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ic.09',load_timeseries_ascii_local,
								args=[sedroot+'SNLS-04D4jv.SED'],version='1.0',
								meta={'url':website,'snid':'SNLS-04D4jv','type':'Ic',
										'subclass':subclass,'reference':ref,
										'note':note})

registry.register_loader(Source,'Ib.01',load_timeseries_ascii_local,
								args=[sedroot+'CSP-2004gv.SED'],version='1.0',
								meta={'url':website,'snid':'CSP-2004gv','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ib.02',load_timeseries_ascii_local,
								args=[sedroot+'CSP-2006ep.SED'],version='1.0',
								meta={'url':website,'snid':'CSP-2006ep','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ib.03',load_timeseries_ascii_local,
								args=[sedroot+'CSP-2007Y.SED'],version='1.0',
								meta={'url':website,'snid':'CSP-2007Y','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ib.04',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-000020.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-000020','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ib.05',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-002744.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-002744','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ib.06',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-014492.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-014492','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'Ib.07',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-019323.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-019323','type':'Ib',
										'subclass':subclass,'reference':ref,
										'note':note})

registry.register_loader(Source,'IIP.01',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-000018.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-000018','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.02',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-003818.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-003818','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.03',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-013376.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-013376','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.04',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-014450.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-014450','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.05',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-014599.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-014599','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.06',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-015031.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-015031','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.07',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-015320.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-015320','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.08',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-015339.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-015339','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.09',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-017564.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-017564','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.10',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-017862.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-017862','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.11',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018109.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018109','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.12',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018297.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018297','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.13',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018408.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018408','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.14',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018441.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018441','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.15',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018457.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018457','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.16',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018590.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018590','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.17',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018596.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018596','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.18',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018700.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018700','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.19',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018713.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018713','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.20',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018734.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018734','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.21',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018793.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018793','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.22',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018834.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018834','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.23',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-018892.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-018892','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIP.24',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-020038.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-020038','type':'IIP',
										'subclass':subclass,'reference':ref,
										'note':note})

registry.register_loader(Source,'IIn.01',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-012842.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-012842','type':'IIN',
										'subclass':subclass,'reference':ref,
										'note':note})
registry.register_loader(Source,'IIn.02',load_timeseries_ascii_local,
								args=[sedroot+'SDSS-013449.SED'],version='1.0',
								meta={'url':website,'snid':'SDSS-013449','type':'IIN',
										'subclass':subclass,'reference':ref,
										'note':note})

