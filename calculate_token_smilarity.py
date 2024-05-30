import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_token_similarity(text1, text2):
    # TF-IDF Vectorizer를 사용하여 텍스트를 벡터화
    vectorizer = TfidfVectorizer().fit_transform([text1, text2])
    vectors = vectorizer.toarray()
    
    # 코사인 유사도를 계산
    similarity = cosine_similarity(vectors)
    
    return similarity[0][1]


data_dir = './data/defects4j'
sub_dir_list = os.listdir(data_dir)



for sub_dir in sub_dir_list:
    similarities = {}
    failing_test_file = os.path.join(data_dir, sub_dir, 'failing_tests')
    with open(failing_test_file, 'r') as ff:
        content = ff.readlines()
        failing_test = content[0].split()[1]
        failing_test_signature = failing_test.replace("::", ".")+"()"

    test_snippet_file = os.path.join(data_dir, sub_dir, 'test_snippet.json')

    with open(test_snippet_file, 'r', encoding='utf-8') as tf:
        test_snippets = json.load(tf)
        # compare_test_signature = 'com.google.javascript.jscomp.TypeCheckTest.testDuplicateLocalVarDecl()'
        for test in test_snippets:
            if test['signature'] == failing_test_signature:
                failing_test_snippet = test['snippet']
                # print(failing_test_snippet)
            # elif test['signature'] == compare_test_signature:
                # print(test['snippet'])
    
        for test in test_snippets:
            if test['signature'] != failing_test_signature:
                passing_test_snippet = test['snippet']
                similarity = calculate_token_similarity(passing_test_snippet, failing_test_snippet)
                similarities[test['signature']] = similarity
    
    output_file = os.path.join(data_dir, sub_dir, 'token_similarity.json')
    with open(output_file, 'w') as wf:
        json.dump(similarities, wf, indent = 4)
    
    


            
    






