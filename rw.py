with open(r"C:\Users\tielb\Desktop\file.txt", 'rb+') as f:
    #全部文件
    #read_data = f.read()
    #遍历
    for line in f:
        print(line, end='')
    f.write(b'0123456789abcdef')
f.closed
#print(read_data)
