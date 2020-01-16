import glob
from distutils.core import setup
import platform

if platform.system() == "Linux":
    prog_inc_pca_so = glob.glob('prog_inc_pca_cpp')[0]
else:
    prog_inc_pca_so = glob.glob('prog_inc_pca_cpp*.so')[0]

setup(
    name='prog_inc_pca',
    version=0.1,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': [prog_inc_pca_so]},
    py_modules=['prog_inc_pca_cpp', 'prog_inc_pca'])
