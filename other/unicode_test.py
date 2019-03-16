# -*- coding: utf-8 -*-

from stanfordnlp.server import CoreNLPClient

line_count = [0]
s = []
# with open('retest0.txt','r',encoding='latin-1') as f:
#
#         for line in f:
#             s.append(line)
#             line_count.append(len(line)+line_count[-1])
#         text = "".join(s)
f = open('retest0.txt','r',encoding='utf-8')
text = f.read()
# print(type(text))
# text = text.encode('utf-8')
# print(type(text))
with CoreNLPClient(annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse','coref'], timeout=30000, memory='16G') as client:
    pattern='[{ner:"CITY"}|{ner: "STATE_OR_PROVINCE"}|{ner:"LOCATION"}]+'
    matches = client.tokensregex(text, pattern)
    print(matches)