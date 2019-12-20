####
#Raheem Charles
#10/19/2020
#httprequest.py
import requests
import sys
from Tkinter import Tk, Label, Button, Entry, StringVar,DoubleVar,END, W, E


class GeoGUI:
    def __init__(self, master):
        self.master = master
        master.title("GeoGUI")
        self.w= "X Min:"
        self.inputw=0
        self.e= "X Max:"
        self.inpute=0
        self.s= "Y Min:"
        self.inputs=0
        self.n= "Y Max:"
        self.inputn=0


        
        self.w_label_text = StringVar()
        self.w_label = Label(master, textvariable=self.w_label_text)     
        self.w_label_text.set(self.w)
        self.e_label_text = StringVar()
        self.e_label = Label(master, textvariable=self.e_label_text)
        self.e_label_text.set(self.e)
        self.n_label_text = StringVar()
        self.n_label = Label(master, textvariable=self.n_label_text)
        self.n_label_text.set(self.n)
        self.s_label_text = StringVar()
        self.s_label = Label(master, textvariable=self.s_label_text)        
        self.s_label_text.set(self.s)  
 
        self.label = Label(master, text="X min:")
        self.label = Label(master, text="X max:")
        self.label = Label(master, text="Y min:")
        self.label = Label(master, text="Y max:")
   
        wvcmd = master.register(self.wvalidate)
        evcmd = master.register(self.evalidate)
        svcmd = master.register(self.svalidate)
        nvcmd = master.register(self.nvalidate)
        
        # we have to wrap the command
        self.entryw = Entry(master, validate="key", validatecommand=(wvcmd, '%s'))
        self.entrye = Entry(master, validate="key", validatecommand=(evcmd, '%s'))
        self.entrys = Entry(master, validate="key", validatecommand=(svcmd, '%s'))
        self.entryn = Entry(master, validate="key", validatecommand=(nvcmd, '%s'))
   
     

        self.w_label.pack()
        self.entryw.pack()
        self.e_label.pack()
        self.entrye.pack()
        self.s_label.pack()
        self.entrys.pack()
        self.n_label.pack()
        self.entryn.pack()
       


        self.run_button = Button(master, text="Run", command=self.run)
        self.run_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


        

        
    
    def evalidate(self, new_text):
        if not new_text: # the field is being cleared
            self.inpute = 0
            return True

        try:
    
            self.inpute = float(new_text)
            print(self.inpute)
            return True
        except ValueError:
            if  new_text[0] == "-":
                self.inpute=-1
                return True
            return False

    def wvalidate(self, new_text):
        if not new_text: # the field is being cleared
            self.inputw = 0
            return True

        try:
            self.inputw = float(new_text)
            print(self.inputw)
            return True
        except ValueError:
            if  new_text[0] == "-":
                self.inputw=-1
                return True
            return False

    def nvalidate(self, new_text):
        if not new_text: # the field is being cleared
            self.inputn = 0
            return True
        try:

            self.inputn = float(new_text)
            print(self.inputn)
            return True
        except ValueError:
            if  new_text[0] == "-":
                self.inputn=-1
                return True
            return False

    def svalidate(self, new_text):
        if not new_text: # the field is being cleared
            self.inputs = 0
            return True

        try:

            self.inputs = float(new_text)
            print(self.inputs)
            return True
        except ValueError:
            if  new_text[0] == "-":
                self.inputs=-1
                return True
            return False

    def run(self):
        getMap(self.inputs,self.inputw,self.inputn,self.inpute)



def getMap(xmin,ymin,xmax,ymax):
    url="https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WCSServer?request=GetCoverage&service=WCS&version=1.1.2&format=image/GeoTIFF&identifier=DEP3Elevation&crs=3857&boundingBox="+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+",urn:ogc:def:crs:EPSG::4326&store=true"
    r = requests.get(url) 
    print(r.text)

def main():
        
    
    root = Tk()
    my_gui = GeoGUI(root)
    root.mainloop()
     #-108.373,38.836,-108.352,38.843
    #getMap("https://elevation.nationalmap.gov/arcgis/services/3DEPElevation/ImageServer/WCSServer?request=GetCoverage&service=WCS&version=1.1.2&format=image/GeoTIFF&identifier=DEP3Elevation&crs=3857&boundingBox="+str(xmin)+","+str(ymin)+","+str(xmax)+","+str(ymax)+",urn:ogc:def:crs:EPSG::4326&store=true")



main()