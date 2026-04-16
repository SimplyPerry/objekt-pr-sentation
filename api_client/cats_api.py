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
    
    def get_multiple_facts(self, amount_of_facts:int):
        """
        Henter antal fakta omkring hunde, defineret i amounts_of_facts
        """

        endpoint = f"/facts?limit={amount_of_facts}"
        url = f"{self.base_url.rstrip('/')}{endpoint}"

        response = httpx.get(url)
        response.raise_for_status()
        return response.json()

        