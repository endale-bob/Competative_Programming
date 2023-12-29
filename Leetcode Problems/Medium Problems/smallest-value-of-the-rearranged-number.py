class Solution:
    def smallestNumber(self, num: int) -> int:
        if(num == 0): return 0
        n = num
        num = [n for n in str(abs(num))]

        def myComparator(x, y):
            if ( x+y > y+x ):
                return 1
            else:
                return -1

        num.sort(key = cmp_to_key(myComparator), reverse = n < 0)

        ind = 0
        while(num[ind] == "0"):
            ind += 1
        
        num[ind], num[0] = num[0], num[ind]

        return int(int("".join(num)) * (n/abs(n)))