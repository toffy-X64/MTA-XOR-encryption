class ErrorHandler:
    def return_error(self, text):
        return {
            "state": False,
            "data": text
        }

    def return_response(self, data):
        return {
            "state": True,
            "data": data
        }