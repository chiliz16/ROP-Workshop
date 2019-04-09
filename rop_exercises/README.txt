#### WELCOME  ####

-----------------------------------------------------------------------
IMPORTANT NOTE: for the first two exercises you have to disable ASLR.
Disable ASLR until the next reboot:
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space

For the third exercise you have to enable ASLR again:
echo 2 | sudo tee /proc/sys/kernel/randomize_va_space
-----------------------------------------------------------------

Your task for every exercise is to start the vulnerable binary and give 
it an exploit-payload which will give you a shell. For this you can use 
the python-template that already contains the rough structure of the exploit. 

There is a slidedeck that guides you through the workshop, with everything I've 
said and done in the workshop, so you might want to walk this one through.
(/slides/IntroToROP_detailed.pdf). 

Every important command (e.g. how to give the exploit to the vulnerable binary)
is included in the cheat sheet. Also tips on how to debug/avoid mistakes are 
included, so read carefully, it may save you some time!

(Remember: when debugging your payload, always set the breakpoint on the return
you want to overwrite. Also, if you see a blinking cursor, you might have already
a shell, as there will be no prompt. You can try 'whoami' to verify.)


structure:
- exercise 1: 64 bit, ASLR disabled (guided)
- exercise 2: 64 bit, ASLR disabled (on your own)
- exercise 3: ASLR enabled (without PIE)


For the third exercise it is useful to inspect how dynamic functions are called 
with Hopper. Load the third binary in Hopper and follow the references 
to the GOT and the PLT by clicking on them. 

If you are interested in 32 bit ROP chains, there is a directory "extras" which
contains slides and exercises for 32 Bit. 
-----------------------------------------------------------------------------------

Maybe check out the following ressources to refresh your memory or read up on missing information: 

- if you don't know about the basics of the Linux command line, e.g. what are input/output 
  stream redirections and pipes (<, >, | ), read through this tutorial: 
  https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection 

- if your knowledge of stack buffer overflows is a bit rusty, check out this video of Live Overflow's
  Youtube channel: "Buffer Overflows can Redirect Program Execution" 
 ( https://www.youtube.com/watch?v=8QzOC8HfOqU&index=14&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)
 ( very good, but fast moving video, I needed to pause it from time to time too)

