#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# Course: Programmering och Systemering - DevOps2018 @Nackademin, Stockholm, Sweden
# Project name: "Plats-Info"
# Author: Johannes Söderberg Eriksson
# Recommended Terminal settings:
# Size: 118*57
# Font: PT Mono Regular 12p, Line spacing: 0,929
# Declare as XTerm-256color. Display ANSI colors.

#----/ API KEYS /-----------------------------------------------------------------------------------#
gKey = "AIzaSyB4NL0TYfdKFSg5FjvbNsQkSWkhsfFtmpU"

#####| BEGIN STYLING CODE |##################################################################
#                                                                                           #
#     This is just a template I made for stuff I want in most projects...                   #
#                                                                                           #
#----/ Imports /-----------------------------------------------------------------------------
import os
import platform
#----/ Functions /---------------------------------------------------------------------------
def senBlirAlltSvart():                                                   # Clears the screen
    if (os.name == "posix"): os.system("clear")
    elif (platform.system() == "Windows"): os.system("cls")# I'll keep this in here, although
    else: pass						                       # this script is POSIX only.
def ln (newLines=1):                                 # ln() prints 1 new line. ln(3) prints 3
    print("\n" * newLines, end = "")
def mv(row, col):                                                          # Move text cursor
	print(f"\33[{row};{col}H",end="")
	return ""
#----/ Color & Style /-----------------------------------------------------------------------
# For a great overview of ANSI escape sequences, see:
# https://stackoverflow.com/a/33206814/4329563
e = '\33['
fBlk, fRed, fGrn, fYel, fBlu, fMag, fCya, fWht = \
e+'30m',e+'31m',e+'32m',e+'33m',e+'34m',e+'35m',e+'36m',e+'37m'                  # Text color
bBlk, bRed, bGrn, bYel, bBlu, bMag, bCya, bWht = \
e+'40m',e+'41m',e+'42m',e+'43m',e+'44m',e+'45m',e+'46m',e+'47m'            # Background color
bold, nobold, ital, noital, under, nounder, blink, noblink = \
e+'1m',e+'22m', e+'3m', e+'23m', e+'4m',e+'24m', e+'5m', e+'25m'                 # Text style
alloff = e+'0m'                                                         # Reset color & style
# Styling example:
#print(f'{bold+bGrn+fRed}These are {bRed+fGrn} some of {bCya+fYel} the color {bWht+fBlk} \
#variations {bCya+fBlu} you {bYel+fMag} can {bRed+fYel} do!{alloff} \n\nAlso: \
#{bold}bold{nobold} {ital}ital{noital} {under}under{nounder} {blink}blink{noblink} {alloff}')
# Some extra stuff:
ForangeBdarkgray = "\33[38;5;166m"
FyellowBdarkgray = "\33[38;5;184;48;5;233m"
#####| END STYLING CODE |####################################################################

#----/ CLASSES /------------------------------------------------------------------------------------#
class VirtualEnvironment:
    # The path to the project folder, which is used throughout the script.
    path = (os.path.dirname(__file__) + "/")
    def __init__(self):
        self.path = VirtualEnvironment.path
        self.result = ""
        self.showOutput = ""
        self.showOutput = "&> /dev/null" # To show pip install output, comment this line out.
    def install_dependencies(self):
        # The modules installed by this function were previously installed in a virtual environment,
        # and with the command 'pip freeze > ~/requirements.txt', I got the file containing all
        # dependencies, which is used here by 'pip install' to get them in the newly created virtualenv.
        print("\nInstallerar nödvändiga moduler i den virtuella miljön...")
        try:
            self.result = os.system("pip install -r " + self.path + "misc/requirements.txt" + self.showOutput)
            self.result = "Klart.\n"
        except:
            self.result = "\nEtt fel uppstod under installationen!\n" + self.result
            print(self.result)
            sys.exit()
        return self.result

