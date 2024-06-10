import strawberry


@strawberry.type
class Query:
    hello: str = "Hello, world!"


schema = strawberry.Schema(query=Query)

