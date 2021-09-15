# AI HUB data -> text로 바꾸기
# 논문자료
import os
import json
from tqdm import tqdm
#############################################
input_dir=r'감성대화말뭉치'
output_dir = r'감성대화말뭉치'
os.makedirs(output_dir, exist_ok=True)
data_list = os.listdir(input_dir)

F = open(os.path.join(output_dir,'감성대화말뭉치.txt'),'w',encoding = 'utf-8')
for i in data_list:
    if i.endswith('json'):
        d = json.load(open(os.path.join(input_dir,i),'rb'))
        for j in tqdm(d):
            for key,value in j['talk']['content'].items():
                F.write(value+'\n')
            F.write('\n')
        
