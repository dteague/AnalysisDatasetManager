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
   "ptl": {  
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
