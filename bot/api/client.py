import asyncio
from aiogram.bot.bot import Bot
from aiohttp import ClientSession
import aiohttp
import os


class APIClient(object):
    """Объект для вызова API"""

    def __init__(self):
        self.base_url = "http://image-process-server:8080/"
        # self.base_url = "http://127.0.0.1:8080/"
        self.session = ClientSession(trust_env=True)

    async def dowload_file(self, file_id: str):
        from bot import bot

        downloaded_image = await bot.download_file_by_id(file_id=file_id)
        return downloaded_image

    async def apply_filter(self, file_id: str, filter_func: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        if filter_func == "grayscale":
            async with self.session.post(
                self.base_url + "grayscale", data=payload
            ) as resp:
                resp = await resp.read()
        elif filter_func == "invert":
            async with self.session.post(
                self.base_url + "invert", data=payload
            ) as resp:
                resp = await resp.read()
        else:
            payload["filter_name"] = filter_func
            async with self.session.post(
                self.base_url + "filter", data=payload
            ) as resp:
                resp = await resp.read()

        return resp

    async def apply_blur(self, file_id: str, radius: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        payload["radius"] = radius
        async with self.session.post(self.base_url + "blur", data=payload) as resp:
            resp = await resp.read()

        return resp

    async def get_image_info(self, file_id: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        async with self.session.post(
            self.base_url + "getImageInfo", data=payload
        ) as resp:
            resp = await resp.json()

        return resp

    async def rotate_image(self, file_id: str, degree: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        payload["angle"] = degree
        async with self.session.post(self.base_url + "rotate", data=payload) as resp:
            resp = await resp.read()

        return resp

    async def get_palette(self, file_id: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        async with self.session.post(
            self.base_url + "getColorPalette", data=payload
        ) as resp:
            resp = await resp.read()

        return resp

    async def mirror(self, file_id: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        async with self.session.post(self.base_url + "mirror", data=payload) as resp:
            resp = await resp.read()

        return resp

    async def brightness(self, file_id: str, factor: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        payload["factor"] = factor
        async with self.session.post(
            self.base_url + "brightness", data=payload
        ) as resp:
            resp = await resp.read()
        return resp

    async def thumbnail(self, file_id: str, width: str, height: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        payload["width"] = width
        payload["height"] = height
        async with self.session.post(self.base_url + "thumbnail", data=payload) as resp:
            resp = await resp.read()
        return resp

    async def compress(self, file_id: str, quality: str):
        payload = {}
        image = await self.dowload_file(file_id)
        payload["image"] = image
        payload["quality"] = quality
        payload["compress_method"] = "jpegoptim"
        async with self.session.post(self.base_url + "compress", data=payload) as resp:
            resp = await resp.read()
        return resp

    async def watermark(self, file_id: str, w_file_id: str):
        payload = {}
        payload["image_1"] = await self.dowload_file(file_id)
        payload["watermark"] = await self.dowload_file(w_file_id)
        payload["position"] = "center"
        async with self.session.post(self.base_url + "watermark", data=payload) as resp:
            resp = await resp.read()
        return resp

    async def close_session(self):
        await self.session.close()

    async def check_status(self, timeout=10):
        await asyncio.sleep(timeout)

        async with self.session.get(self.base_url + "about") as resp:
            resp = await resp.json()


client = APIClient()
