
matrix = [[None for j in range(365 * 24 * 60)] for i in range(3 * n)]


BT = int(time.mktime(datetime.datetime.strptime("20140101 00:00", "%Y%m%d %H:%M").timetuple()))


n = 0 
for folder in directory:
    pathinfolder = os.path.join(dataPath, folder)
    if os.path.isfile(pathinfolder) == False:
        csvfileinonefolder = os.listdir(pathinfolder)
        for file in csvfileinonefolder:
            if file.endswith(".csv"):
                print "process " + file
                bufferreader = open(os.path.join(pathinfolder, file))
                col = bufferreader.readline().split(",")
                previousdate = int(time.mktime(datetime.datetime.strptime(col[1][0:14], "%Y%m%d %H:%M").timetuple()))
                max = col[2]
                print "\n"
                min = col[2]
                final = col[2]
                line = bufferreader.readline()
                while line:
                	matrix[3 * n][(previousdate - BT) / 60] = max
                n = n+1

#interpolation
def linerinterpolate(y1, y2, mu):
    return y1 * (1 - mu) + y2 * mu

def cosineinterpolate(y1, y2, mu):
    mu2 = (1 - math.cos(mu * math.pi)) / 2
    return y1 * (1 - mu2) + y2 * mu2

def interpolate(csvarray, formular):
    for y in csvarray:
        columlength = len(y)
        for i in range(columlength):
            if y[i]>0:
                break
        for j in range(i + 1, columlength):
            if y[j]>0 and j-i>1:
                    for k in range(i + 1, j):
                        mu = float(k - i) / (j - i)
                        y[k] = formular(y[i], y[j],mu)
            i = j

print dataPath
interpolate(linercsv, linerinterpolate)
print dataPath
interpolate(coscsv, cosineinterpolate)



def cubicinterpolate(y1, y2, m1, m2, mu):
    mu2 = mu * mu
    a0 = 2 * y1 + m1 - 2 * y2 + m2
    a1 = -3 * y1 - 2 * m1 + 3 * y2 - m2
    a2 = m1
    a3 = y1
    return a0 * mu2 * mu + a1 * mu2 + a2 * mu + a3
    

print dataPath
for y in cubcsv:
        columlength = len(y)
        for i in range(columlength):
            if y[i]:
                break
    
        for j in range(i+1, columlength):
            if y[j]:
                break
                    
        for k in range(j+1, columlength):
            if y[k]:
                break
                            
        for l in range(k+1, columlength):
            if y[l]:
                if k-j > 1:
                    for target in range(j+1, k):
                        y[target] = cubicinterpolate(y[j], y[k], (y[k] - y[i])*(k-j) / (k-i), (y[e] - y[i])*(l-k) / (l-j), float(targer-j) / (k-j))
                i = j
                j = k
                k = l
                l =l+1



