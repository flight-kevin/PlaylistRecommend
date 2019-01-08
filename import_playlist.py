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

        # # test code if sp_get_playlist needs to be moved to application server
        # get the id range
        # args = (0, 0)   # predefined parameters for the stored procedure
        # result_args = cur.callproc('sp_get_start_end_rawdata_id', args)
        # print(result_args[0])
        # print(result_args[1])
        #
        # # get the playlist
        # min_playsecond = 90
        # sql = "SELECT id, mac, channelNo, createTime, actionData/1000 playsecond FROM litvdb.li_tblclientlog_channel_201810" \
        # " WHERE id BETWEEN " + str(result_args[0]+ 1) + " AND " + str(result_args[1]) + " AND ACTION = 'vod.player.playTime'" \
        # " AND actionData/1000 > " + str(min_playsecond) + " ORDER BY mac, createTime"
        # # print(sql)
        # cur.execute(sql)
        # rs = cur.fetchall()  # get the recordset
        #
        # new_playlist_table = []
        # for x in rs:
        #     print(x)

        # run sp_get_playlist
        # min_playsecond = 90

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