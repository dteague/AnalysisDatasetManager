import socket
import array
uwlogin = "uwlogin" in socket.gethostname() 
uw = "hep.wisc.edu" in socket.gethostname() 
import subprocess
converteps = subprocess.call(["command", "-v", "epstopdf"]) != 0

info = {
    "yW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 200,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "y^{W}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 70000000
        }
    },
   "ptW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 1500,
            "xmin": 0,
            "xmax": 1500
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}(W) [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2  ,
            "Rebin" : [24, "", array.array('d', range(0,125,5))],
            "SetMaximum" : 150000000
        }
    },
    "mW": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 200,
            "xmin": 70,
            "xmax": 90
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell\\nu} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 250000000
        }
    },
    "mTmet": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 300,
            "xmin": 0,
            "xmax": 150
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{T}(W_{MET}) [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 100000000
        }
    },
    "mTtrue": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 1000,
            "xmin": 50,
            "xmax": 100
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "m_{\\ell\\nu} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 100000000
        }
    },
    "yWmet": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "y^{l+p_{T}^{miss}}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 70000000
        }
    },
   "ptWmet": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 1500,
            "xmin": 0,
            "xmax": 1500
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}(l+MET) [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 150000000
        }
    },
    "mWmet": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 200,
            "xmin": 0,
            "xmax": 200
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"m_{\ell+pTmiss} \,\mathrm{[GeV]}",  
            "GetYaxis().SetTitle": "Events / GeV", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 1000000000
        }
    },
   "ptl": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 240,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}^{l} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 30000000
        }
    },
   "ptl_smear": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 240,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}^{l} (smeared) [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 30000000
        }
    },
    "etal": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta^{\\ell}" if not converteps else "#eta^{l}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 70000000
        }
    },
    "phil": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 7
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\phi^{\\ell}",
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
        }
    },
   "ptnu": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 240,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}(\\nu) [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 30000000
        }
    },
    "etanu": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta^{\\nu}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 70000000
        }
    },
    "phinu": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 20,
            "xmin": 0,
            "xmax": 7
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\phi^{\\ell}",
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 7000000
        }
    },
    "CutFlow": {  
        "Initialize": {  
            "type": "TH1D",
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
            "type": "TH1D",
            "nbins": 40,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta^{\\mathrm{j}_1}" if uw else "#eta_{j1}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 4000000
        }
    },
    "etaj2": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 40,
            "xmin": -5,
            "xmax": 5
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "\\eta^{\\mathrm{j}_2}" if uw else "#eta_{j2}",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 2000000
        }
    },
    "nJets": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 10,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Num p_{T} > 30 GeV GenJets",  
            "GetYaxis().SetTitle": "Events", 
            "GetYaxis().SetTitleOffset": 1.3,
            "SetMinimum" : 0.1,
            "SetMaximum" : 20000000
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
   "dRlgamma_maxptassoc" : {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": 0,
            "xmax": 0.1
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"\DeltaR(\gamma, \ell)_{\mathrm{min}}\,[GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
        }
    },
    "dRlgamma_minassoc" : {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": 0,
            "xmax": 0.1
        },
        "Attributes": {  
            "GetXaxis().SetTitle": r"\DeltaR(\gamma, \ell)_{\mathrm{min}}\,[GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.1,
        }
    },
    "ptg_closeassoc" : {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Closest assoc photon p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.01,
        }
    },
    "ptgmax_assoc" : {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 120,
            "xmin": 0,
            "xmax": 120
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Max assoc photon p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.01,
        }
    },
    "nGammaAssoc" : {
        "Initialize": {  
            "type": "TH1D",
            "nbins": 10,
            "xmin": 0,
            "xmax": 10
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "# associated photons",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMinimum" : 0.01,
        }
    },
   "etal_ptl_2D": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 50,
            "xmin": -2.5,
            "xmax": 2.5,
            "nbinsy": 75,
            "ymin": 25,
            "ymax": 100,
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 30000000
        }
    },
   "etal_ptl_smear_2D": {  
        "Initialize": {  
            "type": "TH2D",
            "nbinsx": 50,
            "xmin": -2.5,
            "xmax": 2.5,
            "nbinsy": 75,
            "ymin": 25,
            "ymax": 100,
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "Gen Lepton p_{T} [GeV]",  
            "GetYaxis().SetTitle": "Events / GeV",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 30000000
        }
    },
   "etal_ptl_unrolled": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": -0,
            "xmax": 100,
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}/#eta bin",  
            "GetYaxis().SetTitle": "Events / bin",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 3000000
        }
    },
   "etal_ptl_smear_unrolled": {  
        "Initialize": {  
            "type": "TH1D",
            "nbins": 100,
            "xmin": -0,
            "xmax": 100,
        },
        "Attributes": {  
            "GetXaxis().SetTitle": "p_{T}/#eta bin",  
            "GetYaxis().SetTitle": "Events / bin",
            "GetYaxis().SetTitleOffset": 1.2,
            "SetMaximum" : 3000000
        }
    },
}

import copy
altleps = {}
for i in info:
    altleps[i+"_barelep"] = copy.deepcopy(info[i])
    altleps[i+"_born"] = copy.deepcopy(info[i])
    altleps[i+"_lhe"] = copy.deepcopy(info[i])

info.update(altleps)
