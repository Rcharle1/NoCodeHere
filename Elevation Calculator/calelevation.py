####
#calelevation.py
#Raheem Charles
######




from elevateinto import *
from client import *
from Tkinter import Tk, Label, Button, Entry, StringVar,DoubleVar,END, W, E
import datetime
import os.path






class GeoGUI:
    def __init__(self, master):
        self.master = master
        master.title("GeoGUI")
        self.w= "W:"
        self.inputw=0
        self.e= "E:"
        self.inpute=0
        self.s= "S:"
        self.inputs=0
        self.n= "N:"
        self.inputn=0
        self.r= "Resolution:"
        self.inputr=0
        self.lele= "Lower Elevation Limits:"
        self.inputlele=-40000
        self.hele= "Higher Elevation Limits:"
        self.inputhele=40000
        self.step= "Step size:"
        self.inputstep=.1

        
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
        self.r_label_text = DoubleVar()
        self.r_label = Label(master, textvariable=self.r_label_text)        
        self.r_label_text.set(self.r)  
        self.lele_label_text = DoubleVar()
        self.lele_label = Label(master, textvariable=self.lele_label_text)        
        self.lele_label_text.set(self.lele) 
        self.hele_label_text = DoubleVar()
        self.hele_label = Label(master, textvariable=self.hele_label_text)        
        self.hele_label_text.set(self.hele) 
        self.step_label_text = DoubleVar()
        self.step_label = Label(master, textvariable=self.step_label_text)        
        self.step_label_text.set(self.step) 
        self.label = Label(master, text="W:")
        self.label = Label(master, text="E:")
        self.label = Label(master, text="N:")
        self.label = Label(master, text="S:")
        self.label = Label(master, text="Resolution:")
        self.label = Label(master, text="Lower Elevation Limits:")
        self.label = Label(master, text="Higher Elevation Limits:")
        self.label = Label(master, text="Step size:")
        wvcmd = master.register(self.wvalidate)
        evcmd = master.register(self.evalidate)
        svcmd = master.register(self.svalidate)
        nvcmd = master.register(self.nvalidate)
        rvcmd = master.register(self.rvalidate) 
        lelevcmd = master.register(self.lelevalidate)
        helevcmd = master.register(self.helevalidate)
        stepvcmd = master.register(self.stepvalidate) # we have to wrap the command
        self.entryw = Entry(master, validate="key", validatecommand=(wvcmd, '%s'))
        self.entrye = Entry(master, validate="key", validatecommand=(evcmd, '%s'))
        self.entrys = Entry(master, validate="key", validatecommand=(svcmd, '%s'))
        self.entryn = Entry(master, validate="key", validatecommand=(nvcmd, '%s'))
        self.entryr = Entry(master, validate="key", validatecommand=(rvcmd, '%P'))
        self.entrylele = Entry(master, validate="key", validatecommand=(lelevcmd, '%P'))     
        self.entryhele = Entry(master, validate="key", validatecommand=(helevcmd, '%P'))     
        self.entrystep = Entry(master, validate="key", validatecommand=(stepvcmd, '%P'))       
     

        self.w_label.pack()
        self.entryw.pack()
        self.e_label.pack()
        self.entrye.pack()
        self.s_label.pack()
        self.entrys.pack()
        self.n_label.pack()
        self.entryn.pack()
        self.r_label.pack()
        self.entryr.pack()
        self.lele_label.pack()
        self.entrylele.pack()
        self.hele_label.pack()
        self.entryhele.pack()
        self.step_label.pack()
        self.entrystep.pack()


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


    def rvalidate(self, new_text):
        if not new_text: # the field is being cleared
            self.inputr = 0
            return True

        try:
            self.inputr = int(new_text)
            return True
        except ValueError:
            return False

    def lelevalidate(self, new_text):
        if not new_text: # the field is being cleared
           
            return True

        try:
            self.inputlele = float(new_text)
            return True
        except ValueError:
            return False

    def helevalidate(self, new_text):
        if not new_text: # the field is being cleared
            
            return True

        try:
            self.inputhele = float(new_text)
            return True
        except ValueError:
            return False

    def stepvalidate(self, new_text):
        if not new_text: # the field is being cleared
            
            return True

        try:
            self.inputstep = float(new_text)
            return True
        except ValueError:
            return False
    
    


    
    def run(self):
        locations=[]
        tstamp= str(datetime.datetime.now())

        
        foutname= os.path.join(os.path.expanduser("~"),"Documents",tstamp+".ascii")
        fout = open(foutname, 'w')
        w=self.inputw
        s= self.inputs
        while s <= self.inputn:
           
            while w <= self.inpute+.1:
                locations.append((w,s))
                w+=self.inputstep
               

            getElevation(locations,self.inputr,self.inputlele,self.inputhele,fout)
            s+=self.inputstep
            w=self.inputw
            #print(self.inputs)
            locations=[]
        
        fout.close()
        
        




def getElevation(locations,resolution,minE,maxE,fout):
        googlemapsClient = Client("AIzaSyBOt8PEJIU909tppPkEUmu7rooeQ3KLS1Y")
        elevationlist=elevation_along_path(googlemapsClient,locations,resolution)
      

        
        for i in range(len(elevationlist)-1):
            if elevationlist[i][u'elevation'] < minE and elevationlist[i][u'elevation'] > maxE:
                fout.write(str(elevationlist[i][u'location'][u'lng'])+","+str(elevationlist[i][u'location'][u'lat'])+","+str(0)+"\n")
            else:
                fout.write(str(elevationlist[i][u'location'][u'lng'])+","+str(elevationlist[i][u'location'][u'lat'])+","+str(elevationlist[i][u'elevation'])+"\n")
        
        
def main():
    
    
    root = Tk()
    my_gui = GeoGUI(root)
    root.mainloop()




main()
