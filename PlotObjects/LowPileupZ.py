info = {
    "yZ": {  
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
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "ptl1": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell_{1}) \\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "ptl2": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": 0,
            "xmax": 100
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{\\mathrm{T}}(\\ell_{2}) \\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "etal1": {  
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
   "etal2": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": -2.5,
            "xmax": 2.5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta(\\ell_{2}) \\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
   "mZ": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 60,
            "xmin": 60,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell\\ell} \\, \\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  
        }
    },
}

