# PlatsInfo

This is a project I did for the Python beginner course "Programmering och systemering" at Nackademin in Stockholm 2018. The assignment was to make a CLI application, making use of classes.

My intention was to provide an information platform for people inclined to relocate inside of Sweden, and for (Swedish reading) foreigners who plan to move here.

It aims to collect information about a place from different sources and present them in a neat way, giving the user an overview of a place they might be interested in. The result can be seen in action below:

![](/misc/sthlm.gif)

## Prerequisites

* The project is developed and tested under macOS 10.13 & Python 3.7.0. It might be fine to run it pretty much as-is in Linux, but to run it in Windows will definitely need some tinkering.
* It uses a bunch of modules (weighing in at about 300MiB), temporarily installed inside a virtual environment in ./tmp/, which is erased upon exiting by pressing 'E'. 
* You will need an XTerm compatible terminal emulator capable of showing 16 colors, such as MacOS Terminal.app or iTerm2. In macOS Terminal, make sure to select "Display ANSI colors" under Preferences->Profiles->Text.
* A Google Cloud API key. The program runs without it, but you won't see the map. It's a paid service, but they offer a 1 year trial with $300 in free credits, which goes a long way if you're not using it for any actual products.
* The information is presented entirely in Swedish, although most variable and function names are English. 

#### Recommended terminal settings:
* Window size: 118 * 57
* Font: PT Mono Regular 12p (or any font that displays things correctly, you'll see what looks good)

## Usage
Clone the repository and put your Google API key on line 13 of 'project.py':
```
gKey = "YOUR-GOOGLE-CLOUD-API-KEY-HERE"
```

Make 'run.sh' executable and execute it. 
```
$ chmod u+x run.sh
$ ./run.sh
```

This will create the dir /tmp/VirtEnv/ inside the dir from which the shell script is executed, activate the environment and then run the main script, 'project.py', which installs the neccessary modules from 'requirements.txt' inside the venv.

When all things are in place, the script will pick a postal code from "platsdata.txt", call the API's and present you with some basic stats of a random municipality in Sweden along with a crude map of the concerned part of the country and the municipality's coat of arms.
You will also see a menu with the following options:
* #### [A]llmänt (General)
An extract of the municipality's Wikipedia entry. (Data source: https://sv.wikipedia.org/w/api.php)
* #### [P]olitik (Politics)
An overview of the results from the latest municipal council elections. The 8 largest parties (on a national level) are color-coded, the rest are shown in white. Red=the left/social democrats, Green=treehuggers/farmers, Blue=conservatives/neo-liberals, Yellow=Stay away (their words, not mine!). (Data source: http://api.scb.se)
* #### [D]ejting (Swedified form of the word 'Dating')
Let's you input the sex(es) and age ranges of your potential partners, and bluntly lays out your statistical chanses of success in the municipality. Protip if you're into women over 95: In Älvkarleby, 7.1% are devorced and the rest of them are widows! (Data source: http://api.scb.se)
* #### [B]rott (Crime)
Prints the latest public police report from the area. (Data source: https://brottsplatskartan.se/api)
* #### [R]andom
Picks a random place from the list.
* #### [V]älj (New post code)
Let's you input the postal code for the area you are interested in.
* #### [E]xit
Deletes the /tmp/ directory and exits.

## Built With

* [img_term](https://github.com/JonnoFTW/img_term) - Jonathan Mackenzie's 'img-term.py' converts the images to ANSI color codes. Thanks for sharing it, those ANSI graphics are just so incredibly satisfying :)
#### For a complete list of dependencies, please see /misc/requirements.txt.
### API:s
* [Brottsplatskartan](https://brottsplatskartan.se/) - Offers a free API for police reports.
* [Google: StaticMaps](https://developers.google.com/maps/documentation/maps-static/intro) - Spits out a picture of a map.
* [Wikipedia](https://en.wikipedia.org/w/api.php?action=help&modules=query%2Bextracts) - Gives us a neat string of wiki goodness. The coats of arms are also from Wikipedia, but are fetched through /data/wiki_urls.txt.
* [SCB: Statistikdatabasen](http://www.statistikdatabasen.scb.se/) - A true goldmine of Swedish statistics!

## Author

**Johannes Söderberg Eriksson** - First year DevOps Integration student at Nackademin in Stockholm
