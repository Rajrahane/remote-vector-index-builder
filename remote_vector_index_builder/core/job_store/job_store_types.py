from enum import Enum


class JobStoreType(str, Enum):
    InMemory = "inmemory"
    DynamoDB = "dynamodb"
