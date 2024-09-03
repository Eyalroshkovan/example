import asyncio

from playwright.async_api import async_playwright

async def root():
    async with async_playwright() as p:
        browser = await p.chromium.connect("wss://chrome.browserless.io?token=QmcNq8L5Wa9jMu14c85e16fff9236811c34a5767a8")

        context = await browser.new_context()
        page = await context.new_page()

        await page.set_viewport_size({'width': 1920, 'height': 1080})

        await page.goto('https://example.com')

        await browser.close()

asyncio.run(root())