const faker = require("faker");
const puppeteer = require("puppeteer");

const bar = {
  name: faker.name.firstName(),
  description: faker.random.words(),
  address: faker.address.streetAddress()
};

describe('Title Text', () => {
  test('page loads correctly', async () => {
	let browser = await puppeteer.launch({
	  headless: false
  });

	let page = await browser.newPage();
	await page.goto('http://localhost:3000/');
	await page.waitForSelector('.app-title');

	let html = await page.$eval('.app-title', e => e.innerHTML);
	expect(html).toBe('Game Bar App');

	browser.close();
  }, 16000);
});

describe("Bar Form", () => {
  test("Can submit bar form", async () => {
    let browser = await puppeteer.launch({
      headless: false,
      slowMo: 50
    });
    let page = await browser.newPage();

    await page.goto("http://localhost:3000/");
    await page.waitForSelector(".btn-add-bar");
    await page.click(".btn-add-bar");

    await page.waitForSelector(".bar-form");

    await page.click(".input-name");
    await page.type(".input-name", bar.name);   
    let name = await page.$eval(".input-name", e => e.value); 
    await expect(name).toBe( bar.name);

    await page.click(".input-description");
    await page.type(".input-description", bar.description);
    let description = await page.$eval(".input-description", e => e.value); 
    await expect(description).toBe( bar.description);

    await page.click(".input-address");
    await page.type(".input-address", bar.address);
    let address = await page.$eval(".input-address", e => e.value); 
    await expect(address).toBe(bar.address);

    await page.click(".input-status");
    let status = await page.$eval(".input-status", e => e.value); 
    await expect(status).toBe("on");

    await page.click(".btn-submit");

    let html = await page.evaluate(() => document.querySelector(".bar-form"));
    expect(html).toBeNull();

    browser.close();
  }, 16000);
});
