import subprocess
import sys

input_file = sys.argv[1]
bids = []
bams = []
with open(input_file) as _:
    for line in _:
        if line.strip()[0] == '#':
            continue
        bid_type, bid, bam = line.rstrip('\n').split('\t')
        bids.append(bid)
        bams.append(bam)

#bids = ['2015-17', '2014-1456', '2015-18', '2014-1457', '2015-19', '2014-1458', '2015-20', '2014-1459', '2015-21', '2015-19']
#bams = ['/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-17/2015-17_150109_SN484_0326_AC5FU8ACXX_8Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1456/2014-1456_140820_SN1070_0247_AHA97GADXX_2Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-18/2015-18_150109_SN484_0326_AC5FU8ACXX_8Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1457/2014-1457_140806_SN1070_0243_AH9FTFADXX_1Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-19/2015-19_150109_SN484_0326_AC5FU8ACXX_5Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1458/2014-1458_140806_SN1070_0243_AH9FTFADXX_1Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-20/2015-20_150109_SN484_0326_AC5FU8ACXX_5Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2014-1459/2014-1459_140806_SN1070_0243_AH9FTFADXX_2Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-21/2015-21_150109_SN484_0326_AC5FU8ACXX_3Aligned.out.bam',
#'/mnt/cinder/SCRATCH/SCRATCH/RAW/2015-19/2015-19_150616_SN484_0358_AC73V5ACXX_8Aligned.out.bam']

novosort_path = '~/TOOLS/nova/novosort'
prefix = '/mnt/cinder/SCRATCH/SCRATCH/RAW/'
run_cmd = ''

for i,bam in enumerate(bams):
    file_name = bam.split('/')[7]
    file_name = file_name.split('.')[0]
    output_path = prefix + bids[i] + '/' + file_name + '.sorted.Aligned.out.bam'
    run_cmd += novosort_path + ' --output ' + output_path + ' --index ' + bam + ' 2>' + prefix + bids[i] + '/' + 'novosort.run.log;'
print run_cmd


