import csv
def create_csv(csv_head,csv_name):       #新建csv文件，参数为标题行，使用py列表
    path = csv_name
    with open(path,'w',newline='',encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(csv_head)
def write_csv(data_row,csv_name):        #为csv文件追加行信息，使用py列表
    path  = csv_name
    with open(path,'a+',newline='',encoding='utf-8') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(data_row)
