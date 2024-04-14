import os
import hashlib
from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad, unpad  
from Crypto.Random import get_random_bytes  
  
def calculate_file_md5(file_path):  
    """  
    计算文件的MD5哈希值。  
  
    :param file_path: 要计算MD5的文件路径。  
    :return: 文件的MD5哈希值的十六进制字符串表示。  
    """  
    if not os.path.isfile(file_path):  
        raise FileNotFoundError(f"文件 {file_path} 不存在")  
  
    # 创建一个md5 hash对象  
    md5_hash = hashlib.md5()  
  
    # 以二进制模式打开文件  
    with open(file_path, "rb") as file:  
        # 读取文件内容并更新hash对象  
        for chunk in iter(lambda: file.read(4096), b""):  
            md5_hash.update(chunk)  
  
    # 获取MD5哈希值并返回其十六进制字符串表示  
    return md5_hash.hexdigest()  

# 示例用法  
# file_path = './北邮-郑凤-举报信.pdf'  # 替换为你的文件路径  
# md5_value=None
# try:  
#     md5_value = calculate_file_md5(file_path)  
#     print(f"文件的MD5哈希值为: {md5_value}")  
# except FileNotFoundError as e:  
#     print(e)
# if not os.path.exists(f"./{md5_value}"):
#     os.mkdir(f"./{md5_value}")

 
  
def encrypt_file(input_filename, output_filename, key):  
    """  
    加密文件。  
  
    :param input_filename: 要加密的文件名。  
    :param output_filename: 加密后的文件名。  
    :param key: 加密密钥，应为16（AES128）、24（AES192）或32（AES256）字节长。  
    """  
    cipher = AES.new(key, AES.MODE_CBC)  
      
    # 读取原始文件内容  
    with open(input_filename, "rb") as f:  
        plaintext = f.read()  
      
    # 对明文进行填充  
    padded_text = pad(plaintext, AES.block_size)  
      
    # 加密填充后的文本  
    ciphertext = cipher.encrypt(padded_text)  
      
    # 获取IV（初始化向量），通常与密文一起保存  
    iv = cipher.iv  
      
    # 将IV和密文一起写入输出文件  
    with open(output_filename, "wb") as f:  
        f.write(iv)  
        f.write(ciphertext)  
  

  
# 生成一个随机的密钥，这里为了简化，我们直接用一个固定的密钥  
# 在实际应用中，应使用安全的随机密钥生成方法，并妥善保管密钥  
key = get_random_bytes(16)  # 对于AES-128，密钥长度应为16字节  
  
# 加密文件  
input_file = 'plaintext.txt'  
encrypted_file = 'encrypted.bin'  
encrypt_file(input_file, encrypted_file, key)  
print(f"文件 {input_file} 已加密为 {encrypted_file}")  
  
# 解密文件  
decrypted_file = 'decrypted.txt'  
decrypt_file(encrypted_file, decrypted_file, key)  
print(f"文件 {encrypted_file} 已解密为 {decrypted_file}")