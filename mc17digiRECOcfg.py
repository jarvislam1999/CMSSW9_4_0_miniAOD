# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein file:../../CMSSW_9_3_6/src/GenStudy/Dimuon/test/2017test.root --fileout file:B2G-RunIIFall17DRPremix-00001_step1.root --pileup_input dbs:/Neutrino_E-10_gun/RunIISummer17PrePremix-MC_v2_94X_mc2017_realistic_v9-v1/GEN-SIM-DIGI-RAW --mc --eventcontent PREMIXRAW --datatier GEN-SIM-RAW --conditions 94X_mc2017_realistic_v10 --step DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,HLT:2e34v40 --nThreads 8 --datamix PreMix --era Run2_2017 --python_filename B2G-RunIIFall17DRPremix-00001_1_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 1751
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('HLTrigger.Configuration.HLT_2e34v40_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/uscms/home/qlam/nobackup/CMSSW_9_3_6/src/GenStudy/Dimuon/test/2017test.root'),
#    secondaryFileNames = cms.untracked.vstring('/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MC_v2_94X_mc2017_realistic_v9-v1/30000/4EADA2FF-ADCA-E711-8C8F-001E67397E54.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:1751'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.PREMIXRAWoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:MC17digiRECO.root'),
    outputCommands = process.PREMIXRAWEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring(['root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/F4CEFFB5-FC0E-E811-A015-0025905B857E.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/72092F18-080F-E811-9A77-0025905A610C.root' , 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/6639B410-110F-E811-8BD3-0CC47A4C8F10.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/B46B6480-110F-E811-A9A0-0CC47A7C3572.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/08F933F2-110F-E811-9723-0CC47A4D7606.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/1EB39C59-FE0E-E811-8724-0025905B8580.root', ' root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/FEB40EDF-010F-E811-9C81-0025905B85B2.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/E6281466-0F0F-E811-B8F3-0CC47A4D7678.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80021/48661D80-100F-E811-B625-0CC47A7C360E.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/329AF42D-130F-E811-B39F-0CC47A4D76C8.root', 'root://cms-xrd-global.cern.ch//store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/80022/FCB963F4-020F-E811-ACB6-0025905B85FC.root'])

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v10', '')

# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.PREMIXRAWoutput_step = cms.EndPath(process.PREMIXRAWoutput)

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.PREMIXRAWoutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#Setup FWK for multithreaded
#process.options.numberOfThreads=cms.untracked.uint32(8)
#process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
