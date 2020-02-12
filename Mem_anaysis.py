from elftools.elf.elffile import ELFFile
from capstone import *
import pandas as pd

def process_file(fname):
 with open(fname, 'rb') as f:
  e = ELFFile(f)
  temp = []
  text1 = e.get_section_by_name('.text')
  stext1 = text1.header['sh_size']
  ro1 = e.get_section_by_name('.rodata')
  sro1 = ro1.header['sh_size']
  data11 = e.get_section_by_name('.data')
  sdata11 = data11.header['sh_size']
  bss1 = e.get_section_by_name('.bss')
  sbss1 = bss1.header['sh_size']
  data12 = e.get_section_by_name('.data.wlan')
  sdata12 = data12.header['sh_size']
  data13 = e.get_section_by_name('.data.wlan.platform')
  sdata13 = data13.header['sh_size']
  data14 = e.get_section_by_name('.sdata')
  sdata14 = data14.header['sh_size']
  data15 = e.get_section_by_name('.405_DEVCFG_DATA')
  sdata15 = data15.header['sh_size']
  data1 = sdata11 + sdata12+sdata13+sdata14+sdata15
  temp = [["WLAN",stext1,sro1,data1,sbss1]]
  return temp

def process_file1(fname):
 with open(fname, 'rb') as f:
  e = ELFFile(f)
  temp = []
  text1 = e.get_section_by_name('.text_sw')
  stext1 = text1.header['sh_size']
  ro1 = e.get_section_by_name('.rodata')
  sro1 = ro1.header['sh_size']
  data11 = e.get_section_by_name('.data')
  sdata11 = data11.header['sh_size']
  bss1 = e.get_section_by_name('.bss')
  sbss1 = bss1.header['sh_size']
  data12 = e.get_section_by_name('.data_l1wb_l2uc')
  sdata12 = data12.header['sh_size']
  data13 = e.get_section_by_name('.data_uncached')
  sdata13 = data13.header['sh_size']
  data14 = e.get_section_by_name('.sdata')
  sdata14 = data14.header['sh_size']
  data15 = e.get_section_by_name('.405_DEVCFG_DATA')
  sdata15 = data15.header['sh_size']
  data1 = sdata11 + sdata12+sdata13+sdata14+sdata15
  temp = [["CORE",stext1,sro1,data1,sbss1]]
  return temp  

def process_file2(fname):
 with open(fname, 'rb') as f:
  e = ELFFile(f)
  temp = []
  text1 = e.get_section_by_name('.text_sw')
  stext1 = text1.header['sh_size']
  ro1 = e.get_section_by_name('.rodata')
  sro1 = ro1.header['sh_size']
  data11 = e.get_section_by_name('.data')
  sdata11 = data11.header['sh_size']
  bss1 = e.get_section_by_name('.bss')
  sbss1 = bss1.header['sh_size']
  data12 = e.get_section_by_name('.data_l1wb_l2uc')
  sdata12 = data12.header['sh_size']
  data13 = e.get_section_by_name('.data_uncached')
  sdata13 = data13.header['sh_size']
  data14 = e.get_section_by_name('.sdata')
  sdata14 = data14.header['sh_size']
  data15 = e.get_section_by_name('.405_DEVCFG_DATA')
  sdata15 = data15.header['sh_size']
  data1 = sdata11 + sdata12+sdata13+sdata14+sdata15
  temp = ["CORE",stext1,sro1,data1,sbss1]
  return temp    


if __name__ == '__main__':
 print("\n*Press 1 for Wlan\n"+"*Press 2 for Core\n"+"*Press 3 for Both\n ")
 input = raw_input("Enter your Choice :  ")
 i = int(input)
 if i==1 :
  print("wlan")
  f1 = raw_input("Enter wlan file name along with the path from current directory : ")
  n1 = process_file(f1)
  df = pd.DataFrame(n1,columns=['Section','TEXT','RoDATA','DATA','BSS'])
  df['TOTAL'] = df.sum(axis=1)
  print(df)
  df.to_csv('memory.csv')
 elif i==2 :
  f1 = raw_input("Enter core file name along with the path from current directory : ")
  n1 = process_file1(f1)
  df = pd.DataFrame(n1,columns=['Section','TEXT','RoDATA','DATA','BSS'])
  df['TOTAL'] = df.sum(axis=1)
  print(df)
  df.to_csv('memory.csv')
 else :
  f1 = raw_input("Enter wlan file name along with the path from current directory : ")
  f2 = raw_input("Enter core file name along with the path from current directory : ")
  n1 = process_file(f1)
  n2 = process_file2(f2)
  df = pd.DataFrame(n1,columns=['Section','TEXT','RoDATA','DATA','BSS'])
  df1=df.append({'Section':n2[0],'TEXT': n2[1],'RoDATA':n2[2],'DATA':n2[3],'BSS':n2[4]},ignore_index=True)
  df1['TOTAL'] = df1.sum(axis=1)
  df2=df1.append({'Section':'TOTAL','TEXT': df1['TEXT'].sum(),'RoDATA':df1['RoDATA'].sum(),'DATA':df1['DATA'].sum(),'BSS':df1['BSS'].sum(),'TOTAL':df1['TOTAL'].sum()},ignore_index=True)
  print(df2)
  df2.to_csv('memory.csv')

 