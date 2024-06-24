import os, json
from tqdm import tqdm
import numpy as np

def calculate_cos_similarity(a, b):
    v1 = np.array(a)
    v2 = np.array(b)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    return np.dot(v1, v2) / (norm_v1 * norm_v2)


data_dir = './data/defects4j'
cov_data_dir = './coverage_data'
sub_dir_list = os.listdir(data_dir)
sub_dir_list = ['Chart_10']



for sub_dir in tqdm(sub_dir_list):
    output_file = os.path.join(data_dir, sub_dir, 'coverage_similarity.json')
    similarities = {}
    # failing_test_file = os.path.join(data_dir, sub_dir, 'failing_tests')
    test_snippet_file = os.path.join(data_dir, sub_dir, 'test_snippet.json')

    tests_sig_hash_format = []
    test_matrix = {}

    with open(os.path.join(data_dir, sub_dir, 'failing_tests'), 'r') as ff:
        for l in ff:
            if l.startswith('--- '):
                failing_test = l.split()[-1]
                failing_test_signature = failing_test.replace("::", ".")+"()"
                # failing_test_in_matrix = failing_test.replace("::", '#')[:-2]
                similarities[failing_test_signature] = {}
                
    with open(test_snippet_file, 'r', encoding='utf-8') as tf:
        test_snippets = json.load(tf)

        for test in test_snippets:
            sig_split = test["signature"].split('.')
            sig_in_matrix = '.'.join(sig_split[:-1])+'#'+(sig_split[-1][:-2])
            tests_sig_hash_format.append(sig_in_matrix)

    # autofl_with_passingtest/coverage_data/Chart_1/matrix.txt
    with open(os.path.join(cov_data_dir, sub_dir, "matrix.txt"), 'r') as mf:
        lines = mf.readlines()
        for i, line in enumerate(lines):
            lines[i] = list(map(int, line.split()[:-1]))
        
        with open(os.path.join(cov_data_dir, sub_dir, "tests.csv"), 'r') as tf:
            tests = tf.readlines()
            for i in range(1, len(tests)):
                test_sig = tests[i].split(',')[0]
                if test_sig in tests_sig_hash_format:
                    test_matrix[test_sig] = lines[i-1]

    for failing_test in similarities.keys():
        failing_test_in_matrix = '.'.join(failing_test.split('.')[:-1])+'#'+failing_test.split('.')[-1][:-2]
        for test in test_matrix.keys():
            if test != failing_test_in_matrix:
                try:
                    similarities[failing_test][test.replace('#', '.')+'()'] = calculate_cos_similarity(test_matrix[test], test_matrix[failing_test_in_matrix])
                except:
                    pass
                # print(calculate_cos_similarity(test_matrix[test], test_matrix[failing_test_in_matrix]))


        # sorted_similarities = sorted(similarities[failing_test].items(), key = lambda item:item[1], reverse = True)
        # similarities[failing_test] = sorted_similarities

    with open(output_file, 'w') as wf:
        json.dump(similarities, wf, indent = 4)

        




    # with open(failing_test_file, 'r') as ff:
    #     for l in ff:
    #         if l.startswith('--- '):
    #             failing_test = l.split()[-1]
    #             failing_test_signature = failing_test.replace("::", ".")+"()"
    #             failing_test_in_matrix = failing_test.replace("::", '#')
    #             similarities[failing_test_signature] = {}

    #         with open(test_snippet_file, 'r', encoding='utf-8') as tf:
    #             test_snippets = json.load(tf)
                

    #             for test in test_snippets:
    #                 if test['signature'] != failing_test_signature:
    #                     passing_test_snippet = test['snippet']
    #                     similarity = calculate_token_similarity(passing_test_snippet, failing_test_snippet)
    #                     similarities[failing_test_signature][test['signature']] = similarity

    # output_file = os.path.join(data_dir, sub_dir, 'token_similarity.json')
    # with open(output_file, 'w') as wf:
    #     json.dump(similarities, wf, indent = 4)