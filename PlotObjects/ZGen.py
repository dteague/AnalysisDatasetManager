import socket
uwlogin = "uwlogin" in socket.gethostname() 
uw = "hep.wisc.edu" in socket.gethostname() 
info = {
    "HT": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 150,
            "xmin": 0,
            "xmax": 1500
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "H_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / bin", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 10000000
        }
    },
    "phiZ": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 70,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\phi_{\\ell^{+}\\ell^{-}}" if uw else "#phi_Z",  
            "GetYaxis().SetTitle": "Events / bin", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "ptZ": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 1500,
            "xmin": 0,
            "xmax": 1500
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell^{+}\\ell^{-}) [GeV]" if uw else "p_{T}(Z) [GeV]",  
            "GetYaxis().SetTitle": "Events / bin", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "yZ": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 100,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "y^{Z}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
        }
    },
    "ZMass": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 2000,
            "xmin": 81, #50,
            "xmax": 101, #150
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell^{+}\\ell^{-}} [GeV]" if uw else "m_{Z}",  
            "GetYaxis().SetTitle": "Events / GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
   "ptl1": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 160,
            "xmin": 0,
            "xmax": 160
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"p_{T}(\ell_{1}) [GeV]" if uw else "p_{T}^{l1} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 10000000,
        }
    },
   "ptl2": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}(l_{2}) [GeV]" if uw else "p_{T}^{l2} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 10000000,
        }
    },
    "etal1": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 20,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta^{\\ell_1}" if uw else "#eta_{l1}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "etal2": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 20,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta^{\\ell_2}" if uw else "#eta_{l2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "phil1": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 70,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\phi^{\\ell_1}" if uw else "#phi_{l1}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "phil2": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 70,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\phi^{\\ell_2}" if uw else "#phi_{l2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
   "ptj1": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 40,
            "xmin": 20,
            "xmax": 420
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen jet 1 p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
        }
    },
   "ptj2": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 40,
            "xmin": 20,
            "xmax": 420
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen jet 2 p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
        }
    },
    "etaj1": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 40,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "#eta_{j1}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 4000000
        }
    },
    "etaj2": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 40,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "#eta_{j2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 2000000
        }
    },
    "phij1": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 70,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "#phi_{j1}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "phij2": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 70,
            "xmin": -3.5,
            "xmax": 3.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "#phi_{j2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 15000000
        }
    },
    "nJets": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 10,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Num p_{T} > 30 GeV GenJets",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 150000000
        }
    },
   "MET": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": 0,
            "xmax": 500
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}^{miss} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
        }
    },
    "CutFlow": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 10,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Cut flow",  
            "GetYaxis().SetTitle": "Events / selection", 
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
            "SetMaximum" : 70000000
        }
    },
}

#partonicChans = ["uu_dd", "uubar_ddbar", "ug_dg", "ubarg_dbarg", "gg", "other"]
#tempdict = {}
#for key, value in info.iteritems():
#    for partonicChan in partonicChans:
#        tempdict["_".join([partonicChan, key])] = value
#info.update(tempdict)

import copy
altleps = {}
for i in info:
    if "barelep" in i or i == "nGammaAssoc":
        continue
    altleps[i+"_barelep"] = copy.deepcopy(info[i])
    altleps[i+"_born"] = copy.deepcopy(info[i])
    altleps[i+"_lhe"] = copy.deepcopy(info[i])

info.update(altleps)
