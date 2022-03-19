# md5-hash-password-decrypter Project Description
Operating system: Linux 
Software required: Crypto libraries. You are allowed to use only the primitive hash functions that take a single input. For instance, hashlib.md5(string) in python.   Password cracking utilities are explicitly prohibited (but can be used for verification).  
Language: C/C++ or any other that you prefer. Note that speed may be a consideration.  

### Compiling project:
```
1. git clone https://github.com/brycehills/md5-hash-password-decrypter.git 
2. python cracker.py
```


In this project, you are asked to crack passwords from a "stolen" /etc/shadow file on a Linux system (See the file etc_shadow). You will work as teams of two. Each   teacm will crack the password for team[i] where i is the team number that is assigned by the TA. Each line in the file has the hash type, salt, and the hash of the   password.  
For instance, consider an example first line "team0:$1$hfT7jp2q$/sDfNdP2e3OCxg2zGq1FK0:16653:0:99999:7:::",   
$1$ indicates the hash algorithm to be MD5  
$hfT7jp2q$ indicates the salt to be hfT7jp2q  
$/sDfNdP2e3OCxg2zGq1FK0 indicates the password hash to be /sDfNdP2e3OCxg2zGq1FK0  

For more examples, there is a folder called "sample files (for testing and verification only)" where you can find password hashes along with their original passwords.  

A common password cracking strategy is to bruteforce all possible passwords. This can be time-consuming and sometimes inefficient. Therefore, various "dictionary" of   commonly used passwords from leaked sources have been used to speed up the process. However, in our case, the passwords are intentionally randomized so that the    dictionary approach may not work well. Therefore, you are better off writing your bruteforce-style program to crack the password hashes. Note that there are existing   tools that implement bruteforce password cracking on the Internet. You are NOT allowed to use them. You are, however, allowed to use the primitive hash functions such   as hashlib.md5(string). Check out tutorials on how md5 password hashes are computed (with 1000 rounds of primitive md5 hashes):    https://www.vidarholen.net/contents/blog/?p=32. You may also learn (but not directly COPY) from reference implementations in various open source libraries as follows:  

Shell: https://www.vidarholen.net/contents/junk/files/md5crypt.bash  
Javascript: https://unix4lyfe.org/crypt/crypt.js  
C: https://github.com/openssh/openssh-portable/blob/master/md5crypt.c  

Reference that explains the ins and outs of password hashing: https://crackstation.net/hashing-security.htm  
Online tool that generates the password hash (for verification purposes): https://unix4lyfe.org/crypt/  

 
  # Project Results:

![alt text](https://github.com/brycehills/md5-hash-password-decrypter/blob/main/passwordcracked.png?raw=true)


