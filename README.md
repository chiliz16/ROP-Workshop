# ROP-Workshop
Slides, exercises, cheatsheet and instructions for my ROP-Workshop 


ROP stands for Return Oriented Programming, which is a binary exploitation technique
that allows you to circumvent certain security mechanisms like a non executable stack.

This repository can be seen as an online tutorial version of the workshop.
With this material you should be able to complete all 3 exercises if this is something
you wanted to achieve.

You can find the slides of the workshop in the directory slides, and the exercises we 
worked through in the folder exercises. 
In the slides folder you can find a slidedeck including everything I've said and
done during the workshop (including screenshots of the exercises) with detailed 
description. 

If you want to follow along, it's a good idea to set up this workshop VM:


Set Up Your Workhop VM
======================
- You can use a Hypervisor of your choice, e.g. VirtualBox. 

- Download the Ubuntu16.04 ISO http://releases.ubuntu.com/16.04/ (Ubuntu16.04 is mandatory, 
  Ubuntu 18.04 will have issues with stack alignment, which I do not cover until now)

- VirtualBox: Machine => New (Type: Linux, Version: 64 Bit Ubuntu)
        => Next => Memory size: 2048 MB (we won't need much)
	
- start the VM and it will ask for the .iso file, 
  eventually you will get to the ubuntu installation wizard that
  will guide you through the ubuntu installation. 
  (default settings)

- Get started as usual, make sure you have internet connectivity (NAT or Bridged), Guest
  Extensions and Shared folders are optional but nice to have

- install pwntools:
  pwntools is a python-module we will use. 
  It is installed via pip.
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
  if no errors occure, both ipython and pwntools are installed correctly


- install ROPgadget 
```
	$ sudo pip install capstone
	$ sudo pip install ropgadget
	$ ROPgadget --version
```


- install ropper:
  $ sudo pip install ropper

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

- clone this git repo inside your VM to get the exercises
- Read through the Readme in the exercises folder

- If you havent done it by now, get your favourite text editor (I provided sublime-text, gedit, vim)
- make a snapshot :) 

Congratz, you build your own ROP-Machine!



