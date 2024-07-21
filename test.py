import __main__
from collections import defaultdict, deque
import collections
import heapq
import itertools
from typing import List, Optional
import unittest
import random
# import pytest

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert_word(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def search_word(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end_of_word
    
    def append_words(self,words, search):
        for word in words:
            self.insert_word(word)

        # return self.search_word(search)
    
    def generate_random_words(self,num_words):
        result = []
        
        def dfs(node: TrieNode, path: str):

            if node.end_of_word:
                result.append(path)
                return
            
            if len(result) >= num_words:
                return
            if node.children:
                chars = list(node.children.keys())
                random.shuffle(chars)

            for chr in chars:
                dfs(node.children[chr],path+chr)
        dfs(self.root,'')
        return result
    
    def generate_random_words_choice(self,num_words):
        result = []
        def dfs(node:TrieNode, path:str):
            if node.end_of_word:
                result.append(path)
                return
            
            if len(result) >= num_words:
                return
            
            if node.children:
                chars = list(node.children.keys())
                while chars:
                    chr = random.choice(chars)
                    dfs(node.children[chr],path+chr)
                    chars.remove(chr)
        dfs(self.root,'')
        return result

    def generate_random_words_set(self,words,num_words):
        result = set()
        while len(result) < num_words:
            rand = random.randint(0,len(words)-1)
            ele = words[rand]
            if ele not in result:
                result.add(ele)
        return result
    
    def reverse_in_place_arr(self,nums):
        l = 0
        r = len(nums)-1

        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
        return nums
        
class Permutations:
    def __init__(self):
        self.root = TrieNode()

    def generate_permutations(self,string):
        result = []

        def permutations(word,path):
            if len(path) == len(string):
                result.append(path)
                return
            for i in range(len(word)):
                permutations(word[:i]+word[i+1:],path+word[i])

        permutations(string,'')
        return result

    def insert_words(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True
    
    def append_words(self,words):
        for word in words:
            self.insert_words(word)

    def generate_combinations(self,input):
        result = []

        def combinations(node: TrieNode, path: str, chars: str):
            if node.end_of_word:
                result.append(path)
                return
            
            for i,chr in enumerate(chars):
                if chr in node.children:
                    combinations(node.children[chr],path+chr,chars[:i]+chars[i+1:])

        combinations(self.root, '', input)
        return result
    
obj = Permutations()
# obj.append_words(['plea','leap','apple','pela'])
# print(obj.generate_combinations('plea'))    
trie = Trie()
# print(trie.generate_random_words_set(num_words=2,words=['apple','data','trie','fine']))
# print(trie.append_words(words=['apple','data','trie','fine'], search='trie'))
# print(trie.generate_random_words_choice(num_words=2))
print(trie.reverse_in_place_arr(nums=[1,2,3,4,5,6]))

class TreeNode:
     def __init__(self,val=0,left=None,right=None):
          self.val = val
          self.left = left
          self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DSA:
    
    def partition_list(self,head,x):
        if not head:
            return
        before_head = ListNode()
        after_head = ListNode()
        before = before_head
        after = after_head

        cur = head
        while cur:
            if cur.val < x:
                before.next = cur
                before = before.next
            else:
                after.next = cur
                after = after.next

            cur = cur.next

        after.next = None
        before.next = after_head.next
        return before_head.next


class testcAse(unittest.TestCase):
    def test_partition(self):
        linked_list = ListNode(2)
        linked_list.next = ListNode(2)
        linked_list.next.next = ListNode(3)
        linked_list.next.next.next = ListNode(1)
        linked_list.next.next.next.next = ListNode(4)

        linked_list_test = ListNode(2)
        linked_list_test.next = ListNode(2)
        linked_list_test.next.next = ListNode(1)
        linked_list_test.next.next.next = ListNode(3)
        linked_list_test.next.next.next.next = ListNode(4)
        # linked_list_test.next.next.next.next.next = None

        jump = DSA()
        result = jump.partition_list(head=linked_list, x=3)
        self.assertTrue(result,linked_list_test)
        # self.assertTrue(jump.partition_list(head=linked_list, x=3),linked_list_test)

    def test_generate_random_words(self):
        trie = Trie()
        trie.append_words(['apple','data','fine','fix'],search='apple')
        output = ['apple','data']
        self.assertEqual(trie.generate_random_words_choice(num_words=2),output)
    # def test_partition_fail(self):
    #     jump = DSA()
    #     self.assertEqual(jump.jump_game(nums=[1,3,1,1,4]),2)


# if __name__ == '__main__':
#     unittest.main()

def partition_list(head,x):
    if not head:
        return
    before_head = ListNode()
    after_head = ListNode()
    before = before_head
    after = after_head

    cur = head
    while cur:
        if cur.val < x:
            before.next = cur
            before = before.next
        else:
            after.next = cur
            after = after.next

        cur = cur.next

    after.next = None
    before.next = after_head.next

    result = []
    main_node = before_head.next
    while main_node:
        result.append(main_node.val)
        main_node = main_node.next
    return result

linked_list = ListNode(2)
linked_list.next = ListNode(2)
linked_list.next.next = ListNode(3)
linked_list.next.next.next = ListNode(1)
linked_list.next.next.next.next = ListNode(4)

print(partition_list(head=linked_list,x=3))

def jump_game(nums):
    if len(nums) == 0:
        return 0

    current_end = 0
    last_ele = 0
    jump = 0

    for i in range(len(nums)-1):
        last_ele = max(last_ele, i+nums[i])

        if  i == current_end:
            jump+=1
            current_end = last_ele

            if current_end >= len(nums)-1:
                break
    return jump

# print(jump_game(nums=[1,3,1,1,4]))

def interchange_number(nums):
    if len(nums) == 1:
        return nums
    
    for i,num in enumerate(nums):
        if i > 0 and i % 2 != 0:
            nums[i-1],nums[i] = nums[i],nums[i-1]
    return nums

def two_sum(root,target):
    result = []

    def path_sum(root,summ,path=[]):
        if not root:
            return
        summ = summ + root.val
        path.append(root.val)

        if not root.left and not root.right:
            if target == summ:
                result.append(path.copy())
                path.pop()
                return
            
        path_sum(root.left,summ,path)
        path_sum(root.right,summ,path)
        path.pop()

    path_sum(root,0)
    return result

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

# print(two_sum(root,target=22))

def first_non_repeat(s):
    dic = {}
    for c in s:
        if c not in dic:
            dic[c] = 1
        else:
            dic[c] += 1

    count = 0
    for k,v in dic.items():
        if v == 1 and count == 1:
            return k
        elif v == 1:
            count += 1

print(first_non_repeat('khichdi'))    

def simplify_the_path(s):
    components = s.split('/')
    print(components)
    stack = []

    for com in components:
        if com == '' or com == '.':
            continue
        elif com == '..':
            if stack:
                stack.pop()
        else:
            stack.append(com)

    path = '/' + '/'.join(stack)
    return path

# print(simplify_the_path('/home//data/../file/'))

# def combinations(n,k):
#     result = []
#     def permutations(start,path):

#         if len(path) == k:
#             result.append(path)

#         for i in range(start,n+1):
#             permutations(i+1,path+[i])
#     permutations(1,[])
#     return result

# print(combinations(4,2))


# def join_words(words):

#     def permutation(word,result,path):
#         if len(path) == len(words):
#             result.append(''.join(path))
#             return
        
#         for i in range(len(word)):
#             # words[start],words[i] = words[i],words[start]
#             permutation(word[:i]+word[i+1:],result,path+[words[i]])
#             # words[start],words[i] = words[i],words[start]

#     result = []
#     permutation(words,result,[])
#     print(result)
#     return result


# join_words(words=['ab','cd','ef'])



def binary_search(nums,target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l+r)//2

        if nums[mid] == target:
            return mid
        
        if nums[l] <= nums[mid]: #Left part is sorted   [4,5,6,0,1,2,3]
            if nums[l] <= target < nums[mid]: # Mid is greater than target
                r = mid-1
            else:
                l = mid+1
        else:
            if nums[mid] < target <= nums[r]: # Target element is less than and right part is sorted
                l = mid+1
            else:
                r = mid-1

    return -1

# print(binary_search(nums=[4,5,6,0,1,2,3], target=2))


