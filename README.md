#  AAS241 Seattle - Jan 2022

## Software Carpentry

* SWC website: https://abostroem.github.io/2023-01-07-aas-swc/

  * Automating Tasks with the Unix Shell (2)
  * Building Programs with Python (3)
  * Version Control with Git (2)
  * TBD (1)


## History

How I started this repo?  You can create a new repo via github.com, but
there is a now a new command line interface to github.com available,
called "github CLI". This delivers a new command **gh** in your shell. See
https://cli.github.com/manual/installation 

After installing, these were the steps I took:

      gh auth login

after which you can now create a new repo from the commandline

      gh repo create --public AAS241

and after starting a new file README.md adding it

      $EDITOR README.md
      gh add README.md
      gh commit -m initial README.md


