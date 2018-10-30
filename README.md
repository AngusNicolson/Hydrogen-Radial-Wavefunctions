# Hydrogen-Radial-Wavefunctions
Python code to calculate and display the radial wavefunction of Hydrogen. This is a simple two particle system so can be solved analytically. The code is relatively simple but an attempt to explain the science behind the equations has been made.

# Theory
#### What is a wavefunction?
Wavefunctions are a quantum mechanical description of a system. If you can determine the wavefunction (and how it evolves with time) of a specific system you can calculate everything there is to know about it. To find such a wavefunction you must solve the schrodinger equation for that system. The basic schrodinger equation is

<a href="https://www.codecogs.com/eqnedit.php?latex=\hat{H}\psi&space;=&space;E\psi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{H}\psi&space;=&space;E\psi" title="\hat{H}\psi = E\psi" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{H}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{H}" title="\hat{H}" /></a> is the Hamiltonian, <a href="https://www.codecogs.com/eqnedit.php?latex=E" target="_blank"><img src="https://latex.codecogs.com/gif.latex?E" title="E" /></a> is the energy and <a href="https://www.codecogs.com/eqnedit.php?latex=\psi" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\psi" title="\psi" /></a> is the wavefunction. This equation is desceptively simple but involves matrix algebra and is an eigenvalue problem. I'm not going to go into the maths here but there's plenty of material online. The Hamilitonian can further be split into <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{T}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{T}" title="\hat{T}" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=\hat{V}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\hat{V}" title="\hat{V}" /></a> which correspond to the kinetic and potential energies respectively. This means the schrodinger equation is simply stating that the kinetic plus the potential energy is equal to the total energy.

#### Solving the schrodinger equation for Hydrogen
The schrodinger equation is analytically solvable in very few cases. One such case is a hydrogen-like system i.e. a system where there are only two particles; a nucleus and an electron. In the case of hydrogen this is a single proton and a single electon but He<sup>+</sup> and Li<sup>2+</sup>, among others, are also hydrogen-like systems. The Hamiltonian for hydrogen is

<a href="https://www.codecogs.com/eqnedit.php?latex=-\frac{i\bar{h}^2}{2\mu}\nabla^2&space;-&space;\frac{Ze^2}{4\pi\epsilon_0&space;r}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?-\frac{i\bar{h}^2}{2\mu}\nabla^2&space;-&space;\frac{Ze^2}{4\pi\epsilon_0&space;r}" title="-\frac{i\bar{h}^2}{2\mu}\nabla^2 - \frac{Ze^2}{4\pi\epsilon_0 r}" /></a>

# Improvements
- Implement a function to calculate normalisation term of each wavefunction. i.e. solve analytically rather than numerically. This would mean small sections of a wavefunction could be drawn and normalised correctly. Currently, to show an accurate representation of the wavefunction, most of it be visible in the plot. i.e. upper x limit must be large enough
- Finish the README
