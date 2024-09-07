# A program that has a custom class "FCPDCrime" that extends the list class
# Purpose - read the CSV file and processing it in various ways
# Author - Nuhamin Teshome


class FCPDCrime(list):
    def __init__(self, name='Fairfax County Police Crime Report'):
        self.name = name
        super().__init__()


    def load(self, file = 'CrimeReports.csv'):
        with open(file, 'r') as f:
            lines = f.readlines()
            for l in lines:
                line = l.split(',')
                for i in range(len(line)):
                    line[i] = line[i].strip()
                self.append(line)
            return len(lines)


    def printCrimes(self, searchKey='all', zip='all', locale='all'):
        print('IT 209 - Assignment #7: ')
        print('FCPD Police crime calls for the week 4/1/2024 through 4/7/2024')
        print('')
        for i in self:
            if (searchKey == 'all' or searchKey == i[2]) and (zip == 'all' or zip == i[8]) and (locale == 'all' or locale == i[6]):
                print("{:<8} {:<35} {:<45} {:<12} {:<8} {:<30} {:<8} {:<15}".format(*i))

    def zipCodeList(self, zip='22030'):
        for j in self:
            if zip == j[8]:
                print(j)

    def countByZip(self):
        print('Count of number of reports by Zip Code, sorted by frequency')
        print('FCPD Police crime calls for the week 4/1/2024 through 4/7/2024')
        print('')
        zipCount = {}
        for l in self:
            z = l[8]
            if z != '':
                if z in zipCount:
                    zipCount[z] += 1
                else:
                    zipCount[z] = 1
        sortedZip = sorted(zipCount.items(), key=lambda x: x[1], reverse=True)
        for key, value in sortedZip:
            percentage = str(round(value/len(self)*100,2)) + '%'
            print("{:<10} {:<10} {:<10}".format(key, value, percentage))

    def countByCrime(self, select ='all'):
        print('List of crimes by code, sorted by frequency, for all zip codes')
        print('FCPD Police crime calls for the week 4/1/2024 through 4/7/2024')
        print('')
        crimeCount = {}
        for i in self:
            zipcode = i[8]
            type = i[1]
            descr = i[2]
            if select == 'all' or select == zipcode:
                if type not in crimeCount:
                    crimeCount[type] = 0
                else:
                    crimeCount[type] += 1
        sortedCrime = sorted(crimeCount.items(), key=lambda x: x[1], reverse=True)
        for key, value in sortedCrime:
            percentage = str(round(value / len(self) * 100, 2)) + '%'
            print("{:<15} {:<10} {:<10}".format(key, value, percentage))



FC = FCPDCrime('IT209 A7 - FCPD Crime Reporting Analytics Class')
FC.load('CrimeReports.csv')
FC.printCrimes()
ZL = FC.zipCodeList(zip='22030')
FC.countByZip()
FC.countByCrime(select = 'all')



