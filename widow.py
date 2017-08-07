# This program uses difference equations to make a stepwise modeling
# of a Latrodectus ("Black widow") venom kinetics after a bite.
# We make use the estimated LD50 for mice as a reference: 0.2-0.9 mg/kg
# and we must take a pure guess at the rate of absorbtion to blood
# as well as the very important biological half-life.

from pylab import *

#One LD50 estimate in mg/kg for mice
#LD50 = 0.9

N = 200

tick_time = 5
venom_diffusion_constant = 0.11
venom_elimination_constant = 0.01

venom_vein = zeros(N)
venom_bite_site = zeros(N)
time_since_bite = zeros(N)

#injected venom in mg
injected_venom = 0.05

venom_bite_site[0] = injected_venom

# Models the first 40 time steps
for n in range(1,40):
    time_since_bite[n] = time_since_bite[n-1]+tick_time
    venom_vein[n] = venom_vein[n-1]+(venom_bite_site[n-1]*venom_diffusion_constant)-(venom_vein[n-1]*venom_elimination_constant)
    venom_bite_site[n] = venom_bite_site[n-1]-(venom_bite_site[n-1]*venom_diffusion_constant)

# Models the steps from 40 to 200 with the changed elimination constant
venom_elimination_constant = 0.02
for n in range(40,200):
    time_since_bite[n] = time_since_bite[n-1]+tick_time
    venom_vein[n] = (venom_vein[n-1]+(venom_bite_site[n-1]*venom_diffusion_constant))-(venom_vein[n-1]*venom_elimination_constant)
    venom_bite_site[n] = venom_bite_site[n-1]-(venom_bite_site[n-1]*venom_diffusion_constant)


plot(time_since_bite, venom_vein, 'g-', label='Venom in blood')
xlabel('Time in minutes')
ylabel('Amount of venom in vein and bite site')

plot(time_since_bite, venom_bite_site, 'b-', label='Venom in bite site')
legend(loc="center right")
show()
