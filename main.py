import playlist


# Create sample playlist tree
def main():
    try:
        ary_PlaylistTree = playlist.PlaylistTree()
        NewPlaylistTable = [["C", "A", "B"]
            , ["C", "D", "A"]
            , ["C", "D", "E"]
            , ["C", "D", "F"]
            , ["D", "B"]
            , ["G", "A", "E"]
            , ["G", "F", "B"]
            , ["G", "F", "D"]
            , ["C", "D", "A"]
            , ["D", "B"]
            , ["G", "F"]
            , ["C", "A", "B"]
            , ["G", "F", "B"]
            , ["C", "D", "A"]]

        ary_PlaylistTree.add_playlist_node(playlist.PlaylistNode(0, 0, "/", 0, 0))  # root node of ary_PlaylistTree.playlist
        for NewPlaylist in NewPlaylistTable:
            gv_node_id = 0
            gv_level_id = 0
            gv_parent_node_id = 0
            while gv_level_id < len(NewPlaylist):

                gv_node_name = NewPlaylist[gv_level_id]
                gv_level_id += 1
                cur_node = ary_PlaylistTree.get_node_by_level_name(gv_parent_node_id, gv_level_id, gv_node_name)
                if len(cur_node) > 0:
                    updateResult = ary_PlaylistTree.update_node_by_id(cur_node[0].node_id, cur_node[0].view_count + 1)
                    gv_parent_node_id = cur_node[0].node_id
                else:
                    gv_node_id = max(node.node_id for node in ary_PlaylistTree.playlist) + 1
                    ary_PlaylistTree.add_playlist_node(playlist.PlaylistNode(gv_node_id, gv_level_id, gv_node_name, 1, gv_parent_node_id))
                    gv_parent_node_id = gv_node_id

        # print("%s\t%s\t%s\t%s\t%s" % ("node_id", "level_id", "parent_node_id", "node_name", "view_count"))
        # for member in ary_PlaylistTree.playlist:
        #     print("%2d\t%2d\t%2d\t%s\t%3d" % (
        #     member.node_id, member.level_id, member.parent_node_id, member.node_name, member.view_count))

        # Input playlist to test the recommendation output

        TestPlaylist = ["C", "D"]
        gv_parent_node_id = 0
        gv_level_id = 1

        for TestNode in TestPlaylist:
            parent_node = ary_PlaylistTree.get_node_by_level_name(gv_parent_node_id, gv_level_id, TestNode)
            gv_parent_node_id = parent_node[0].node_id
            gv_level_id += 1


        print("\nRecommendation list:")
        print("%s\t%s\t%s\t%s\t%s" % ("node_id", "level_id", "parent_node_id", "node_name", "view_count"))
        for member in ary_PlaylistTree.get_children_nodes_by_id(gv_parent_node_id):
            print("%2d\t%2d\t%2d\t%s\t%3d" % (
                member.node_id, member.level_id, member.parent_node_id, member.node_name, member.view_count))

    except Exception as e:
        print(e.message, e.args)

    finally:
        print('program main.py ends.')


if __name__ == "__main__":
    main()