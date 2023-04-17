from maxpar import *

def runT1():
	global X
	X = 1
def runT2():
	global Y
	Y = 2
def runT3():
	global X, Y, Z
	Z = X + Y


def main():
	print('Lancement main')	
	t1 = Task("T1", runT1, ["M1,M2"], ["M3"])	
	t2 = Task("T2", runT2, ["M1"], ["M4"])	
	t3 = Task("T3", runT3, ["M3", "M4"], ["M1"])	

	print("---------Task System valide--------------------")
	ts = TaskSystem([t1, t2, t3], {"T1": [], "T2": ["T1"], "T3": ["T2"]})

	ts.run()


main()
