import numpy as np
import sys
import os.path
import sys
import glob
import shlex
import shutil
import importlib
from shutil import copyfile

def replace_temp(Drell_Yan, FF, q, dilep, XMIN, XMAX, ufo_model, delphes_card, path_out, Nevs):
    
    ll=''.join(dilep)
    l_dic={'e':'1','mu':'2','ta':'3', 've':'1', 'vm':'2', 'vt':'3' }
    q_dic={'u':'1','d':'1','c':'2', 's':'2', 'b':'3'}
    
    for ff in list(FF.keys()):

        temp_file='PROC_FX_NM_Q_CURRENT_TYPE_XMIN_XMAX_template'
        file=temp_file.replace('FX',ff.split('_')[0])
        file=file.replace('Q',q)
        file=file.replace('TYPE','_'.join(FF[ff]['Type']))
        file=file.replace('CURRENT',ll)
        file=file.replace('NM',FF[ff]['coeff'])
        file=file.replace('XMIN',str(XMIN))
        file=file.replace('XMAX',str(XMAX))
        file=file.split('_')[:-1]
        file='_'.join(file)

        template='templates/'+temp_file+'.txt'
        script=open(path_out+'/'+file,'w')
        Break=True
        
        with open(template) as f:

            for line in f:    

                line=line.replace('FR_MODEL',ufo_model)
                line=line.replace('DELPHES_CARD_PATH',delphes_card)
                line=line.replace('NEVENTS', str(Nevs))
                line=line.replace('L1',dilep[0])
                line=line.replace('L2',dilep[1])
                if FF[ff]['veto_mediators']:
                    line=line.replace('VETO_STATES',FF[ff]['veto_mediators'])
                else:
                    line=line.replace('VETO_STATES','')
                line=line.replace('_Q_',q)
                line=line.replace('CPL',FF[ff]['coupl_order'])
                line=line.replace('TYPE','_'.join(FF[ff]['Type']))
                line=line.replace('FX',ff.split('_')[0])
                line=line.replace('NM',FF[ff]['coeff'])  
                line=line.replace('_ALPHA_','')  
                line=line.replace('_BETA_','')
                line=line.replace('XMAX',str(XMAX))
                line=line.replace('XMIN',str(XMIN))
                
                if Drell_Yan=='NC':

                    line=line.replace('_Ql1_','-')
                    line=line.replace('_Ql2_','+')

                    if q in ['d','s','b']:
                        line=line.replace('_P_','d~ s~ b~')
                        if FF[ff]['WC1_d']:

                            line=line.replace('WXC1',FF[ff]['WC1_d'][0])
                            line=line.replace('X1',str(FF[ff]['WC1_d'][1]))
                            line=line.replace('_Q1_','d')
                            line=line.replace('_Q2_','s')
                            line=line.replace('_Q3_','b')
                            line=set_ij_indx(FF[ff]['WC1_d'], q, line)
                            
                            if '>>>' in line:
                                line=line.replace('>>>','')
                            if 'WXC2' in line:
                                if FF[ff]['WC2_d']:
                                    line=line.replace('WXC2',FF[ff]['WC2_d'][0])
                                    line=line.replace('X2',str(FF[ff]['WC2_d'][1]))
                                    line=set_ij_indx(FF[ff]['WC2_d'], q, line)
                                else:
                                    line=''                                
                        elif FF[ff]['coeff']=='SM':
                            line=line.replace('_Q1_',q)
                            if 'WXC' in line:
                                line=''
                            if '# run 2'in line:
                                Break=False
                        else:                        
                            os.remove(path_out+'/'+file)
                            break

                    else:
                        line=line.replace('_P_','u~ c~')
                        if FF[ff]['WC1_u']:

                            line=line.replace('WXC1',FF[ff]['WC1_u'][0])
                            line=line.replace('X1',str(FF[ff]['WC1_u'][1]))
                            line=line.replace('_Q1_','u')
                            line=line.replace('_Q2_','c')
                            line=set_ij_indx(FF[ff]['WC1_u'], q, line)

                            if '>>>' in line:
                                line=''

                            if 'WXC2' in line:
                                if FF[ff]['WC2_u']:
                                    line=line.replace('WXC2',FF[ff]['WC2_u'][0])
                                    line=line.replace('X2',str(FF[ff]['WC2_u'][1]))
                                    line=set_ij_indx(FF[ff]['WC2_u'], q, line)
                                else:
                                    line=''
                        elif FF[ff]['coeff']=='SM':

                            line=line.replace('_Q1_',q)
                            if 'WXC' in line:
                                line=''
                            if '# run 2'in line:
                                Break=False
                        else:
                            os.remove(path_out+'/'+file)
                            break

                    if 'MLLMIN' or 'MLLMAX' in line:
                        line=line.replace('MLLMIN',str(int(XMIN)))
                        line=line.replace('MLLMAX',str(int(XMAX)))
                        
                    if 'PTMIN' or 'PTMAX' in line:
                        line=line.replace('PTMIN','0.0')
                        line=line.replace('PTMAX','-1.0')

                    if Break:
                        script.write(line)
                    else:
                        script.write('')

                elif Drell_Yan=='CC':

                    if q in ['d','s','b']:
                        line=line.replace('_P_','u~ c~')
                        line=line.replace('_Ql1_','-')
                        line=line.replace('_Ql2_','~')
                        
                        if FF[ff]['WC1_du']:

                            line=line.replace('WXC1',FF[ff]['WC1_du'][0])
                            line=line.replace('X1',str(FF[ff]['WC1_du'][1]))
                            line=line.replace('_Q1_','u')
                            line=line.replace('_Q2_','c')
                            line=set_ij_indx(FF[ff]['WC1_du'], q, line)

                            if '>>>' in line:
                                line=''
                            if 'WXC2' in line:

                                if FF[ff]['WC2_du']:
                                    line=line.replace('WXC2',FF[ff]['WC2_du'][0])
                                    line=line.replace('X2',str(FF[ff]['WC2_du'][1]))
                                    line=set_ij_indx(FF[ff]['WC2_du'], q, line)
                                else:
                                    line=''       

                        elif FF[ff]['coeff']=='SM':

                            line=line.replace('_Q1_',q)
                            if 'WXC' in line:
                                line=''
                            if '# run 2'in line:
                                Break=False
                        else:                        
                            os.remove(path_out+'/'+file)
                            break
                    else:
                        line=line.replace('_P_','d~ s~ b~')
                        line=line.replace('_Ql1_','+')
                        line=line.replace('_Ql2_','')

                        if FF[ff]['WC1_ud']:
                            line=line.replace('WXC1',FF[ff]['WC1_ud'][0])
                            line=line.replace('X1',str(FF[ff]['WC1_ud'][1]))
                            line=line.replace('_Q1_','d')
                            line=line.replace('_Q2_','s')
                            line=line.replace('_Q3_','b')
                            line=set_ij_indx(FF[ff]['WC1_ud'], q, line)

                            if '>>>' in line:
                                line=line.replace('>>>','')

                            if 'WXC2' in line:
                                if FF[ff]['WC2_ud']:
                                    line=line.replace('WXC2',FF[ff]['WC2_ud'][0])
                                    line=line.replace('X2',str(FF[ff]['WC2_ud'][1]))
                                    line=set_ij_indx(FF[ff]['WC2_ud'], q, line)
                                else:
                                    line=''

                        elif FF[ff]['coeff']=='SM':
                            line=line.replace('_Q1_',q)
                            if 'WXC' in line:
                                line=''
                            if '# run 2'in line:
                                Break=False
                        else:
                            os.remove(path_out+'/'+file)
                            break

                    if 'PTMIN' or 'PTMAX' in line:
                        line=line.replace('PTMIN',str(int(XMIN)))
                        line=line.replace('PTMAX',str(int(XMAX)))
                        
                    if 'MLLMIN' or 'MLLMAX' in line:
                        line=line.replace('MLLMIN','0.0')
                        line=line.replace('MLLMAX','-1.0')
                        
                    if Break:
                        script.write(line)
                    else:
                        script.write('')

            script.close()

