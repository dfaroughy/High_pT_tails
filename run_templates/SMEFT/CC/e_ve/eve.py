drell_yan = 'CC'
dilep = ['e','ve'];
bins = [200,300,400,500,600,700,800,900,1000,1200,1400,1600,1800,2000,2250,2500,2750,3000,3500,4000,15000];
delphes_card = '/disk/data11/ttp/faroughy/Flavor_at_LHC/e_ve/SMEFT/cards/delphes_card_mono-lepton.dat';
ufo_model = 'Semi_Leptonic_SMEFT_Dim6_UFO'
nevents = 50000
form_factors = {
    
     'FV_WW':{
        'coeff':'SM',
        'flavor_indx':None,
        'Type':['W','W'],
        'veto_mediators':None,
        'coupl_order':'QED=2 NP=0',
        'WC1_ud':None,
        'WC2_ud':None,
        'WC1_du':None,
        'WC2_du':None 
     },
    
    'FS':{
        'coeff':'00',
        'flavor_indx':'abij->abji q=u',
        'Type':['Reg','Reg'],
        'veto_mediators':None,
        'coupl_order':'NP^2==2',
        'WC1_ud':['Cledq',1.0],
        'WC2_ud':None,
        'WC1_du':['Cledq',1.0],
        'WC2_du':None 
     },

    'FT':{
        'coeff':'00',
        'flavor_indx':'abij->abji q=u',
        'Type':['Reg','Reg'],
        'veto_mediators':None,
        'coupl_order':'NP^2==2',
        'WC1_ud':['C3lequ',1.0],
        'WC2_ud':None,
        'WC1_du':['C3lequ',1.0],
        'WC2_du':None 
     },

    'FST':{
        'coeff':'00',
        'flavor_indx':'abij->abji q=u',
        'Type':['Reg','Reg'],
        'veto_mediators':None,
        'coupl_order':'WC1lequ^2==1 WC3lequ^2==1',
        'WC1_ud':['C1lequ',1.0],
        'WC2_ud':['C3lequ',1.0],
        'WC1_du':['C1lequ',1.0],
        'WC2_du':['C3lequ',1.0], 
     },

    'FVLL':{
        'coeff':'00',
        'flavor_indx':'abij',
        'Type':['Reg','Reg'],
        'veto_mediators':None,
        'coupl_order':'NP^2==2',
        'WC1_ud':['C3lq',1.0],
        'WC2_ud':None,
        'WC1_du':['C3lq',1.0],
        'WC2_du':None 
     },

    'FVLL_W':{
        'coeff':'00',
        'flavor_indx':'abij',
        'Type':['W','Reg'],
        'veto_mediators':None,
        'coupl_order':'NP^2==1',
        'WC1_ud':['C3lq',1.0],
        'WC2_ud':None,
        'WC1_du':['C3lq',1.0],
        'WC2_du':None 
     },
   
    'FD':{
        'coeff':'00',
        'flavor_indx':'ij',
        'Type':['W','W'],
        'veto_mediators':None,
        'coupl_order':'NP^2==2',
        'WC1_ud':['CuW',1.0],
        'WC2_ud':None,
        'WC1_du':['CdW',1.0],
        'WC2_du':None 
     }  
}
