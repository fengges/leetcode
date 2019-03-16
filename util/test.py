
with open('F:\\project\\test.txt','r',encoding ='utf8') as f:
    text=f.read()
with  CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse','coref'], timeout=30000, memory='16G') as client:
    pattern='[{ner:"CITY"}|{ner: "STATE_OR_PROVINCE"}|{ner:"LOCATION"}]+'
    matches = client.tokensregex(text, pattern, to_words=True)
    print(matches)