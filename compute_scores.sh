[ ! -d combined_fl_results ] && mkdir combined_fl_results

# Defects4J (AUTOFL-GPT-3.5)
python compute_score.py \
    results/passing_test_and_explain_1/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/passing_test_and_explain_results_R1_full.json

python compute_score.py \
    results/passing_test_and_explain_1/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_2/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/passing_test_and_explain_results_R2_full.json

python compute_score.py \
    results/passing_test_and_explain_1/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_2/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_3/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/passing_test_and_explain_results_R3_full.json

python compute_score.py \
    results/passing_test_and_explain_1/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_2/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_3/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_4/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/passing_test_and_explain_results_R4_full.json

python compute_score.py \
    results/passing_test_and_explain_1/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_2/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_3/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_4/gpt-3.5-turbo-0125 \
    results/passing_test_and_explain_5/gpt-3.5-turbo-0125 \
    -l java -a -v -o combined_fl_results/passing_test_and_explain_results_R5_full.json

