## C++ Library and Python Module for Progressive Usage of Incremental PCA for Streaming Multidimensional Data

This algorithm provides progressive usage of incremental PCA for visualizing streaming multidimensional data from Fujiwara et al., "An Incremental Dimensionality Reduction Method for Visualizing Streaming Multidimensional Data", 2020.
For more details, please refer to Kesavan et al., "A Visual Analytics Framework for Reviewing Streaming Performance Data", 2020.

-----

Requirements
-----
* C++11 compiler, Python3, Eigen3, Pybind11, Numpy

* Note: Tested on macOS Mojave and Ubuntu 18.0.4 LTS.

Setup
-----
#### Mac OS with Homebrew
* Install libraries

    `brew install python3`

    `brew install eigen`

    `brew install pybind11`

    `pip3 install numpy`

* Modify CMakeLists.txt based on your Python3 and Eigen include directory paths.

* Build with cmake

    `mv /path/to/directory-of-CmakeLists.txt`

    `cmake .`

    `make`

* This generates a shared library, "prog_inc_pca_cpp.xxxx.so" (e.g., prog_inc_pca_cpp.cpython-37m-darwin.so).

* Install the modules with pip3.

    `pip3 install .`

* If you want to run sample.py in this directory. You need to install additional libraries.

    `pip3 install matplotlib`

    `pip3 install sklearn`

#### Linux (tested on Ubuntu 18.0.4 LTS)
* Install libraries

    `sudo apt update`

    `sudo apt install libeigen3-dev`

    `sudo apt install python3-pip python3-dev`

    `pip3 install pybind11`

    `pip3 install numpy`

* Move to 'inc_pca' directory then compile with:

    ``c++ -O3 -Wall -mtune=native -march=native -shared -std=c++11 -I../inc_pca/ -I/usr/include/eigen3/ -fPIC `python3 -m pybind11 --includes` ../streaming-vis-pca/inc_pca.cpp prog_inc_pca.cpp prog_inc_pca_wrap.cpp -o prog_inc_pca_cpp`python3-config --extension-suffix` ``

* This generates a shared library, "prog_inc_pca_cpp.xxxx.so" (e.g., prog_inc_pca_cpp.cpython-37m-x86_64-linux-gnu.so).

* Install the modules with pip3.

    `pip3 install .`

* If you want to run sample.py in this directory. You need to install additional libraries.

    `sudo apt install python3-tk`

    `pip3 install matplotlib`

    `pip3 install sklearn`

Usage
-----
* With Python3
    * Import the installed module from python (e.g., `from prog_inc_pca import ProgIncPCA`). See sample.py for examples.

* With C++
    * Include header files (prog_inc_pca.hpp, inc_pca.hpp in ../streaming-vis-pca/) in C++ code with cpp files (prog_inc_pca.cpp, inc_pca.cpp in ../streaming-vis-pca/).

******

## How to Cite
Please, cite:    
Suraj P. Kesavan, Takanori Fujiwara, Jianping Kelvin Li, Caitlin Ross, Misbah Mubarak, Christopher D. Carothers, Robert B. Ross, and Kwan-Liu Ma, "A Visual Analytics Framework for Reviewing Streaming Performance Data".
In Proceedings of of IEEE Pacific Visualization Symposium (PacificVis), forthcoming.
