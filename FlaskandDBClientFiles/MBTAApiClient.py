import urllib.request, json
import mysqldb
import sys
def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    try:
        with urllib.request.urlopen(mbtaUrl) as url:
            data = json.loads(url.read().decode()) # Convert bytes to a str
            for bus in data['data']:
                busDict = dict()
                # complete the fields below based on the entries of your SQL table
                busDict['id'] = bus['id']
                busDict['latitude'] = bus['attributes']['latitude']
                busDict['longitude'] = bus['attributes']['longitude']
                busDict['label'] = bus['attributes']['label']
                busDict['current_status'] = bus['attributes']['current_status']
                busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
                busDict['occupancy_status'] = bus['attributes']['occupancy_status']
                busDict['speed'] = bus['attributes']['speed']
                busDict['updated_at'] = bus['attributes']['updated_at']
                busDict['direction_id'] = bus['attributes']['direction_id'] 
                mbtaDictList.append(busDict)
        mysqldb.insertMBTARecord(mbtaDictList) 
    except:
        print(sys.exc_info())
    return mbtaDictList  

#print(callMBTAApi())