class Image:
    # This class uses img_term.py by Jonathan Mackenzie.
    # It converts images into ANSI color codes.
    # https://github.com/JonnoFTW/img_term
    def __init__(self, name, width):
        self.path = VirtualEnvironment.path
        self.name = name.split("/") # The input dir is in the name.
        self.width = str(width)
        self.result = ""
        self.convert()
    def convert(self):
        # This function tells img_term.py to make a terminal friendly version of an image, in
        # 8-bit color. 24-bit is also available and makes much prettier images, but I could only
        # get it to display properly in iTerm2, and not in MacOS Terminal.app, so I went with 8-bit.
        try:
            self.result = os.system("python3 " + self.path + "misc/" + "img_term.py -img " + self.path\
            + self.name[0] + "/" + self.name[1] + " -width " + self.width + " -col 8 > " + self.path + "tmp/" + self.name[1] + ".txt")
            self.name = self.name[1]
        except:
            print(f"[BILDVISNINGSFEL]")
        # Since img_term.py puts some screen clearing and positioning ANSI codes in the beginning
        # and end of the file, and I don't want to change the original script, the bytes in question
        # are cut off with these lines:
        with open(self.path + "tmp/" + self.name + ".txt", "rb") as f:
            bytes_read = f.read()
        cut_bytes = bytes_read[9:-5]
        with open(self.path + "tmp/" + self.name + ".txt", "wb") as f:
            f.write(cut_bytes) # Here the new version is saved to file.
        return self.result
    def display(self, xloc, yloc, cropL, cropR, cropT, cropB):
        # In and by itself, img_term just clears the screen and puts the image in the top-left corner.
        # I wanted to be able to put it where I want and I also needed to be able to crop it, so this
        # function deals with those things.
        self.xloc = str(xloc)
        self.yloc = str(yloc)
        self.cropL = cropL
        self.cropR = cropR
        self.cropT = cropT
        self.cropB = cropB
        with open(self.path + "tmp/" + self.name + ".txt", "r") as f:
            lines = [line.rstrip() for line in f]
        for x in range(self.cropT,len(lines)-self.cropB):
            lines[x] = lines[x].split("▀") #The char that "images" are made of, I use it to count pixels.
            if self.cropR > 0: # It wouldn't take "[:-0]", so I had to make two versions of the crop stuff.
                lines[x] = "▀".join(lines[x][self.cropL:-self.cropR]) # One if right side cropping is used,
            else: # and one if we don't crop at all, or just the left side:
                lines[x] = "▀".join(lines[x][self.cropL:]) # To position the image, I use "\33[Y;XH":
            print(f"\33[{x-self.cropT + int(self.yloc) + 1};{int(self.xloc) + 1}H", end="")
            print(lines[x])
        print('\33[0m') # Reset ANSI colors

class Place:
    # The file "platsdata.txt" contains postal codes for all of Sweden, along with postal town, municipality,
    # county (postort, kommun, län) and coordinates. At first I used the Google Maps API Geocoding to get
    # this info, but it gave very inconsistent results. For some post codes the address I got in the
    # response was simply "Sweden". Since I wanted to be able to search for every little place in Sweden,
    # I decided to keep this info locally instead.
    def __init__(self, postcode):
        self.postcode = postcode
        with open(VirtualEnvironment.path + "data/" + "platsdata.txt", "r") as datafile:
            for line in datafile:
                if self.postcode in line:
                    theLine = line
        theLine = theLine.split("\t") # Cut the line up and feed the info into some variables:
        self.postalTown = theLine[2]
        self.county = theLine[3]
        self.municipality = theLine[5]
        self.muniCode = theLine[6]
        if len(self.muniCode) == 3: # The municipality codes are missing leading zeroes.
            self.muniCode = ("0" + str(self.muniCode))
        self.lat = theLine[9]
        self.long = theLine[10]

class General_Url_API:
    # The only thing this class does is to take a url and desired file name, fetch the Info,
    # and save it as byte data to a file if a filename is given. If not, it
    # returns that data to the class that requested it.
    def __init__(self):
        pass
    def getStuff(self, url, fileName):
        self.request = requests.Session()
        self.data = self.request.get(self.url)
        if self.fileName != "":
            with open(VirtualEnvironment.path + self.fileName, "wb") as self.f:
                self.f.write(self.data.content)
        else:
            return self.data.content

class MuniCoats(General_Url_API):
    # This class scans the file "wiki_urls.txt" for the right municipality, takes the
    # url on the same line, and sends it back to the parent class for fetching.
    def __init__(self, filename):
        with open(VirtualEnvironment.path + "data/" + "wiki_urls.txt", "r") as datafile:
            for line in datafile:
                if newPlace.municipality in line:
                    theLine = line
        theLine = theLine.split()
        self.url = theLine[1]
        self.fileName = filename
        self.getStuff(self.url, self.fileName)

