# #!/bin/bash
# #===================================================================

MG_PATH='/home/ttp/fwilsc/programs/MG5_aMC_v3_1_1'
SCRIPTS_PATH='/disk/data11/ttp/faroughy/Flavor_at_LHC/e_ve/SMEFT/'
PROC='scripts_SMEFT_e_ve_2750_3000'
DELPHES_CARD=/disk/data11/ttp/faroughy/Flavor_at_LHC/e_ve/SMEFT/cards/delphes_card_mono-lepton.dat
JOB_TIME='standard'  # standard express long 
NODES=1
TASKS=1
CPUS=16
NAME='e_ve'

#===================================================================

for MG5_SCRIPT in $SCRIPTS_PATH/$PROC/* ; do
  lhco_name=$(basename $MG5_SCRIPT)'.lhco.gz'
  SCRIPT='aux/'$(basename $MG5_SCRIPT)
  echo "#!/bin/bash"                                                         >> $SCRIPT.slurm
  echo "#SBATCH --job-name="$NAME                                            >> $SCRIPT.slurm
  echo "#SBATCH --nodes="$NODES                                              >> $SCRIPT.slurm
  echo "#SBATCH --ntasks="$TASKS                                             >> $SCRIPT.slurm
  echo "#SBATCH --cpus-per-task="$CPUS                                       >> $SCRIPT.slurm
 
  echo 'mkdir -p /scratch/$USER/$SLURM_JOB_ID'                               >> $SCRIPT.slurm
  echo 'mkdir -p /scratch/$USER/$SLURM_JOB_ID/tmp'                           >> $SCRIPT.slurm
  echo 'export TMPDIR=/scratch/$USER/$SLURM_JOB_ID/tmp'                      >> $SCRIPT.slurm
  echo 'cd /scratch/$USER/$SLURM_JOB_ID'                                     >> $SCRIPT.slurm
 
  echo 'echo "*********************** SLURM INFO *************************"' >> $SCRIPT.slurm
  echo date                                                                  >> $SCRIPT.slurm
  echo 'echo "* host is    : "$SLURMD_NODENAME'                              >> $SCRIPT.slurm
  echo 'echo "* queue is   : "$SLURM_JOB_PARTITION'                          >> $SCRIPT.slurm
  echo 'echo "* batch id   : "$SLURM_JOB_ID'                                 >> $SCRIPT.slurm
  echo 'echo "* job name   : "$SLURM_JOB_NAME'                               >> $SCRIPT.slurm
  echo 'echo "* script name: "'$SCRIPT                                       >> $SCRIPT.slurm
  echo 'echo "* working dir: "$SLURM_SUBMIT_DIR'                             >> $SCRIPT.slurm
  echo 'echo "* tmp dir    : "$TMPDIR'                                       >> $SCRIPT.slurm

  echo "#----------------------------------------"                           >> $SCRIPT.slurm
  echo "cp "$DELPHES_CARD '/scratch/$USER/$SLURM_JOB_ID'                     >> $SCRIPT.slurm 
  echo "python2.7 "$MG_PATH"/bin/mg5_aMC "$MG5_SCRIPT                        >> $SCRIPT.slurm
  echo "#----------------------------------------"                           >> $SCRIPT.slurm
 
  echo 'rm -rf /scratch/$USER/$SLURM_JOB_ID/tmp'                             >> $SCRIPT.slurm
  echo 'cp /scratch/$USER/$SLURM_JOB_ID/*/*/*/Events/*/*.lhco.gz /disk/data11/ttp/faroughy/Flavor_at_LHC/e_ve/SMEFT/lhco_files/' >> $SCRIPT.slurm
  echo 'cd'                                                                  >> $SCRIPT.slurm
  echo 'rm -rf /scratch/$USER/$SLURM_JOB_ID'                                 >> $SCRIPT.slurm
 
  echo date                                                                  >> $SCRIPT.slurm
  
  sbatch -p $JOB_TIME $SCRIPT.slurm
  rm $SCRIPT.slurm
done
