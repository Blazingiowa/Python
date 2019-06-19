in_file="data.csv"
out_file="kion10y.csv"

with open(in_file, "rt",encoding="Shift_JIS")as fr:
    lines=fr.readlines()

lines=["年,月,日,気温,品質,均質\n"]+lines[5:]
lines=map(lambda v: v.replace('/',','),lines)
result="".join(lines).strip()

with open(out_file, "wt",encoding="utf-8")as fw:
    fw.write(result)
    print("saved.")