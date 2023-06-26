for x in '0123456789A':
    s1 = '3364' + x
    s2 = x + '7946'
    s3 = '55' + x + '87'
 
    left = int(s1, 11) + int(s2, 12)
    right = int(s3, 14)
    if left == right:
        print(right)
