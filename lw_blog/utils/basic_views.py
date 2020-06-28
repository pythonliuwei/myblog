from rest_framework.views import APIView


class MyAPIView(APIView):
    def __init__(self):
        super().__init__()
        self.TEM_SUCCESS_CODE = {
            "code": 0,
            "msg": "成功",
        }
        self.SUCCESS_CODE = {
            "code": 1000,
            "message": "成功",
        }
        self.QUERY_ERR_CODE = {
            "code": 2001,
            "message": "查询不存在",
        }
        self.UNEXPECTED_CODE = {
            "code": 2002,
            "message": "条件不符合",
        }
        self.PARAMETER_ERR_CODE = {
            "code": 3001,
            "message": "上传参数不足",
        }
        self.PARAMETER_TYPE_ERR_CODE = {
            "code": 3002,
            "message": "上传参数格式错误or类型错误",
        }
        self.SIZE_ERR_CODE = {
            "code": 3003,
            "message": "上传文件大小超限",
        }
        self.UPDATE_ERROR_CODE = {
            "code": 4000,
            "message": "更新失败"
        }
        self.REQUEST_ERR_CODE = {
            "code": 5000,
            "message": "获取第三方数据异常"
        }
        self.SYSTEM_ERR_CODE = {
            "code": 9999,
            "message": "系统异常",
        }
