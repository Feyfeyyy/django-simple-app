from gqlauth.core.middlewares import JwtSchema
from strawberry.tools import merge_types

import users.schema as user_schema
import blog.schema as blog_schema

query = merge_types("Query", (user_schema.Query, blog_schema.Query))
mutation = merge_types("mutation", (user_schema.Mutation,))

schema = JwtSchema(query=query, mutation=mutation)
