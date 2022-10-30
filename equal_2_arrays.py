#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        freq = {}
        for i in A:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
        for i in B:
            if i not in freq.keys():
                return False
            elif freq[i] == 0:
                return False
            else:
                freq[i] -= 1
        
        return True



if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
