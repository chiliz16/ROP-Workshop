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
This may include:

- start a terminal, navigate to exercises/ and check that
  each subdirectory contains at least a source file (.c file) and an executable
  binary. 

- Choose your weapon e.g. vim, gedit or Sublime text 

- Start "Hopper Disassembler". Click "Try the Demo" when it starts. Navigate
  to "File -> Read Executable to Disassemble" and open any binary just to check
  if it is working (e.g. exercises/01_demo/01_demo_32_bit).



-----------------------------------------------------------------------------------

Maybe check out the following ressources to refresh your memory: 

- have a look at the usage of gdb (peda), e.g. how to set breakpoints and step through the execution 
  (e.g. https://kapeli.com/cheat_sheets/GDB.docset/Contents/Resources/Documents/index )

- Play a little with ipython, e.g. declare variables, call functions etc. You
  don't need to know how to code in python, just getting a feeling for it is
  enough.  (The template for the scripts will be given in the workshop, so we can
  focus on the principles of ROP)

- if you don't know about the basics of the Linux command line, e.g. what are input/output 
  stream redirections and pipes (<, >, | ), read through this tutorial: 
  https://www.digitalocean.com/community/tutorials/an-introduction-to-linux-i-o-redirection 

- if your knowledge of stack buffer overflows is a bit rusty, check out this video of Live Overflow's
  Youtube channel: "Buffer Overflows can Redirect Program Execution" 
 ( https://www.youtube.com/watch?v=8QzOC8HfOqU&index=14&list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)
 ( very good, but fast moving video, I needed to pause it from time to time too)

