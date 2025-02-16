import asyncio


async def start_strongman(name: str, power: int) -> None:
    balls = 5
    print(f'Strongman {name} has started challenge...')
    for ball in range(1, balls + 1):
        await asyncio.sleep(balls / power)
        print(f'Strongman {name} has lifted ball number {ball}')
    print(f'Strongman {name} has finished challenge!')


async def tournament():
    man_1 = asyncio.create_task(start_strongman('Michael', 5))
    man_2 = asyncio.create_task(start_strongman('Alex', 3))
    man_3 = asyncio.create_task(start_strongman('Feodor', 8))
    await man_1
    await man_2
    await man_3


asyncio.run(tournament())
