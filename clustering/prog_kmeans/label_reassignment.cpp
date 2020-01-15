#include "label_reassignment.hpp"

#include <algorithm>
#include <chrono>
#include <iostream>
#include <set>
#include <unordered_set>

std::pair<std::vector<unsigned int>, std::map<unsigned int, unsigned int>>
LabelReassignment::consistentLabels(unsigned int const k,
                       std::vector<unsigned int> const &prevLabels,
                       std::vector<unsigned int> const &currLabels,
                       unsigned int const latencyLimitInMSec,
                       bool const verbose) {
  auto startTime = std::chrono::steady_clock::now();

  auto n = currLabels.size();
  auto order = randomOrderFromEachCluster(n, currLabels);
  std::map<unsigned int, std::map<unsigned int, unsigned int>> counts;

  std::unordered_set<int> uniqueLabels;
  for (unsigned int i = 0; i < k; ++i) {
    uniqueLabels.insert(i);
  }

  for (auto const &currLabel : uniqueLabels) {
    for (auto const &prevLabel : uniqueLabels) {
      counts[currLabel][prevLabel] = 0;
    }
  }

  // calculate freqency of each prev label for each current label
  auto duration = 0;
  unsigned int noProcessed = 0;
  do {
    auto idx = order[noProcessed];

    auto i = counts.find(currLabels[idx]);
    auto j = i->second.find(prevLabels[idx]);
    j->second++;

    noProcessed++;
    duration = std::chrono::duration_cast<std::chrono::milliseconds>(
                   std::chrono::steady_clock::now() - startTime)
                   .count();
  } while (duration < latencyLimitInMSec && noProcessed < n);

  if (verbose) {
    std::cout << "consistentLabels(): " << noProcessed << " of " << n
              << " data points processed in " << duration << " msec."
              << std::endl;
  }

  // to avoid multiple clusters convert to the same prev label,
  // sort current labels by decending order of total data points
  std::map<unsigned int, unsigned int> totalCounts;
  for (auto const &label : currLabels) {
    auto i = totalCounts.find(label);
    if (i == totalCounts.end()) {
      totalCounts.insert(i, std::make_pair(label, 0));
    } else {
      i->second++;
    }
  }
  for (auto const &label : uniqueLabels) {
    auto i = totalCounts.find(label);
    if (i == totalCounts.end()) {
      totalCounts.insert(i, std::make_pair(label, 0));
    }
  }

  std::vector<std::pair<unsigned int, unsigned int>> labelsCounts;
  labelsCounts.reserve(n);

  for (auto const &keyVal : totalCounts) {
    labelsCounts.push_back(std::make_pair(keyVal.first, keyVal.second));
  }
  std::sort(labelsCounts.begin(), labelsCounts.end(),
            [](const std::pair<unsigned int, unsigned int> &v1,
               const std::pair<unsigned int, unsigned int> &v2) {
              return v1.second > v2.second;
            });

  // make map of current label to the highest frequent prev label
  std::map<unsigned int, unsigned int> currLabelToPrevLabel;
  std::set<unsigned int> alreadyAssignedLabels;
  for (auto const &labelCount : labelsCounts) {
    auto currLabel = labelCount.first;
    unsigned int prevLabel = *uniqueLabels.begin();
    unsigned int max = 0;

    for (auto const &prevLabelCount : counts[currLabel]) {
      auto candPrevLabel = prevLabelCount.first;
      auto count = prevLabelCount.second;
      if (count > max && alreadyAssignedLabels.find(candPrevLabel) ==
                             alreadyAssignedLabels.end()) {
        max = count;
        prevLabel = candPrevLabel;
      }
    }

    uniqueLabels.erase(prevLabel);
    alreadyAssignedLabels.insert(prevLabel);

    currLabelToPrevLabel[currLabel] = prevLabel;
  }

  // generate result
  std::vector<unsigned int> labels;
  labels.reserve(n);

  for (auto const &currLabel : currLabels) {
    labels.push_back(currLabelToPrevLabel[currLabel]);
  }
  return std::make_pair(labels, currLabelToPrevLabel);
}

std::vector<unsigned int> LabelReassignment::randomOrder(unsigned int const n) {
  std::vector<unsigned int> order;
  order.reserve(n);
  for (unsigned int i = 0; i < n; ++i) {
    order.push_back(i);
  }
  std::random_shuffle(order.begin(), order.end());

  return order;
}

std::vector<unsigned int>
LabelReassignment::randomOrderFromEachCluster(unsigned int const n,
                                 std::vector<unsigned int> const &labels) {
  if (labels.size() != n) {
    std::cerr << "# of points != # of cluster labels" << std::endl;
  }

  // collect indices for each cluster
  std::map<int, std::vector<unsigned int>> indicesForEachCluster;
  for (unsigned int i = 0; i < n; ++i) {
    indicesForEachCluster[labels[i]].push_back(i);
  }

  // shuffle indices within each cluster
  for (auto &keyVal : indicesForEachCluster) {
    std::random_shuffle(keyVal.second.begin(), keyVal.second.end());
  }

  std::vector<unsigned int> order;
  order.reserve(n);
  // take one element from each cluster at each loop
  while (order.size() < n) {
    for (auto &keyVal : indicesForEachCluster) {
      if (keyVal.second.size() > 0) {
        order.push_back(keyVal.second.back());
        keyVal.second.pop_back();
      }
    }
  }

  return order;
}
