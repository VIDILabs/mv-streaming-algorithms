import glob
from distutils.core import setup
import platform

if len(glob.glob('prog_inc_pca_cpp*.so')) == 0:
    raise ValueError(
        'prog_inc_pca_cpp*.so is not found. You have not finished \
        compiling related cpp hpp files or \'python3-config --extension-suffix\'\
        command does not work properly in your environment')
prog_inc_pca_so = glob.glob('prog_inc_pca_cpp*.so')[0]

setup(
    name='prog_inc_pca',
    version=0.1,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': [prog_inc_pca_so]},
    py_modules=['prog_inc_pca_cpp', 'prog_inc_pca'])
