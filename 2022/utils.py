import re
def extract_nums(input_str:str) -> list[float]:
    return [float(x) for x in re.findall(r'\d+', input_str)]

def read_input(input_dir:str):
    with open(input_dir) as f:
        return f.read().strip()