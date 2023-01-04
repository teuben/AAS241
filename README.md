#  AAS241 Seattle - Jan 7-8, 2023

My links and notes for AAS241.

## Software Carpentry

* SWC website for this meeting: https://abostroem.github.io/2023-01-07-aas-swc/

  * Lives Notes
    * etherpad: https://pad.carpentries.org/2023-01-07-aas-swc
    * slack: https://app.slack.com/client/T043ALX86GG/C04E62RQF50 (you would need an invite)
  * Automating Tasks with the Unix Shell (2)
    * https://swcarpentry.github.io/shell-novice/
    * https://carpentries-incubator.github.io/shell-extras/
  * Building Programs with Python (3)
    * https://swcarpentry.github.io/python-novice-inflammation/
    * https://swcarpentry.github.io/python-novice-gapminder/
    * https://datacarpentry.github.io/astronomy-python
  * Version Control with Git (2)
    * https://swcarpentry.github.io/git-novice/
    * https://carpentries-incubator.github.io/git-novice-branch-pr/
    * https://carpentries-incubator.github.io/git-Rstudio-course/
  * TBD (1)
    * https://carpentries-incubator.github.io/good-enough-practices/
    * https://carpentries-incubator.github.io/python-intermediate-development/
    * https://carpentries-incubator.github.io/introduction-to-conda-for-data-scientists/
    * https://carpentries-incubator.github.io/snakemake-novice-bioinformatics/
  * A full set of SC lessons:
    * https://software-carpentry.org/lessons/

## Miscellaneous

### Entry points for my own codes

* https://github.com/teuben/teunix : my home away from home
* https://github.com/teuben/nemo : niche C code for stellar dynamics and image processing

### My Favorite Tools

In 2022 this was my daily computing environment

- editor:        **ec** (logging script to run emacsclient) + persistent ; org mode for diary
- shell:         **bash**  with  **aliases.sh**
- load env:      **rc**    (source project dependant files from ~/rc/*.rc) 
- git tool:      **gitk** (and some gitg) - also for overleaf!
- diff tool:     **meld**
- file manager:  **dolphin**
- VNC:           **x2go** + persistent
- desktop:       **kde**  + persisent, focus-follows-mouse, 3x2 virtual desktops
- os:            **kubuntu**   (20 and 22 currently)
- dotfiles:      **teunix** (essential since too often now I bootstrap on a new machine)
- open:          **o=xdg-open** (on Mac: open)

## Git History

How I started this repo?  You can create a new repo graphicaly via github.com, but
this is slightly cumbersome (lots of point and click and back and forth between browser
and terminal, typical instruction pages require screendumps to explain).

There is a now a new command line interface to github.com,
called "github CLI". This delivers a new command **gh** in your shell. See
https://cli.github.com/manual/installation  It will be able to bypass you having
to go onto github.com a lot less!

After installing, these were the steps I took:

1. first authenticate

       gh auth login

2. after which you can now create a new repo from the commandline

       gh repo create --public AAS241

3. and after starting a new file README.md adding it

       cd AAS241
       $EDITOR README.md
       git add README.md
       git commit -m initial README.md

4. for others cloning the repo would be 43 characters

       git clone https://github.com/teuben/AAS241

   for me it would be 28 characters

       gh repo clone teuben/AAS241

5. The real power shows when you want to fork a repo and work on it
   in a local branch to prepare a pull request. Lets use the SWC for this

        gh repo fork https://github.com/abostroem/2023-01-07-aas-swc
	cd 2023-01-07-aas-swc
	git checkout -b teuben1
	$EDITOR index.md
	gh pr create 

   Again, a lot simpler than the back and forth going between github.com and the terminal.

   Once the branch has been merged by the upstream, I should remove it:

        git branch -d teuben1
	git push original --delete teuben1
	
