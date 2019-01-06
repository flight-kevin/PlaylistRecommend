# coding=utf-8
# !/usr/bin/python

import mysql.connector
import playlist


# Create sample playlist tree
def main():
    try:

        # setting up MySQL database connection
        conn = mysql.connector.connect(host='172.21.101.136', port='3306', user='dw_owner', password='1qaz@WSX',
                                       database='playlist_recommend',  use_unicode=True)
        cursor = conn.cursor()

        # get the id range
        args = (0, 0)
        result_args = cursor.callproc('sp_get_start_end_rawdata_id', args)
        print(result_args[0])
        print(result_args[1])

    except mysql.connector.Error as e:
        print('Error : {}'.format(e))

    finally:
        # closing MySQL database connection
        cursor.close
        conn.close
        print("\n")
        print("Connection closed in finally\n")
        print("program main.py ends.\n")


if __name__ == "__main__":
    main()