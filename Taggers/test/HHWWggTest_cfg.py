import FWCore.ParameterSet.Config as cms  # imports our CMS-specific Python classes and functions
import os # python module for os dependent functionality 

from flashgg.Taggers.flashggHHWWggCandidate_cfi import FlashggHHWWggCandidate # flashggHHWWggCandidate parameters 
#from flashgg.Taggers.flashggPreselectedDiPhotons_LowMass_cfi import flashggPreselectedDiPhotonsLowMass
from flashgg.Taggers.flashggPreselectedDiPhotons_cfi import flashggPreselectedDiPhotons
import flashgg.Taggers.dumperConfigTools as cfgTools


process = cms.Process("FLASHggHHWWggTest") # Process name. Can't use HH_WWgg because '_' is a non-alphanumeric character
from flashgg.Taggers.flashggTags_cff import flashggUnpackedJets
process.flashggUnpackedJets = flashggUnpackedJets

###---HHWWgg candidates production
process.FlashggHHWWggCandidate = FlashggHHWWggCandidate.clone() # clone flashgg HHWWggCandidate parameters here 
process.FlashggHHWWggCandidate.idSelection = cms.PSet(
        # rho = flashggPreselectedDiPhotonsLowMass.rho,
        # cut = flashggPreselectedDiPhotonsLowMass.cut,
        # variables = flashggPreselectedDiPhotonsLowMass.variables,
        # categories = flashggPreselectedDiPhotonsLowMass.categories
        rho = flashggPreselectedDiPhotons.rho,
        cut = flashggPreselectedDiPhotons.cut, # diphoton preselection cuts. I guess somehow applied to FlashggHHWWggCandidate 
        variables = flashggPreselectedDiPhotons.variables,
        categories = flashggPreselectedDiPhotons.categories
        )

###--- get the variables
import flashgg.Taggers.HHWWggTagVariables as var # python file of lists of strings 
#all_variables = var.pho_variables + var.dipho_variables + var.tp_variables + var.abe_variables # add variable lists together 
all_variables = var.HHWWgg_variables # add variable lists together 

from flashgg.Taggers.HHWWggCandidateDumper_cfi import HHWWggCandidateDumper
process.HHWWggCandidateDumper = HHWWggCandidateDumper.clone() # clone parameters from HHWWggCandidateDumpConfig_cff (className, src, ...)
process.HHWWggCandidateDumper.dumpTrees = True # Needs to be set to true here. Default in _cff is false 
process.HHWWggCandidateDumper.dumpWorkspace = False

# Create histograms 
cfgTools.addCategories(process.HHWWggCandidateDumper, # className, src, ... from _cff ^^ 
                        [
                            # Add the categories you'd like to have in the output file 
                            #("4photons","phoVector.size() > 3", 0), # label, cutbased, subcats
                            #("Reject", "", -1), # not cut based, and sub cats !>= 0, so nothing will be done 
                            #("Dipho_PS","diphoVector.size() > 0",0),
                            #("All_Events","1",0), # all events 
                            ("Dipho_PS","diphoVector.size() >= 1",0) # events with at least one diphoton passing preselection  
                            #("SemiLeptonic","electronVector.size() == 1", 0), # Or muon vector
                            #("FullyLeptonic","electronVector.size() == 2", 0), # Or muons 
                            #("FullyHadronic","electronVector.size() == 0 || electronVector.size() > 2", 0)

                            #("Reject", "", -1),
                            #("All","electronVector.size() != 0", 0),
                            #("All","diphoVector.size() == 0 || diphoVector.size() != 0", 0),

                            # Cut 1
                            #("1a3_1","electronVector.size() != 0", 0), 
                            #("1a3_1","muonVector.size() != 0", 0), 

                            # Cut 2
                            #("1a3_1","electronVector.size() >= 2", 0), 
                            #("1a3_1","muonVector.size() >= 2", 0), 

                            # Cut 3
                            #("1a3_1","diphoVector.size() > 0", 0),

                            # Cuts 1 and 3 
                            #("1a3_1","electronVector.size() != 0 && diphoVector.size() > 0", 0), 
                            #("1a3_1","muonVector.size() != 0 && diphoVector.size() > 0", 0), 

                            # Cuts 2 and 3 
                            #("1a3_1","electronVector.size() >= 2 && diphoVector.size() > 0", 0), 
                            #("1a3_1","muonVector.size() >= 2 && diphoVector.size() > 0", 0), 

                            #("Reject", "", -1),
                            #("4photons","phoVector.size() > 3", 0),
                            #("3photons","phoVector.size() == 3", 0),
                            #("2photons","phoVector.size() == 2", 0)

                            # process.HHWWggCandidateDumper.classifierCfg.categories.append(cb) done for each cut here. phoVector.size() > 3, ... 
                            # default of classifierCfg.categories in _cff file. # categories = cms.VPSet(), (I think empty)
                        ],

                        variables = all_variables, # input desired variables from HHWWggTagVariables. They end up getting added by dumperConfigTools.py 
                        # I think you can add things like binning as well, but I can just deal with this in the off-flashgg plotter 
                        histograms=[]
                        )

# process.source = cms.Source ("PoolSource",
#                              fileNames = cms.untracked.vstring(
# "root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/HiggsExo/HHWWggamma/MicroAOD/HHWWgg_Jun7/v0/SUSYGluGluToHToAA_AToGG_M-60_TuneCUETP8M1_13TeV_pythia8/Test_jun7-R2S16MAODv2-PUM17_GT/170607_180035/0000/myMicroAODOutputFile_1.root"
# ))

