from array import array

def encrypt(txt, key):
    txt = txt.upper()
    key = key.upper()
    txt_arr = array('B', txt.encode('utf-8'))
    key_arr = array('B', key.encode('utf-8'))
    
    for i in range(len(txt_arr)):
        if txt_arr[i] == 32 or txt_arr[i] < 65 or txt_arr[i] > 90:
            continue
        txt_arr[i] = (txt_arr[i] + key_arr[i % len(key_arr)]) % 26 + 65
    return txt_arr.tobytes().decode('utf-8')

def decrypt(txt, key):
    txt = txt.upper()
    key = key.upper()
    txt_arr = array('B', txt.encode('utf-8'))
    key_arr = array('B', key.encode('utf-8'))

    for i in range(len(txt_arr)):
        if txt_arr[i] == 32 or txt_arr[i] < 65 or txt_arr[i] > 90:
            continue
        txt_arr[i] = (txt_arr[i] - key_arr[i % len(key_arr)]) % 26 + 65

    return txt_arr.tobytes().decode('utf-8')

def main():
    txt = input('Enter text: ')
    key = ''
    while key == '' or key.count(' ') >= 1:
        key = input('Enter key: ')
    key = key.replace('\n', '')
    key = key.replace('\t', '')
    print(encrypt(txt, key))
    print(decrypt(encrypt(txt, key), key))

if __name__ == '__main__':
    main()