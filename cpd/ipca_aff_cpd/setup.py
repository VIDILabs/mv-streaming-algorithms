import glob
from distutils.core import setup
import platform

if platform.system() == "Linux":
    ipca_aff_cpd_so = glob.glob('ipca_aff_cpd')[0]
else:
    ipca_aff_cpd_so = glob.glob('ipca_aff_cpd*.so')[0]

setup(
    name='ipca_aff_cpd',
    version=0.1,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': [ipca_aff_cpd_so]},
    py_modules=['ipca_aff_cpd_cpp', 'ipca_aff_cpd'])
