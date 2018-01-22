import numpy as np
import matplotlib.pyplot as plt
import scipy.special
from scipy.integrate import simps

a = 5.29*10**-11
numValues = 20000

def R(n,l,r):
	y=np.zeros(numValues)#generates a numpy array of 0s
	#print(type(y))
	Lag = scipy.special.genlaguerre(n-l-1, 2*l+1)#Generates an associated laguerre polynomial as a scipy.special.orthogonal.orthopoly1d
	#print(Lag)
	for i in range(len(Lag)+1):
		i = float(i)
		y = y + (((r/(n*a))**(l))*(np.exp(-r/(a*n)))*Lag[int(i)]*(((2*r)/(a*n))**i))#The main equation (What its all about)
		

	return y

#Approximates integral value and divides by the absolute value. Uses simpsons over trapezium because smaller error
def normalise(x,y):#Doesnt normalise. Calculates integral, we want area under the graphs.
	integral = simps(np.absolute(y),x)
	print(integral, "simps")
	print(type(integral))
	#integral = np.trapz(y,x)
	#print(integral, "trapz")
	y = y/np.absolute(integral)
	return y

def plotPsi(r,psi):
	plt.subplot(311)
	plt.plot(r, psi)
	plt.grid(True)
	plt.xlabel("r/a (m)")
	plt.ylabel("Psi")

def plotPsiSquared(r,psi):
	psiSquared = psi**2
	psiSquared = normalise(r,psiSquared)

	
	plt.plot(r, psiSquared)
	plt.grid(True)
	plt.xlabel("r/a (m)")
	plt.ylabel("Psi^2")

def plotRadialDistribution(r,psi):
	radialDistribution = 4*np.pi*(r**2)*psi**2
	radialDistribution = normalise(r, radialDistribution)

	
	plt.plot(r, radialDistribution)
	plt.grid(True)
	plt.xlabel("r/a (m)")
	plt.ylabel("4*pi*(r^2)*Psi")

def plotAll(r,psi):
	plt.figure(1)
	plt.subplot(311)#3 rows, 1 column, this plot is first plot
	plotPsi(r,psi)
	plt.subplot(312)
	plotPsiSquared(r,psi)
	plt.subplot(313)
	plotRadialDistribution(r,psi)


def graphs(r, psi,choice):
	
	print(choice)
	if choice == 1:
		plotPsi(r,psi)
	elif choice == 2:
		plotPsiSquared(r,psi)
	elif choice == 3:
		plotRadialDistribution(r,psi)
	else:
		plotAll(r,psi)

	
	

	


def main():
	numPsi = int(input("How many wavefunctions do you want to draw?"))
	width = float(input("To what value of r (in units of a) do you want to plot?")) * a
	print("1: Plot the wavefunction")
	print("2: Plot the wavefunction squared (the probability density)")
	print("3: Plot the wavefunction squared times pi r^2 (the radial distribution function)")
	print("4: Plot all 3")
	choice = int(input("Choose an option:"))
	for i in range(numPsi):
		print("Wavefunction " + str(i+1))
		n = float(input("Enter n:"))
		l = float(input("Enter l:"))
		r = np.linspace(0,width, numValues)
		psi = R(n,l,r)

		#Converts r into units of a
		r = r/a
		psi = normalise(r, psi)
		
		graphs(r, psi,choice)
	plt.show()


if __name__ == '__main__':
    main()