class WikiEntry(General_Url_API):
    # In that same "wiki_urls.txt" I also put the municipality names url formatted, so that this
    # class can build a url that requests a short extract of the Wikipedia entry for the place.
    # In this case, nothing needs to be saved to file, so no fileName is sent to General_Url_API,
    # which makes it respond with just the byte data.
    # That data is processed below by the "json" module, that responds with the data neatly packed
    # into dicts and lists. The .values() function is used where a dict key is an unknown ID number.
    def __init__(self):
        with open(VirtualEnvironment.path + "data/" + "wiki_urls.txt", "r") as datafile:
            for line in datafile:
                if newPlace.municipality in line:
                    theLine = line
        theLine = theLine.split()
        self.url = "https://sv.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&titles="\
                    + theLine[3] + "&exchars=1000&exintro=1&explaintext=1&exsectionformat=plain"
        self.fileName = ""
        self.wikiJSON = self.getStuff(self.url, self.fileName)
        json_response = json.loads(self.wikiJSON)
        # For debugging, I used this code to get a nice visual presentation of the json data:
        # print(json.dumps(json_response, indent=4, separators=(',', ': ')))
        self.cont = list(json_response["query"]["pages"].values())[0]["extract"]

class StaticMap_API(General_Url_API):
    # This class construes a url for fetching a map image of the place. Since the image is displayed in such
    # low resolution, it didn't make any sense to zoom in too much, but instead just give an overview of
    # where in the country the place is. Before I noticed that the API would take a custom marker, I had a
    # lot of trouble with a huge blob taking over half the image, at the zoom level and resolution I wanted.
    # But, Google was so kind as to let me draw my own little pixly arrow, so now I can actually use the map!
    def __init__(self, lat, long, zoom, width, height, key, type, arrow, fileName):
        self.urlList = ["https://maps.google.com/maps/api/staticmap?center=", str(lat),\
                ",", str(long), "&zoom=", str(zoom), "&key=", str(key), "&size=", str(width), "x", str(height),\
                "&maptype=", type]
        if arrow == "on":
            self.urlList.extend(["&markers=anchor:topleft%7Cicon:http://kravallklang.se/johannes/test_public/arrow2.png",\
                                 "%7C", str(lat), ",", str(long)])
        self.url = "".join(self.urlList)
        self.fileName = fileName
        self.getStuff(self.url, self.fileName)

class Crime_API(General_Url_API): # https://brottsplatskartan.se/api/eventsNearby?lat=59.32&lng=18.06
    # This class takes the coordinates of the postal code, to get the latest police report from a 5km radius.
    # The response is html code which was annoying at first (I didn't want to drag yet another module into this),
    # but then I realized I could use the tags for my own formatting! I ended up showing everything pretty much
    # the same, but the possibility is there :)
    def __init__(self, lat, long):
        self.urlList = ["https://brottsplatskartan.se/api/eventsNearby?lat=", str(lat), "&lng=", str(long)]
        self.url = "".join(self.urlList)
        self.fileName = ""
        self.crimeJSON = self.getStuff(self.url, self.fileName)
        json_response = json.loads(self.crimeJSON)
        try:
            self.desc = "\33[38;5;184;48;5;233m" + json_response["data"][0]["description"]
            self.cont = json_response["data"][0]["content"]
            self.cont = self.cont.replace("<br>", "\n")
            self.cont = self.cont.replace("<br />", "\n")
            self.cont = self.cont.replace("<p>", "")
            self.cont = self.cont.replace("</p>", "")
            self.cont = self.cont.replace("<strong>", "\33[33m")
            self.cont = self.cont.replace("</strong>", "\33[38;5;184;48;5;233m")
            self.time = "\33[33m" + json_response["data"][0]["pubdate_iso8601"][:10] + " " + \
                        json_response["data"][0]["pubdate_iso8601"][11:16] + "\33[38;5;184;48;5;233m"
        except:
            self.desc = "Polisen i " + newPlace.municipality + " har inte rapporterat något den senaste tiden!"
            self.cont = ""
            self.time = "N/A"

