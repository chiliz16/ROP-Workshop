all: 
	clang 01_demo_32_bit.c -m32 -fno-stack-protector -O0 -o 01_demo_32_bit
	# Note 1: we don't use gcc because its stackframe layout caused some problems for the payload. 
	# Note 2: newer versions of clang require "-no-pie" to disable position
	# independent executables
	# 
	
