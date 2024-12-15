#!/usr/bin/env python3
"""A script that provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient


def nginx_log_stats():
    """Provides some stats about Nginx logs stored in MongoDB"""
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client.logs
        collection = db.nginx

        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")

        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            count = collection.count_documents({"method": method})
            print(f"\tmethod {method}: {count}")

        status_checks = collection.count_documents({"method": "GET", "path": "/status"})
        print(f"{status_checks} status check")

if __name__ == "__main__":
    nginx_log_stats()
