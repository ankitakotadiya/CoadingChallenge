'''
Given a string path, which is an absolute path (starting with a slash '/') to a file or directory in a Unix-style file system, convert it to the simplified canonical path.
In a Unix-style file system, a period '.' refers to the current directory, a double period '..' refers to the directory up a level, and any multiple consecutive slashes (i.e. '//') are treated as a single slash '/'. For this problem, any other format of periods such as '...' are treated as file/directory names.

The canonical path should have the following format:

The path starts with a single slash '/'.
Any two directories are separated by a single slash '/'.
The path does not end with a trailing '/'.
The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period '.' or double period '..')

Input: path = "/home/"
Output: "/home"
Explanation: Note that there is no trailing slash after the last directory name.
'''

'''
# To simply path will use stack
# Split path by '/' so we have one list.
# Iterate one by one element and append at the top of the stack except '.' and '..' and ''(empty string).
# If we see someting like '..' then we remove topmost element from the stack as we have to jump back to the parent directory.
# If we find multiple /// then will ignore it because they are equivalent single /.
# At the end of iteration join all the elements in the stack by /.
# Return / + simplified path string.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        
        ans = []
        l = path.split("/")
        print(l)
        for i in l:
            if i!= "" and i!= "." and i!="..":
                ans.append(i)
            if i == ".." and len(ans)>0:
                ans.pop()
            
        return '/'+'/'.join(ans)
