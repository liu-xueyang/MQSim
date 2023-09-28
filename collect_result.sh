set -x
set -e

result_dir=$1 # result directory name

for file in $(find $result_dir -name "*.xml"); do
    # run parser
    python3 parse_MQSim_out.py -i $file >> summary.csv
done