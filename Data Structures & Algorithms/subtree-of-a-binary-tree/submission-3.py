class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def serialize(node, path):
            if not node:
                path.append("#")
                return
            
            # Use delimiters to prevent a node value like "2" 
            # from matching part of a node value like "12"
            path.append(f"^{node.val}^")
            serialize(node.left, path)
            serialize(node.right, path)

        root_path = []
        serialize(root, root_path)
        print(root_path)
        root_str = "".join(root_path)

        subRoot_path = []
        serialize(subRoot, subRoot_path)
        subRoot_str = "".join(subRoot_path)

        # Python's 'in' operator uses Boyer-Moore-Horspool under the hood,
        # which is highly optimized and runs in O(N + M) time on average.
        return subRoot_str in root_str