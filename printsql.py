def printsql(cur, length = 10):
    # 获取结果集的每一行
    rows = cur.fetchall()
    # 获取所有字段名
    all_fields = cur.description
    
    
    # 首先打印字段名
    field_messages = []
    for i in range(len(all_fields)):
        # 格式化输出结果，len参数是各列的显示宽度，可以指定常量，也可自定义函数进行获取。
        field_messages.append("{str:<{len}}".format(str=str(all_fields[i][0]), len=length))
    
    field_message = "".join(field_messages)
    print(field_message)
    
    # 然后逐行打印结果集
    for row in rows:
        row_messages = []
        for j in range(len(row)):
            # 格式化结果集
            row_messages.append("{str:<{len}}".format(str=str(row[j]), len=length))
        row_message = "".join(row_messages)
        print(row_message)