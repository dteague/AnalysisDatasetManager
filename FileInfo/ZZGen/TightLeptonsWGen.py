import os
uwlogin = "login" in os.environ["HOSTNAME"] 
info = {
    "zz4l_powheg" : {
        "file_path" : "/data/uhussain/ZZSkimmedFiles/ZZ2018AnalysisTightWGen_2019-04-16/TightLeptons/2019-04-16-zz4l-powheg-ZZ4l2018-TightSIPToZZSelection-v1/*" if uwlogin else \
            "",
        "plot_group" : "zz"
    },
}
