#!/usr/bin/env python
import os
import json
import argparse
from modifyHelper import *

"""
Weird code I wrote to set global variables of analysis etc.
Call the ana(), sel(), inp() and it takes care of finding choices
and picking a choice

TODO: allow ability to add ana, sel, inp, etc
"""

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


    
def menu(beginText, lister):
    """
    Takes list of options and print text and chooses one of those options
      Does all of the checking that it's a valid choice so it return only
      good options
    """
    print beginText
    returnText = ""

    
    half = int((len(lister)+1)/2)
    for i in xrange(int((len(lister))/2)):
        print "%2s: %-25s %2s: %-25s" % (i+1, lister[i], i+half+1, lister[i+half])
    if len(lister) % 2 == 1:
        print "%2s: %-25s" % (half, lister[half-1])
        
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

#################################################################
# Main functions used for setting up Adding things to the files #
# based on the names in the main menu.                          #
# NOTE: capital "Add" used to note this is a menu option        #
#################################################################

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


def AddFile(ana, inp, file_path):
    #### to do
    groups=getGroups(ana)
    groups.append("New Group")
    group_choice = menu("Which group will this go with?", groups)
    if group_choice == "New Group":
        group_choice  = raw_input("What is abbreviated name of the Group: ")
        addPlotGroup(ana, group_choice)
        print
    
    mcList = getMCNames()
    mcList.sort()
    mcList.append("New Name")
    mc_choice = menu("What do you want to name it", mcList)
    if mc_choice == "New Name":
        mc_choice = raw_input("What do you want the new Name to be: ")
        addMCItem(mc_choice)
        print
        
    addFileInfo(ana, inp, mc_choice, group_choice, file_path)
    addMember(ana, group_choice, mc_choice)
    return


 ############################
 # ___  ___  ___  __ __  __ #
 # ||\\//|| // \\ || ||\ || #
 # || \/ || ||=|| || ||\\|| #
 # ||    || || || || || \|| #
 ############################


parser = argparse.ArgumentParser()
parser.add_argument("-s", "--selection", type=str, default="",
                    help="Name of selection to make, "
                    " as defined in Cuts/<analysis>/<selection>.json")
parser.add_argument("-a", "--analysis", type=str, required=False, default="",
                    help="Analysis name, used in selecting the cut json")
parser.add_argument("-i", "--input_tier", type=str, default="",required=False)
                    
parser.add_argument("--AddFile", type=str, default="",
                    help="Go straight to AddFile and add filename given")
parser.add_argument("--AddHistogram", action='store_true',
                    help="Go straight to AddHistogram and add filename given")


args = parser.parse_args()
Analysis = args.analysis
Selection = args.selection
InputTier = args.input_tier



if args.AddFile:
    AddFile(ana(), inp(), args.AddFile)
    exit(0)
elif args.AddHistogram:
    AddHistogram(ana(), sel())
    exit(0)

#############
# Main Menu #
#############
    
actionList = ["Add a File", "Add a Histogram", "List Data", "List MC", "List Histograms", "Quit"]
while True:
    action = menu("What action do you want to do?", actionList)
    # Add a file
    if action == "Add a File":
        file_path=raw_input("What is the File Path: ")
        AddFile(ana(), inp(), file_path)

    # Add a Histogram
    elif action == "Add a Histogram":
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

