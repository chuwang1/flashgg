#!/bin/bash
export XRD_NETWORKSTACK=IPv4
export X509_USER_PROXY=/afs/cern.ch/user/c/chuw/x509up_u117482
WD=$PWD
echo
echo
echo
cd /afs/cern.ch/work/c/chuw/HHWWgg/FullLep/CMSSW_10_6_8
eval $(scram runtime -sh)
cd $WD
mkdir SM_2017
echo "ls $X509_USER_PROXY"
ls $X509_USER_PROXY
mkdir .dasmaps 
mv das_maps_dbs_prod.js .dasmaps/ 

declare -a jobIdsMap=( 2 7 16 18)
cmsRun /afs/cern.ch/work/c/chuw/HHWWgg/FullLep/CMSSW_10_6_8/src/flashgg/SM_2017/workspaceStd.py maxEvents=-1 metaConditions=/afs/cern.ch/work/c/chuw/HHWWgg/FullLep/CMSSW_10_6_8/src/flashgg/MetaData/data/MetaConditions/Era2017_RR-31Mar2018_v1.json doHHWWggTag=True HHWWggTagsOnly=True doSystematics=True dumpTrees=False dumpWorkspace=True campaign=NonRes2017 HHWWggAnalysisChannel=FL HHWWggYear=2017 doHHWWggNonResAnalysis=1 targetLumi=1e+3 useAAA=True puTarget=6.245e-06,2.63e-05,4.92e-05,9.084e-05,9.854e-05,0.0001426,0.0001557,0.0001656,0.0002269,0.0005395,0.001076,0.002034,0.003219,0.004616,0.006528,0.009201,0.01283,0.01707,0.02125,0.0251,0.02847,0.03118,0.03325,0.03486,0.03626,0.03758,0.0387,0.03937,0.03946,0.03892,0.03782,0.03627,0.03435,0.03211,0.02967,0.02719,0.02482,0.02264,0.0207,0.01907,0.01784,0.01709,0.01685,0.0171,0.01771,0.01849,0.01916,0.01945,0.01911,0.01804,0.01627,0.01399,0.01147,0.008976,0.006728,0.004848,0.003375,0.002281,0.001504,0.0009715,0.0006178,0.0003882,0.0002419,0.0001501,9.294e-05,5.768e-05,3.598e-05,2.263e-05,1.437e-05,9.233e-06,5.996e-06,3.933e-06,2.601e-06,1.731e-06,1.157e-06,7.743e-07,5.184e-07,3.466e-07,2.311e-07,1.535e-07,1.015e-07,6.676e-08,4.365e-08,2.836e-08,1.829e-08,1.171e-08,7.437e-09,4.685e-09,2.926e-09,1.812e-09,1.111e-09,6.754e-10,4.066e-10,2.424e-10,1.431e-10,8.363e-11,4.839e-11,2.771e-11,1.571e-11,8.814e-12 processIdMap=/afs/cern.ch/work/c/chuw/HHWWgg/FullLep/CMSSW_10_6_8/src/flashgg/SM_2017/config.json dataset=/GluGluToHHTo2G2l2nu_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8 outputFile=SM_2017/output_GluGluToHHTo2G2l2nu_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root nJobs=20 jobId=${jobIdsMap[${1}]} 
retval=$?
if [[ $retval != 0 ]]; then
    retval=$(( ${jobIdsMap[${1}]} + 1 )) 
fi 
if [[ $retval == 0 ]]; then
    errors=""
    for file in $(find -name '*.root' -or -name '*.xml'); do
        echo "cp -pv ${file} /afs/cern.ch/work/c/chuw/HHWWgg/FullLep/CMSSW_10_6_8/src/flashgg/SM_2017"
        cp -pv $file /afs/cern.ch/work/c/chuw/HHWWgg/FullLep/CMSSW_10_6_8/src/flashgg/SM_2017
        if [[ $? != 0 ]]; then
            errors="$errors $file($?)"
        fi
    done
    if [[ -n "$errors" ]]; then
       echo "Errors while staging files"
       echo "$errors"
       exit -2
    fi
fi

exit $retval