def set_ij_indx(x, q, line):

    q_dic={'u':'1','d':'1','c':'2', 's':'2', 'b':'3'}

    if len(x)==2:
        line=line.replace('_I_',q_dic[q])
        return line.replace('_J_','')

    elif (len(x)==3 and x[2]=='ij->ji'):
        line=line.replace('_J_',q_dic[q])
        return line.replace('_I_','')

    elif (len(x)==3 and x[2]=='3j->j3'):
        if q=='b':
            line=line.replace('_J_',q_dic[q])
            return line.replace('_I_','')
        else:
            line=line.replace('_I_',q_dic[q])
            return line.replace('_J_','')

    elif (len(x)==3 and x[2]=='2j->j2'):            
        if (q=='s' or q=='c'):
            line=line.replace('_J_',q_dic[q])
            return line.replace('_I_','')
        else:
            line=line.replace('_I_',q_dic[q])
            return line.replace('_J_','')
            
    elif (len(x)==3 and x[2]=='1j->j1'):            
        if (q=='d' or q=='u'):
            line=line.replace('_J_',q_dic[q])
            return line.replace('_I_','')
        else:
            line=line.replace('_I_',q_dic[q])
            return line.replace('_J_','')

def generate_scripts(Drell_Yan, dilep, FF, bins, ufo_model, delphes_card, Nevs):
    
    ll=''.join(dilep)
    path0=make_dir('scripts_'+ll, overwrite=True)
    
    for i,XMAX in enumerate(bins[1:]):
        XMIN=bins[i]
        path=make_dir(path0+'/scripts_SMEFT_'+ll+'_'+str(XMIN)+'_'+str(XMAX), overwrite=True)
        
        for q in ['u','c','d','s','b']:

            replace_temp(Drell_Yan, FF, q, dilep, XMIN, XMAX, ufo_model, delphes_card, path, Nevs)

def make_dir(path_new_dir, overwrite=True):
    Directory=path_new_dir
    if overwrite:
        shutil.rmtree(Directory, ignore_errors=True)
        os.mkdir(Directory)
    else:
        for I in it.count():
            Directory=path_new_dir + '__' + str(I+1)
            if not os.path.isdir(Directory):
                os.mkdir(Directory)
                break
            else:
                continue
    return Directory

def defs(name):
    module = importlib.import_module(name)
    return module

arg_0=defs(sys.argv[1].split('.')[0]).drell_yan
arg_1=defs(sys.argv[1].split('.')[0]).dilep
arg_2=defs(sys.argv[1].split('.')[0]).form_factors
arg_3=defs(sys.argv[1].split('.')[0]).bins
arg_4=defs(sys.argv[1].split('.')[0]).ufo_model
arg_5=defs(sys.argv[1].split('.')[0]).delphes_card
arg_6=defs(sys.argv[1].split('.')[0]).nevents

generate_scripts(arg_0, arg_1, arg_2, arg_3, arg_4, arg_5, arg_6)
           