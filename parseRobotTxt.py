import robotparser


rp = robotparser.RobotFileParser()
rp.set_url('http://example.webscraping.com/robots.txt')
rp.read()
url = 'http://example.webscraping.com'
user_agent = 'BadCrawler'
rp.can_fetch(user_agent, url)

user_agent='GoodCrawler'
rp.can_fetch(user_agent, url)
