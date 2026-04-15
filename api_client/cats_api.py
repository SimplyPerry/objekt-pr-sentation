import httpx


class CatsClient:
    def __init__(
            self,
            base_url:str
        ):
        self.base_url = base_url
    

    def get_one_fact(self):
        endpoint = "/facts"
        url = f"{self.base_url.rstrip('/')}{endpoint}"

        response = httpx.get(url)
        response.raise_for_status()
        return response.json()

        