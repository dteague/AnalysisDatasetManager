import socket
uwlogin = "uwlogin" in socket.gethostname() 
uw = "hep.wisc.edu" in socket.gethostname() 
info = {
    "wz3lnu_powheg" : {
        "file_path" : "/data/kelong/NanoAODSkims/Unskimmed/WZ3LNu_powheg_2016/*.root" if uwlogin \
                else "/nfs_scratch/kdlong/NanoAODSkims/Unskimmed/wz3lnu_powheg_2016/*.root",
        "plot_group" : "wz-powheg"
    },
    "wz3lnu_powheg__testNano" : {
        "file_path" : "/data/kelong/NanoAODSkims/Unskimmed/WZ3LNu_powheg_2016/*.root" if uwlogin \
                else "/nfs_scratch/kdlong/NanoAODSkims/Unskimmed/wz3lnu_powheg_2016/*.root",
        "plot_group" : "wz-powheg_standalone"
    },
}
