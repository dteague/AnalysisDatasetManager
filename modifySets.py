import os
import json

Analysis=""
InputTier=""
Selection=""

def ana():
    global Analysis
    if Analysis != "":
        return Analysis
    else:
        anaList = getAnalysis()
        if len(anaList) == 0:
            print "Can't find analysis!"
            exit(0)
        elif len(anaList) == 1:
            Analysis = anaList[0]
        else:
            Analysis = menu("Choose an Analysis to Modify", anaList)
        return Analysis

def inp():
    global InputTier
    if InputTier != "":
        return InputTier
    else:
        inputList = getInputs(ana())
        if len(inputList) == 0:
            print "Can't find InputTier!"
            exit(0)
        elif len(inputList) == 1:
            InputTier = inputList[0]
        else:
            InputTier = menu("Choose an InputTier to Modify", inputList)
        return InputTier

def sel():
    global Selection
    if Selection != "":
        return Selection
    else:
        selList = getSelections(ana())
        if len(selList) == 0:
            print "Can't find selection!"
            exit(0)
        elif len(selList) == 1:
            Selection = selList[0]
        else:
            Selection = menu("Choose an Selection to Modify", selList)
        return Selection


def checkAnalysis(analysis):
    if analysis not in os.listdir("./FileInfo"):
        return False
    elif analysis not in os.listdir("./PlotObjects"):
        return False
    else:
        return True

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
        if file.endswith(".json"):
            config = dict()
            execfile("./PlotGroups/%s.py" % (analysis), config)
            info = config["info"]
            if name in info:
                return info[name]
    return {}

def getHistograms(analysis, selection):
    with open("./PlotObjects/%s/%s.json" % (analysis, selection)) as ofile:
        info = json.load(ofile)
    return info.keys()
        
def getHistogramInfo(analysis, selection, histogram):
    with open("./PlotObjects/%s/%s.json" % (analysis, selection)) as ofile:
        info = json.load(ofile)
    return info[histogram]
    
    

def addPlotGroup(analysis):
    config = dict()
    execfile("./PlotGroups/%s.py" % (analysis), config)
    info = config["info"]
    # creates a dictionary called info
    tmpdict = {}
    # Template:
    #     Name
    #     Style
    #     Members
    group_name = raw_input("What is the file alias")
    Name = raw_input("What is the file alias")
    Style = raw_input("What is the plot group?")
    Members = []
    tmpdict["Name"] = Name
    tmpdict["Style"] = Sytle
    tmpdict["Members"] = Members
    info[name] = tmpdict
    print "info =", json.dumps(info)

def addFileInfo(analysis, selection):
    config = dict()
    execfile("./FileInfo/%s/%s.py" % (analysis, selection), config)
    info = config["info"]
    # creates a dictionary called info
    tmpdict = {}
    # Template:
    #     plot_group
    #     file_path
    name = raw_input("What is the file alias")
    plot_group = raw_input("What is the plot group?")
    file_path = raw_input("What is the file_path")
    tmpdict["plot_group"] = plot_group
    tmpdict["file_path"] = file_path
    info[name] = tmpdict
    print "info =", json.dumps(info, indent=4)

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

def AddHistogram(ana, sel):
    inpVars = []
    questions = ["What is the Name of the Histogram: ",
                 "What is the Number of bins: ",
                 "What is the low value: ",
                 "What is the high value: ",
                 "What is the X Axis Name: ",
                 "What is the Y Axis Name: ",
    ]
    for q in questions:
        try:
            answer = raw_input(q)
        except SyntaxError:
            answer = ""
        inpVars.append(answer)

    addPlotObject(ana, sel, inpVars)


def AddFile(ana, inp):
    #### to do
    return
    
    
def menu(beginText, lister):
    print beginText
    returnText = ""

    
    half = int((len(lister)+1)/2)
    for i in xrange(int((len(lister))/2)):
        print "%s: %-25s %s: %-25s" % (i+1, lister[i], i+half+1, lister[i+half])
    if len(lister) % 2 == 1:
        print "%s: %-25s" % (half, lister[half-1])
        
    ans=True
    while ans:
        ans=raw_input("$ ")
        try:
            choice = int(ans)
            if choice <= len(lister) and choice > 0:
                returnText = lister[choice-1]
                break
            else:
                print("\nNot Valid Choice Try again")
        except ValueError:
            print("\nNot Valid Choice Try again")

    print
    return returnText

    
actionList = ["Add a File", "Add a Histogram", "List Data", "List MC", "List Histograms", "Quit"]
while True:
    action = menu("What action do you want to do?", actionList)
    # Add a file
    if action == actionList[0]:
        AddFile(ana(), sel())

    # Add a Histogram
    elif action == actionList[1]:
        AddHistogram(ana(), sel())

    # List Data
    elif action == "List Data":
        files = getFiles(ana(), inp())
        for val in files:
            if "data" in val:
                print val
        print

    # List MC
    elif action == "List MC":
        files = getFiles(ana(), inp())
        for val in files:
            if "data" not in val:
                print val
        print            
    # List Histograms
    elif action == "List Histograms":
        hists = getHistograms(ana(), sel())
        hists.append("END")
        while True:
            histChoice = menu("Look at histogram info? (END to return to menu)", hists)
            if histChoice == hists[-1]:
                break
            else:
                print json.dumps(getHistogramInfo(Analysis, Selection, histChoice), indent=2)
                print

    # Quit
    elif action == actionList[-1]:
        print actionList[-1]
        break

