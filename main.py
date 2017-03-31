'''This module runs the main JUICE CHALLENGE application'''
import os
import cherrypy
from juice_bi import Helper
from juice_bi import JuiceException
''' main class'''
class App(object):
    def __init__(self):
        self.RESP_CODE = {
            'SUCCESS': 200,
            'FAILURE': 500
        }
    '''method to receive post data and process csv file'''
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def upload(self, datafile):
        reqHeaders = {}
        for key, val in cherrypy.request.headers.iteritems():
            reqHeaders[key.lower()] = val
        fileSize = int(reqHeaders['content-length'])
        fileData = datafile.file.read(fileSize)
        try:
            return Helper.getResponse(self.RESP_CODE.get('SUCCESS'), Helper.processFile(fileData))
        except JuiceException as ex:
            exDetails = dict(ex.args[0])
            return Helper.getResponse(self.RESP_CODE.get('FAILURE'), exDetails.get('message'))
        except Exception as ex:
            return Helper.getResponse(self.RESP_CODE.get('FAILURE'), ex)
        return fileData
cherrypy.tree.mount(App(), '/', {
    '/': {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': os.path.join(os.path.join(os.getcwd(), 'webapp'), 'app'),
        'tools.staticdir.index': 'index.html'
    }
})
cherrypy.engine.start()
cherrypy.engine.block()
