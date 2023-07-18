from OpenSSL import crypto
import os

def getPk() -> str:
    path = '/home/wintermut3/Área de trabalho/ServerDjango/serverDjango/'
    file_path = os.path.join(path, '/home/wintermut3/Área de trabalho/ServerDjango/serverDjango/', 'cert.pem')
    f = open(file_path, "r")
    cert = f.read()
    pub_key_obj = crypto.load_certificate(crypto.FILETYPE_PEM, cert).get_pubkey()
    pub_key = crypto.dump_publickey(crypto.FILETYPE_PEM, pub_key_obj)

    pk = str(pub_key, 'UTF-8')
    pk = pk[27:425]

    return pk

#getPk()


def getPrivKey() -> str:
    path = '/home/wintermut3/Área de trabalho/ServerDjango/serverDjango/'
    file_path = os.path.join(path, '/home/wintermut3/Área de trabalho/ServerDjango/serverDjango/', 'key.pem')

    with open(file_path, "r") as my_cert_file:
        myKeyPem = my_cert_file.read()
        keyLoader = crypto.load_privatekey(crypto.FILETYPE_PEM, myKeyPem)
        privKey = crypto.dump_privatekey(crypto.FILETYPE_PEM, keyLoader)

        privKey = str(privKey, 'UTF-8')

        privKey_sliced = privKey[28:1677]

        return privKey_sliced

if __name__ == '__main__':
    getPrivKey()
