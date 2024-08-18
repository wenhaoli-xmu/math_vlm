from datasets import load_dataset
from misc import create_dir, dump_data
from itertools import chain
import tqdm

ds = load_dataset("dali-does/clevr-math")


# 1. 创建math_data目录
create_dir("clevr_math")


# 2. 遍历数据集
for x in tqdm.tqdm(chain.from_iterable([ds['train'], ds['test'], ds['validation']])):    
    dump_data("clevr_math", x["id"], x["id"], x['image'], x['question'], x['label'])
