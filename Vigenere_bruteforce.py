from array import array

def encrypt(txt, key):
    txt = txt.upper()
    key = key.upper()
    txt_arr = array('B', txt.encode('utf-8'))
    key_arr = array('B', key.encode('utf-8'))
    j = 0
    for i in range(len(txt_arr)):
        if txt_arr[i] == 32 or txt_arr[i] < 65 or txt_arr[i] > 90:
            j += 1
            continue
        txt_arr[i] = (txt_arr[i] + key_arr[(i - j) % len(key_arr)]) % 26 + 65
    return txt_arr.tobytes().decode('utf-8')


def decrypt(txt, key):
    txt = txt.upper()
    key = key.upper()
    txt_arr = array('B', txt.encode('utf-8'))
    key_arr = array('B', key.encode('utf-8'))
    j = 0
    for i in range(len(txt_arr)):
        if txt_arr[i] == 32 or txt_arr[i] < 65 or txt_arr[i] > 90:
            j += 1
            continue
        txt_arr[i] = (txt_arr[i] - key_arr[(i - j) % len(key_arr)]) % 26 + 65

    return txt_arr.tobytes().decode('utf-8')

def change_name(infile, n):
    inf = open(infile, 'r')
    outf = open(infile + str(n) + '.txt', 'w')
    for line in inf:
        outf.write(line)
    inf.close()


def write(txt, filename, outfile='out.txt'):
    # key 1 letter
    inf = open(filename, 'w')
    for i in range(26):
        inf.write(decrypt(txt, chr(i + 65)) + " - " + chr(i + 65) + "\n")
    inf.close()
    change_name(filename, 1)
    input('Press enter to continue')

    # key 2 letters
    inf = open(filename, 'w')
    for i in range(26):
        for j in range(26):
            inf.write(decrypt(txt, chr(i + 65) + chr(j + 65)) + " - " + chr(i + 65) + chr(j + 65) + '\n')
    inf.close()
    change_name(filename, 2)
    input('Press enter to continue')

    # key 3 letters
    inf = open(filename, 'w')
    for i in range(26):
        for j in range(26):
            for k in range(26):
                inf.write(decrypt(txt, chr(i + 65) + chr(j + 65) + chr(k + 65)) + " - " + chr(i + 65) + chr(j + 65) + chr(k + 65) + '\n')
    inf.close()
    change_name(filename, 3)
    input('Press enter to continue')

    # key 4 letters
    inf = open(filename, 'w')
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    inf.write(decrypt(txt, chr(i + 65) + chr(j + 65) + chr(k + 65) + chr(l + 65)) + " - " + chr(i + 65) + chr(j + 65) + chr(k + 65) + chr(l + 65) + '\n')
    inf.close()
    change_name(filename, 4)
    input('Press enter to continue')

    # key 5 letters
    inf = open(filename, 'w')
    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    for m in range(26):
                        inf.write(decrypt(txt, chr(i + 65) + chr(j + 65) + chr(k + 65) + chr(l + 65) + chr(m + 65)) + " - " + chr(i + 65) + chr(j + 65) + chr(k + 65) + chr(l + 65) + chr(m + 65) + '\n')
    inf.close()
    change_name(filename, 5)




def main():
    txt = input('Enter text: ')
    filename = input('Enter filename: ')
    write(txt, filename)
    print('Done')

if __name__ == '__main__':
    main()
