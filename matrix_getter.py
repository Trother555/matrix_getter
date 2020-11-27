import aiohttp
import asyncio
import typing

import matrix as mt


class Config:
    Timeout = 1  # 1 second


def handle_ok(raw: str) -> typing.List[int]:
    matrix = mt.parse_matrix(raw)
    return mt.traverse(matrix)


async def get_matrix(url: str) -> typing.List[int]:
    session = aiohttp.ClientSession()
    try:
        res = await session.get(url, timeout=Config.Timeout)
        if res.ok:
            return handle_ok(await res.text())
        else:
            print(f'Error occered: {res.status}')
    except asyncio.TimeoutError:
        print('Timeout happend')
    except Exception as err:
        print('Unknown error occured')
        raise err
    finally:
        await session.close()
