import sys

INIT_COUNTS = 0

input_file_path = sys.argv[1]
total_counts = {}
bid_headers = []
with open(input_file_path) as htseq_file:
    for line in htseq_file:
        htseq_file_path, bid = line.rstrip('\n').split(';')
        bid_headers.append(bid)
        with open(htseq_file_path) as htseq_counts:
            for line in htseq_counts:
                (feature_name, feature_count) = line.rstrip('\n').split('\t')
                if feature_name not in total_counts:
                    total_counts[feature_name] = {}
                total_counts[feature_name][bid] = feature_count

print '\t'.join([''] + bid_headers)
#sys.stderr.write(str(total_counts))
for feature_name in total_counts:
    feature_line = [feature_name]
    for bid in bid_headers:
        if bid in total_counts[feature_name]:
            feature_line.append(total_counts[feature_name][bid])
        else:
            feature_line.append('')
    print '\t'.join(feature_line)
    
