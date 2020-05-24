from csv import reader
from matplotlib import pyplot
from dateutil import parser

with open('/home/pi/Desktop/testr/Columbus_Ed_astro_pi_datalog.csv','r') as f:
    data = list(reader(f))

temp = [i[3] for i in data[1::]]        
#print(temp[1:10])
        
time = [parser.parse(i[19]) for i in data[1::]]
#print(time[1:10])



pyplot.plot(time, temp)
pyplot.title('Temperature changes over Time')
pyplot.xlabel('Time/Hours')
pyplot.ylabel('Temperature/$^\circ$C')
pyplot.show()
