import strawberry


@strawberry.type
class Query:
    @strawberry.field
    def example(self, info) -> str:
        return "Hello, world!"


schema = strawberry.Schema(query=Query)
