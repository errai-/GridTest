# -*- coding: utf-8 -*-
from PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff import *
from PhysicsTools.PatAlgos.patSequences_cff import *
from PhysicsTools.PatAlgos.patTemplate_cfg import *

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing('standard')

from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag

process = cms.Process("Ntuplizer")

process.options = cms.untracked.PSet(wantSummary=cms.untracked.bool(True))

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.load("FWCore.MessageLogger.MessageLogger_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 100000
process.MessageLogger.cerr.threshold = cms.untracked.string('INFO')
process.MessageLogger.categories.append('TtSemiLeptonicEvent')
process.MessageLogger.categories.append('JetEnergyScale')
process.MessageLogger.cerr.TtSemiLeptonicEvent = cms.untracked.PSet(limit=cms.untracked.int32(-1))
# Event frequency of Fwk report
process.MessageLogger.cerr.FwkReport.reportEvery = max(1000, int(options.maxEvents / 100))

# register TFileService
process.TFileService = cms.Service("TFileService",fileName=cms.string("out.root"))

process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc')

inFiles = cms.untracked.vstring(
#'/store/mc/RunIISummer19UL17MiniAOD/SingleNeutrino/MINIAODSIM/106X_mc2017_realistic_v6-v2/70000/F62C83FE-2284-4341-86FA-72B4F5F9AC17.root'
#'/store/mc/RunIISummer19UL17MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/100000/00F14449-0E85-FB42-87FA-AD7956E4714B.root'
#'/store/mc/RunIISummer19UL18MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/MINIAODSIM/FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v2/40000/F8EE4D72-7A79-A54E-B3A9-5DCBDE4FF8CE.root'
#'/store/mc/RunIISummer19UL18MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat_13TeV_pythia8/MINIAODSIM/FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v2/40000/E15DB014-9F37-7145-AA67-23E13B978E15.root'
#'/store/mc/RunIISummer19UL18MiniAOD/QCD_Pt-15to7000_TuneCP5_Flat2018_13TeV_pythia8/MINIAODSIM/FlatPU0to70_106X_upgrade2018_realistic_v11_L1v1-v2/240000/EA3B1C7C-711B-1D4F-B3EA-801BACD83BC2.root'
'/store/mc/RunIISummer19UL17MiniAOD/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/30000/B6694231-FE52-1540-B783-28B6D2352998.root'
#'/store/mc/RunIISummer19UL17MiniAOD/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/106X_mc2017_realistic_v6-v2/40000/D65E1284-38E8-D348-9471-07AF0DF7BCD8.root'
)

process.source = cms.Source("PoolSource", fileNames = inFiles)

process.ak4 =  cms.EDAnalyzer('GridTest')
process.path = cms.Path(process.ak4)

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(False))
process.options.allowUnscheduled = cms.untracked.bool(True)
