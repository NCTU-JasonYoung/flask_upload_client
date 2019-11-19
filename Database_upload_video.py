#!coding = utf-8
 

import os
import requests  #請先安裝該函式庫 (pip3 install request2)
from db_api import db_api

class upload_video():
    def __init__(self, source_video_path, match_id, db_host, db_port, db_user, db_passwd, db_name):
        self.api = db_api(db_host = db_host, db_port = db_port, db_user = db_user, db_passwd = db_passwd, db_name = db_name)
        self.match_id = match_id
        self.video_load_path = source_video_path

    def upload(self):
        url = 'http://140.113.216.103:8000/' #server的ip和port 請自行調整
        filepath = self.video_load_path
        filename = os.path.basename(filepath).encode('utf-8')
        files = {'file': open(filepath, 'rb')}
        r = requests.post(url, files=files)
        r.text

        # Upload name to database 5
        filename = filename.strip(b'\00')
        filename = filename.decode()
        self.api.upload_video_name(self.match_id, filename)
        
    