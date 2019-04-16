import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/04A6B5A5-FB18-E911-A86C-AC1F6BAC7C20.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/082CBA8E-F218-E911-9265-0CC47A7452D8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/0CD418AB-9E18-E911-8720-B083FED04CAA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/109AFFCD-F718-E911-B576-0CC47A7C3458.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/10AABDD6-B41B-E911-A386-B083FED04CAA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/166A469D-EA1B-E911-A9F4-0025905B859E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/1685A464-4418-E911-9939-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/16C3A126-B21B-E911-AF0B-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/1A85C436-5719-E911-B992-0242AC1C0504.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/1E346DB9-0A19-E911-BC55-0CC47A4C8F0C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/20FA2104-B41B-E911-86D2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/240F0166-3F18-E911-BEC1-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/26415CB1-F518-E911-8FA9-AC1F6BAC7C2A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/267A3DB9-7319-E911-B929-0242AC1C0507.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/26E44173-5B18-E911-A81B-D067E5F91455.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/28077278-3D18-E911-9108-001E67792592.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/30AB1869-DF19-E911-9FC1-001E67E6F9E5.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/328FA920-B41B-E911-892E-A4BF01125600.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/32E30832-3918-E911-90E5-A4BF01125B70.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/34BF4F26-A718-E911-BAB9-1866DAEA812C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/38421965-2C18-E911-86F2-A4BF0112BE44.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/388B76CC-F419-E911-B205-AC1F6BB1781A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/3893DF01-B11B-E911-8F14-0CC47A4DECD6.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/3A534C55-A71B-E911-9DC1-AC1F6BAC816E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/3CD96510-B41B-E911-8EF2-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/42466078-511C-E911-B7E6-001E677927B2.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/44271DCB-B41B-E911-A5D4-1418774120C3.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/509E634A-6518-E911-AD86-D067E5F9156C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/52E595BB-0919-E911-8AF8-0025905A6064.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/52F32A9C-501C-E911-A504-1866DAEEB0A8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/54A35024-B01B-E911-BDD7-AC1F6B0DE0BA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/54AD34A1-A218-E911-91BA-782BCB5301CE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/58D128CD-5518-E911-93F9-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/5A9DD81B-C71B-E911-B839-0025905B8582.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/5E77B63D-9718-E911-911F-141877410522.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/6034B00D-4B18-E911-998A-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/60B13183-3B18-E911-BC53-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/6250F506-B41B-E911-89B9-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/6261D644-AA18-E911-9C2E-801844DF001C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/668B31D9-AA18-E911-AC58-801844E55BCC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/6C7C914E-321A-E911-8DDE-002590791D3C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/7026E92A-4818-E911-AC25-A0369FD0B144.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/70CC517C-6E19-E911-838B-0242AC1C0502.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/70DA66DD-281C-E911-A058-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/7225ED43-B31B-E911-A8FB-0242AC1C0507.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/72547AE9-281C-E911-9468-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/74C72750-4418-E911-8782-48FD8E282487.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/7EA3913B-D31B-E911-AA1B-20040FE8E90C.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/7ED62A08-6B18-E911-995E-D067E5F91455.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/80069043-3918-E911-A5DC-001E677923F8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/844F5B5E-A618-E911-8506-1866DAEA7E28.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/86633B20-6119-E911-8C65-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/90068A1E-4A18-E911-AA3F-F02FA768CF34.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/92E6CC92-311A-E911-8634-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/9CA68C52-4418-E911-AF03-AC1F6B0DE2E8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/9CB09BB4-AC1B-E911-843D-AC1F6BB177EC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/9E412012-3B18-E911-8DB4-001E6779267A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A0ADB060-2419-E911-98B0-AC1F6BB1783A.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A2082612-3818-E911-9694-48D539F3840E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A2CD1826-B41B-E911-9463-A4BF0112F51E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A2E63424-A718-E911-BAAC-20040FE9CF48.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A816EC4A-A91B-E911-BA60-AC1F6BAC816E.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A8857175-6919-E911-8AFE-AC1F6BAC7EAE.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/A8A2C23D-411A-E911-8C6B-A0369FE2C220.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/B4298833-7B19-E911-A784-0242AC1C0501.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/B6224B06-5F18-E911-9A3D-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/B6C02440-5C19-E911-928C-0242AC1C0507.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/BA1F94ED-301A-E911-A40A-0242AC1C0505.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/BAE5AC21-A718-E911-BFAD-782BCB539693.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/BED5CCF0-0E19-E911-BDC4-AC1F6BAC7EAC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/C294035B-A618-E911-9F79-1866DAEA79D0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/CC11F962-A418-E911-8387-20040FE9C824.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/CEEC5BFF-4A18-E911-8681-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/D095894A-8019-E911-9ADC-0242AC1C0500.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/D0FE69D7-511C-E911-A79E-0CC47AA47914.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/D6CFF454-4418-E911-A783-48D539D33331.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/DAF091A5-501C-E911-9F64-0CC47A4C8E70.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/DC196E67-A61B-E911-A700-0025905B85D0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/DE45E8B1-7419-E911-9BCA-20040FE9BCD4.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/DEEB5963-2518-E911-AF61-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/E0A8E74E-E218-E911-A7E9-0CC47A78A418.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/E0D03E80-511C-E911-97C4-AC1F6B0DE2EA.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/E2958D47-3C18-E911-8F09-001E677925E8.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/E48DEF06-B41B-E911-8DBA-0242AC130002.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/EC54794C-AA18-E911-9BD5-1866DAEA79D0.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/EE1DF21C-1319-E911-947C-AC1F6BAC8070.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/EE915F44-3B1A-E911-A8CE-801844E55BCC.root',
       '/store/mc/RunIISummer16MiniAODv3/SMS-T2bb_mSbot-1650to2600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_pileupfromucsd_94X_mcRun2_asymptotic_v3-v1/80000/F668BBE0-DA1B-E911-8BE0-A0369FD0B3EC.root',
] )