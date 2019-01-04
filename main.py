# coding=utf-8
# !/usr/bin/python

# import mysql.connector
import playlist


# Create sample playlist tree
def main():
    try:

        # setting up MySQL database connection
        # conn = mysql.connector.connect(host='172.23.200.136', port='3306', user='dw_owner', password='1qaz@WSX',
        #                               database='playlist_recommend',  use_unicode=True)
        # cursor = conn.cursor()

        ary_playlist_tree = playlist.PlaylistTree()
        new_playlist_table = [["C", "A", "B"]
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

        # root node of ary_playlist_tree.playlist - not use for database table
        ary_playlist_tree.add_playlist_node(playlist.PlaylistNode(0, 0, "/", 0, 0))
        for NewPlaylist in new_playlist_table:
            gv_node_id = 0
            gv_level_id = 0
            gv_parent_node_id = 0
            while gv_level_id < len(NewPlaylist):

                gv_node_name = NewPlaylist[gv_level_id]
                gv_level_id += 1
                cur_node = ary_playlist_tree.get_node_by_level_name(gv_parent_node_id, gv_level_id, gv_node_name)
                if len(cur_node) > 0:
                    update_result = ary_playlist_tree.update_node_by_id(cur_node[0].node_id, cur_node[0].view_count + 1)
                    gv_parent_node_id = cur_node[0].node_id
                else:
                    gv_node_id = max(node.node_id for node in ary_playlist_tree.playlist) + 1
                    ary_playlist_tree.add_playlist_node(playlist.PlaylistNode(gv_node_id, gv_level_id, gv_node_name, 1, gv_parent_node_id))
                    gv_parent_node_id = gv_node_id

        # print("%s\t%s\t%s\t%s\t%s" % ("node_id", "level_id", "parent_node_id", "node_name", "view_count"))
        # for member in ary_playlist_tree.playlist:
        #     print("%2d\t%2d\t%2d\t%s\t%3d" % (
        #     member.node_id, member.level_id, member.parent_node_id, member.node_name, member.view_count))

        # Input playlist to test the recommendation output

        test_playlist = ["C", "D"]

        gv_parent_node_id = 0
        gv_level_id = 1
        for TestNode in test_playlist:
            parent_node = ary_playlist_tree.get_node_by_level_name(gv_parent_node_id, gv_level_id, TestNode)
            gv_parent_node_id = parent_node[0].node_id
            gv_level_id += 1

        print("\nRecommendation list:")
        print("%s\t%s\t%s\t%s\t%s" % ("node_id", "level_id", "parent_node_id", "node_name", "view_count"))
        for member in ary_playlist_tree.get_children_nodes_by_id(gv_parent_node_id):
            print("%2d\t%2d\t%2d\t%s\t%3d" % (
                member.node_id, member.level_id, member.parent_node_id, member.node_name, member.view_count))

    except Exception as e:
        print(e.message, e.args)

    finally:
        # closing MySQL database connection
        # cursor.close
        # conn.close
        print("\n")
        print("Connection closed in finally\n")
        print("program main.py ends.\n")


if __name__ == "__main__":
    main()