import json


def create_dir(name):
    import os
    if not os.path.exists("math_data"):
        os.mkdir("math_data")

    if not os.path.exists(f"math_data/{name}"):
        os.mkdir(f"math_data/{name}")
        os.mkdir(f"math_data/{name}/images")


def dump_data(name, _id, image_name, image, query, answer):
    conv = [
        {"from": "human", "value": f"<image>\n{query}"},
        {"from": "gpt", "value": f"{answer}"} 
    ]

    image_path = f"math_data/{name}/images/{image_name}"
    image = image.convert("RGB")

    with open(image_path, 'wb') as f:
        image.save(f)

    info = {
        "id": _id,
        "image": image_path,
        "width": image.width,
        "height": image.height,
        "conversations": conv
    }

    with open(f"math_data/{name}/captions.jsonl", 'a+') as f:
        f.write(json.dumps(info) + '\n')
