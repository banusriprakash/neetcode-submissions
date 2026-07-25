class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        ls=[]

        for i in nums1:
            ls.append(i)

        for j in nums2:
            ls.append(j)

        ls.sort()
        print(ls)
        mid=-1

        if len(ls)%2==0:
            rmid=len(ls)//2
            print(mid)
            mid=(len(ls)//2)-1
            print(rmid)
            return ((ls[mid]+ls[rmid])/2)

        mid=len(ls)//2
        return ls[mid]
        