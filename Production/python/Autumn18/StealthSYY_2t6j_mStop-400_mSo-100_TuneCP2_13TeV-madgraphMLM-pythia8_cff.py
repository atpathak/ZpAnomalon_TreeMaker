import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/012FE49D-C48B-F44D-B836-92010E581740.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0434A010-8D9B-4643-BE8C-195C96B800E5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0588AD95-120E-BB42-B627-4DC97752D32D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/05C6932A-6822-8A44-B8C7-2B1C296A93CE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0B5679CC-B7C8-0C48-8CFC-F7324DF2451B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0CA44385-2570-D244-A100-6EEF00D83E8F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0E8C2AE5-688D-8F44-96B5-6BB2BFBBFB54.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/0EDA5D17-1C1A-D143-87F1-CC963562180E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/116818FF-1449-9D45-9CD5-895F167C1E93.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1541F2B1-AD39-9349-8987-7FD8E62B4B64.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/1A91A3E5-B1F8-024D-8F2C-BDB4310AB45F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/204DBD07-63AC-F14E-A1B5-63242724AD8B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/21B283B5-FA49-AF4B-99CD-2E7BBF4521D2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/22F50615-92AA-C74F-BC1A-98BA0D2D5BDD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/23468DA6-32FD-694E-9A61-07B3402D3ACA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2623E40E-9124-6B41-8D82-C1592F5A06FE.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2F8AA644-030A-EB4E-B281-4C5147FE3A77.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/2FAD8809-3A05-9046-B81D-D6C7D6DC2B59.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/446E09A2-48CA-034F-BF79-EC7B72CD3AF7.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/455E15F4-501B-3E40-A64A-F02793E8135E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/4A90607D-1A4A-BB42-A597-BFBA17FDF2E1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5043C7DB-D6A9-A841-8377-55D856A0B3B3.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/5491E1AD-A5B4-8A41-8E84-3815AC0A27EA.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/549B7BF9-585C-6C4F-9705-A1635DCAFE4B.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/58D72A96-2077-9A48-8AFC-C4A92B6A9B70.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/637ACD5F-8C06-BF4D-BA46-6C347675963C.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/68611CA8-301E-D146-ABA5-78AF34C52915.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7048BA75-52F6-DF41-AE2C-C704F39B0C84.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/76812F8F-B90A-C544-9F59-00F8A1B5B775.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/78FF3359-0230-D44C-9494-E1A1384E92E6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7B411404-D432-3246-966A-25D998D2712E.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/7D197F64-C329-FD4B-B76F-51459FA966F4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8796684F-CF26-4047-93B2-650401FDBC1D.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/88BEE6D9-E52E-7346-9539-7D3DD7606873.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/8C0757CE-7833-3B44-92C8-F6D797506F76.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9004C241-2A57-0B4B-A85F-2C3A1FE986DD.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9B3DFD32-4D89-1D44-A318-3A03AF06E431.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9BBC2DCD-8680-1F4D-BA69-ED7EC8AB328F.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9BF7DABC-6736-2F48-A93A-88BB2C9094F8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/9FEDED51-E02E-9A41-AD72-1FCD84E47F9A.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A05FE64B-484D-AB45-990C-13E0F7D0ADD8.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A13843C1-72E5-314F-9A7E-96DE46F322C5.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/A522D7B7-2AC1-8E43-B117-0887FF905996.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/ACD0221E-8B79-334A-B08E-8A7CA9458522.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/AE45CCCB-F6CB-8D41-8A94-A7CB866BAA66.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B04ACB42-652F-9C4E-A582-EEB9C2521C76.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B73E73D1-099C-DD4E-AE43-8D966C9FBEA9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/B9354F20-0374-5C4A-8EB8-4636DE0FE195.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C0D5F324-6930-C949-A40F-C11F65BC6743.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/C0FC94DF-9427-EF4E-9C5D-886447D28531.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D04AB027-4DAC-1943-9972-C764590768E4.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D18C33CD-45AA-7045-A312-02D0DF129205.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D3525A46-E200-2542-903B-1E6494C23392.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D52F0BA1-E1E8-AE4D-AC81-9516333C4D41.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/D6421AA2-D41C-704B-8F95-A0CFA4F8C8A1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DADF1EFA-6A2F-0D4E-94D3-F8EBC0474FC2.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/DFD2E454-89E0-B846-9FFB-F291FA67D718.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E68221CE-E282-5447-9D5B-DB05448D08E9.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/E72C0C7F-5590-E745-AEA6-098A0BCFF1B6.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/EC52CB46-5BEB-1E44-8B3B-9654F8C48459.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F30AC318-2BB6-4E47-B51E-D0DF47DCD5A1.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/F7F64901-8E81-BB49-8927-318257A1F611.root',
       '/store/mc/RunIIAutumn18MiniAOD/StealthSYY_2t6j_mStop-400_mSo-100_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v2/230000/FFA52A57-3982-A24F-834C-AE75E951980D.root',
] )
