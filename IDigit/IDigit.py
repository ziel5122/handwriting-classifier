import Tkinter
from Tkinter import *
import tkFont
from PIL import Image, ImageTk
from tkFileDialog import askopenfilename
import pygame
from Drawpad import DrawPad
import Classifier
import Banana

class IDigit():
	def __init__(self, master, num_neighbors):
	    self.frame = Frame(master, width=200, height=500)
	    self.frame.pack()
	    self.button_frame = Frame(master, width=600, height=100)
	    self.button_frame.pack()
	    
	    self.buildClassifiers(num_neighbors)
	    
	    self.first = True

	def addButton(self, t, f, fg, bg, afg, abg, c, w, s):
		Button(self.button_frame, text=t, font=f, fg=fg, bg=bg, activeforeground=afg, activebackground=abg, command=c, width=w).pack(side=s)
	
	def buildClassifiers(self, num_neighbors):
	    self.KNN8 = Classifier.initializeClassifier(num_neighbors)
	    self.KNNM = Classifier.initializeKNNMNISTsmall(num_neighbors)
	
	def classifyButton(self):
	    if (self.first == True):
	        Button(self.frame, text="C\nL\nA\nS\nS\nI\nF\nY", font=tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD), fg="black", bg="#b6b6b6", activeforeground="white", activebackground="#4d4d4d", command=self.classify88, width=2).pack(side=LEFT) 
	        self.label = Tkinter.Label(self.frame, image=self.tkimage)
	        self.label.pack(side=LEFT)
	        Button(self.frame, text="C\nL\nA\nS\nS\nI\nF\nY", font=tkFont.Font(family="Courier", size=21, weight=tkFont.BOLD), fg="white", bg="#4d4d4d", activeforeground="black", activebackground="#b6b6b6", command=self.classifyMNIST, width=2).pack(side=LEFT) 
	    else:
	        self.label.config(image=self.tkimage)
	        	
	def classify88(self):
	    image = Banana.getSquare(self.image, 200)
	    image = image.convert('L')
	    image.thumbnail((8,8))
	    data = []
	    width, height = image.size
	    pixels = image.load()
	    for h in range(0, height):
	        for w in range(0, width):
	            percentage = float(pixels[w,h]) / 255
	            other_percentage = 1 - percentage
	            data.append(16 * other_percentage)
	    print self.KNN8.predict(data)
	    
	def classifyMNIST(self):
	    image = Banana.getSquare(self.image, 200)
	    image = image.convert('L')
	    image.thumbnail((20,20))
	    new_image = Image.new("RGBA", (28, 28)).convert('L')
	    data = []
	    width, height = new_image.size
	    pixels = image.load()
	    for h in range(0, height):
	        for w in range(0, width):
	            if (w < 4 or w > 23 or h < 4 or h > 23):
	                data.append(0)
	            else:
	                data.append(255 - pixels[w-4,h-4])
	    print self.KNNM.predict(data)
	
	def drawpad(self):
		self.pad = DrawPad((300, 300), "white")
		self.pad.draw(10)
		self.setImage(self.pad.getImage())
		
	def setImage(self, image=None):
		if (image == None):
		    file_ = askopenfilename()
		    self.image = Image.open(file_)
		else:
			self.image = image
		self.tkimage = ImageTk.PhotoImage(self.image)
		self.classifyButton()
		self.first = False
		
			
