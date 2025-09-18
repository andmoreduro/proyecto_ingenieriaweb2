from fastapi import Header, HTTPException, status


def get_current_user_id(x_user_id: int | None = Header(default=None)) -> int:
    """
    A simple dependency that extracts the user ID from the X-User-ID header.
    In a real system, this header would be set by a trusted API Gateway
    after it has validated a JWT.
    """
    if x_user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="X-User-ID header is missing"
        )
    return x_user_id
