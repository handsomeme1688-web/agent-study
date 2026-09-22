def resolve_identity(token: str, token_to_user: dict[str,str]) -> str:
    """D20：凭据由服务端映射身份。"""
    raise NotImplementedError("请按当天任务卡完成 resolve_identity")

def require_owner(actual_owner: str | None, requester: str) -> None:
    """D20：无权或不存在统一抛PermissionError，HTTP层映射404。"""
    raise NotImplementedError("请按当天任务卡完成 require_owner")

