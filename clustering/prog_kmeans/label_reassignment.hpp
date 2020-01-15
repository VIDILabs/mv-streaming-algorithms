#include <map>
#include <utility>
#include <vector>

class LabelReassignment {
public:
  static std::pair<std::vector<unsigned int>,
                   std::map<unsigned int, unsigned int>>
  consistentLabels(unsigned int k, std::vector<unsigned int> const &prevLabels,
                   std::vector<unsigned int> const &currLabels,
                   unsigned int const latencyLimitInMSec = 1000,
                   bool const verbose = false);

  static std::vector<unsigned int> randomOrder(unsigned int const n);

  static std::vector<unsigned int>
  randomOrderFromEachCluster(unsigned int const n,
                             std::vector<unsigned int> const &labels);
};
