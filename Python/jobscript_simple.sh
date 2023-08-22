echo '-------------------------'
echo 'Installing Dependences'
echo '-------------------------'
pip3 install numpy

start=$(date +%s%N)

timestamp=$(date +%Y%m%d%H%M)

echo '-------------------------'
echo 'Setting ouput file'
echo '-------------------------'

declare -u results="results-"
if(($# == 0))
then
    results+="host"
fi
results+=$1
results+="-python-"
results+=${timestamp}
results+=".csv"

touch ${results,,}
cd Experiments

echo 'All set!'
echo '-------------------------'

python3 ../tools/create_file_header.py ${results,,}

echo '-------------------------'
echo 'Look and say sequence'
echo '-------------------------'
python3 exp2_look_and_say.py 40 ${results,,}

echo '-------------------------'
echo 'Count Unique Words in File'
echo '-------------------------'
python3 exp3_count_unique_words.py ../Data/bible.txt ${results,,}

echo '-------------------------'
echo 'Fibonacci Sequence'
echo '-------------------------'
python3 exp4_fibonacci.py 25 ${results,,}
python3 exp4_fibonacci.py 30 ${results,,}


echo '-------------------------'
echo 'Finishing Tasks'
echo '-------------------------'
end=$(date +%s%N)
echo "Elapsed Time $(($(($end-$start))/1000000)) ms"
python3 ../tools/writeTime.py "${start}" "${end}" ${timestamp}
echo 'All finished!'
echo '-------------------------'