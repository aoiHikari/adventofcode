#!/usr/bin/python

import md5

def find_md5_with_prefix(seed, prefix):
    if len(prefix) < 0 or len(prefix) > 7:
        print "Invalid prefix {0}".format(prefix)
        return

    iterator = 0;
    while True:
        hasher = md5.new()
        hasher.update(seed + str(iterator))
        firstFive = hasher.hexdigest()[0:len(prefix)]
        if firstFive == prefix:
            return iterator
        else:
            iterator += 1

def find_md5_with_five_zeroes(seed):
    solution = find_md5_with_prefix(seed, "00000")
    print "First five zeries found at iteration {0}".format(solution)

def find_md5_with_six_zeroes(seed):
    solution = find_md5_with_prefix(seed, "000000")
    print "First six zeroes prefix found at iteration {0}".format(solution)

def main():
    seed = "ckczppom"
    find_md5_with_five_zeroes(seed)
    find_md5_with_six_zeroes(seed)

if __name__ == "__main__":
    main()