#----/ Methods /----------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------#
# Function for reading single keypresses
# From: https://code.activestate.com/recipes/577977-get-single-keypress/
try:
    import tty, termios
except ImportError:
    # Probably Windows.
    try:
        import msvcrt
    except ImportError:
        # FIXME what to do on other platforms?
        # Just give up here.
        raise ImportError('getch not available')
    else:
        getch = msvcrt.getch
else:
    def getch():
        """getch() -> key character

        Read a single keypress from stdin and return the resulting character.
        Nothing is echoed to the console. This call will block if a keypress
        is not already available, but will not wait for Enter to be pressed.

        If the pressed key was a modifier key, nothing will be detected; if
        it were a special function key, it may return the first character of
        of an escape sequence, leaving additional characters in the buffer.
        """
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
#------------------------------------------------------------------------------------#

def dejta():
    global i
    global ages
    gender = ""
    print(f"För att ge dig en rättvis bild av dina dejting-chanser i {newPlace.municipality} " +
          f"ombeds du att svara på ett par frågor:\n\n" +
          f"Vill du dejta en {ForangeBdarkgray}M{FyellowBdarkgray}an, " +
          f"{ForangeBdarkgray}K{FyellowBdarkgray}vinna eller är det " +
          f"{ForangeBdarkgray}S{FyellowBdarkgray}kit samma?")
    genderAnsw = getch()
    if genderAnsw.lower() == "m": gender = ["1"]
    elif genderAnsw.lower() == "k": gender = ["2"]
    elif genderAnsw.lower() == "s": gender = ["1", "2"]
    else: gender = ["1", "2"]
    drawItAll()
    mv(35,0)
    print(f"Vilka åldrar lockar? {ForangeBdarkgray}A{FyellowBdarkgray}v eller {ForangeBdarkgray}P{FyellowBdarkgray}å?\n")
    agesQuery = []
    ages = ["15-19","20-24","25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69",\
            "70-74","75-79","80-84","85-89","90-94","95-99","100+"]
    for item in range(len(ages)):
        print(ages[item])
    for i in range(1,19):
        mv(i+36,7)
        print("<--", end="")
        sys.stdout.flush()
        rightAgeOrNot = getch()
        if rightAgeOrNot.lower() == "p":
            mv(i+36,7)
            print("\33[32m<--", end="\33[0m")
            agesQuery.append(ages[i-1])
        else:
            mv(i+36,7)
            print("\33[31m<--", end="\33[0m")
    payload = {"query":[{"code":"Region","selection":{"filter":"vs:RegionKommun07","values":[newPlace.muniCode]}},\
            {"code":"Civilstand","selection":{"filter":"item","values":["OG","G","SK","ÄNKL"]}},{"code":"Alder",\
            "selection":{"filter":"agg:Ålder5år","values":agesQuery}},{"code":"Kon","selection":{"filter":"item",\
            "values":gender}},{"code":"ContentsCode","selection":{"filter":"item","values":["BE0101N1"]}},\
            {"code":"Tid","selection":{"filter":"item","values":["2017"]}}],"response":{"format":"json"}}
    resp = requests.post("http://api.scb.se/OV0104/v1/doris/sv/ssd/START/BE/BE0101/BE0101A/BefolkningNy",data=json.dumps(payload))
    # The response data is preceded with a BOM signature, so it can't be used as a dict directly. We get rid of it by encoding it
    # and then decoding it again:
    data = resp.text.encode().decode("utf-8-sig")
    try:
        data = eval(data)
        drawItAll()
        mv(35,0)
        agesTot = len(agesQuery)
        agesTot *= len(gender)
        single = 0
        married = 0
        divorced = 0
        widow = 0
        theBar = ""
        for i in range(agesTot):
            single += int(data["data"][i]["values"][0])
        for i in range(agesTot, agesTot*2):
            married += int(data["data"][i]["values"][0])
        for i in range(agesTot*2, agesTot*3):
            divorced += int(data["data"][i]["values"][0])
        for i in range(agesTot*3, agesTot*4):
            widow += int(data["data"][i]["values"][0])
        percentSingle = ((single+divorced+widow)/(married+single+divorced+widow))*100
        print(f"Andel singlar av de {single+married+divorced+widow} personer i {newPlace.municipality} som stämmer in på din målgrupp:")
        mv(55,0)
        for i in range(1,101):
            mv(55,0)
            if i <= percentSingle:
                currPercent = i
                time.sleep(0.02 + currPercent/1200)
                theBar = theBar + fRed + "\u2665"
            else:
                theBar = theBar + fYel + " "
            loveBar = fYel + "[" + theBar + (" " * (100-i)) + fYel + "]" + alloff
            mv(37,0)
            print(f"{fYel}{currPercent:02d}% {loveBar}{alloff}")
        mv(39,0)
        print(f"{fYel}Antal ogifta: {fRed}{str(single)}\n")
        print(f"{fYel}Antal gifta: {fRed}{str(married)}\n")
        print(f"{fYel}Antal skilda: {fRed}{str(divorced)}\n")
        print(f"{fYel}Antal änkor/änklingar: {fRed}{str(widow)}\n")
        print(alloff)
    except:
        drawItAll()
        mv(36,0)
        print(f"{ForangeBdarkgray}Någonting gick fel vid hämtning av data från statistikdatabasen.scb.se...\n\n{alloff}")
        #print("Payload: \n" + str(payload), "\n\n")
        #print("Result: \n" + str(data), "\n\n")


