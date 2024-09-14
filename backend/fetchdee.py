import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from collections import deque
import time

class Agent:
    def __init__(self, topic):
        self.topic = topic

    def extract_relevant_info(self, content):
        # Implement logic to extract relevant information based on the topic
        return content  # Placeholder

    def embed(self, info):
        # Implement embedding logic
        return [0.0] * 300  # Placeholder for a 300-dimensional vector

    def store_vector(self, url, title, vector):
        # Implement logic to store the vector into permanent memory
        pass

class FetchDee:
    def __init__(self, start_url, max_pages=100, delay=1.5, topic=None):
        self.start_url = start_url
        self.max_pages = max_pages
        self.delay = delay
        self.visited = set()
        self.queue = deque([start_url])
        self.knowledge = []
        self.topic = topic
        self.agent = self.initialize_agent()

    def initialize_agent(self):
        # Initialize an agent to supervise the crawl
        return Agent(self.topic)

    def crawl(self):
        pages_crawled = 0
        while self.queue and pages_crawled < self.max_pages:
            url = self.queue.popleft()
            if url not in self.visited:
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        self.visited.add(url)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        self.process_page(url, soup)
                        self.enqueue_links(url, soup)
                        pages_crawled += 1
                        time.sleep(self.delay)
                except Exception as e:
                    print(f"Error crawling {url}: {str(e)}")

    def process_page(self, url, soup):
        title = soup.title.string if soup.title else "No title"
        content = soup.get_text(separator=' ', strip=True)
        relevant_info = self.extract_relevant_info(content)
        if relevant_info:
            vector = self.embed_information(relevant_info)
            self.store_vector(url, title, vector)

    def extract_relevant_info(self, content):
        # Extract information relevant to the topic
        return self.agent.extract_relevant_info(content)

    def embed_information(self, info):
        # Embed the extracted information into a vector
        return self.agent.embed(info)

    def store_vector(self, url, title, vector):
        # Store the vector into permanent memory
        self.agent.store_vector(url, title, vector)

    def enqueue_links(self, base_url, soup):
        for link in soup.find_all('a', href=True):
            url = urljoin(base_url, link['href'])
            if url.startswith(self.start_url) and url not in self.visited:
                self.queue.append(url)

    def get_knowledge(self):
        return self.knowledge