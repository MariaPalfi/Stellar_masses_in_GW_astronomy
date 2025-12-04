# Stellar_masses_in_GW_astronomy
Codes for the paper [*Utilizing Stellar Mass Estimates to Identify Gravitational Wave Host Galaxies*](https://academic.oup.com/mnras/article/539/3/1879/8106602#513609005).

## Content of the files and order of running them:

### Preparations and stellar mass estimations:
1. *Missing_error_estimation_rel.ipynb*: estimating the errors of missing magnitudes
2. *Stellar_mass_estimation.ipynb*: stellar mass estimations based on IR bands
3. *Stellar_masses_from_GAMA.ipynb*: SQL queries to download GAMA stellar masses
4. *oursample.ipynb*: creating sample for the analysis

### Comparision:
1. *sys_err.ipynb*: systematic uncertainty based on the different GAMA stellar masses
2. *Compare_gama_sm.ipynb*: comparing three types of GAMA stellar mass values in our sample
3. *Pearson_corr_sm.ipynb*: Pearson correlation matrix of the different estimations of stellar masses with Monte Carlo
4. *Compare_plots.ipynb*: comparison plots with contours
5. *Calibrating_fits.ipynb*: shifting the linear relations

### Ranking host galaxy of GW170817:
1. *interpolate_Artale*: interpolating host galaxy probabilities for Artale's ranking approach
2. *Possible_hosts_bayestar.ipynb*: finding galaxies inside the localisation volume of GW170817 using initial BAYESTAR skymap
3. *GW170817_rank_volume_bayestar.ipynb*: ranking the host galaxy of GW170817 using initial BAYESTAR skymap
4. *Possible_hosts_lalinference.ipynb*: finding galaxies inside the localisation volume of GW170817 using preliminary LALInference skymap
5. *GW170817_rank_volume_lalinference.ipynb*: ranking the host galaxy of GW170817 using initial preliminary LALInference skymap

### Simulation:
1. *suitable_format.ipynb*: preparing mock galaxy catalogue
2. *injections_with_SNR_for_sm.ipynb*: choosing hosts from the mock galaxy catalogue, injecting events
3. *injection_writer.py*: saving injection parameters to prior files, creating injections with *bilby_pipe* on the cluster (run *create_inj.sh*)
4. *ini_writer.py*: creating *ini* files and bash script for parameter estimation on the cluster(run *running.sh*)
5. *possible_hosts_sim.ipynb*: finding galaxies inside the 90% localisation volume of the simulated events on the cluster
6. *ranking_hosts_sim.ipynb*: ranking the host galaxies of simulatied events on the cluster 
