def NumberOfSmaller(n: int, m: int, a: list, b: list):
    p1 = 0
    p2 = 0
    
    while(p2<m and p1 < n):
        while(p1+1 < n and a[p1 +1 ] < b[p2]):
            p1 += 1
        if(a[p1] < b[p2]): print(p1 + 1)
        else: print(0)
        p2 += 1
    
    while(p2 < m):
        print(p1 + 1)
        p2 += 1
        
        

if __name__ == "__main__":
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    NumberOfSmaller(n, m, a, b)
    
    
