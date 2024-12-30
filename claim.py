import asyncio
from client import Client
from config import CLAIM, CLAIM_CONTRACT
from colorama import Fore, Back, Style


class Claim:
    def __init__(self, client: Client):
        self.client = client
        self.router_contract = self.client.get_contract(
            contract_address=CLAIM_CONTRACT[self.client.chain_name],
            abi=CLAIM
        )

    async def registr(self):
        registr = await self.router_contract.functions.register().build_transaction((await self.client.prepare_tx()))

        tx_hash = await self.client.send_transaction(registr)

        print(Fore.GREEN + "Registr cucsesful")


    async def info(self):
        info = await self.router_contract.functions.claimableTokens(self.client.address).call()

        print(f"Доступно к дропу {self.client.from_wei_custom(info,18)}")



    async def claim(self):

        claim = await self.router_contract.functions.claim(self.client.to_wei_custom(5,18)).build_transaction((await self.client.prepare_tx()))

        tx_hash = await self.client.send_transaction(claim)

        print(Fore.GREEN + "Склеймил  5 токенов")

        info = await self.router_contract.functions.claimableTokens(self.client.address).call()

        print(Fore.GREEN + f"Осталось доступно {self.client.from_wei_custom(info, 18)}")


    async def info_after_claim(self):
        info = await self.router_contract.functions.claimableTokens(self.client.address).call()

        print(f"Доступно к клейму {self.client.from_wei_custom(info,18)}")

        if info == 0:
            print(Fore.GREEN + "Скеймил все токены")
        else:print(Fore.RED + "Что-то пошло не так, надо смотреть...")
        exit()

    async def main(self):
        await claim_client.registr()
        for i in range(5):
            await claim_client.claim()
        await claim_client.info_after_claim()

private_key = ''
proxy = ''

w3_client = Client(private_key=private_key, proxy=proxy)
claim_client = Claim(client=w3_client)

asyncio.run(claim_client.info_after_claim())