# input file. MicroAOD 

# process.source = cms.Source ("PoolSource",
#                              fileNames = cms.untracked.vstring(
# #"file:myMicroAODOutputFile.root" 
# "root://eoscms.cern.ch//eos/cms/store/group/phys_higgs/HiggsExo/H4Gamma/MicroAOD/H4G_Jun7/v0/SUSYGluGluToHToAA_AToGG_M-60_TuneCUETP8M1_13TeV_pythia8/Test_jun7-R2S16MAODv2-PUM17_GT/170607_180035/0000/myMicroAODOutputFile_1.root"
# ))

process.source = cms.Source ("PoolSource",
                             fileNames = cms.untracked.vstring(
"file:myMicroAODOutputFile.root"
#"file:/eos/cms/store/user/atishelm/ggF_X1250_WWgg_qqenugg/10000events_woPU_MICROAOD/myMicroAODOutputFile.root" # qqenu 
#"file:/eos/cms/store/user/atishelm/ggF_X1250_WWgg_qqmunugg/10000events_woPU_MICROAOD/myMicroAODOutputFile.root" # qqmunu
#"file:/eos/cms/store/user/atishelm/ggF_X1250_WWgg_enuenugg/10000events_woPU_MICROAOD/myMicroAODOutputFile.root" # enuenu 
#"file:/eos/cms/store/user/atishelm/ggF_X1250_WWgg_munumunugg/10000events_woPU_MICROAOD/myMicroAODOutputFile.root" # munumunu 
))


process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string("test.root"),
                                   closeFileFast = cms.untracked.bool(True)
)
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )


from flashgg.MetaData.JobConfig import customize
customize.setDefault("maxEvents",-1)
#customize.setDefault("maxEvents",100)


# customize.setDefault("puTarget",'2.39e+05,8.38e+05,2.31e+06,3.12e+06,4.48e+06,6e+06,7e+06,1.29e+07,3.53e+07,7.87e+07,1.77e+08,3.6e+08,6.03e+08,8.77e+08,1.17e+09,1.49e+09,1.76e+09,1.94e+09,2.05e+09,2.1e+09,2.13e+09,2.15e+09,2.13e+09,2.06e+09,1.96e+09,1.84e+09,1.7e+09,1.55e+09,1.4e+09,1.24e+09,1.09e+09,9.37e+08,7.92e+08,6.57e+08,5.34e+08,4.27e+08,3.35e+08,2.58e+08,1.94e+08,1.42e+08,1.01e+08,6.9e+07,4.55e+07,2.88e+07,1.75e+07,1.02e+07,5.64e+06,2.99e+06,1.51e+06,7.32e+05,3.4e+05,1.53e+05,6.74e+04,3.05e+04,1.52e+04,8.98e+03,6.5e+03,5.43e+03,4.89e+03,4.52e+03,4.21e+03,3.91e+03,3.61e+03,3.32e+03,3.03e+03,2.75e+03,2.47e+03,2.21e+03,1.97e+03,1.74e+03,1.52e+03,1.32e+03,1.14e+03,983,839')


# import FWCore.ParameterSet.VarParsing as VarParsing
# customize(process)
# if customize.inputFiles:
#     inputFile = customize.inputFiles
#
# if customize.outputFile:
#     outputFile = customize.outputFile

# customize.parse()
# process.TFileService = cms.Service("TFileService",
#                                    fileName = cms.string("output.root"),
#                                    closeFileFast = cms.untracked.bool(True)
# )

# Require low mass diphoton triggers
from HLTrigger.HLTfilters.hltHighLevel_cfi import hltHighLevel
process.hltHighLevel= hltHighLevel.clone(HLTPaths = cms.vstring(
                                                                #"HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90_v*",
                                                                #"HLT_Diphoton30_18_R9Id_OR_IsoCaloId_AND_HE_R9Id_Mass90",
                                                              #"HLT_Diphoton30PV_18PV_R9Id_AND_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v*",
                                                              #"HLT_Diphoton30EB_18EB_R9Id_OR_IsoCaloId_AND_HE_R9Id_DoublePixelVeto_Mass55_v*"
                                                               ))
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#############   Geometry  ###############
process.load("Geometry.CMSCommonData.cmsIdealGeometryXML_cfi")
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load('RecoMET.METFilters.eeBadScFilter_cfi')
process.load("Configuration.Geometry.GeometryECALHCAL_cff")
process.eeBadScFilter.EERecHitSource = cms.InputTag("reducedEgamma","reducedEERecHits") # Saved MicroAOD Collection (data only)

process.dataRequirements = cms.Sequence()

#process.dataRequirements += process.hltHighLevel # HLT 

if customize.processId == "Data":
   # process.dataRequirements += process.hltHighLevel
   process.dataRequirements += process.eeBadScFilter

# customize.register('puTarget',
#                    " ",
#                    VarParsing.VarParsing.multiplicity.singleton,
#                    VarParsing.VarParsing.varType.string,
#                    "puTarget")
###--- call the customization
# process.HHWWggCandidateDumper.puReWeight=cms.bool( bool(customize.PURW) )
# if customize.PURW == False:
# 	process.HHWWggCandidateDumper.puTarget = cms.vdouble()

process.path = cms.Path(process.flashggUnpackedJets*process.dataRequirements*process.FlashggHHWWggCandidate*process.HHWWggCandidateDumper)

# process.path = cms.Path(process.FlashggHHWWggCandidate+process.HHWWggCandidateDumper)
#process.e = cms.EndPath(process.out)

customize(process) 
