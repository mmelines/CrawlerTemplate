from sources import CrawlSources as config
from sources import DatabaseConfig as dbConfig
from urllib.parse import urlparse as parse

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
        self.uri = "postgres://{0}:{1}@{2}:{3}/{4}".format("user", "pwd", "host", "port", "dbname")

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

if __name__ == '__main__':
    Database().__repr__()