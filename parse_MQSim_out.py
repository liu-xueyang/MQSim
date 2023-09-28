# parse the result into:
# name,IOPS,IOPS_Read,IOPS_Write,Bandwidth,Bandwidth_Read,Bandwidth_Write,
# Device_Response_Time,Min_Device_Response_Time,Max_Device_Response_Time,Avg_Rd_Turnaround_Time,Avg_Wr_Turnaround_Time
import xml.etree.ElementTree as ET
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-i", help="Input file to parse", 
	type=str, dest="input_fname")
parser.add_argument("-o", help="Parse output file destination", 
	type=str, dest="output_fname")
args= parser.parse_args()

result_tree = ET.parse(args.input_fname)
root = result_tree.getroot()

Host_IO_Flow = root[0][0]
IOPS = Host_IO_Flow[4].text
IOPS_Read = Host_IO_Flow[5].text
IOPS_Write = Host_IO_Flow[6].text
Bandwidth = Host_IO_Flow[10].text
Bandwidth_Read = Host_IO_Flow[11].text
Bandwidth_Write = Host_IO_Flow[12].text
Device_Response_Time = Host_IO_Flow[13].text
Min_Device_Response_Time = Host_IO_Flow[14].text
Max_Device_Response_Time = Host_IO_Flow[15].text

Device_IO = root[1][0][1]
Avg_Rd_Turnaround_Time = Device_IO[1].text
Avg_Wr_Turnaround_Time = Device_IO[5].text

print(args.input_fname+","+IOPS+","+IOPS_Read+","+IOPS_Write+","+
  Bandwidth+","+Bandwidth_Read+","+Bandwidth_Write+","+
  Device_Response_Time+","+Min_Device_Response_Time+","+Max_Device_Response_Time+","+
  Avg_Rd_Turnaround_Time+","+Avg_Wr_Turnaround_Time)