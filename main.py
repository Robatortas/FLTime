import pyflp
import os

import pyflp.project

project = 0
# dir = "C://Users/robat/Escritorio/Progra_Workspace/FL_Time/flps"

flFiles = []
times = []
numFiles = 0
totalTime = 0

def consoleView():
    print("FLTime : by NoFall.")

def findFiles(dir):
    filesInDir = []
    fileNames = []
    global numFiles
    try:
        numFiles = len(os.listdir(dir))
        # if inputted dir is a file
        if os.path.isfile(dir):
            filesInDir = getFileName(dir)
        else: # if inputted dir is a folder dir
            print("Checking which files in dir are .flp files  . . . \n")
            for i in range(numFiles):
                filesInDir += [dir + "/" + os.listdir(dir)[i]]
                fileNames += [getFileName(filesInDir[i])]

                if filesInDir[i].endswith(".flp"):
                    print(filesInDir[i] + " is an FL Studio file")
                    flFiles.append(filesInDir[i])
    except:
        print("Couldn't find specified path !")
    return flFiles

def getFileName(dir):
    fileNames = []
    for i in range(len(dir)):
            if i == dir.rfind("/"):
                fileNames += [dir[i+1:len(dir)]]
    return fileNames

def getMetaData():
    global numFiles
    print(numFiles)
    for i in range(numFiles):
        global project
        global projectTitle
        global time
        project = pyflp.parse(flFiles[i-1])
        projectTitle = project.title
        time = project.time_spent
        print(projectTitle)
        global totalTime
        calcTotalTime(time)
        # totalTime += times[i]
        # print("TOTALTIME")
        # print(totalTime)

# Parse time string to divide into three sections
def calcTotalTime(time): 
    hours = 0
    mins = 0
    secs = 0

    

class Gui:
    import PySimpleGUI as gui

    title = "FL TIME"
    font = ("Cascadia Code", 40)
    margins = (50, 50)

    backgroundColor = '#222831'
    buttonColor = "#76ABAE"
    gui.theme = backgroundColor

    layout = [[gui.Text(title, size=(0, 0), key="TITLE", font=font, background_color=backgroundColor)], 
            [gui.Text("Directory", background_color=backgroundColor)],
            [gui.In(size=(25, 1), enable_events=True, key="CHOSEN_PATH")],  [gui.FolderBrowse(button_color=buttonColor, key="BROWSE")],
            [gui.Text("Files Found: " + str(numFiles), background_color=backgroundColor)],
            [gui.Text("Hours: ", background_color=backgroundColor)],
            [gui.Text("Minutes: ", background_color=backgroundColor)],
            [gui.Text("Seconds: ", background_color=backgroundColor)],
            [gui.Button("DOWNLOAD", button_color=buttonColor)]]
    
    window = gui.Window(title, layout, margins=margins, background_color=backgroundColor)

    while True:
        event, values = window.read()

        if(event == "BROWSE"):
            values["CHOSE_PATH"] = values["BROWSE"]

        if(event == "CHOSEN_PATH"):
            chosenPath = str(values["CHOSEN_PATH"])
            if(os.path.exists(chosenPath)):
                findFiles(chosenPath)
                getMetaData()
                print("Path Chosen: " + chosenPath)
                window.refresh()

        if event == "Exit" or event == gui.WIN_CLOSED or event == "OK_WARN":
            break

    window.close()
    
def main():
    consoleView()
    
main()
# Gui()