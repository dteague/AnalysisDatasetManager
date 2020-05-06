# From http://colorbrewer2.org/#type=qualitative&scheme=Paired&n=10
info = {
    "qual12_red" : {
        "SetLineColor": "ROOT.TColor.GetColor(#e31a1c)",
        "SetLineStyle": 1,
        "SetLineWidth": 2,
        "SetMarkerSize" : 0
    },
}

colors = {
    "qual12_lightblue" : "#a6cee3",
    "qual12_blue" : "#1f78b4",
    "qual12_lightgreen" : "#b2df8a",
    "qual12_green" : "#33a02c",
    "qual12_pink" : "#fb9a99",
    "qual12_burntorange" : "#fdbf6f",
    "qual12_orange" : "#ff7f00",
    "qual12_lightpurple" : "#cab2d6",
    "qual12_purple" : "#6a3d9a",
    "qual12_yellow" : "#ffff99",
    "qual12_brown" : "#b15928",
}

import copy
for name, color in colors.iteritems():
    info[name] = copy.deepcopy(info["qual12_red"])
    info[name]["SetLineColor"] = "ROOT.TColor.GetColor(%s)" % color

dash = copy.deepcopy(info)
for name in info:
    dash[name+"_dash"] = copy.deepcopy(info[name])
    dash[name+"_dash"]["SetLineStyle"] = 7

    dash[name+"_dotdash"] = copy.deepcopy(info[name])
    dash[name+"_dotdash"]["SetLineStyle"] = 4

    dash[name+"_finedash"] = copy.deepcopy(info[name])
    dash[name+"_finedash"]["SetLineStyle"] = 2

info.update(dash) 
