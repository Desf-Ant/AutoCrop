from PIL import Image
import csv

class AutoCropCore :

    def __init__ (self):
        self.view = None
        self.csvPath = ""
        self.folderCsv = ""
        self.finalFolderPath = ""
        self.hasHeader = False

    def setView(self,view) :
        self.view = view

    def sendCSVPath(self, path):
        self.csvPath = path

    def sendFinalFolder(self,path) :
        self.finalFolderPath = path

    def sendChangeHeader(self, state) :
        self.hasHeader = state

    def startCropping(self) :
        self.getFolderPath()
        if self.csvPath == "" or self.finalFolderPath == "" :
            self.view.showAlert("You need to fill in all fields")
            return
        self.croppingProcess()

    def croppingProcess(self) :
        with open(self.csvPath, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader) :
                index = i if self.hasHeader else i+1
                if self.hasHeader and i == 0 : continue
                img = Image.open(self.folderCsv+"/"+row[0])
                img_res = img.crop((int(row[1]), int(row[2]), int(row[3]), int(row[4])))
                img_res.save(self.finalFolderPath + "/" + row[5] + self.reIndex(index)+".jpg")
        self.view.showAlert("Finish !")

    def getFolderPath(self):
        temp = self.csvPath.split("/")
        del temp[-1]
        for i in range(len(temp)) :
            if i == 0 : self.folderCsv += temp[i]
            else : self.folderCsv += "/" + temp[i]

    def reIndex(self, index) :
        i = str(index)
        while (len(i) < 5) :
            i = '0'+i
        return i
