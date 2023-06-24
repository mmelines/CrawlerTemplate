from Config.sources import CrawlSources as config
from Config.sources import DatabaseConfig as dbConfig
from urllib.parse import urlparse as parse
import psycopg2

class CrawlConfig(config):

    def __init__(self):
        super().__init__()
        url_tuple = parse(CrawlConfig.url)
        self.scheme = url_tuple.scheme
        self.netloc = url_tuple.netloc
        self.top = url_tuple.netloc[url_tuple.netloc.find(".") + 1:]
        self.path = url_tuple.path
        self.params = url_tuple.params
        self.query = url_tuple.query

class Database(dbConfig):
	
    def __init__(self):
        """ parent class inherited attributes:
          @ self.dbname
          @ self.user
          @ self.password
          @ self.host
          @ self.port
        """
        super().__init__()
        self.uri = "postgres://{0}:{1}@{2}:{3}/{4}".format(self.user, self.password, self.host, self.dbname, self.port)
        self.cursor = None

    def __repr__(self):
        msg = "Database() configuration: \n"
        msg += "    dbconfig: {dbname} \n".format(dbname = self.dbname)
        msg += "    user: {user} \n".format(user = self.user)
        msg += "    password: {password} \n".format(password=self.password)
        msg += "    host: {host} \n".format(host=self.host)
        msg += "    port: {port} \n".format(port=self.port)
        msg += "    uri: {uri} \n".format(uri=str(self.uri))
        print(msg)
        return msg

    def openConnection(self):
        conn = psycopg2.connect()
        self.cursor = conn.cursor()
        print("opened cursor: " + str(self.cursor))
        return True
        try:
            conn = psycopg2.connect()
            self.cursor = conn.cursor()
            print("opened cursor: " + str(self.cursor))
            return True
        except:
            print("Cursor could not be opened")
        finally:
            return False

    def closeConnection(self):
        result = False
        if self.cursor == None:
            print("self.cursor is none")
        try:
            self.cursor.close()
            self.cursor = None
            result = True
            print("Cursor was closed")
        except AttributeError as e:
            print("Cursor could not be closed " + str(e))
        finally:
            return result
            

if __name__ == '__main__':
    db = Database()
    db.openConnection()
    db.closeConnection()
