import pyflp
import os

project = 0
dir = "C://Users/robat/Escritorio/Progra_Workspace/FL_Time/flps"
global files

flFiles = []

def consoleView():
    findFiles()
    print("\n\n")

    flFiles = findFiles()

    for i in range(len(flFiles)):
        # print(findFiles()[i])

        project = pyflp.parse(flFiles()[i])
        projectTitle = pyflp.FLP_HEADER
        time = project.time_spent
        print(projectTitle)

def getFileName(dir):
    fileNames = []
    for i in range(len(dir)):
            if i == dir.rfind("/"):
                fileNames += [dir[i+1:len(dir)]]
    return fileNames

def findFiles():
    result = []
    filesInDir = []
    fileNames = []
    ints = [1, 2, 3, 4]
    # if inputted dir is a file
    if os.path.isfile(dir):
        filesInDir = getFileName(dir)
    else: # if inputted dir is a folder dir
        print("Checking which files in dir are .flp files  . . . \n")
        for i in range(len(os.listdir(dir))):
            filesInDir += [dir + "/" + os.listdir(dir)[i]]
            fileNames += [getFileName(filesInDir[i])]

            if filesInDir[i].endswith(".flp"):
                print(filesInDir[i] + " is an FL Studio file")
                result += [filesInDir[i]]
    return result
    # print(fileNames)

# def timeLookout():
#     for i in 

# class Gui:
#     import PySimpleGUI as gui
    
#     print("Bye World")

#     title = "FL TIME"
#     font = ("Cascadia Code", 40)
#     margins = (50, 50)

#     backgroundColor = '#222831'
#     buttonColor = "#76ABAE"
#     gui.theme = backgroundColor

#     layout = [[gui.Text(title, size=(0, 0), key="TITLE", font=font, background_color=backgroundColor)], 
#             [gui.Text("Directory", background_color=backgroundColor)], 
#             [gui.In(size=(25, 1), enable_events=True, key="LINK")], 
#             [gui.Text("Files Found: ", background_color=backgroundColor)],
#             [gui.Text("Hours: ", background_color=backgroundColor)],
#             [gui.Text("Minutes: ", background_color=backgroundColor)],
#             [gui.Text("Seconds: ", background_color=backgroundColor)],
#             [gui.Button("DOWNLOAD", button_color=buttonColor)]]
    
#     window = gui.Window(title, layout, margins=margins, background_color=backgroundColor)

#     while True:
#         event, values = window.read()

#         if event == "Exit" or event == gui.WIN_CLOSED or event == "OK_WARN":
#             break

#     window.close()
    
def main():
    print("Hello World")
    consoleView()
    
main()
# Gui()