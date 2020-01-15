#include "label_reassignment.hpp"

// #include <pybind11/eigen.h>
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(label_reassignment_cpp, m) {
  m.doc() = "xxx";
  py::class_<LabelReassignment>(m, "LabelReassignment")
      .def("consistent_labels", &LabelReassignment::consistentLabels)
      .def("random_order_from_each_cluster",
           &LabelReassignment::randomOrderFromEachCluster);
}
