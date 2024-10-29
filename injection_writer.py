"""
Code for saving injection parameters to prior files and creating bash script with commands for injections with bilby_pipe.

Written by Mária Pálfi (marika97@student.elte.hu).
"""


import pandas as pd
import bilby

directory = 'injections_sm/'

for i in range(0, 195):
    params = pd.read_csv(directory+'injection_params'+str(i)+'.csv', header=None)
    params = params.T # transpose
    params.columns = params.loc[0,:] # the header will be 0. row
    params.drop( axis = 0, index = 0, inplace = True ) # delete the unecessary row
    
    # calculating mass_ratio
    mass_ratio = bilby.gw.conversion.component_masses_to_mass_ratio(params.mass_1[1], params.mass_2[1])
    
    # write the file
    # directory is injection_priors
    with open('injection_priors/inj'+str(i)+'.prior', 'a') as f:
        f.write('mass_1 = '+str(params.mass_1[1])+'\n')
        f.write('mass_2 = '+str(params.mass_2[1])+'\n')
        f.write('mass_ratio = '+str(mass_ratio)+'\n')
        f.write('a_1 = '+str(params.a_1[1])+'\n')
        f.write('a_2 = '+str(params.a_2[1])+'\n')
        f.write('tilt_1 = '+str(params.tilt_1[1])+'\n')
        f.write('tilt_2 = '+str(params.tilt_2[1])+'\n')
        f.write('phi_12 = '+str(params.phi_12[1])+'\n')
        f.write('phi_jl = '+str(params.phi_jl[1])+'\n')
        f.write('luminosity_distance = '+str(params.luminosity_distance[1])+'\n')
        f.write('dec = '+str(params.dec[1])+'\n')
        f.write('ra = '+str(params.ra[1])+'\n')
        f.write('theta_jn = '+str(params.theta_jn[1])+'\n')
        f.write('psi = '+str(params.psi[1])+'\n')
        f.write('phase = '+str(params.phase[1]))

# directory is injections
with open( 'create_inj.sh', 'w' ) as f:
    for i in range(0, 195):
        f.write( "bilby_pipe_create_injection_file injection_priors/inj"+str(i)+".prior  --n-injection 1 --generation-seed 1234 -f injections/injection"+str(i)+".json\n" )
