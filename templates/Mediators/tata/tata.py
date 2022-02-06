drell_yan = 'NC'
dilep = ['ta','ta'];
mass  = [1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3500, 4000, 4500, 5000, 5500, 6000];
width = [0.0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]

delphes_card = '/disk/data11/ttp/faroughy/Flavor_at_LHC/ditaus/SMEFT/cards/delphes_card_ATLAS_1902.08103.dat';
ufo_model = ' '
nevents = 50000
form_factors = {
    
    'FVLL' :{
        'coeff':'s',
        'Type':['s','s'] ,
        'veto_mediators':None,
        'coupl_order':'NP^2==2',
        'WC1_u':['g1q',1.0],
        'WC2_u':['g1l',1.0],
        'WC1_d':None,
        'WC2_d':None 
     }
}
