#include "prog_inc_pca.hpp"

#include <pybind11/eigen.h>
#include <pybind11/functional.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

PYBIND11_MODULE(prog_inc_pca_cpp, m) {
  m.doc() = "Progressive Incremental PCA wrapped with pybind11";
  py::class_<ProgIncPCA>(m, "ProgIncPCA")
      .def(py::init<Eigen::Index const, double const>())
      .def("initialize", &ProgIncPCA::initialize)
      .def("transform", &ProgIncPCA::transform)
      .def("progressive_fit", &ProgIncPCA::progressiveFit)
      .def("partial_fit", &ProgIncPCA::partialFit)
      .def("get_loadings", &ProgIncPCA::getLoadings)
      .def("geom_trans", &ProgIncPCA::geomTrans)
      .def("pos_est", &ProgIncPCA::posEst)
      .def("get_uncert_v", &ProgIncPCA::getUncertV)
      .def("update_uncert_weight", &ProgIncPCA::updateUncertWeight)
      .def("get_n_processed", &ProgIncPCA::getNProcessed);
}
