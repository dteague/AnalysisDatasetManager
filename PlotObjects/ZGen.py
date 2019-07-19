info = {
    "ptZ": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 50,
            "xmin": 0,
            "xmax": 100
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell^{+}\\ell^{-}) [GeV]",  
            "GetYaxis().SetTitle": "Events / 2 GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 10000000
        }
    },
    "yZ": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 56,
            "xmin": -3,
            "xmax": 3
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
            "nbins": 31,
            "xmin": 75,
            "xmax": 106
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell^{+}\\ell^{-}} [GeV]",  
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
            "GetXaxis().SetTitle": "Gen Lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
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
            "GetXaxis().SetTitle": "Gen Lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
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
            "GetXaxis().SetTitle": "\\eta^{\\ell_1}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
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
            "GetXaxis().SetTitle": "\\eta^{\\ell_2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
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
            "GetXaxis().SetTitle": "\\eta^{\\mathrm{j}_1}",  
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
            "GetXaxis().SetTitle": "\\eta^{\\mathrm{j}_2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 2000000
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
            "SetMaximum" : 40000000
        }
    },
   "MET": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}^{miss} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "ptZ": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}(ll) [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
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
