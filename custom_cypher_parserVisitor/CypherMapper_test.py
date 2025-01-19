import time
import unittest
import asyncio
from CypherMapper import CypherMapper

class TestCypherMapper(unittest.TestCase):
    def setUp(self):
        self.mapper = CypherMapper("mapping.json")
        self.queries = [
            'MATCH (a)-[:父亲 *2 {name: "爸爸"}]->(b) RETURN a, b',
            'MATCH shortestPath((a:Person {name: "Alice"})-[*]-(b:Person {name: "Bob"})) RETURN p',
            'MATCH p = shortestPath((a:Person {name: "Alice"})-[:FRIEND*]-(b:Person {name: "Bob"})) RETURN length(p) AS shortest_path_length',
            'MATCH (n:Entity) WHERE n.time STARTS WITH "2025-01-01" RETURN n'
        ]

    async def _test_query(self, query, n=1):
        print(f'original query: {query}')
        mapped_query = await self.mapper.map_query(query)
        print(f'mapped query  : {mapped_query}')
        # 添加你的断言逻辑
        self.assertIsNotNone(mapped_query)

    async def _test_concurrent_query(self, query, n=1):
        start_time = time.time()
        results = []
        for _ in range(n):
            result_future = self.mapper.map_query(query)
            results.append(result_future)
        await asyncio.gather(*results)
        end_time = time.time()
        print(f"{n} queries took {end_time - start_time :.4f} seconds, average time: {(end_time - start_time) / n :.4f} seconds")

    def test_multiple_queries(self):
        for query in self.queries:
            asyncio.run(self._test_query(query))

    def test_concurrent_queries(self):
        async def run_concurrent_tests():
            tasks = [self._test_query(query) for query in self.queries]
            await asyncio.gather(*tasks)
        asyncio.run(run_concurrent_tests())

    def test_concurrent_queries2(self):
        asyncio.run(self._test_concurrent_query(self.queries[0],5000))

if __name__ == '__main__':
    unittest.main()
