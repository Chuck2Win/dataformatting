# k scholar 입법 정보 회의록
import pandas as pd
from tqdm import tqdm
import re
import os

input_dir = r'/data/nlp/ai_data/대화체/K-Scholar_입법정보_회의록'
output_dir = r'/data/nlp/ai_data/ok_0915/K-Scholar_입법정보_회의록'

data_list = [i for i in os.listdir(input_dir) if i.endswith('csv')]

os.makedirs(output_dir, exist_ok=True)
F = open(os.path.join(output_dir, 'K-Scholar.txt'),'w',encoding='utf-8')
for adr in tqdm(data_list):
    #  error_bad_lines 같은 경우에서 error가 있으면 그냥 skip해준다.
    data = pd.read_csv(os.path.join(input_dir,adr),header=0,error_bad_lines = False)
    d = data['발언내용'].tolist()
    for i in d:
        try:
            F.write(i)
            F.write('\n')
        except:
            continue
    F.write('\n')
F.close()
