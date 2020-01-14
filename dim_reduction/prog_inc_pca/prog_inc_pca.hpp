#ifndef ProgIncPCA_HPP
#define ProgIncPCA_HPP

#include "inc_pca.hpp"

class ProgIncPCA : public IncPCA {
public:
  ProgIncPCA(Eigen::Index const nComponents = 2,
             double const forgettingFactor = 1.0);
  void progressiveFit(Eigen::MatrixXd const &X,
                      unsigned int const latencyLimitInMSec = 1000,
                      std::string pointChoiceMethod = "random",
                      bool const verbose = false);
  int getNProcessed(){ return nProcessed; }

private:
  int nProcessed = 0;
  static std::vector<unsigned int> randomOrder(unsigned int const n);
  static void shuffleMatrix2D(Eigen::MatrixX2d &X1, Eigen::MatrixX2d &X2);
};

#endif // ProgIncPCA_HPP
