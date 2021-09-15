import os
import json
from tqdm import tqdm
input_dir=r'/data/nlp/ai_data/NIA/상담_데이터'
output_dir = r'/data/nlp/ai_data/ok_0915/NIA/상담_데이터'
os.makedirs(output_dir, exist_ok=True)
data_list = ['data','data2','data3','data4','data5']
for _,i in enumerate(data_list):
    F = open(os.path.join(output_dir,'상담_데이터_%d.txt'%(_+1)),'w',encoding = 'utf-8')
    out_path = os.path.join(input_dir, i)
    out_list = os.listdir(out_path)
    for j in tqdm(out_list):
        new_path = os.path.join(out_path, j)
        inner_path = [i for i in os.listdir(new_path) if i.endswith('txt')]
        new_path = os.path.join(new_path, inner_path[0])
        data = open(new_path,'r', encoding = 'utf-8').read()
        # 개행문자, 스페이스바 도 없애준다.
        data = data.strip()
        F.write(data)
        F.write('\n\n')
    F.close()    
