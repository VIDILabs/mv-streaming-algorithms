#include "fff.hpp"
#include <iostream>
#include <list>

class Detector{
public:
  Detector(); //default BL
  Detector(int); //setting BL

  //need virtual destructor - this adds AND defines it
  virtual ~Detector() {}
  //the update method will be implemented in derived classes
  virtual void update(double) {};

  int getBL();
  void setBL(int);
  double getStreamEstMean();
  void setStreamEstMean(double);
  double getStreamEstSigma();
  void setStreamEstSigma(double);
  //NEW: adding Sq variables
  double getStreamEstSigmaSq();
  void setStreamEstSigmaSq(double);
  double getPval();
  void setPval(double);
  bool getChangeDetected();

  //detect multiple changepoints
  //uses virtual update method
  //need to make it public so accessible in detectVectors.cpp
  std::list<double> detectMultiple(std::vector<double>);
  std::list<double> detectSingle(std::vector<double>);
  std::list<double> detectSinglePrechangeKnown(std::vector<double>, double, double);
protected: 
  int BL;
  int BLcount;
  double pval;
  bool inBurnIn;
  bool inDetectState;
  bool changeDetected;
  FFF streamEstimator;
  void setStreamEstMean();
  //Note: Removing this function for setting Sigma, only
  //will allow setting SigmaSq, to avoid needing square root function
  //void setStreamEstSigma();
  void setStreamEstSigmaSq();
  void stopBurnIn();
  void startBurnIn();
private:
  double streamEstMean;
  double streamEstSigma;
  double streamEstSigmaSq;

};

