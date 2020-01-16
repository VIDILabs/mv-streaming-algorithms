import glob
from distutils.core import setup
import platform

if len(glob.glob('label_reassignment*.so')) == 0:
    raise ValueError(
        'label_reassignment_cpp*.so is not found. You have not finished \
        compiling related cpp hpp files or \'python3-config --extension-suffix\'\
        command does not work properly in your environment')
label_reassignment_so = glob.glob('label_reassignment*.so')[0]

setup(
    name='prog_kmeans',
    version=0.1,
    packages=[''],
    package_dir={'': '.'},
    package_data={'': [label_reassignment_so]},
    py_modules=['label_reassignment_cpp', 'prog_kmeans'])
