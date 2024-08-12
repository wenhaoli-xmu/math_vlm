from datasets import load_dataset
from misc import create_dir, dump_data

ds = load_dataset("AI4Math/MathVerse", 'testmini')


# 1. 创建math_data目录
create_dir("math_verse")


# 2. 遍历数据集
for x in ds['testmini']:    
    dump_data("math_verse", x['sample_index'], f"{x['sample_index']}.png", x['image'], x['query_cot'], x['answer'])