def politik():
    payload = {"query":[{"code":"Region","selection":{"filter":"vs:RegionKommun07+BaraEjAggr","values":[newPlace.muniCode]}},\
                {"code":"ContentsCode","selection":{"filter":"item","values":["ME0104B2"]}},{"code":"Tid",\
                "selection":{"filter": "item","values":["2018"]}}],"response":{"format":"json"}}
    resp = requests.post("http://api.scb.se/OV0104/v1/doris/sv/ssd/START/ME/ME0104/ME0104A/ME0104T1",data=json.dumps(payload))
    # The response data is preceded with a BOM signature, so it can't be used as a dict directly, we have to shave it off first.
    data = resp.text.encode().decode("utf-8-sig")
    try:
        data = eval(data)
        parties = {}
        parties["Moderaterna"] = float(data["data"][0]["values"][0])
        parties["Centerpartiet"] = float(data["data"][1]["values"][0])
        parties["Liberalerna"] = float(data["data"][2]["values"][0])
        parties["Kristdemokraterna"] = float(data["data"][3]["values"][0])
        parties["Miljöpartiet"] = float(data["data"][4]["values"][0])
        parties["Socialdemokraterna"] = float(data["data"][5]["values"][0])
        parties["Vänsterpartiet"] = float(data["data"][6]["values"][0])
        parties["Sverigedemokraterna"] = float(data["data"][7]["values"][0])
        parties["Övriga"] = float(data["data"][8]["values"][0])
        colors = {}
        colors["Moderaterna"] = fBlu
        colors["Centerpartiet"] = fGrn
        colors["Liberalerna"] = fBlu
        colors["Kristdemokraterna"] = fBlu
        colors["Miljöpartiet"] = fGrn
        colors["Socialdemokraterna"] = fRed
        colors["Vänsterpartiet"] = fRed
        colors["Sverigedemokraterna"] = fYel
        colors["Övriga"] = fWht
        name = [None] * 9
        votes = [None] * 9
        color = [None] * 9
        i = 0
        for key, value in sorted(parties.items(), key = itemgetter(1), reverse = True):
            name[i] = key
            votes[i] = value
            color[i] = colors[key]
            i = i + 1
        drawItAll()
        mv(35,0)
        print(f"Valresultat i Kommunfullmäktigvalet, {newPlace.municipality} 2018:\n\n")
        for x in range(0,9):
            print(f"{color[x]}{name[x]}: {ForangeBdarkgray}{votes[x]}%\n")
        print(alloff)
    except:
        drawItAll()
        mv(36,0)
        print(f"{ForangeBdarkgray}Någonting gick fel vid hämtning av data från statistikdatabasen.scb.se...\n\n{alloff}")
        # print("Payload: \n" + str(payload), "\n\n")
        # print("Result: \n" + str(data), "\n\n")


