[ ! -d combined_fl_results ] && mkdir combined_fl_results

# Defects4J (AUTOFL-GPT-3.5)
python compute_score.py \
    results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R1_full.json

python compute_score.py \
    results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R2_full.json

python compute_score.py \
    results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_3/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R3_full.json

python compute_score.py \
    results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_3/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_4/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R4_full.json

python compute_score.py \
    results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_3/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_4/gpt-3.5-turbo-0125 \
    results/just_cov_sim_passing_test_5/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R5_full.json

