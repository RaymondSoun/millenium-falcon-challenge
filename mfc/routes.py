from pathlib import Path
import sqlite3
from collections import defaultdict

class Routes:
    def __init__(self, database_file: Path) -> None:
        con = sqlite3.connect(database_file)
        cursor = con.cursor()

        cursor.execute("select * from routes;")
        rows = cursor.fetchall()

        self.routes = defaultdict(dict)
        for row in rows:
            self.routes[row[0]][row[1]] = row[2]
        

    def get_travel_time(self, origin: str, arrival: str) -> int:
        if origin not in self.routes:
            raise Exception(f"Unknown origin planet: {origin}")
        
        reachable_routes = self.routes[origin]
        if arrival not in reachable_routes:
            raise Exception(f"Unknown destination planet: {arrival}")

        return self.routes[origin][arrival]