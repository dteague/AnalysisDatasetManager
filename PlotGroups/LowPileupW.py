import subprocess
converteps = subprocess.call(["command", "-v", "epstopdf"]) != 0

info = {
    "wlnu_jetbinned_nlo" : {
        "Name" : r"\mathrm{W} \to \ell\nu" if not converteps else "W #rightarrow l#nu",
        "Style" : "fill-yelloworange",
        "Members" : [
            "wlnu_0j_nlo__m",
            "wlnu_1j_nlo__m",
            "wlnu_2j_nlo__m",
            "wlnu_0j_nlo__e",
            "wlnu_1j_nlo__e",
            "wlnu_2j_nlo__e",
        ]
    },
    "wlnu_0j_nlo" : {
        "Name" : "\\mathrm{W} \\rightarrow \\mu\\nu",
        "Style" : "fill-yelloworange",
        "Members" : [
            "wlnu_0j_nlo",
        ]
    },
    "wlnu_1j_nlo" : {
        "Name" : "\\mathrm{W} \\rightarrow \\mu\\nu",
        "Style" : "fill-yelloworange",
        "Members" : [
            "wlnu_1j_nlo",
        ]
    },
    "wlnu_2j_nlo" : {
        "Name" : "\\mathrm{W} \\rightarrow \\mu\\nu",
        "Style" : "fill-yelloworange",
        "Members" : [
            "wlnu_2j_nlo",
        ]
    },
    "top" : {
        "Name" : "Top",
        "Style" : "fill-green",
        "Members" : [
            "tt_lep__e",
            "tt_lep__m",
            "tt_semilep__e",
            "tt_semilep__m",
            "tt_had__e",
            "tt_had__m",
        ]
    },
    "ewk" : {
        "Name" : "EW",
        "Style" : "fill-darkpink",
        "Members" : [
            "DYm50__e",
            "DYm50__m",
            "wlnu_0j_nlo__te",
            "wlnu_1j_nlo__te",
            "wlnu_2j_nlo__te",
            "wlnu_0j_nlo__tm",
            "wlnu_1j_nlo__tm",
            "wlnu_2j_nlo__tm",
            "ww__e",
            "wz__e",
            "zz__e",
            "ww__m",
            "wz__m",
            "zz__m",
        ]
    },
    "dy" : {
        "Name" : "Drell-Yan",
        "Style" : "fill-darkpink",
        "Members" : [
            "DYm50__e",
            "DYm50__m",
        ]
    },
    "wtv" : {
        "Name" : r"\mathrm{W}\to\tau\nu",
        "Style" : "fill-darkpink",
        "Members" : [
            "wlnu_0j_nlo__te",
            "wlnu_1j_nlo__te",
            "wlnu_2j_nlo__te",
            "wlnu_0j_nlo__tm",
            "wlnu_1j_nlo__tm",
            "wlnu_2j_nlo__tm",
        ]
    },
    "vv" : {
        "Name" : "Diboson",
        "Style" : "fill-darkpink",
        "Members" : [
            "ww__e",
            "wz__e",
            "zz__e",
            "ww__m",
            "wz__m",
            "zz__m",
        ]
    },
    "data" : {
        "Name" : "Data",
        "Style" : "data",
        "Members" : [
            "data__e",
            "data__m",
        ]
    },
    "nonprompt_m" : {
        "Name" : "Nonprompt",
        "Scale" : 0.12,
        "Style" : "fill-lightpink",
        "Members" : [
            "data__m",
            "-DYm50__m",
            "-ww__m",
            "-wz__m",
            "-tt_lep__m",
            "-wlnu_0j_nlo__m", 
            "-wlnu_1j_nlo__m", 
            "-wlnu_2j_nlo__m", 
            "-wlnu_0j_nlo__tm", 
            "-wlnu_1j_nlo__tm",
            "-wlnu_2j_nlo__tm",
            "-tt_lep__m",
            "-tt_semilep__m",
            "-tt_had__m",
        ],
    },
    "nonprompt_e" : {
        "Name" : "Nonprompt",
        "Scale" : 2,
        "Style" : "fill-lightpink",
        "Members" : [
            "data__e",
            "-DYm50__e",
            "-ww__e",
            "-wz__e",
            "-tt_lep__e",
            "-wlnu_0j_nlo__e", 
            "-wlnu_1j_nlo__e", 
            "-wlnu_2j_nlo__e", 
            "-wlnu_0j_nlo__te", 
            "-wlnu_1j_nlo__te", 
            "-wlnu_2j_nlo__te", 
            "-tt_lep__e",
            "-tt_semilep__e",
            "-tt_had__e",
        ],
    },
    "wlnu_jetbinned_nlo_pt0to13" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [0, 13] \,\mathrm{GeV}",
        "Style" : "fill-red-shade1",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_0_13__m",
            "wlnu_1j_nlo_GenPtW_0_13__m",
            "wlnu_2j_nlo_GenPtW_0_13__m",
            "wlnu_0j_nlo_GenPtW_0_13__e",
            "wlnu_1j_nlo_GenPtW_0_13__e",
            "wlnu_2j_nlo_GenPtW_0_13__e",
        ]
    },
    "wlnu_jetbinned_nlo_pt13to26" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [13, 26] \,\mathrm{GeV}",
        "Style" : "fill-red-shade2",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_13_26__m",
            "wlnu_1j_nlo_GenPtW_13_26__m",
            "wlnu_2j_nlo_GenPtW_13_26__m",
            "wlnu_0j_nlo_GenPtW_13_26__e",
            "wlnu_1j_nlo_GenPtW_13_26__e",
            "wlnu_2j_nlo_GenPtW_13_26__e",
        ]
    },
    "wlnu_jetbinned_nlo_pt26to38" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [26, 38] \,\mathrm{GeV}",
        "Style" : "fill-red-shade3",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_26_38__m",
            "wlnu_1j_nlo_GenPtW_26_38__m",
            "wlnu_2j_nlo_GenPtW_26_38__m",
            "wlnu_0j_nlo_GenPtW_26_38__e",
            "wlnu_1j_nlo_GenPtW_26_38__e",
            "wlnu_2j_nlo_GenPtW_26_38__e",
        ]
    },
    "wlnu_jetbinned_nlo_pt38to50" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [38, 50] \,\mathrm{GeV}",
        "Style" : "fill-red-shade4",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_38_50__m",
            "wlnu_1j_nlo_GenPtW_38_50__m",
            "wlnu_2j_nlo_GenPtW_38_50__m",
            "wlnu_0j_nlo_GenPtW_38_50__e",
            "wlnu_1j_nlo_GenPtW_38_50__e",
            "wlnu_2j_nlo_GenPtW_38_50__e",
        ]
    },
    "wlnu_jetbinned_nlo_pt50to62" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [50, 62] \,\mathrm{GeV}",
        "Style" : "fill-red-shade6",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_50_62__m",
            "wlnu_1j_nlo_GenPtW_50_62__m",
            "wlnu_2j_nlo_GenPtW_50_62__m",
            "wlnu_0j_nlo_GenPtW_50_62__e",
            "wlnu_1j_nlo_GenPtW_50_62__e",
            "wlnu_2j_nlo_GenPtW_50_62__e",
        ]
    },
    "wlnu_jetbinned_nlo_pt62to75" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [62, 75] \,\mathrm{GeV}",
        "Style" : "fill-red-shade7",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_62_75__m",
            "wlnu_1j_nlo_GenPtW_62_75__m",
            "wlnu_2j_nlo_GenPtW_62_75__m",
            "wlnu_0j_nlo_GenPtW_62_75__e",
            "wlnu_1j_nlo_GenPtW_62_75__e",
            "wlnu_2j_nlo_GenPtW_62_75__e",
        ]
    },
    "wlnu_jetbinned_nlo_pt75to100" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [75, 100] \,\mathrm{GeV}",
        "Style" : "fill-red-shade8",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_75_100__e",
            "wlnu_1j_nlo_GenPtW_75_100__e",
            "wlnu_2j_nlo_GenPtW_75_100__e",
            "wlnu_0j_nlo_GenPtW_75_100__m",
            "wlnu_1j_nlo_GenPtW_75_100__m",
            "wlnu_2j_nlo_GenPtW_75_100__m",
        ]
    },
    "wlnu_jetbinned_nlo_pt100" : {
        "Name" : r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) > 100 \,\mathrm{GeV}",
        "Style" : "fill-red-shade11",
        "Members" : [
            "wlnu_0j_nlo_GenPtW_100__e",
            "wlnu_1j_nlo_GenPtW_100__e",
            "wlnu_2j_nlo_GenPtW_100__e",
            "wlnu_2j_nlo_GenPtW_100__m",
            "wlnu_0j_nlo_GenPtW_100__m",
            "wlnu_1j_nlo_GenPtW_100__m",
        ]
    },
}

