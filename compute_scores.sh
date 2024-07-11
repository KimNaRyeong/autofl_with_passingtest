[ ! -d combined_fl_results ] && mkdir combined_fl_results

# Defects4J (AUTOFL-GPT-3.5)
# python compute_score.py \
#     results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
#     -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R1_full.json

# python compute_score.py \
#     results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
#     -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R2_full.json

# python compute_score.py \
#     results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_3/gpt-3.5-turbo-0125 \
#     -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R3_full.json

# python compute_score.py \
#     results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_3/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_4/gpt-3.5-turbo-0125 \
#     -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R4_full.json

# python compute_score.py \
#     results/just_cov_sim_passing_test_1/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_2/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_3/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_4/gpt-3.5-turbo-0125 \
#     results/just_cov_sim_passing_test_5/gpt-3.5-turbo-0125 \
#     -l java -a -v -o combined_fl_results/just_cov_sim_passing_test_results_R5_full.json

# python compute_score.py \
#     results/d4j_autofl_1/gpt-4o \
#     results/d4j_autofl_2/gpt-4o \
#     results/d4j_autofl_3/gpt-4o \
#     results/d4j_autofl_4/gpt-4o \
#     results/d4j_autofl_5/gpt-4o \
#     results/d4j_autofl_6/gpt-4o \
#     results/d4j_autofl_7/gpt-4o \
#     results/d4j_autofl_8/gpt-4o \
#     results/d4j_autofl_9/gpt-4o \
#     results/d4j_autofl_10/gpt-4o \
#     -l java -a -v -o combined_fl_results/token_sim_gpt-4o_results_R10_full.json

# python compute_score.py \
#     results/d4j_autofl_1/gpt-3.5-turbo-0125 \
#     results/d4j_autofl_2/gpt-3.5-turbo-0125 \
#     results/d4j_autofl_3/gpt-3.5-turbo-0125 \
#     results/d4j_autofl_4/gpt-3.5-turbo-0125 \
#     results/d4j_autofl_5/gpt-3.5-turbo-0125 \
#     -l java -a -v -o combined_fl_results/d4j_gpt3-0125_results_R10_full.json

python compute_score.py \
    results/with_passing_test_1/gpt-3.5-turbo-0125 \
    results/with_passing_test_2/gpt-3.5-turbo-0125 \
    results/with_passing_test_3/gpt-3.5-turbo-0125 \
    results/with_passing_test_4/gpt-3.5-turbo-0125 \
    results/with_passing_test_5/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/d4j_token_sim_results_R5_full.json