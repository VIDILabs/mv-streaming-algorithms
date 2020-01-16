## C++ Library and Python Module for Progressive MiniBatchKMeans for Visualization with Streaming time-series clustering

Progressive version of https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html.
This algorithm is introduced in Kesavan et al., "A Visual Analytics Framework for Reviewing Streaming Performance Data", 2020.
Note: For C++, currently, we only support the label reassignment introduced.

-----

Requirements
-----
* C++11 compiler, Python3, Pybind11, Numpy

* Note: Tested on macOS Mojave and Ubuntu 18.0.4 LTS.

Setup
-----
#### Mac OS with Homebrew
* Install libraries

    `brew install python3`

    `brew install pybind11`

    `pip3 install numpy`

* Build with cmake

    `mv /path/to/directory-of-CmakeLists.txt`

    `cmake .`

    `make`

* This generates a shared library, "label_reassignment_cpp.xxxx.so" (e.g., label_reassignment_cpp.cpython-37m-darwin.so).

* Install the modules (label_reassignment, prog_kmeans) with pip3.

    `pip3 install .`

* If you want to run sample.py in this directory. You need to install additional libraries.

    `pip3 install matplotlib`

    `pip3 install pandas`

#### Linux (tested on Ubuntu 18.0.4 LTS)
* Install libraries

    `sudo apt update`

    `sudo apt install python3-pip python3-dev`

    `pip3 install pybind11`

    `pip3 install numpy`

* Move to 'prog_kmeans' directory then compile with:

    ``c++ -O3 -Wall -mtune=native -march=native -shared -std=c++11 -I../core/ -fPIC `python3 -m pybind11 --includes` label_reassignment.cpp label_reassignment_wrap.cpp -o label_reassignment_cpp`python3-config --extension-suffix` ``

* This generates a shared library, "label_reassignment_cpp.xxxx.so" (e.g., label_reassignment_cpp.cpython-37m-x86_64-linux-gnu.so).

* Install the modules (label_reassignment, prog_kmeans)  with pip3.

    `pip3 install .`

* If you want to run sample.py in this directory. You need to install additional libraries.

    `sudo apt install python3-tk`

    `pip3 install matplotlib`

    `pip3 install pandas`

Usage
-----
* Place prog_kmeans_cpp.xxxx.so and prog_kmeans.py in the same directory.

* Import "prog_kmeans" from python. See prog_kmeans.py or docs/index.html for detailed usage examples.

Usage
-----
* With Python3
    * Import the installed module from python (e.g., `from prog_kmeans import ProgKMeans`). See sample.py for examples.

* With C++
    * Currently, we only support our label reassignment. Include header files (label_reassignment.hpp) in C++ code with cpp files (label_reassignment.cpp).

******

## How to Cite
Please, cite:    
Suraj P. Kesavan, Takanori Fujiwara, Jianping Kelvin Li, Caitlin Ross, Misbah Mubarak, Christopher D. Carothers, Robert B. Ross, and Kwan-Liu Ma, "A Visual Analytics Framework for Reviewing Streaming Performance Data".
In Proceedings of of IEEE Pacific Visualization Symposium (PacificVis), forthcoming.
