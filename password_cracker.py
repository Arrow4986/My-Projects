import hashlib

def crack_sha1_hash(hash, use_salts = False):
    pass_arr = []
    readfile("top-10000-passwords.txt", pass_arr)

    if use_salts:
        pass_salt_arr = []
        readfile("known-salts.txt", pass_salt_arr)
      
        for ps in pass_salt_arr:
            for pw in pass_arr:
                appended = hashlib.sha1((pw + ps).encode('utf-8')).hexdigest()
                prepended = hashlib.sha1((ps + pw).encode('utf-8')).hexdigest()
                if appended == hash or prepended == hash:
                    return pw

    for pw in pass_arr:
        hash_pw = hashlib.sha1(pw.encode('utf-8')).hexdigest()
        if hash_pw == hash:
            return pw
    
    return "PASSWORD NOT IN DATABASE"

def readfile(filename, array):
    with open(filename, "r") as f:
      line = f.readline().strip()
      while line:
          array.append(line)
          line = f.readline().strip()