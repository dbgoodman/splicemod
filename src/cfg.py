'''
User modifiable global variables for the splicemod package

@author: dbgoodman
'''

import string
import sys
import os

from numpy import array
    
#import score

#===============================================================================
# general parameters
#===============================================================================
topDir = os.getcwd()+'/'
#where all this stuff should happen, usually one dir up from the src/ dir

logFile = ('%s/parseFASTA.log' % topDir)
#not currently used

#####maxEnt Settings
maxEntPath = topDir+"perl_utils/max_ent"
#path to maxEnt executable

maxEntBounds = {'me_donor': array([-3, 6]),
                'me_acceptor': array([-20,3])}
#donor input lengths for MaxEnt

maxEntInvariants = {'me_donor': [3,4],
                    'me_acceptor': [18,19]}
#regions in acceptor and donor motifs that should not be mutated

maxEnt5Prime = {'me_donor': 'exon', 'me_acceptor': 'intron'}
#what type of sequence is 5' of this motif type

filterScore = 1
#the filterScore determines at what score to print a cryptic motif

maxEntScoreDicts = {'me_donor': {}, 'me_acceptor': {}}
#these dicts will hold stored maxEnt scores for donors/acceptors
#this way, we won't have to recompute maxEnt scores with slow perl calls

######bs-finder Settings
findBSPath = topDir+"perl_utils"
findBSProg = "find_branchsite.pl"
bsUpstreamSearch = 50
#number of bases upstream of 3' acceptor to look for branch sites


######ppt-finder Settings
maxPPT3prime = 10 #maximum distance upstream of AG for ppt to end
minPPT3prime = 2  #minimum distance upstream of AG for ppt to end (incl AG)
minPPTpctCT = 0.5  #minimum percentage CT in PPT

######motif-finder Settings
motifDir = topDir+"/sequences/motifs/"

######context Settings
#NOTE: Currently not using...
context = ('ACCCGATTCAGCGAACCGCCTCGGTTTCCCTAACCCAATCCAGCCAGTAC',
           'TAATTTTCATAATTTGTTTTGTACTGAGTGCTGGCTAGTCAGATTACCTG') #2.2
context_size = 5


#===============================================================================
# mutate-motif Settings
#===============================================================================

max_mut_iter = 5 #number of times to mutate a single motif before stopping
mutate_record_iter = 5 #number of times to scan entire sequence iteratively
mutate_record_max = 5 #number of times to start over from original sequence

#when mutating motifs, if multiple motifs score below this value on maxent, then
#take one of them randomly. If all motifs are above this score, then just take
#the best one. Setting this to 0 means that if multiple mutations remove the 
#original motif, then any of them are fine, but if none of them do, then only
#pick the best replacement
mutate_min_rand_choice = 1.5 

correct_splice_signals = set() 
#this will hold a unique set of splice signals that we want to keep


#see mutate.mutate_meta_feature() fxn for details on these
MUT_META_FINAL_PCT = .1
MUT_META_MAX_ITER = 3
MUT_META_MUT_PER_ITER = 2

#mammalian conservation settings
MAM_CONSERV_MIN_WINDOW_SCORE = 0.6


#####score_exons/generate_mutant Settings

#maxEnt score ranges to generate tuples in
gen_mut_ranges = [(-10,0),(3,5),(7,8),(10,20)] 

#number of mutants to find per range (above) 
gen_mut_count = 4

#this controls the amount of 'branching' when searching for mutants in a range,
#increasing will use more memory, but it might help find some mutant scores. 
#12 is good, lower will be faster, higher will get you more mutants if you are
#stuck. It corresponds to the number of single-nucleotide mutant branches to 
#CREATE.
gen_mut_stored_sbps = 12

#similar implications to above, except it controls number of mutant branches to
#follow based on their closeness to the desired range after scoring.
gen_mut_follow_sbps = 5

######entropy Settings 

#any string with a kolmogorov approx (computed with zlib) that is less than this
#number will not be kept when mutating motifs. This is to avoid long n-runs or
#short repeats. It's just an approximation of kolmogorov, of course, and doesn't
#work on very short strings.
use_entropy = True        #if False, don't calculate entropy changes

#currently not using improve_entropy 
#if True, try to increase entropy if it starts too low 
improve_entropy = True 
#this it the minimum allowable entropy 
kol_minscore = 0.5
#this is how much to expand around the motif when looking
kol_neighborhood = 4
#this is the size of the        
kol_winsize = 8

#===============================================================================
# ensembl-exon Settings
#===============================================================================

#ensembl database settings

ens_release = 63

ens_lcl_db_dict = {'host':  "127.0.0.1",
                   'user':  "root",
                   'passwd': "",
                   'port':   3306,
                   'db':     "homo_sapiens_core_63_37"}

ens_rmt_db_dict = {'host': 'ensembldb.ensembl.org',
                   'user': 'anonymous',
                   'port': 5306,
                   'passwd': ''}

ens_data_dir   = '/Users/dbgoodman/Dropbox/intron/data/ccds_ensembl/'
ens_gbk_dir    = ens_data_dir + 'gbk/'
ens_fas_dir    = ens_data_dir + 'fas/'
ens_exon_fn    = ens_data_dir + 'all_CCDS_exons.sorted.tsv' 
ens_exon_stats = ens_data_dir + '1000_CCDS_exon_stats.txt'
ens_mutstats_fn= ens_data_dir + 'CCDS_exon_mutants.txt'

cut_sites = ['GGCGCGCC',
             'TTAATTAA']

######common globals
programTemplate = string.Template("$path/$program")
#for convenience


