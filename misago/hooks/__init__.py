from typing import Any, Dict, List, Type

from ariadne import SchemaBindable, SchemaDirectiveVisitor

from .action import ActionHook
from .filter import FilterHook
from .filters import (
    AuthenticateUserHook,
    CreateUserHook,
    CreateUserTokenHook,
    CreateUserTokenPayloadHook,
    GetAuthUserHook,
    GetUserFromContextHook,
    GetUserFromTokenHook,
    GetUserFromTokenPayloadHook,
    GraphQLContextHook,
    RegisterInputHook,
    RegisterInputModelHook,
    RegisterUserHook,
    TemplateContextHook,
)


authenticate_user_hook = AuthenticateUserHook()
create_user_hook = CreateUserHook()
create_user_token_hook = CreateUserTokenHook()
create_user_token_payload_hook = CreateUserTokenPayloadHook()
get_auth_user_hook = GetAuthUserHook()
get_user_from_context_hook = GetUserFromContextHook()
get_user_from_token_hook = GetUserFromTokenHook()
get_user_from_token_payload_hook = GetUserFromTokenPayloadHook()
graphql_context_hook = GraphQLContextHook()
graphql_directives_hook: Dict[str, Type[SchemaDirectiveVisitor]] = {}
graphql_type_defs_hook: List[str] = []
graphql_types_hook: List[SchemaBindable] = []
jinja2_extensions: List[Any] = []
jinja2_filters: Dict[str, Any] = {}
register_input_hook = RegisterInputHook()
register_input_model_hook = RegisterInputModelHook()
register_user_hook = RegisterUserHook()
template_context_hook = TemplateContextHook()
