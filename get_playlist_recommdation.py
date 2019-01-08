# coding=utf-8
# !/usr/bin/python

import mysql.connector
import os

# Create sample playlist tree
def main():
    try:

        # setting up MySQL database connection
        conn = mysql.connector.connect(host='172.21.101.136', port='3306', user='dw_owner', password='1qaz@WSX',
                                       database='playlist_recommend',  use_unicode=True)
        cur = conn.cursor()

        # Input playlist to test the recommendation output

        test_playlist = ["C", "D"]

        gv_parent_node_id = 1
        gv_level_id = 1
        for TestNode in test_playlist:
            sql1 = "SELECT node_id FROM playlist_tree_test WHERE level_id = " + str(gv_level_id) + " AND parent_node_id = " \
                  + str(gv_parent_node_id) + " AND node_name = \'" + TestNode + "\' ORDER BY node_name DESC LIMIT 1"
            # print(sql1)
            cur.execute(sql1)
            result1 = cur.fetchone()  # get the recordset
            if result1:
                gv_parent_node_id = result1[0]
            else:
                gv_parent_node_id = -1
                break

            gv_level_id += 1

        print("\nRecommendation list: ")
        if gv_parent_node_id > 0:
            sql2 = "SELECT node_name FROM playlist_tree_test WHERE parent_node_id = " + str(gv_parent_node_id) + " ORDER BY view_count DESC"
            # print(sql2)
            cur.execute(sql2)
            result2 = cur.fetchall()  # get the recordset
            for x in result2:
                print(x[0])
        else:
            print("\n No recommendation.")

    except mysql.connector.Error as e:
        print('Error : {}'.format(e))

    finally:
        # closing MySQL database connection
        cur.close
        conn.close
        print("\n")
        # print("Connection closed in finally")
        print("program " + os.path.basename(__file__) + " ends.")


if __name__ == "__main__":
    main()