def displayCursive(text):
    # This method shows the name of the municipality in large, friendly letters on the top of the screen. I made the
    # "font" using the same script, img_term.py, that I use for converting the other graphics. I spent so much time
    # manually changing small things here and there though, so I wrote a script for automating the conversion process.
    # It's in the folder "FontMaker", and takes individual letters in png, named after the char they represent, and
    # and the width in pixels (e.g. "A13.png") and converts them into a font that can be displayed by this function.
    X = [""]*len(text)
    wordLine = [""]*10
    for letter in range(len(text)):
        value = hex(ord(text[letter]))
        with open(VirtualEnvironment.path + "data/" + "font_txt/" + str(value) + ".txt", "r") as f:
            X[letter] = f.readlines()
    for line in range(10):
        for letter in range(len(text)):
            wordLine[line] += X[letter][line].rstrip()
    for i in range(len(wordLine)):
        print(wordLine[i], end='\n')
    print(len(wordLine[0]))

def drawItAll():
    # This is the function that actually displays everything.
    global menuChoice
    senBlirAlltSvart() # This just clears the screen, as defined in the styling template at the beginning of the script.
    print("\33[38;48;5;233m" + "          "*1000) # An ugly way of painting the screen in the color I want it.
    mv(0,0) # Another styling function, used as a cleaner way to print positional ANSI codes.
    displayCursive(newPlace.municipality)
    mapImg.display(xloc=26, yloc=10, cropL=30, cropR=30, cropT=10, cropB=10) # I hope Google forgives me for cropping
    coatImg.display(xloc=85, yloc=10, cropL=0, cropR=0, cropT=0, cropB=0)    # out their logo, but I promise it's all
    frameImg.display(xloc=0, yloc=10, cropL=0, cropR=0, cropT=0, cropB=0)    # for the best. It was so mangled you
    menuImg.display(xloc=0, yloc=30, cropL=0, cropR=0, cropT=0, cropB=0)     # couldn't even see what it was :)
    mv(12,3)
    print(f"\33[38;5;184;48;5;233m{bold}Postnummer: ", newPlace.postcode, sep="",end="") # Make it bold and yellow!
    mv(15,3)
    print("Ort: ", newPlace.postalTown, sep="",end="")
    mv(18,3)
    print("Kommun: ", newPlace.municipality, sep="",end="")
    mv(21,3)
    print("Län: ", newPlace.county, sep="",end="")
    mv(24,3)
    print("Latitud: ", newPlace.lat, sep="",end="")
    mv(27,3)
    print("Longitud: ", newPlace.long, sep="",end="")
    mv(32,3)
    print("\33[38;5;166mA\33[38;5;184;48;5;233mLLMÄNT", sep="",end="")
    mv(32,14)
    print("\33[38;5;166mP\33[38;5;184;48;5;233mOLITIK", sep="",end="")
    mv(32,25)
    print("\33[38;5;166mD\33[38;5;184;48;5;233mEJTING", sep="",end="")
    mv(32,36)
    print("\33[38;5;166mB\33[38;5;184;48;5;233mROTT", sep="",end="")
    # mv(32,47)
    # print("\33[38;5;166mE\33[38;5;184;48;5;233mMPTY", sep="",end="")
    # mv(32,58)
    # print("\33[38;5;166mE\33[38;5;184;48;5;233mMPTY", sep="",end="")
    # mv(32,69)
    # print("\33[38;5;166mE\33[38;5;184;48;5;233mMPTY", sep="",end="")
    mv(32,80)
    print("\33[38;5;166mR\33[38;5;184;48;5;233mANDOM", sep="",end="")
    mv(32,91)
    print("\33[38;5;166mV\33[38;5;184;48;5;233mÄLJ", sep="",end="")
    mv(32,102)
    print("\33[38;5;166mE\33[38;5;184;48;5;233mXIT", sep="",end="")
    mv(32,3)

