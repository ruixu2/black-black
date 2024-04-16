import json
raw_text="""# 对于部分资料不易明文存储，避免和谐，加密后存储
info.json 文件记录加密的相关信息\n\n """
text=raw_text
f=open("./README.md",mode='w',encoding='utf-8')

f1=open("info.json",mode='r')
info_dict=json.load(f1)
print(info_dict)
f1.close()

keys=info_dict.keys()
for idx,key in enumerate(keys):

    text+=f"## {idx}-{info_dict[key][1]}\n md5:{str(key)}\n en_key: {info_dict[key][0]}\n\n"
f.write(text)
f.close