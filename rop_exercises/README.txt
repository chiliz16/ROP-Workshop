#### WELCOME  ####

Congratulations, you successfully started the ROP Machine. 
-----------------------------------------------------------------------
IMPORTANT NOTE: for the first two exercises you have to disable ASLR.
Disable ASLR until the next reboot:
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

For the third exercise you have to enable ASLR again:
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
-----------------------------------------------------------------

The next important thing is to make yourself comfortable.
Start a terminal, navigate to exercises/
Every exercise folder contains:
- the vulnerable binary
- source code for the vulnerable binary
- a python template that gives a structure for the exploit

Your task for every exercise is to start the vulnerable binary and give 
it an exploit-payload which will give you a shell. For this you can use 
the python-template that already contains the rough structure of the exploit. 

Every important command (e.g. how to give the exploit to the vulnerable binary)
is included in the cheat sheet. Also tips on how to debug/avoid mistakes are 
included, so read carefully, it may save you some time!

(Remember: when debugging your payload, always set the breakpoint on the return
you want to overwrite. Also, if you see a blinking cursor, you might have already
a shell, as there will be no prompt. You can try 'whoami' to verify.)

The slides together with the cheatsheet and the templates should provide you 
with the information to solve the exercises. 
slides:
- exercise 1: p. 1-32
- exercise 2: p. 33-53
- exercise 3: p. 54-72


For the third exercise it is useful to inspect how dynamic functions are called 
with Hopper. Load the third binary in Hopper and follow the references 
to the GOT and the PLT by clicking on them. 


-----------------------------------------------------------------------------------

Maybe check out the following ressources to refresh your memory or read up on missing information: 

- if you don't know about the basics of the Linux command line, e.g. what are input/output 
  stream redirections and pipes (<, >, | ), read through this tutorial: 
  https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection 

- if your knowledge of stack buffer overflows is a bit rusty, check out this video of Live Overflow's
  Youtube channel: "Buffer Overflows can Redirect Program Execution" 
 ( https://www.youtube.com/watch?v=8QzOC8HfOqU&index=14&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)
 ( very good, but fast moving video, I needed to pause it from time to time too)