import copy
for name in ["data", "wlnu_jetbinned_nlo", "ewk", "top"]:
    info["nonprompt_"+name] = copy.deepcopy(info[name])
#ptbins = [0.0, 13.0, 26.0, 38.0, 50.0, 62.0, 75.0, 100.0]
#bin_pairs = [(ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
#regions = ["pt%ito%i" % pair for pair in bin_pairs]

ptbins = [0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 100]
bin_pairs = [(ptbins[i], ptbins[i+1]) for i in range(len(ptbins)-1)]
regions = ["pt%ito%i" % pair for pair in bin_pairs]

plot_groups = ["wlnu_jetbinned_nlo_%s" % region for region in regions]
plot_groups.append("wlnu_jetbinned_nlo_pt100")

for chan in ["e", "m"]:
    for ptbin, plot_group in zip(bin_pairs, plot_groups):
        info[plot_group] = {}
        if not converteps:
            info[plot_group]["Name"] = r"\mathrm{W} \rightarrow \mu\nu: p_{\mathrm{T}}^{true}(W) \in [%i, %i] \,\mathrm{GeV}" % ptbin
        else:
            info[plot_group]["Name"] = "W #rightarrow l#nu: p_T^{true}(W) #in [%i, %i] GeV" % ptbin
        info[plot_group]["Style"] = "fill-red-shade%i" % (bin_pairs.index(ptbin)+1)
        name = plot_group.replace("pt", "GenPtW_") + "__" + chan
        name = name.replace("to", "_") 
        info[plot_group]["Members"] = [name.replace("jetbinned", "%ij" % j) for j in range(3)] 
