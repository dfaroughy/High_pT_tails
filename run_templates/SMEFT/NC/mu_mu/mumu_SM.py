drell_yan = 'NC'
dilep = ['mu','mu'];
bins = [200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2250,2500,2750,3000,3500,4000,15000];
delphes_card = '/disk/data11/ttp/faroughy/Flavor_at_LHC/dimuons/SMEFT/cards/delphes_card_ATLAS_mumu.dat';
ufo_model = 'sm_for_interference_UFO'
nevents = 50000
form_factors = {

    'FV_AA':{
        'coeff':'SM',
        'flavor_indx':None,
        'Type':['A','A'],
        'veto_mediators':'Z',
        'coupl_order':'QED=2',
        'WC1_u':None,
        'WC2_u':None ,
        'WC1_d':None,
        'WC2_d':None 
     },
    
    'FV_ZZ':{
        'coeff':'SM',
        'flavor_indx':None,
        'Type':['Z','Z'] ,
        'veto_mediators':'A',
        'coupl_order':'QED=2',
        'WC1_u':None,
        'WC2_u':None ,
        'WC1_d':None,
        'WC2_d':None 
     },
    
    'FV_AZ':{
        'coeff':'SM',
        'flavor_indx':None,
        'Type':['A','Z'] ,
        'veto_mediators':None,
        'coupl_order':'ZLL^2==2 GAMMALL^2==2',
        'WC1_u':None,
        'WC2_u':None ,
        'WC1_d':None,
        'WC2_d':None 
     }
    
}
