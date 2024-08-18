from datasets import load_dataset
from misc import create_dir, dump_data
from itertools import chain

ds = load_dataset("AI4Math/MathVista")


# 1. 创建math_data目录
create_dir("math_vista")

# 2. 遍历数据集
for x in ds['testmini']:
    x['image'] = x['image'].split('/')[-1]
    dump_data("math_vista", x['pid'], x['image'], x['decoded_image'], x['query'], x['answer'])
