import sys
import re

def extract_names(filename):
    names = []
    f = open(filename,'r')
    text = f.read()
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>',text)
    # print (tuples)

    for tup in tuples:
        print(tup[0],tup[1],tup[2])


if __name__ == '__main__':
    args = sys.argv[1:]    
    if not args:
        print('file 명을 parameter 로 입력 바랍니다.')
        sys.exit(1)
    filename = './babynames/' + args[0]
    extract_names(filename)