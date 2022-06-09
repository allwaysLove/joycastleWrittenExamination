# 日志行 记录类
class RowData:
    ip = None
    time = None
    request_method = None
    query = None
    raw_uri = None
    domain = None
    status = None
    content_length = None
    
    def __init__(self, ip, time, request_method, query, raw_uri, domain, status, content_length):
        self.ip = ip
        self.time = time
        self.request_method = request_method
        self.query = query
        self.raw_uri = raw_uri
        self.domain = domain
        self.status = status
        self.content_length = content_length
    
    def test_state(self):
        return {
            key: getattr(self, key) for key in ['ip', 'time', 'request_method', 'query', 'raw_uri', 'domain', 'status', 'content_length']
        }
    
    def __getstate__(self):
        return {
            key: getattr(self, key) for key in ['ip', 'time', 'request_method', 'query', 'raw_uri', 'domain', 'status', 'content_length']
        }
    
#     def __setstate__(self, state):
#         key_list = ['ip', 'time', 'request_method', 'query', 'raw_uri', 'domain', 'status', 'content_length']
#         for key in key_list:
#             setattr(self, key, state[key])
    
    def __str__(self):
        return '\n'.join([f'{key}: {getattr(self, key)}' for key in ['ip', 'time', 'request_method', 'query', 'raw_uri', 'domain', 'status', 'content_length']])
    
    def __repr__(self):
        return self.__str__()

