#!/bin/bash -f

#SBATCH --time=05:50:00
#SBATCH --job-name=numpy
#SBATCH --ntasks=40
#SBATCH --constraint=sky
#SBATCH -A j1008
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH -o Python2021-%j.out


#######################################################################
#                  System Environment Variables
#######################################################################

umask 022

#limit

source /usr/share/modules/init/csh
module purge

module load python/GEOSpyD/Min4.9.2_py3.9
#module load python/GEOSpyD/Ana2019.10_py3.7
start=$(date +%s%N)
timestamp=$(date +%Y%m%d%H%M)

echo '-------------------------'
echo 'Setting ouput file'

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
python3 tools/create_file_header.py ${results,,}

echo 'All set!'
echo '-------------------------'


echo '-------------------------'
echo 'Copy Matrix'
echo '-------------------------'
python3 Experiments/exp1_copy_matrix.py 1000 ${results,,}
python3 Experiments/exp1_copy_matrix.py 1500 ${results,,}
python3 Experiments/exp1_copy_matrix.py 2000 ${results,,}

echo '-------------------------'
echo 'Look and say sequence'
echo '-------------------------'
python3 Experiments/exp2_look_and_say.py 30 ${results,,}
python3 Experiments/exp2_look_and_say.py 35 ${results,,}
python3 Experiments/exp2_look_and_say.py 42 ${results,,}

echo '-------------------------'
echo 'Count Unique Words in File'
echo '-------------------------'
python3 Experiments/exp3_count_unique_words.py ./Data/bible.txt ${results,,}
python3 Experiments/exp3_count_unique_words.py ./Data/book1.txt ${results,,}
python3 Experiments/exp3_count_unique_words.py ./Data/plrabn12.txt ${results,,}
python3 Experiments/exp3_count_unique_words.py ./Data/world192.txt ${results,,}

echo '-------------------------'
echo 'Fibonacci Sequence'
echo '-------------------------'
python3 Experiments/exp4_fibonacci.py 25 ${results,,}
python3 Experiments/exp4_fibonacci.py 35 ${results,,}
python3 Experiments/exp4_fibonacci.py 40 ${results,,}

echo '-------------------------'
echo 'Matrix Multiplication'
echo '-------------------------'
python3 Experiments/exp5_matrix_multiplication.py 1500 ${results,,}
python3 Experiments/exp5_matrix_multiplication.py 1750 ${results,,}
python3 Experiments/exp5_matrix_multiplication.py 2000 ${results,,}

echo '-------------------------'
echo 'Belief Propagation'
echo '-------------------------'
python3 Experiments/exp6_belief_propagation.py 250 ${results,,}
python3 Experiments/exp6_belief_propagation.py 500 ${results,,}
python3 Experiments/exp6_belief_propagation.py 1000 ${results,,}

echo '-------------------------'
echo 'Markov Chain'
echo '-------------------------'
python3 Experiments/exp7_markov_chain.py 5000 ${results,,}
python3 Experiments/exp7_markov_chain.py 10000 ${results,,}
python3 Experiments/exp7_markov_chain.py 15000 ${results,,}

echo '-------------------------'
echo 'Compute FFT'
echo '-------------------------'
python3 Experiments/exp8_compute_FFT.py 10000 ${results,,}
python3 Experiments/exp8_compute_FFT.py 15000 ${results,,}
python3 Experiments/exp8_compute_FFT.py 20000 ${results,,}

echo '-------------------------'
echo 'Jacobi Iterative solver'
echo '-------------------------'
python3 Experiments/exp9_laplace_jacobi_4.py 100 ${results,,}
python3 Experiments/exp9_laplace_jacobi_4.py 150 ${results,,}
python3 Experiments/exp9_laplace_jacobi_4.py 200 ${results,,}

echo '-------------------------'
echo 'Compute square root of a matrix'
echo '-------------------------'
python3 Experiments/exp10_sqrt_matrix.py 1000 ${results,,}
python3 Experiments/exp10_sqrt_matrix.py 2000 ${results,,}
python3 Experiments/exp10_sqrt_matrix.py 4000 ${results,,}

echo 'Gauss Legendre quadrature'
echo '-------------------------'
python3 Experiments/exp11_gauss_legendre_quadrature.py 50 ${results,,}
python3 Experiments/exp11_gauss_legendre_quadrature.py 75 ${results,,}
python3 Experiments/exp11_gauss_legendre_quadrature.py 100 ${results,,}

echo '-------------------------'
echo 'Evaluation of functions'
echo '-------------------------'
python3 Experiments/exp12_evaluate_functions.py 7000 ${results,,}
python3 Experiments/exp12_evaluate_functions.py 8000 ${results,,}
python3 Experiments/exp12_evaluate_functions.py 9000 ${results,,}

echo '-------------------------'
echo 'Compute Munchausen Numbers'
echo '-------------------------'
python3 Experiments/exp13_munchausen_number.py 0 ${results,,}

echo '-------------------------'
echo 'Compute Pernicious Numbers'
echo '-------------------------'
python3 Experiments/exp14_pernicious_numbers.py 100000 ${results,,}

echo '-------------------------'
echo 'Processing a collection of files'
echo '-------------------------'
python3 Experiments/./Data/create_nc4Files.py

python3 Experiments/exp15_A_time_series_AOA.py 0 ${results,,}
end=$(date +%s%N)
echo "Elapsed Time $(($(($end-$start))/1000000)) ms"
python3 tools/writeTime.py "${start}" "${end}" ${results,,}
#time python exp_time_series_AOA_multiproc.py 1
#time python exp_time_series_AOA_multiproc.py 2
#time python exp_time_series_AOA_multiproc.py 4
#time python exp_time_series_AOA_multiproc.py 8
#time python exp_time_series_AOA_multiproc.py 16
#time python exp_time_series_AOA_multiproc.py 24
##time python exp_time_series_AOA_multiproc.py 28


