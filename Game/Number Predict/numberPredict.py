
import random
r = random.randint(1,20)

while(True):
	inp = int(input())
	if(inp<r):
		print("oops,try a greater number")
	elif(inp>r):
		print("oops,try a smaller number")
	else:
		print("congrats you choosed write number")
		break;
