import requests

class LUAC_API:
    def __init__(self):
        self.url_raw = 'luac.mtasa.com'
        self.url = f'https://{self.url_raw}'
        self.url_file = f'{self.url}/index.php'

        self.newLine = '\r\n'
        self.boundary = '------WebKitFormBoundary'
        self.boundaryLine = f'{self.boundary}{self.newLine}'

        self.headers = {
            'Host': self.url_raw,
            'Origin': self.url,
            'Referer': self.url_file,
            'Content-Type': f'multipart/form-data; boundary={self.boundary[2:]}',        
        }

        self.debug = 1
        self.docompile = 1

    async def ObfuscateLUAC(self, fileName, fileContent, obfuscateLevel):
        payload = [
            [
                f'Content-Disposition: form-data; name="luasource"; filename="{fileName}"'.encode('utf-8'),
                b'Content-Type: application/octet-stream',
                f'{self.newLine}{fileContent}'.encode('utf-8')
            ],
            [
                b'Content-Disposition: form-data; name="compile"',
                f'{self.newLine}{self.docompile}'.encode('utf-8')
            ],
            [
                b'Content-Disposition: form-data; name="obfuscate"',
                f'{self.newLine}{obfuscateLevel}'.encode('utf-8')
            ],
            [
                b'Content-Disposition: form-data; name="debug"',
                f'{self.newLine}{self.debug}'.encode('utf-8')
            ],
            [
                b'Content-Disposition: form-data; name="Submit"',
                f'{self.newLine}Submit'.encode('utf-8')
            ]
        ]

        data = self.boundaryLine
        for c in payload:
            for cc in c:
                data += cc.decode('utf-8') + '\r\n'
            data += self.boundaryLine
    
        return requests.post(self.url_file, headers=self.headers, data=data)
    