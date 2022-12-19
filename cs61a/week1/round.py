def round(n,digits=0):
    if digits==0:
        return int(n);
    else:
        return round(n*10**digits)/10**digits

# if not in the repeating(recursive) way
def round2(n,digits=0):
    if digits==0:
        return int(n);
    else:
        return (int(n*10**digits))/10**digits

if __name__ == '__main__':
    ans1=round(1.23)
    print(ans1)
    print(round(1.23,1))
    print(round(1.23,0))
    print(round(1.23,5))
    print("round2")
    print(round2(1.23,1))
    print(round2(1.23,0))
    print(round2(1.23,5))
 