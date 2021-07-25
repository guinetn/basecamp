import ftplib

def chunks(data, rows=10000):
    """ Divides the data into 10000 rows each """

    for i in range(0, len(data), rows):
        yield data[i:i+rows]

#Open ftp connection
ftp = ftplib.FTP('ftp.seismo.nrcan.gc.ca', 'anonymous',
'user')

#List the files in the current directory
print("File List:")
files = ftp.dir()

import datetime

now=datetime.datetime.now()
ftp.cwd("intermagnet/minute/provisional/IAGA2002/" + str(now.year) + "/" + str(now.strftime("%m")))
# files = ftp.dir()

ftp.pwd()

# ftp.retrbinary("RETR " + "cki20200813pmin.min",open("cki20200813pmin.min", 'wb').write)

file_list = ftp.nlst()
