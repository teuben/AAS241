#  AAS241 Seattle - Jan 2022

## Software Carpentry

* SWC website for this meeting: https://abostroem.github.io/2023-01-07-aas-swc/

  * Automating Tasks with the Unix Shell (2)
    * https://swcarpentry.github.io/shell-novice/
  * Building Programs with Python (3)
    * https://swcarpentry.github.io/python-novice-inflammation/
    * https://swcarpentry.github.io/python-novice-gapminder/
  * Version Control with Git (2)
    * https://swcarpentry.github.io/git-novice/
    * https://carpentries-incubator.github.io/git-novice-branch-pr/
  * TBD (1)
  * A full set of SC lessons:
    * https://software-carpentry.org/lessons/

## Miscellaneous

Other entry points for my own codes

* https://github.com/teuben/teunix : my home away from home
* https://github.com/teuben/nemo : niche C code for stellar dynamics and image processing

## History

How I started this repo?  You can create a new repo via github.com, but
there is a now a new command line interface to github.com available,
called "github CLI". This delivers a new command **gh** in your shell. See
https://cli.github.com/manual/installation 

After installing, these were the steps I took:

1. first authenticate

       gh auth login

2. after which you can now create a new repo from the commandline

       gh repo create --public AAS241

3. and after starting a new file README.md adding it

       $EDITOR README.md
       gh add README.md
       gh commit -m initial README.md

4. whereas for others cloning the repo would be

       git clone https://github.com/teuben/AAS241


