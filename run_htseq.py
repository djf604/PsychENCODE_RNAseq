import subprocess
import sys

input_file = sys.argv[1]
bids_rz = []
bids_polyA = []
bams_rz = []
bams_polyA = []
with open(input_file) as _:
    for line in _:
        if line.strip()[0] == '#':
            continue
        bid_type, bid, bam = line.rstrip('\n').split('\t')
        if bid_type == 'polyA':
            bids_polyA.append(bid)
            bams_polyA.append(bam)
        else:
            bids_rz.append(bid)
            bams_rz.append(bam)

#bids_rz = ['2015-17', '2015-18', '2015-19', '2015-20', '2015-21', '2015-19_extra']
#bids_polyA = ['2014-1455', '2014-1456', '2014-1457', '2014-1458', '2014-1459']
#bams_rz = ['/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-17/2015-17_150109_SN484_0326_AC5FU8ACXX_8.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-18/2015-18_150109_SN484_0326_AC5FU8ACXX_8.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-19/2015-19_150109_SN484_0326_AC5FU8ACXX_5.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-20/2015-20_150109_SN484_0326_AC5FU8ACXX_5.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-21/2015-21_150109_SN484_0326_AC5FU8ACXX_3.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-19/2015-19_150616_SN484_0358_AC73V5ACXX_8.sorted.Aligned.out.bam']
#bams_polyA = ['/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1455/2014-1455_140806_SN1070_0243_AH9FTFADXX_1.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1456/2014-1456_140820_SN1070_0247_AHA97GADXX_2.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1457/2014-1457_140806_SN1070_0243_AH9FTFADXX_1.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1458/2014-1458_140806_SN1070_0243_AH9FTFADXX_1.sorted.Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1459/2014-1459_140806_SN1070_0243_AH9FTFADXX_2.sorted.Aligned.out.bam']

feature_types=['gene', 'transcript', 'exon']

htseq_path = 'htseq-count'
#gtf_path = '/mnt/cinder/SCRATCH/REFS/annotation/spike_in_hg19/spike_in_hg19_gencode.v19.chr_patch_hapl_scaff.annotation_fasta_matched.gtf'
gtf_path = '/mnt/cinder/old_SCRATCH/REFS/GENCODE19/Transcriptome/gencode.v19_w_spike.gtf'
options_rz = ' --format=bam --stranded=reverse '
options_polyA = ' --format=bam --stranded=no '
output_path_prefix = '/mnt/cinder/SCRATCH/SCRATCH/RAW/htseq_results/'
bam_file_path_prefix = '/mnt/cinder/SCRATCH/SCRATCH/RAW/'
run_cmd = ''

for i, bid in enumerate(bids_rz):
    run_cmd += 'mkdir -p ' + output_path_prefix + '/' + bid + ';'
    for feature in feature_types:
        idattr = 'transcript_name'
        if feature == 'gene':
            idattr = 'gene_name'
        run_cmd += htseq_path + options_rz + '--idattr=' + idattr + ' --type=' + feature + ' ' + bams_rz[i] + ' ' + gtf_path + ' > ' + output_path_prefix + bid + '/' + feature + '.named.counts 2>' + output_path_prefix + bid + '/' + feature + '.named.log;'
        
for i, bid in enumerate(bids_polyA):
    run_cmd += 'mkdir -p ' + output_path_prefix + '/' + bid + ';'
    for feature in feature_types:
        idattr = 'transcript_name'
        if feature == 'gene':
            idattr = 'gene_name'
        run_cmd += htseq_path + options_polyA + '--idattr=' + idattr + ' --type=' + feature + ' ' + bams_polyA[i] + ' ' + gtf_path + ' > ' + output_path_prefix + bid + '/' + feature + '.named.counts 2>' + output_path_prefix + bid + '/' + feature + '.named.log;'

print run_cmd


