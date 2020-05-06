import subprocess
converteps = subprocess.call(["command", "-v", "epstopdf"]) != 0

info = {
    "yW": {  
        "Initialize": {  
            "type": "TH1F",
            "nbins": 24,
            "xmin": -3,
            "xmax": 3
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "y^{W}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
        }
    },
   "pfMet": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": 0,
            "xmax": 100
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "PF p^{miss}_{T}[GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
            "SetMaximum" : 20000000
        }
    },
    "pfMetPhi": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 28,
            "xmin": 0,
            "xmax": 7
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "pfMET phi",
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 20000000
        }
    },
   "ptW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"p_{\mathrm{T}}(\mathrm{W}) \mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  ,
            "SetMinimum" : 0.1,
            "SetMaximum" : 10000000
        }
    },
    "phiW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 28,
            "xmin": 0,
            "xmax": 7
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "#phi^{W}",
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 20000000
        }
    },
   "ptl": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": 25,
            "xmax": 125
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell) \\mathrm{[GeV]}" if not converteps else
                                        "p_{T}^{l} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  ,
            "SetMinimum" : 0.1,
            "SetMaximum" : 90000000
        }
    },
   "etal": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta(\\ell_{1}) \\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "mW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 60,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell\\ell} \\, \\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 50000000,
        }
    },
   "mtWUncorr": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 200,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"m_{T}(\mathrm{W}) \, \mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 50000000,
        }
    },
   "mtW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 200,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"m_{T}(\mathrm{W}) \, \mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 50000000,
        }
    },
}

