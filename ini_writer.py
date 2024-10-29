"""
Code for creating ini files and saving commands for running the parameter estimation to bash script. 

Written by Mária Pálfi (marika97@student.elte.hu).
"""

for i in range(0, 195):
    with open('/home/maria.palfi/bilby/sim_sm/ini_files/running_'+str(i)+'.ini', 'w') as f:
        f.write( 'label = bbh_injection\n' )
        f.write( 'outdir = /home/maria.palfi/bilby/sim_sm/outdir_folder/bbh_injection_' + str(i) + '\n\n' )
        f.write( 'detectors = [H1, L1, V1]\n\n')
        f.write( 'duration = 4\n\n' )
        f.write( 'sampler = dynesty\n' )
        f.write( "sampler-kwargs = {'nlive': 1000}\n\n")
        f.write( 'default-prior = BBHPriorDict\n\n' )
        f.write( 'plot-skymap = True\n' )
        f.write( 'injection = True\n' )
        f.write( 'injection-file = /home/maria.palfi/bilby/sim_sm/injections/injection'+str(i)+'.json\n')
        f.write( 'gaussian-noise = True\n' )
        f.write( 'accounting = ligo.sim.o4.cbc.pe.bilby\n')
        f.write( 'n-simulation = 1\n')
        f.write( 'n-parallel = 1\n' )
        f.write( 'request-cpus = 4' )

# running the parameter estimation
with open( 'running.sh', 'w' ) as f:
    for i in range(0, 195):
        f.write( "bilby_pipe ini_files/running_"+str(i)+".ini --submit\n" )
