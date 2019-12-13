def maxDepth(root: 'Node') -> int:
        if not root:
            return 0
        queue=[root]
        queue2=[]
        depth=0
        while len(queue):
            depth+=1
            for node in queue:
                for child in node.children:
                    queue2.append(child)
            queue=queue2
            queue2=[]
        return depth