"""
Define HST WFC3 and ACS bandpasses for sncosmo, using registry.register_loader
to make them accessible for on-the-fly loading.
"""
__author__ = 'rodney'
from astropy import units as u
from astropy.utils.data import get_pkg_data_filename

from sncosmo import registry
from sncosmo.spectral import Bandpass, read_bandpass

def load_bandpass(pkg_data_name, name=None):
    fname = get_pkg_data_filename(pkg_data_name)
    return read_bandpass(fname, wave_unit=u.AA, name=name)

# --------------------------------------------------------------------------
# HST WFC3-IR
wfc3ir_meta = {'filterset': 'wfc3-ir',
            'dataurl': ('http://www.stsci.edu/hst/wfc3/ins_performance/throughputs/Throughput_Tables'
                        'wfc3ir'),
            'retrieved': '05 Aug 2014',
            'description': 'Hubble Space Telescope WFC3 IR filters'}
registry.register_loader(Bandpass, 'f098m', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f098m.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f105w', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f105w.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f110w', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f110w.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f125w', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f125w.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f127m', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f127m.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f139m', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f139m.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f140w', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f140w.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f153m', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f153m.dat'], meta=wfc3ir_meta)
registry.register_loader(Bandpass, 'f160w', load_bandpass, args=['data/bandpasses/hst_wfc3_ir_f160w.dat'], meta=wfc3ir_meta)

del wfc3ir_meta

# --------------------------------------------------------------------------
# HST WFC3-UVIS
wfc3uvis_meta = {'filterset': 'wfc3-uvis',
            'dataurl': ('http://www.stsci.edu/hst/wfc3/ins_performance/throughputs/Throughput_Tables'
                        'wfc3uvis'),
            'retrieved': '05 Aug 2014',
            'description': 'Hubble Space Telescope WFC3 UVIS filters'}
registry.register_loader(Bandpass, 'f218w', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f218w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f225w', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f225w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f275w', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f275w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f300x', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f300x.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f336w', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f336w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f350lp',load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f350lp.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f390w', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f390w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f689m', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f689m.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f763m', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f763m.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f845m', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f845m.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'f438w', load_bandpass, args=['data/bandpasses/hst_wfc3_uvis_f438w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf475w',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f475w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf555w',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f555w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf606w',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f606w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf625w',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f625w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf775w',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f775w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf814w',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f814w.dat'], meta=wfc3uvis_meta)
registry.register_loader(Bandpass, 'uvf850lp',load_bandpass,args=['data/bandpasses/hst_wfc3_uvis_f850lp.dat'], meta=wfc3uvis_meta)

del wfc3uvis_meta

# --------------------------------------------------------------------------
# HST ACS
acs_meta = {'filterset': 'acs',
            'dataurl': ('http://www.stsci.edu/hst/acs/analysis/throughputs'
                        'acs'),
            'retrieved': '05 Aug 2014',
            'description': 'Hubble Space Telescope ACS WFC filters'}
registry.register_loader(Bandpass, 'f435w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f435w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f475w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f475w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f555w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f555w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f606w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f606w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f625w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f625w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f775w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f775w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f814w', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f814w.dat'], meta=acs_meta)
registry.register_loader(Bandpass, 'f850lp', load_bandpass, args=['data/bandpasses/hst_acs_wfc_f850lp.dat'],meta=acs_meta)

del acs_meta