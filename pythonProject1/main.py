from fastapi import FastAPI, Response
from playwright.async_api import async_playwright
import os

app = FastAPI()

@app.get("/")
async def root():
    async with async_playwright() as p:
        browser = await p.chromium.connect("wss://chrome.browserless.io?token=QmcNq8L5Wa9jMu14c85e16fff9236811c34a5767a8")

        context = await browser.new_context()
        page = await context.new_page()

        await page.set_viewport_size({'width': 1920, 'height': 1080})

        await page.goto('https://example.com')
        screenshot_bytes = await page.screenshot()

        await browser.close()

        return Response(content=screenshot_bytes, media_type='image/png')