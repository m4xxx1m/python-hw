import aiohttp
import asyncio
import sys
import os


async def download_image(session, target_path: str, index: int):
    async with session.get('https://random-image-pepebigotes.vercel.app/api/skeleton-random-image') as response:
        if response.ok:
            content = await response.read()
            filename = os.path.join(target_path, f'{index}.jpg')
            with open(filename, 'wb') as f:
                f.write(content)
        else:
            print(response.status)


async def download_images(num_images: int, target_path: str):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image(session, target_path, i) for i in range(num_images)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    num_images = int(sys.argv[1])
    target_path = sys.argv[2]
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    asyncio.run(download_images(num_images, target_path))
