from fastapi import status


class SwaggerBase():
    def __init__(self, response_model, success_status_code: int=status.HTTP_200_OK, success_description: str = None, fail_status_code: int = status.HTTP_400_BAD_REQUEST, fail_description: str = None):
        self.response_model = response_model
        self.success_status_code = success_status_code
        self.success_description = success_description
        self.fail_status_code = fail_status_code
    

    def reponse(self):
        status_code__details = {
            self.success_status_code: {
                'model': self.response_model
            },
            self.fail_status_code: {
                'model': None
            }
        }
        if self.success_description:
            status_code__details[self.success_status_code]['description'] = self.success_description

        if self.fail_description:
            status_code__details[self.fail_status_code]['description'] = self.fail_description

        return status_code__details
