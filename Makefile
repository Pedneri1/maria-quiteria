install:
	cp .env.example .env
	docker-compose pull && docker-compose build
	pip install --user pre-commit
	pre-commit install

run_spider:
	docker-compose run --rm scraper bash -c "cd scraper && scrapy crawl $(SPIDER)"

test:
	docker-compose run --rm scraper pytest
