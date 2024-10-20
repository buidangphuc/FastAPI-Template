from fastapi import APIRouter, Depends
from starlette.concurrency import run_in_threadpool

from backend.common.response.response_schema import ResponseModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.common.security.permission import RequestPermission
from backend.utils.server_info import server_info

router = APIRouter()


@router.get(
    "",
    summary="Get server info",
    dependencies=[
        Depends(RequestPermission("sys:monitor:server")),
        DependsJwtAuth,
    ],
)
async def get_server_info() -> ResponseModel:
    data = {
        "cpu": await run_in_threadpool(server_info.get_cpu_info),
        "mem": await run_in_threadpool(server_info.get_mem_info),
        "sys": await run_in_threadpool(server_info.get_sys_info),
        "disk": await run_in_threadpool(server_info.get_disk_info),
        "service": await run_in_threadpool(server_info.get_service_info),
    }
    return response_base.success(data=data)
