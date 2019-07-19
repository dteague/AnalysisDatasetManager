import os
uwlogin = "uwlogin" in os.environ["HOSTNAME"] 
uw = "hep.wisc.edu" in os.environ["HOSTNAME"] 
info = {
    "DYm50" : {
        "file_path" : "/eos/cms/store/user/kelong/NanoAOD_DileptonSkims_16Jun2019/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/*/*/*/*.root",
        "plot_group" : "dy"
    },
}

if uwlogin:
    for key, value in info.iteritems():
        filelabels = value["file_path"].strip("/").split("/")
        name = filelabels[5]
        if "store" not in filelabels[0]:
            continue # Take data from eos for now
        if "data" in value["plot_group"]:
            name = "_".join(filelabels[5:7])
        #value["file_path"] = "/".join(["/data", os.getlogin(), "NanoAODSkims/Dilepton", name, "*"]) 
        value["file_path"] = "/".join(["/data", "dteague", "NanoAODSkims/Dilepton", name, "*"]) 

elif uw:
    for key, value in info.iteritems():
        value["file_path"] = value["file_path"].replace("/eos/cms", "")

