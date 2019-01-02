class PlaylistNode:
    def __init__(self, pv_node_id, pv_level_id, pv_node_name, pv_view_count, pv_parent_node_id):
        self.node_id = pv_node_id
        self.level_id = pv_level_id
        self.parent_node_id = pv_parent_node_id
        self.node_name = pv_node_name
        self.view_count = pv_view_count

    def __getitem__(self, pv_node_id):
        return self.node_name

    def update_view_count(self, pv_view_count):
        self.view_count = pv_view_count


class PlaylistTree:
    def __init__(self):
        self.playlist = []

    def __iter__(self):
        return self.playlist

    def get_node_by_level_name(self, pv_parent_node_id, pv_level_id, pv_node_name):
        result = [x for x in self.playlist if
                  x.level_id == pv_level_id and x.node_name == pv_node_name and x.parent_node_id == pv_parent_node_id]
        return result

    def get_node_by_id(self, pv_node_id):
        result = [x for x in self.playlist if x.node_id == pv_node_id]
        return result

    def get_children_nodes_by_id(self, pv_node_id):
        result = [x for x in self.playlist if x.parent_node_id == pv_node_id]
        result.sort(key=lambda x: x.view_count, reverse=True)
        return result

    def add_playlist_node(self, pv_playlist_node):
        self.playlist.append(pv_playlist_node)

    def update_node_by_id(self, pv_node_id, pv_view_count):
        result = 0
        for node in self.playlist:
            if node.node_id == pv_node_id:
                node.update_view_count(pv_view_count)
                result = 1
        return result
