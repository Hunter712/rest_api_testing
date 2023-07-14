import requests


class HTTPClient:
    ENDPOINT = 'https://gorest.co.in/public/v2/users/'

    HEADER = {"Accept": "application/json",
              "Content-Type": "application/json",
              "Authorization": "Bearer d06a40bd96cc7d11bacb7df9ad3d746cb69304e4d2207db6d48f9dc3df1e3144"}

    USER_DATA = {"name": "Vlad F", "gender": "male", "email": "vladf@gmail.com", "status": "active"}
    POST_DATA = {'title': '123', 'body': '456'}
    PARAMS = {}
    ID = "id"

    def create_user(self):
        response = requests.post(url=self.ENDPOINT, headers=self.HEADER, json=self.USER_DATA)
        # print(response.status_code)
        # print(response.headers)
        # print(response.json())
        self.PARAMS[self.ID] = str(response.json()[self.ID])
        return response.status_code

    def create_post(self):
        url = self.ENDPOINT + self.PARAMS[self.ID] + "/posts"
        response = requests.post(url=url, headers=self.HEADER, json=self.POST_DATA)
        # print(response.status_code)
        # print(response.headers)
        # print(response.json())
        return response.status_code

    def get_user_posts(self):
        url = self.ENDPOINT + self.PARAMS[self.ID] + "/posts"
        response = requests.get(url=url, headers=self.HEADER)
        # print(response.status_code)
        # print(response.json())
        return response.status_code

    def get_user(self):
        response = requests.get(url=self.ENDPOINT, headers=self.HEADER, params=self.PARAMS)
        # print(response.status_code)
        # print(response.json())
        return response.status_code

    def delete_user(self):
        url = self.ENDPOINT + self.PARAMS[self.ID]
        response = requests.delete(url=url, headers=self.HEADER)
        # print(response.status_code)
        # print(response.headers)
        return response.status_code
