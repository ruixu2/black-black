def decrypt_file(input_filename, output_filename, key):  
    """  
    解密文件。  
  
    :param input_filename: 要解密的文件名。  
    :param output_filename: 解密后的文件名。  
    :param key: 解密密钥，应与加密时使用的密钥相同。  
    """  
    with open(input_filename, "rb") as f:  
        # 读取IV和密文  
        iv = f.read(16)  
        ciphertext = f.read()  
      
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)  
      
    # 解密密文  
    decrypted_text = cipher.decrypt(ciphertext)  
      
    # 去除填充  
    plaintext = unpad(decrypted_text, AES.block_size)  
      
    # 将解密后的明文写入输出文件  
    with open(output_filename, "wb") as f:  
        f.write(plaintext)  