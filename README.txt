#### Project: movie_website
   By: Don Coffman
   Project 1 in Udacity's Full Stack Web Developer Nanodegree Program (2018)


## Description:
Project is based on a Python program that generates HTML code for a Movie Trailer Website. 
The generated HTML is automatically opened in a web browser session, with the 
website providing the following info on my favorite movies:
- Movie Name
- Movie Poster graphics
- Movie Synopsis  
- Click to play the _YouTube_ movie trailer


## Project Contents:
- entertainment_center.py: Main Python program code file containing instances of Movie class, loaded into a list, 
                           and passed to the fresh_tomatoes.open_movies_page() function. 
- media.py: Python code file containing Class definition for Movie class
- fresh_tomatoes.py: Python code file which generates final HTML and opens web browser session. (Original code supplied
                     by Udacity - customized for this project ... see below)
- fresh_tomatoes.html: Dynamically-generated HTML file
- README.md: Project README file (GitHub Markdown) 
- README.txt: Project README file (Ascii Text Version) 


## Requirements / Prerequisites:
- Python 2.7xx (Min) must be installed on target system and path to interpreter should be included in environment variables.


## Installation:
- Clone this GitHub repository on local system 
  -- OR --
- Download Zip File to local system and unzip


## Usage:
- Using local system command-line interface (Shell or Windows cmd prompt):  
  - Change directory to the above installation location
  - Execute the following:
    python entertainment_center.py
    -- OR --
    ./entertainment_center.py (for UNIX/LINUX)
  - Web browser will be opened  

- Using local system File Browser Window interface (GUI):  
  - Change directory to the above installation location
  - Double-click the program: `entertainment_center.py`
  - Web browser will be opened  


## Contributions:
- The general layout of this README file is based on a template suggested by PhillipCoach in a Udacity Forum post
  and previously used/mentioned by Steven Wooding
- The fresh_tomatoes.py Python code module was originally supplied by Udacity and was customized to incorporate the
  changes shows in the 'Extra Credit Changes Description' section below.


## Extra Credit Changes Description:
- Incorporate a Movie Synopsis into the Movie data and display it to the User via the standard 'Title' attribute and related 'ToolTip' 
  functionality triggered by the Mouse hover event.
- Extend Movie Poster graphic element Mouse hover event animation to include a subtle Scale (1.05) change.

