## 1. The SQLite Shell ##


# +--------------------------------+
# |                                |
# |     RUN THE COMMANDS BELOW     |
# |                                |
# +--------------------------------+
#
# /home/dq$ sqlite3 chinook.db
#
#  sqlite3> .tables
#  sqlite3> .headers on
#  sqlite3> .mode column
#  sqlite3> SELECT
#      ...>   track_id,
#      ...>   name,
#      ...>   album_id
#      ...> FROM track
#      ...> WHERE album_id = 3;
#  sqlite3> .help
#  sqlite3> .shell clear
#  sqlite3> .quit