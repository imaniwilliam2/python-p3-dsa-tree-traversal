from collections import deque

class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id, depth_first=True):
        if self.root is None:
            return None

        if depth_first:
            return self._depth_first_search(self.root, target_id)
        else:
            return self._breadth_first_search(target_id)

    def _depth_first_search(self, node, target_id):
        if node['id'] == target_id:
            return node

        for child in node['children']:
            result = self._depth_first_search(child, target_id)
            if result:
                return result

        return None

    # def _breadth_first_search(self, target_id):
    #     queue = deque([self.root])

    #     while queue:
    #         node = queue.popleft()
    #         if node['id'] == target_id:
    #             return node

    #         for child in node['children']:
    #             queue.append(child)

    #     return None

