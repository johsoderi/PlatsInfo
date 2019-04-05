#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# Course: Programmering och Systemering - DevOps2018 @ Nackademin
# Johannes Söderberg Eriksson, 2018
#
# This is a script for making a "font" for scripts running on ANSI terminals.
# It uses img_term.py by Jonathan Mackenzie (https://github.com/JonnoFTW/img_term),
# to convert PNG images of letters into TXT files with 8-bit color codes.
# The image file names should be the character it represents, followed by the pixel width, two digits.
# Special characters and punctuation are defined in the code.
# This script is part of another project of mine, "Plats-Info".
#-----------------------------------------------------------------------------------------------------
import os
import platform

path = os.path.dirname(os.path.abspath(__file__)) + "/"
print(path)

class Image:
    def __init__(self, name, width, outName):
        self.path = path
        self.name = name
        self.outName = outName
        self.width = str(width)
        self.width = str(width).zfill(2)
        self.result = ""
        self.convert()
    def convert(self):
        try:
            self.result = os.system("python3 " + self.path + "img_term.py -img " + self.path\
            + self.name + " -width " + self.width + " -col 8 > " + self.path + self.outName)
        except:
            print(f"[IMG ERROR]")
        # Since img_term.py puts some ANSI code stuff in the beginning and end of the file that I
        # don't want, the bytes in question are cut off:
        with open(self.path + self.outName, "rb") as f:
            bytes_read = f.read()
        cut_bytes = bytes_read[9:-5]
        with open(self.path + self.outName, "wb") as f:
            f.write(self.width.encode('utf-8') + cut_bytes)
        return self.result

pathUpper = path + "font_png/upper/"
pathLower = path + "font_png/lower/"
pathOther = path + "font_png/other/"
pathNumbers = path + "font_png/numbers/"

def convertUpper():
    upperCaseFiles = os.listdir(pathUpper)
    for item in range(len(upperCaseFiles)):
        if upperCaseFiles[item][0] != ".": # Don't process hidden system files
            unicodeName = hex(ord(upperCaseFiles[item][0])) # Get the unicode for the first letter in the file name
            try: # The letter Å for example counts as two chars (A and  ̊) so we need an offset in those cases.
                charWidth = int(upperCaseFiles[item][1:3])
            except ValueError:
                charWidth = upperCaseFiles[item][2:4]
                if upperCaseFiles[item][0:2] == "AA": unicodeName = hex(ord("Å"))
                if upperCaseFiles[item][0:2] == "AE": unicodeName = hex(ord("Ä"))
                if upperCaseFiles[item][0:2] == "OE": unicodeName = hex(ord("Ö"))
            inputName = upperCaseFiles[item]
            print("Character:",chr(int(unicodeName, 16)),"Input:",upperCaseFiles[item],"Output:",unicodeName+".txt","Width:", charWidth)
            A = Image(name="font_png/upper/" + inputName, outName="font_txt/" + unicodeName + ".txt", width=charWidth)

def convertLower():
    lowerCaseFiles = os.listdir(pathLower)
    for item in range(len(lowerCaseFiles)):
        if lowerCaseFiles[item][0] != ".": # Don't process hidden system files
            unicodeName = hex(ord(lowerCaseFiles[item][0])) # Get the unicode for the first letter in the file name
            try: # The letter Å for example counts as two chars (A and  ̊) so we need an offset in those cases.
                charWidth = int(lowerCaseFiles[item][1:3])
            except ValueError:
                charWidth = lowerCaseFiles[item][2:4]
                if lowerCaseFiles[item][0:2] == "aa": unicodeName = hex(ord("å"))
                if lowerCaseFiles[item][0:2] == "ae": unicodeName = hex(ord("ä"))
                if lowerCaseFiles[item][0:2] == "oe": unicodeName = hex(ord("ö"))
            inputName = lowerCaseFiles[item]
            print("Character:",chr(int(unicodeName, 16)),"Input:",lowerCaseFiles[item],"Output:",unicodeName+".txt","Width:", charWidth)
            A = Image(name="font_png/lower/" + inputName, outName="font_txt/" + unicodeName + ".txt", width=charWidth)

def convertNumbers():
    numbersCaseFiles = os.listdir(pathNumbers)
    for item in range(len(numbersCaseFiles)):
        if numbersCaseFiles[item][0] != ".": # Don't process hidden system files
            unicodeName = hex(ord(numbersCaseFiles[item][0])) # Get the unicode for the first letter in the file name
            charWidth = int(numbersCaseFiles[item][1:3])
            inputName = numbersCaseFiles[item]
            print("Character:",chr(int(unicodeName, 16)),"Input:",numbersCaseFiles[item],"Output:",unicodeName+".txt","Width:", charWidth)
            A = Image(name="font_png/numbers/" + inputName, outName="font_txt/" + unicodeName + ".txt", width=charWidth)

