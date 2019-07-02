import os

################################################
# File to hold the getter and setter functions #
# Note: setters are of convention "addXXXXX"   #
#       To imply it writes out to file         #
################################################


def checkAnalysis(analysis):
    """
    Makes sure Files for analysis are there
    (implied PlotGroups file is there because that's where ana name comes from)
    """
    if analysis not in os.listdir("./FileInfo"):
        return False
    elif analysis not in os.listdir("./PlotObjects"):
        return False
    else:
        return True

 ###############################################
 #   ___   ____ ______ ______  ____ ____   __  #
 #  // \\ ||    | || | | || | ||    || \\ (( \ #
 # (( ___ ||==    ||     ||   ||==  ||_//  \\  #
 #  \\_|| ||___   ||     ||   ||___ || \\ \_)) #
 ###############################################
                                            
def getSelections(analysis):
    valid = []
    for file in os.listdir("./PlotObjects/" + analysis):
        if file.endswith(".json"):
            valid.append(file.split(".")[0])
    return valid

def getInputs(analysis):
    valid = []
    tmplist = []
    for file in os.listdir("./FileInfo/" + analysis):
        if file.endswith(".py"):
            valid.append(file.split(".")[0])
    return valid

def getAnalysis():
    anaList = []
    for file in os.listdir("./PlotGroups"):
        if file.endswith(".py"):
            anaTemp = file.split(".")[0]
            if checkAnalysis(anaTemp):
                anaList.append(anaTemp)
    return anaList

def getFiles(analysis, selection):
    config = dict()
    execfile("./FileInfo/%s/%s.py" % (analysis,selection), config)
    info = config["info"]
    return info.keys()

    
def getGroups(analysis):
    config = dict()
    execfile("./PlotGroups/%s.py" % (analysis), config)
    info = config["info"]
    return info.keys()

def getMCInfo(name):
    for file in os.listdir("./FileInfo/montecarlo/"):
        if file.endswith(".py"):
            config = dict()
            execfile("./FileInfo/montecarlo/%s" % file, config)
            info = config["info"]
            if name in info:
                return info[name]
    return {}

def getMCNames():
    for file in os.listdir("./FileInfo/montecarlo/"):
        if file.endswith(".py") and file != "__init__.py":
            config = dict()
            execfile("./FileInfo/montecarlo/%s" % (file), config)
            info = config["info"]
            return info.keys()

def getHistograms(analysis, selection):
    with open("./PlotObjects/%s/%s.json" % (analysis, selection)) as ofile:
        info = json.load(ofile)
    return info.keys()
        
def getHistogramInfo(analysis, selection, histogram):
    with open("./PlotObjects/%s/%s.json" % (analysis, selection)) as ofile:
        info = json.load(ofile)
    return info[histogram]


 #############################################
 #  __   ____ ______ ______  ____ ____   __  #
 # (( \ ||    | || | | || | ||    || \\ (( \ #
 #  \\  ||==    ||     ||   ||==  ||_//  \\  #
 # \_)) ||___   ||     ||   ||___ || \\ \_)) #
 #############################################
    

def addPlotGroup(analysis, group_name):
    config = dict()
    execfile("./PlotGroups/%s.py" % (analysis), config)
    info = config["info"]
    # creates a dictionary called info
    tmpdict = {}
    # Template:
    #     Name
    #     Style
    #     Members
    Name = raw_input("What is the official name of the Group: ")
    Style = "fill-yellow"
    Members = []
    tmpdict["Name"] = Name
    tmpdict["Style"] = Style
    tmpdict["Members"] = []
    info[group_name] = tmpdict
    with open("./PlotGroups/%s.py" % (analysis),'w') as ofile:
        ofile.write("info ="+ json.dumps(info, indent=4))

def addMCItem(name):
    config = dict()
    execfile("./FileInfo/montecarlo/montecarlo_2016.py", config)
    info = config["info"]
    # creates a dictionary called info
    tmpdict = {}
    # Template:
    #     Name
    #     Style
    #     Members
    cross_section = raw_input("What is cross section of the Event: ")
    tmpdict["cross_section"] = cross_section
    tmpdict["Source of cross section"] = ""
    tmpdict["DAS Name"] = ""
    tmpdict["Generator"] = ""
    tmpdict["Cards"] = ""
    print "You will need to manually put in generation info!"
    print
    info[name] = tmpdict
    with open("./FileInfo/montecarlo/montecarlo_2016.py",'w') as ofile:
        ofile.write("info ="+ json.dumps(info, indent=4))

def addMemeber(analysis, group_name, member):
    config = dict()
    execfile("./PlotGroups/%s.py" % (analysis), config)
    info = config["info"]
    # creates a dictionary called info
    info[group_name]["Members"].append(member)
    with open("./PlotGroups/%s.py" % (analysis),'w') as ofile:
        ofile.write("info ="+ json.dumps(info, indent=4))
        
        
def addFileInfo(analysis, selection, name, plot_group, file_path):
    config = dict()
    execfile("./FileInfo/%s/%s.py" % (analysis, selection), config)
    info = config["info"]
    # creates a dictionary called info
    tmpdict = {}
    # Template:
    #     plot_group
    #     file_path
    tmpdict["plot_group"] = plot_group
    tmpdict["file_path"] = file_path
    info[name] = tmpdict
    with open("./FileInfo/%s/%s.py" % (analysis, selection),'w') as ofile:
        ofile.write("info ="+ json.dumps(info, indent=4))


def addPlotObject(analysis, selection, inpVars):
    with open("./PlotObjects/%s/%s.json" % (analysis, selection)) as ofile:
        info = json.load(ofile)

    # creates a dictionary called info
    tmpdict = {}
    # Template:
    #     type
    #     nbins
    #     xmin
    #     xmax
    #     Xaxis Title
    #     Yaxis Title
    name = inpVars.pop(0)
    tmpdict["Initialize"] = {}
    tmpdict["Attributes"] = {}
    tmpdict["Initialize"]["type"] = "TH1F"
    tmpdict["Initialize"]["nbins"] = inpVars.pop(0)
    tmpdict["Initialize"]["xmin"] = inpVars.pop(0)
    tmpdict["Initialize"]["xmax"] = inpVars.pop(0)
    tmpdict["Attributes"]["GetXaxis().SetTitle"] = inpVars.pop(0)
    tmpdict["Attributes"]["GetYaxis().SetTitle"] = inpVars.pop(0)
    tmpdict["Attributes"]["GetYaxis().SetTitleOffset"] = 1.3
    tmpdict["Attributes"]["SetMinimum"] = 0.1
    tmpdict["Attributes"]["SetMaximum"] = 3000
    info[name]=tmpdict
    with open("./PlotObjects/%s/%s.json" % (analysis, selection),'w') as ofile:
        ofile.write(json.dumps(info, indent=4))

