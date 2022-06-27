import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    port = 3300, #local port
    user="root",
    password= <some password>,
    host="127.0.0.1",
    db="MBTAdb",
    use_pure = True
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = """insert into `mbta_buses` (
        id, latitude, longitude, current_status, current_stop_sequence, occupancy_status, speed, updated_at, direction_id, label)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""
        
        

    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (
            mbtaDict['id'], mbtaDict['latitude'], mbtaDict['longitude'], 
            mbtaDict['current_status'], mbtaDict['current_stop_sequence'], mbtaDict['occupancy_status'], 
            mbtaDict['speed'], mbtaDict['updated_at'], mbtaDict['direction_id'], mbtaDict['label']
            )
        mycursor.execute(sql, val)
        #mycursor.execute(sql_1, mbtaDict['bus_label'])

    mydb.commit()