def convertOther():
    otherCaseFiles = os.listdir(pathOther)
    for item in range(len(otherCaseFiles)):
        if otherCaseFiles[item][0] != ".": # Don't process hidden system files
            charWidth = int(otherCaseFiles[item][4:6])
            if otherCaseFiles[item][0:4] == "dash":
                unicodeName = hex(ord("-"))
            if otherCaseFiles[item][0:4] == "spac":
                unicodeName = hex(ord(" "))
            if otherCaseFiles[item][0:4] == "excl":
                unicodeName = hex(ord("!"))
            if otherCaseFiles[item][0:4] == "ques":
                unicodeName = hex(ord("?"))
            if otherCaseFiles[item][0:4] == "ampe":
                unicodeName = hex(ord("&"))
            if otherCaseFiles[item][0:4] == "aste":
                unicodeName = hex(ord("*"))
            if otherCaseFiles[item][0:4] == "bsla":
                unicodeName = hex(ord("\\"))
            if otherCaseFiles[item][0:4] == "colo":
                unicodeName = hex(ord(":"))
            if otherCaseFiles[item][0:4] == "comm":
                unicodeName = hex(ord(","))
            if otherCaseFiles[item][0:4] == "doll":
                unicodeName = hex(ord("$"))
            if otherCaseFiles[item][0:4] == "dots":
                unicodeName = hex(ord("¨"))
            if otherCaseFiles[item][0:4] == "dquo":
                unicodeName = hex(ord("\""))
            if otherCaseFiles[item][0:4] == "equa":
                unicodeName = hex(ord("="))
            if otherCaseFiles[item][0:4] == "fsla":
                unicodeName = hex(ord("/"))
            if otherCaseFiles[item][0:4] == "hash":
                unicodeName = hex(ord("#"))
            if otherCaseFiles[item][0:4] == "less":
                unicodeName = hex(ord("<"))
            if otherCaseFiles[item][0:4] == "lpar":
                unicodeName = hex(ord("("))
            if otherCaseFiles[item][0:4] == "more":
                unicodeName = hex(ord(">"))
            if otherCaseFiles[item][0:4] == "perc":
                unicodeName = hex(ord("%"))
            if otherCaseFiles[item][0:4] == "peri":
                unicodeName = hex(ord("."))
            if otherCaseFiles[item][0:4] == "plus":
                unicodeName = hex(ord("+"))
            if otherCaseFiles[item][0:4] == "rpar":
                unicodeName = hex(ord(")"))
            if otherCaseFiles[item][0:4] == "semi":
                unicodeName = hex(ord(";"))
            if otherCaseFiles[item][0:4] == "squo":
                unicodeName = hex(ord("'"))
            if otherCaseFiles[item][0:4] == "tild":
                unicodeName = hex(ord("~"))
            if otherCaseFiles[item][0:4] == "upxx":
                unicodeName = hex(ord("^"))
            if otherCaseFiles[item][0:4] == "usco":
                unicodeName = hex(ord("_"))
            if otherCaseFiles[item][0:4] == "xxx1":
                unicodeName = hex(ord("´"))
            if otherCaseFiles[item][0:4] == "xxx2":
                unicodeName = hex(ord("`"))
            inputName = otherCaseFiles[item]
            print("Character:",chr(int(unicodeName, 16)),"Input:",otherCaseFiles[item],"Output:",unicodeName+".txt","Width:", charWidth)
            A = Image(name="font_png/other/" + inputName, outName="font_txt/" + unicodeName + ".txt", width=charWidth)

def displayText(text):
    X = [""]*len(text)
    wordLine = [""]*10
    for letter in range(len(text)):
        value = hex(ord(text[letter]))
        with open(path + "font_txt/" + str(value) + ".txt", "r") as f:
            X[letter] = f.readlines()
        X[letter][0] = X[letter][0][2:]
    for line in range(10):
        for letter in range(len(text)):
            wordLine[line] += X[letter][line].rstrip()
    for i in range(len(wordLine)):
        print(wordLine[i], end='\33[0m\n')

def displayTextWrapped(text):
    termWidth = 80
    X = [""]*len(text)
    lettersTotal = 0
    wordLine = [""]*10
    lineColLength = 0
    lineCharLength = 0
    for letter in range(len(text)):
        value = hex(ord(text[letter]))
        with open(path + "font_txt/" + str(value) + ".txt", "r") as f:
            X[letter] = f.readlines()
        charWidth = X[letter][0][0:2]
        lineColLength += int(charWidth)
        lineCharLength += 1
        X[letter][0] = X[letter][0][2:]
        if lineColLength > (termWidth-10):
            lineFinal = lineCharLength
            for line in range(10):
                for letter in range(lineFinal):
                    wordLine[line] += X[lettersTotal+letter][line].rstrip()
            for i in range(len(wordLine)):
                print(wordLine[i], end='\33[0m\n') # '\33[38;5;233;48;5;233m'
            lettersTotal += lineFinal
            lineColLength = 0
            lineCharLength = 0
            wordLine = [""]*10
    lineFinal = lineCharLength
    for line in range(10):
        for letter in range(lineFinal):
            wordLine[line] += X[lettersTotal+letter][line].rstrip()
    for i in range(len(wordLine)):
        print(wordLine[i], end='\33[0m\n') # '\33[38;5;233;48;5;233m'



os.system("clear")
# convertLower()
# convertUpper()
# convertNumbers()
# convertOther()

displayTextWrapped("AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÅåÄäÖö")
displayTextWrapped("0123456789")
displayTextWrapped("The quick brown fox jumped over the lazy dog")
