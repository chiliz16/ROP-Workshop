# ROP-Workshop
Slides, exercises, cheatsheet and instructions for my ROP-Workshop (Blackhoodie18)

You can find the slides of the workshop in the directory slides, and the exercises we worked through in the folder exercises. 
If you want to follow along, it's a good idea to set up this workshop VM:


Set Up Your Workhop VM
======================

- Download the Ubuntu16.04 ISO http://releases.ubuntu.com/16.04/ (Ubuntu16.04 is mandatory, Ubuntu 18.04 will not work, and other Distros I did not check)
- Get started as usual, make sure you have internet connectivity (NAT or Bridged), Guest Extensions and Shared folders are optional but nice to have
- make your first snapshot (at least if you installed guest extensions), because the following steps could need a reset

- install pwntools:
  pwntools is a python-module we will use. 
  It is installed via pip. Before doing that, taking a snapshot is very wise. 
```
	$ sudo apt-get update
	$ sudo apt-get install python2.7 python-pip python-dev git libssl-dev libffi-dev build-essential
	$ sudo pip install pwntools
```

- install ipython:
```
	$ sudo apt install ipython
```
=> open a terminal, type in "ipython", you see the following prompt: 
```
	[1]:
```
=> Try the following: 
```
 	[1]: from pwn import * 
```
  if no errors occure, both ipython and pwntools are installed correctly => snapshot!


- install ROPgadget (another pip install, so make sure you did a snapshot)
```
	$ sudo pip install capstone
	$ sudo pip install ropgadget
	$ ROPgadget --version
```


- install gdb-peda:
```
	$ sudo apt install git
	$ git clone https://github.com/longld/peda.git ~/peda
	$ echo "source ~/peda/peda.py" >> ~/.gdbinit
```
=> open gdb in your terminal, the prompt should look like this now: 
```
	gdb-peda$ 
```


- install the free Demo version of Hopper: https://www.hopperapp.com/download.html

- clone this get repo inside your VM to get the exercises
- Read through the Readme in the exercises folder

- If you havent done it by now, get your favourite text editor (I provided sublime-text, gedit, vim)
- make a snapshot :) 

Congratz, you build your own ROP-Machine!



