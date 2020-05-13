import csv,os
FileName=Data=''
def Csv_format(filename,Mode,dict_=None):
    if Mode=='a+':
        FileName=filename
        header=[a for a in dict_.keys()]   
        status=Csv_format(filename, 'check',dict_)
        f=open(filename,Mode)
        s=csv.DictWriter(f,fieldnames=header)
        if not status:
            s.writeheader()
        s.writerow(dict_)
    elif Mode=='r':
        f=open(filename,Mode)
        s=csv.DictReader(f)
        return s
    elif Mode == 'check':
        return os.path.isfile(filename)