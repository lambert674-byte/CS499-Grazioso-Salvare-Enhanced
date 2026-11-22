
from pymongo import MongoClient
from time import perf_counter

client = MongoClient("mongodb://127.0.0.1:27017/")
collection = client["aac"]["animals"]

query = {"Animal Type": "Bird"}

def benchmark(label, hint):
    times = []
    count = 0

    for _ in range(5):
        start = perf_counter()

        cursor = collection.find(
            query, {"_id": 1}
        ).hint(hint)

        count = sum(1 for _ in cursor)

        elapsed = (perf_counter() - start) * 1000
        times.append(elapsed)

    explain = collection.database.command(
        "explain",
        {
            "find": collection.name,
            "filter": query,
            "projection": {"_id": 1},
            "hint": hint
        },
        verbosity="executionStats"
    )

    stats = explain["executionStats"]

    print(f"\n{label}")
    print(f"Matching records: {count}")
    print(f"Average time: {sum(times)/len(times):.2f} ms")
    print(f"Documents examined: {stats['totalDocsExamined']}")
    print(f"Index keys examined: {stats['totalKeysExamined']}")

benchmark("Full Collection Scan", {"$natural": 1})
benchmark("Indexed Query", "Animal Type_1")

client.close()
