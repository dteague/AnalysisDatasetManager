import os
uw = "hep.wisc.edu" in os.environ["HOSTNAME"] 
info = {
    "DYm50" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8/*/*/*",
        "plot_group" : "dy"
    },
    "tt_lep" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8//*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/TTJets_TuneCP5_13TeV-amcatnloFXFX-pythia8//*/*/*",
        "plot_group" : "tt"
    },
    "data_DoubleMuon_Run2017B" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/DoubleMuon_Run2017B-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/DoubleMuon_Run2017B-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_DoubleMuon_Run2017C" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/DoubleMuon_Run2017C-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/DoubleMuon_Run2017C-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_DoubleMuon_Run2017D" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/DoubleMuon_Run2017D-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/DoubleMuon_Run2017D-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_DoubleMuon_Run2017E" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/DoubleMuon_Run2017E-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/DoubleMuon_Run2017E-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_DoubleMuon_Run2017F" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/DoubleMuon_Run2017F-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/DoubleMuon_Run2017F-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017B" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleMuon_Run2017B-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleMuon_Run2017B-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017C" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleMuon_Run2017C-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleMuon_Run2017C-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017D" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleMuon_Run2017D-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleMuon_Run2017D-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017E" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleMuon_Run2017E-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleMuon_Run2017E-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleMuon_Run2017F" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleMuon_Run2017F-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleMuon_Run2017F-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017B" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleElectron_Run2017B-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleElectron_Run2017B-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017C" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleElectron_Run2017C-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleElectron_Run2017C-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017D" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleElectron_Run2017D-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleElectron_Run2017D-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017E" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleElectron_Run2017E-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleElectron_Run2017E-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
    "data_SingleElectron_Run2017F" : {
        "file_path" : "/nfs_scratch/kdlong/UWVVNtuples/ZNtuples/SingleElectron_Run2017F-31Mar2018-v1/*.root" if uw else \
            "/store/user/uhussain/UWVVNtuplesZ_05Mar2019/SingleElectron_Run2017F-31Mar2018-v1/*/*/*",
        "plot_group" : "data"
    },
}

