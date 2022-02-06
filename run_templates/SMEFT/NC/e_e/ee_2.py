drell_yan = 'NC'
dilep = ['e','e'];
bins = [200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2250,2500,2750,3000,3500,4000,15000];
delphes_card = '/disk/data11/ttp/faroughy/Flavor_at_LHC/dielectrons/SMEFT/cards/delphes_card_ATLAS_ee.dat';
ufo_model = 'Semi_Leptonic_SMEFT_Dim6_UFO'
nevents = 50000
form_factors = {
        
    'FD_AA':{
        'coeff':'00',
        'flavor_indx':'ij',
        'Type':['A','A'],
        'veto_mediators':'Z',
        'coupl_order':'NP^2==2',
        'WC1_u':['CuW', 0.483424],
        'WC2_u':['CuB',-0.875386],
        'WC1_d':['CdW', 0.483424],
        'WC2_d':['CdB',-0.875386]
     },
    
    'FD_ZZ':{
        'coeff':'00',
        'flavor_indx':'ij',
        'Type':['Z','Z'],
        'veto_mediators':'A',
        'coupl_order':'NP^2==2',
        'WC1_u':['CuW', 0.875386],
        'WC2_u':['CuB', 0.483424],
        'WC1_d':['CdW', 0.875386],
        'WC2_d':['CdB', 0.483424]
     },
    
    'FD_AZ':{
        'coeff':'00',
        'flavor_indx':'ij',
        'Type':['A','Z'],
        'veto_mediators':None,
        'coupl_order':'NP^2==2',
        'WC1_u':['CuW', 1.0],
        'WC2_u': None,
        'WC1_d':['CdW', 1.0],
        'WC2_d': None
     }
}