def menu():
    global menuChoice
    mv(55,0)
    print(" ")
    menuChoice = getch()
    if menuChoice == "A" or menuChoice == "a":
        drawItAll()
        mv(35,0)
        print(textwrap.fill(getWiki.cont, 110))
        menu()
    # if menuChoice == "N" or menuChoice == "n":
    #     drawItAll()
    #     mv(35,0)
    #     print("\33[38;5;184;48;5;233mAlternativet är inte implementerat ännu.", sep="",end="\n\n")
    #     menu()
    if menuChoice == "D" or menuChoice == "d":
        drawItAll()
        mv(35,0)
        print("\33[38;5;184;48;5;233m", sep="",end="")
        dejta()
        menu()
    if menuChoice == "B" or menuChoice == "b":
        drawItAll()
        mv(35,0)
        print("\33[38;5;184;48;5;233mPolisens senaste rapport från området: " + latestCrime.time)
        print(textwrap.fill(latestCrime.desc, 110))
        print(textwrap.fill(latestCrime.cont, 110))
        menu()
    if menuChoice == "P" or menuChoice == "p":
        drawItAll()
        mv(35,0)
        print("\33[38;5;184;48;5;233m", sep="",end="")
        politik()
        menu()
    if menuChoice == "V" or menuChoice == "v":
        mv(35,0)
        newStuff("")
    if menuChoice == "R" or menuChoice == "r":
        with open(VirtualEnvironment.path + "data/" + "platsdata.txt", "r") as datafile:
            randomLine = (random.choice(datafile.readlines()))
        postc = (randomLine.split("\t"))[1]
        mv(35,0)
        newStuff(postc)
    if menuChoice == "E" or menuChoice == "e":
        senBlirAlltSvart()
        print("\33[38;5;184;48;5;233mProgrammet avslutas.", sep="",end="\33[0m\n\n")
        sys.exit()
    else:
        mv(57,0)
        menu()

def newStuff(postc):
    # This function makes objects out of the classes. Get's things done.
    drawItAll()
    mv(35,0)
    global postcode
    global newPlace
    global latestCrime
    global getMap
    global getCoat
    global getWiki
    global mapImg
    global frameImg
    global menuImg
    global coatImg
    if postc == "":
        postcode = input("Mata in postnummer (XXX XX), och tryck Retur: ")
        # Check to see if the postcode is formatted correctly. Else: Go to menu.
        try: # First check if a five digit int is given, and in that case put a space after the third digit:
            int(postcode)
            if (len(postcode) == 5):
                postcode = (str(postcode))[0:3] + " " + (str(postcode))[3:5]
            else:
                raise Exception()
        except: # If it's not, check if the input is correct:
            try:
                # See if the fourth char is a space and the length is right:
                if (postcode[3] == " ") and (len(postcode) == 6):
                    pass
                else:
                    raise Exception()
                int(postcode[0:3]) # Throws an exception if first 3 chars are non-digits
                int(postcode[3:5]) # Throws an exception if chars 4-5 are non-digits
            except:
                postcode = newPlace.postcode
                print("Felaktigt format på postnr, återgår.")
    else:
        postcode = postc
    try:
        newPlace = Place(postcode)
        print("Hämtar data...")
        latestCrime = Crime_API(newPlace.lat, newPlace.long)
        getMap = StaticMap_API(newPlace.lat, newPlace.long, 4, 300, 200, gKey, "satellite", "on", "tmp/map.png")
        getCoat = MuniCoats("tmp/coat.png")
        getWiki = WikiEntry()
        print("Konverterar bilder...")
        mapImg = Image(name="tmp/map.png", width=118)
        frameImg = Image(name="data/frame.png", width=25)
        menuImg = Image(name="data/meny.png", width=117)
        coatImg = Image(name="tmp/coat.png", width=32)
        drawItAll()
        menu()
    except:
        pass

#----/ Imports, etc /-----------------------------------------------------------------------------------
virtualOne = VirtualEnvironment()
print(virtualOne.install_dependencies())
import sys
from datetime import datetime
import requests
import json
import re
import textwrap
import time
import random
from operator import itemgetter

#----/ Do Stuff /---------------------------------------------------------------------------------------
with open(VirtualEnvironment.path + "data/" + "platsdata.txt", "r") as datafile:
    randomLine = (random.choice(datafile.readlines()))
postcode = (randomLine.split("\t"))[1]
print("Hämtar data...")
newPlace = Place(postcode)
latestCrime = Crime_API(newPlace.lat, newPlace.long)
getMap = StaticMap_API(newPlace.lat, newPlace.long, 4, 300, 200, gKey, "satellite", "on", "tmp/map.png")
getCoat = MuniCoats("tmp/coat.png")
getWiki = WikiEntry()
print("Konverterar bilder...")
mapImg = Image(name="tmp/map.png", width=118)
frameImg = Image(name="data/frame.png", width=25)
menuImg = Image(name="data/meny.png", width=117)
coatImg = Image(name="tmp/coat.png", width=32)
drawItAll()
menu()
