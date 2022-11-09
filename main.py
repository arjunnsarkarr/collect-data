from selenium import webdriver     
import bs4

driver = webdriver.Chrome("driver\chromedriver.exe")
driver.get("https://in.indeed.com/jobs?q=software+developer+fresher&l=&from=searchOnHP&vjk=faca97c3fbd03e6f")

