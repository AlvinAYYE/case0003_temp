# 悦康开放平台 OPEN-API SPECIFICATION


**简介**:悦康开放平台 OPEN-API SPECIFICATION


**HOST**:https://emuat01-ym-openapi-svc.lcuat.cn


**联系人**:悦康开放平台团队


**Version**:1.8.1-SNAPSHOT


**接口路径**:/v3/api-docs/default


[TOC]






# 01. 基础安全机制


## 根据注册的APPID获取访问令牌（Token）


**接口地址**:`/api/v1/auth/login`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>Access Token 会在指定时间(一般30分钟)内过期，需要及时更新，或者重新获取</p>



**请求示例**:


```javascript
{
  "code": "",
  "appId": "",
  "secret": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|authLoginParams|AuthLoginParams|body|true|AuthLoginParams|AuthLoginParams|
|&emsp;&emsp;code|公司代码||false|string||
|&emsp;&emsp;appId|集成开发分配的APP ID||true|string||
|&emsp;&emsp;secret|集成开发分配的APP 密钥||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|AuthResultDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|accessToken|Access token API访问令牌，token应放入http header中，header名称为header属性值|string||
|refreshTicket|刷新Access token凭据|string||
|headerName|Access token HTTP请求头名称|string||
|expireAt|Token 过期时间|string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"accessToken": "",
	"refreshTicket": "",
	"headerName": "",
	"expireAt": ""
}
```


## 在访问令牌（Token）过期之前，使用临时ticket更新令牌，可避免secret泄漏


**接口地址**:`/api/v1/auth/refresh`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "accessToken": "",
  "refreshTicket": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|authRefreshParams|AuthRefreshParams|body|true|AuthRefreshParams|AuthRefreshParams|
|&emsp;&emsp;accessToken|Access Token API访问授权令牌||true|string||
|&emsp;&emsp;refreshTicket|Access Token API访问授权令牌刷新ticket||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|AuthResultDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|accessToken|Access token API访问令牌，token应放入http header中，header名称为header属性值|string||
|refreshTicket|刷新Access token凭据|string||
|headerName|Access token HTTP请求头名称|string||
|expireAt|Token 过期时间|string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"accessToken": "",
	"refreshTicket": "",
	"headerName": "",
	"expireAt": ""
}
```


# 02. 基础运营数据


## 获取授权机构下的客户渠道信息


**接口地址**:`/api/v1/foundation/channel`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|enabled|是否包含禁用|query|false|boolean||
|keyword|关键字（二级渠道名称）|query|false|string||
|channelCategoryId|渠道分类ID|query|false|string||
|channelId|一级渠道ID|query|false|string||
|referrerId|二级渠道ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageReferrerDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ReferrerDetailDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;channelCategory||ChannelCategory|ChannelCategory|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;channel||ChannelInfo|ChannelInfo|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;contact|联系人|string||
|&emsp;&emsp;&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;code|编号|string||
|&emsp;&emsp;enabled|是否启用|boolean||
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;contact|联系人|string||
|&emsp;&emsp;phone|手机号|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"channelCategory": {
				"id": "",
				"name": ""
			},
			"channel": {
				"id": "",
				"name": "",
				"contact": "",
				"phone": "",
				"note": ""
			},
			"code": "",
			"enabled": true,
			"type": {
				"code": "",
				"name": "",
				"system": ""
			},
			"note": "",
			"contact": "",
			"phone": ""
		}
	],
	"number": 0
}
```


## 在指定层级下创建渠道新节点


**接口地址**:`/api/v1/foundation/channel`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "type": "",
  "categoryId": "",
  "channelId": "",
  "organizationId": "",
  "contactName": "",
  "contactPhone": "",
  "contactEmail": "",
  "note": "",
  "enabled": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createChannelParam|CreateChannelParam|body|true|CreateChannelParam|CreateChannelParam|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;type|层级类型（渠道分类/一级渠道/二级渠道）,可用值:channelCategory,channel,referrer||true|string||
|&emsp;&emsp;categoryId|渠道分类ID，一二级渠道必填||false|string||
|&emsp;&emsp;channelId|一级渠道ID，二级渠道必填||false|string||
|&emsp;&emsp;organizationId|所属组织/部门ID，默认为总部||false|string||
|&emsp;&emsp;contactName|联系人||false|string||
|&emsp;&emsp;contactPhone|联系电话||false|string||
|&emsp;&emsp;contactEmail|联系邮箱||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;enabled|是否激活||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 部分修改指定渠道节点


**接口地址**:`/api/v1/foundation/channel/partial/{type}/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "organizationId": "",
  "contactName": "",
  "contactPhone": "",
  "contactEmail": "",
  "note": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|type||path|true|string||
|id||path|true|string||
|partialModifyChannelParam|PartialModifyChannelParam|body|true|PartialModifyChannelParam|PartialModifyChannelParam|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;organizationId|所属组织/部门ID，默认为总部||false|string||
|&emsp;&emsp;contactName|联系人||false|string||
|&emsp;&emsp;contactPhone|联系电话||false|string||
|&emsp;&emsp;contactEmail|联系邮箱||false|string||
|&emsp;&emsp;note|备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除指定层级的指定渠道节点


**接口地址**:`/api/v1/foundation/channel/{type}/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|type||path|true|string||
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 改变指定渠道节点(不包含分类)启用状态


**接口地址**:`/api/v1/foundation/channel/{type}/{id}/active`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "isActive": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|type||path|true|string||
|id||path|true|string||
|activeChannelParams|ActiveChannelParams|body|true|ActiveChannelParams|ActiveChannelParams|
|&emsp;&emsp;isActive|启用状态||true|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的诊所信息


**接口地址**:`/api/v1/foundation/clinic`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|keyword|关键字：编号/名称|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ClinicDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|formalName|正式名称|string||
|abbreviationName|简称|string||
|billingHeader|开票抬头|string||
|manager||Manager|Manager|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|address|门店地址|string||
|phone|门店电话|string||
|contact|联系人|string||
|contactPhone|联系人电话|string||
|aptitude||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|isActive|是否启用|boolean||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"number": "",
		"formalName": "",
		"abbreviationName": "",
		"billingHeader": "",
		"manager": {
			"id": "",
			"name": ""
		},
		"address": "",
		"phone": "",
		"contact": "",
		"contactPhone": "",
		"aptitude": {
			"code": "",
			"name": "",
			"system": ""
		},
		"isActive": true
	}
]
```


## 根据ID获取诊所信息


**接口地址**:`/api/v1/foundation/clinic/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ClinicDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|formalName|正式名称|string||
|abbreviationName|简称|string||
|billingHeader|开票抬头|string||
|manager||Manager|Manager|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|address|门店地址|string||
|phone|门店电话|string||
|contact|联系人|string||
|contactPhone|联系人电话|string||
|aptitude||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|isActive|是否启用|boolean||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"number": "",
	"formalName": "",
	"abbreviationName": "",
	"billingHeader": "",
	"manager": {
		"id": "",
		"name": ""
	},
	"address": "",
	"phone": "",
	"contact": "",
	"contactPhone": "",
	"aptitude": {
		"code": "",
		"name": "",
		"system": ""
	},
	"isActive": true
}
```


## 查找指定诊所的治疗房间、手术房间


**接口地址**:`/api/v1/foundation/clinic/{id}/room`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|RoomDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|ID|string||
|name|名称/姓名|string||
|type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"type": {
			"code": "",
			"name": "",
			"system": ""
		}
	}
]
```


## 获取授权机构下的指定字典数据


**接口地址**:`/api/v1/foundation/code/{system}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|system||path|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCodeValueDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"code": "",
			"name": "",
			"system": ""
		}
	],
	"number": 0
}
```


## 在授权机构下新增组织节点 - 部门


**接口地址**:`/api/v1/foundation/department`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "parentId": "",
  "name": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createDepartmentParams|CreateDepartmentParams|body|true|CreateDepartmentParams|CreateDepartmentParams|
|&emsp;&emsp;parentId|上级组织节点ID||true|string||
|&emsp;&emsp;name|部门名称||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 下载文件接口


**接口地址**:`/api/v1/foundation/download/{fileId}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|fileId||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的员工信息


**接口地址**:`/api/v1/foundation/employee`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|keyword|关键字：姓名/员工号/手机|query|false|string||
|clinicId|所在诊所ID|query|false|string||
|onboard|在离职标识，true代表在职，false代表离职,不填代表查询在职|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageEmployeeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|EmployeeDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;mobile|手机|string||
|&emsp;&emsp;job|工作职位|array|JobDto|
|&emsp;&emsp;&emsp;&emsp;organization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;role|职位角色|array|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;isPrimary|行政隶属|boolean||
|&emsp;&emsp;&emsp;&emsp;schedulable|是否排班|boolean||
|&emsp;&emsp;medicalDepartments|所属科室|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;professionalTitle||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;account|登录名|string||
|&emsp;&emsp;alias|别名|string||
|&emsp;&emsp;gender|性别(M/F)|string||
|&emsp;&emsp;canLogin|是否可登录|boolean||
|&emsp;&emsp;onboard|在离职标识，true代表在职，false代表离职|boolean||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;tagInfo|标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"number": "",
			"mobile": "",
			"job": [
				{
					"organization": {
						"id": "",
						"name": ""
					},
					"role": [
						{
							"code": "",
							"name": "",
							"system": ""
						}
					],
					"isPrimary": true,
					"schedulable": true
				}
			],
			"medicalDepartments": [
				{
					"id": "",
					"name": ""
				}
			],
			"professionalTitle": {
				"code": "",
				"name": "",
				"system": ""
			},
			"account": "",
			"alias": "",
			"gender": "",
			"canLogin": true,
			"onboard": true,
			"note": "",
			"tagInfo": [
				{
					"id": "",
					"name": ""
				}
			]
		}
	],
	"number": 0
}
```


## 在授权机构下创建员工


**接口地址**:`/api/v1/foundation/employee`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "alias": "",
  "gender": "",
  "number": "",
  "mobile": "",
  "note": "",
  "jobs": [
    {
      "organizationId": "",
      "jobRoleCodes": [],
      "isPrimary": true,
      "schedulable": true
    }
  ],
  "login": {
    "account": "",
    "password": "",
    "roles": []
  }
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createEmployeeParams|创建员工|body|true|CreateEmployeeParams|CreateEmployeeParams|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;alias|别名||false|string||
|&emsp;&emsp;gender|性别(M/F)||false|string||
|&emsp;&emsp;number|编号||false|string||
|&emsp;&emsp;mobile|手机||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;jobs|职位角色||false|array|JobRoleParams|
|&emsp;&emsp;&emsp;&emsp;organizationId|诊所或部门ID||true|string||
|&emsp;&emsp;&emsp;&emsp;jobRoleCodes|职位角色列表（参考 基础数据-职位角色）||true|array|string|
|&emsp;&emsp;&emsp;&emsp;isPrimary|行政隶属||false|boolean||
|&emsp;&emsp;&emsp;&emsp;schedulable|是否排班||false|boolean||
|&emsp;&emsp;login|||false|LoginAccountParams|LoginAccountParams|
|&emsp;&emsp;&emsp;&emsp;account|登录名||true|string||
|&emsp;&emsp;&emsp;&emsp;password|初始密码||true|string||
|&emsp;&emsp;&emsp;&emsp;roles|功能角色ID（参考 基础数据-功能角色）||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取授权机构下的指定员工信息


**接口地址**:`/api/v1/foundation/employee/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|EmployeeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|mobile|手机|string||
|job|工作职位|array|JobDto|
|&emsp;&emsp;organization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;role|职位角色|array|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;isPrimary|行政隶属|boolean||
|&emsp;&emsp;schedulable|是否排班|boolean||
|medicalDepartments|所属科室|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|professionalTitle||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|account|登录名|string||
|alias|别名|string||
|gender|性别(M/F)|string||
|canLogin|是否可登录|boolean||
|onboard|在离职标识，true代表在职，false代表离职|boolean||
|note|备注|string||
|tagInfo|标签|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"number": "",
	"mobile": "",
	"job": [
		{
			"organization": {
				"id": "",
				"name": ""
			},
			"role": [
				{
					"code": "",
					"name": "",
					"system": ""
				}
			],
			"isPrimary": true,
			"schedulable": true
		}
	],
	"medicalDepartments": [
		{
			"id": "",
			"name": ""
		}
	],
	"professionalTitle": {
		"code": "",
		"name": "",
		"system": ""
	},
	"account": "",
	"alias": "",
	"gender": "",
	"canLogin": true,
	"onboard": true,
	"note": "",
	"tagInfo": [
		{
			"id": "",
			"name": ""
		}
	]
}
```


## 修改员工信息


**接口地址**:`/api/v1/foundation/employee/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "alias": "",
  "gender": "",
  "number": "",
  "mobile": "",
  "note": "",
  "jobs": [
    {
      "organizationId": "",
      "jobRoleCodes": [],
      "isPrimary": true,
      "schedulable": true
    }
  ],
  "login": {
    "account": "",
    "password": "",
    "roles": []
  },
  "canLogin": true,
  "onboard": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyEmployParams|修改员工|body|true|ModifyEmployParams|ModifyEmployParams|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;alias|别名||false|string||
|&emsp;&emsp;gender|性别(M/F)||false|string||
|&emsp;&emsp;number|编号||false|string||
|&emsp;&emsp;mobile|手机||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;jobs|职位角色||false|array|JobRoleParams|
|&emsp;&emsp;&emsp;&emsp;organizationId|诊所或部门ID||true|string||
|&emsp;&emsp;&emsp;&emsp;jobRoleCodes|职位角色列表（参考 基础数据-职位角色）||true|array|string|
|&emsp;&emsp;&emsp;&emsp;isPrimary|行政隶属||false|boolean||
|&emsp;&emsp;&emsp;&emsp;schedulable|是否排班||false|boolean||
|&emsp;&emsp;login|||false|LoginAccountParams|LoginAccountParams|
|&emsp;&emsp;&emsp;&emsp;account|登录名||true|string||
|&emsp;&emsp;&emsp;&emsp;password|初始密码||true|string||
|&emsp;&emsp;&emsp;&emsp;roles|功能角色ID（参考 基础数据-功能角色）||false|array|string|
|&emsp;&emsp;canLogin|是否可登录||false|boolean||
|&emsp;&emsp;onboard|在离职标识，true代表在职，false代表离职，为空代表不修改||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的指定员工功能权限


**接口地址**:`/api/v1/foundation/employee/{id}/roles`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|EmployeeRolesDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|permissions|权限字|array||
|roleIds|功能角色Id|array||
|roleNames|功能角色名称|array||


**响应示例**:
```javascript
{
	"permissions": [],
	"roleIds": [],
	"roleNames": []
}
```


## 修改员工基础信息


**接口地址**:`/api/v1/foundation/employeeBase/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "alias": "",
  "gender": "",
  "number": "",
  "mobile": "",
  "note": "",
  "jobs": [
    {
      "organizationId": "",
      "jobRoleCodes": [],
      "isPrimary": true,
      "schedulable": true
    }
  ],
  "canLogin": true,
  "onboard": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyEmployBaseParams|修改员工|body|true|ModifyEmployBaseParams|ModifyEmployBaseParams|
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;alias|别名||false|string||
|&emsp;&emsp;gender|性别(M/F)||false|string||
|&emsp;&emsp;number|编号||false|string||
|&emsp;&emsp;mobile|手机||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;jobs|职位角色||false|array|JobRoleParams|
|&emsp;&emsp;&emsp;&emsp;organizationId|诊所或部门ID||true|string||
|&emsp;&emsp;&emsp;&emsp;jobRoleCodes|职位角色列表（参考 基础数据-职位角色）||true|array|string|
|&emsp;&emsp;&emsp;&emsp;isPrimary|行政隶属||false|boolean||
|&emsp;&emsp;&emsp;&emsp;schedulable|是否排班||false|boolean||
|&emsp;&emsp;canLogin|是否可登录||false|boolean||
|&emsp;&emsp;onboard|在离职标识，true代表在职，false代表离职，为空代表不修改||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的员工职位角色信息


**接口地址**:`/api/v1/foundation/job`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|JobRoleDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|代码|string||
|name|名称|string||
|system|编码系统|string||


**响应示例**:
```javascript
[
	{
		"code": "",
		"name": "",
		"system": ""
	}
]
```


## 获取授权机构的logo(Base64格式，空代表未设置)


**接口地址**:`/api/v1/foundation/logo`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|StringData|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|data||string||


**响应示例**:
```javascript
{
	"data": ""
}
```


## 获取授权机构下医疗科室信息


**接口地址**:`/api/v1/foundation/medical-department`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|MedicalDepartmentDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|manager|负责人|string||
|mobile|电话|string||
|note|备注|string||
|enabled|是否启用|boolean||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"code": "",
		"manager": "",
		"mobile": "",
		"note": "",
		"enabled": true
	}
]
```


## 获取授权机构下的组织架构，包括公司、区域、诊所、部门


**接口地址**:`/api/v1/foundation/organization`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|500|API访问错误|ErrorInfoDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|错误代码|string||
|message|错误描述|string||


**响应示例**:
```javascript
{
	"code": "",
	"message": ""
}
```


## 获取授权机构下的员工功能角色信息


**接口地址**:`/api/v1/foundation/role`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SecurityRoleDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|permissions|权限字|array||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"permissions": []
	}
]
```


## 获取授权机构下指定功能角色信息


**接口地址**:`/api/v1/foundation/role/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SecurityRoleDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|permissions|权限字|array||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"permissions": []
}
```


## 创建标签


**接口地址**:`/api/v1/foundation/tagDict/create`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "groupId": "",
  "tagName": "",
  "enabled": true,
  "color": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagCreateParam|TagCreateParam|body|true|TagCreateParam|TagCreateParam|
|&emsp;&emsp;groupId|标签组id||false|string||
|&emsp;&emsp;tagName|标签名称||false|string||
|&emsp;&emsp;enabled|标签状态，默认启用||false|boolean||
|&emsp;&emsp;color|标签颜色,例如:#941402||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|TagCreateResponse|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|tagId|标签id|string||


**响应示例**:
```javascript
{
	"tagId": ""
}
```


## 创建标签组


**接口地址**:`/api/v1/foundation/tagDict/group/create`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "groupName": "",
  "types": [],
  "tags": [
    {
      "color": "",
      "setId": "",
      "value": "",
      "custom": true
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagGroupCreateParam|TagGroupCreateParam|body|true|TagGroupCreateParam|TagGroupCreateParam|
|&emsp;&emsp;groupName|标签组名||false|string||
|&emsp;&emsp;types|适用范围 (客户印象标签:customer)或者(员工:employee;项目:care-service;商品&药品:product;卡项:fusion-card;促销:promotion)||false|array|string|
|&emsp;&emsp;tags|标签||false|array|Tag|
|&emsp;&emsp;&emsp;&emsp;color|标签颜色||false|string||
|&emsp;&emsp;&emsp;&emsp;setId|标签id||false|string||
|&emsp;&emsp;&emsp;&emsp;value|标签描述||false|string||
|&emsp;&emsp;&emsp;&emsp;custom|||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|TagGroupCreateResponse|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|groupId|标签组id|string||


**响应示例**:
```javascript
{
	"groupId": ""
}
```


## 修改标签组


**接口地址**:`/api/v1/foundation/tagDict/group/update`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "groupId": "",
  "groupName": "",
  "types": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagGroupUpdateParam|TagGroupUpdateParam|body|true|TagGroupUpdateParam|TagGroupUpdateParam|
|&emsp;&emsp;groupId|标签组id||false|string||
|&emsp;&emsp;groupName|标签组名||false|string||
|&emsp;&emsp;types|适用范围 (客户印象标签:customer)或者(员工:employee;项目:care-service;商品&药品:product;卡项:fusion-card;促销:promotion)||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改标签


**接口地址**:`/api/v1/foundation/tagDict/update`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "tagId": "",
  "tagName": "",
  "enabled": true,
  "color": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|tagUpdateParam|TagUpdateParam|body|true|TagUpdateParam|TagUpdateParam|
|&emsp;&emsp;tagId|标签id||false|string||
|&emsp;&emsp;tagName|标签名称||false|string||
|&emsp;&emsp;enabled|标签状态，默认启用||false|boolean||
|&emsp;&emsp;color|标签颜色,例如:#941402||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取标签信息


**接口地址**:`/api/v1/foundation/tagSets`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|TagSetDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|标签组ID|string||
|name|标签组名称|string||
|type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|scopes|适用范围|array|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|options|标签选项|array|TagOptionDto|
|&emsp;&emsp;id|标签id|string||
|&emsp;&emsp;value|标签选项值|string||
|&emsp;&emsp;color|标签选项颜色|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"type": {
			"code": "",
			"name": "",
			"system": ""
		},
		"scopes": [
			{
				"code": "",
				"name": "",
				"system": ""
			}
		],
		"options": [
			{
				"id": "",
				"value": "",
				"color": ""
			}
		]
	}
]
```


# 03. 产品类目数据


## 指定类型下创建分类新节点 - 各类型通用


**接口地址**:`/api/v1/catalog/category`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "type": "",
  "name": "",
  "parentId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createCategoryParam|CreateCategoryParam|body|true|CreateCategoryParam|CreateCategoryParam|
|&emsp;&emsp;type|类型(物资/药品/项目),可用值:goods,drug,service||true|string||
|&emsp;&emsp;name|名称||true|string||
|&emsp;&emsp;parentId|上级分类ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取授权机构下的物料类数据分类(树状结构)


**接口地址**:`/api/v1/catalog/category/goods/tree`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CategoryDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|parentId|父ID，空则为顶级元素|string||
|children|子元素，空则为叶子元素|array|CategoryDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|业务编码|string||
|&emsp;&emsp;parentId|父ID，空则为顶级元素|string||
|&emsp;&emsp;children|子元素，空则为叶子元素|array|CategoryDto|
|&emsp;&emsp;scope|类型(商品、药品、服务项目),可用值:goods,drug,service|string||
|scope|类型(商品、药品、服务项目),可用值:goods,drug,service|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"code": "",
		"parentId": "",
		"children": [
			{
				"id": "",
				"name": "",
				"code": "",
				"parentId": "",
				"children": [],
				"scope": ""
			}
		],
		"scope": ""
	}
]
```


## 获取授权机构下的服务类项目分类(树状结构)


**接口地址**:`/api/v1/catalog/category/service/tree`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CategoryDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|parentId|父ID，空则为顶级元素|string||
|children|子元素，空则为叶子元素|array|CategoryDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|业务编码|string||
|&emsp;&emsp;parentId|父ID，空则为顶级元素|string||
|&emsp;&emsp;children|子元素，空则为叶子元素|array|CategoryDto|
|&emsp;&emsp;scope|类型(商品、药品、服务项目),可用值:goods,drug,service|string||
|scope|类型(商品、药品、服务项目),可用值:goods,drug,service|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"code": "",
		"parentId": "",
		"children": [
			{
				"id": "",
				"name": "",
				"code": "",
				"parentId": "",
				"children": [],
				"scope": ""
			}
		],
		"scope": ""
	}
]
```


## 获取指定ID分类节点 - 各类型通用


**接口地址**:`/api/v1/catalog/category/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CategoryDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|parentId|父ID，空则为顶级元素|string||
|children|子元素，空则为叶子元素|array|CategoryDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|业务编码|string||
|&emsp;&emsp;parentId|父ID，空则为顶级元素|string||
|&emsp;&emsp;children|子元素，空则为叶子元素|array|CategoryDto|
|&emsp;&emsp;scope|类型(商品、药品、服务项目),可用值:goods,drug,service|string||
|scope|类型(商品、药品、服务项目),可用值:goods,drug,service|string||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"code": "",
	"parentId": "",
	"children": [
		{
			"id": "",
			"name": "",
			"code": "",
			"parentId": "",
			"children": [],
			"scope": ""
		}
	],
	"scope": ""
}
```


## 修改指定ID分类节点 - 各类型通用


**接口地址**:`/api/v1/catalog/category/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyCategoryParam|ModifyCategoryParam|body|true|ModifyCategoryParam|ModifyCategoryParam|
|&emsp;&emsp;name|名称||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除指定ID分类节点 - 各类型通用


**接口地址**:`/api/v1/catalog/category/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询项目-商品下发


**接口地址**:`/api/v1/catalog/product/clinic-sales-price/list`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "productIds": [],
  "productType": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|queryProductSalesPriceParams|查询项目/商品下发|body|true|QueryProductSalesPriceParams|QueryProductSalesPriceParams|
|&emsp;&emsp;productIds|项目/商品ID 最多支持50个||true|array|string|
|&emsp;&emsp;productType|项目/商品,可用值:service,product||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ProductClinicSalesPriceDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|productId|项目/商品ID|string||
|productType|项目/商品,可用值:service,product|string||
|clinicSalesPrices|下发门店|array|ClinicSalesPriceDto|
|&emsp;&emsp;clinicId|诊所ID|string||
|&emsp;&emsp;clinicName|诊所名称|string||
|&emsp;&emsp;salesPriceFlag|是否允许自定义价格|boolean||
|&emsp;&emsp;salesPrice|自定义价格 可能为空仅salesPriceFlag=true时存在|number||


**响应示例**:
```javascript
[
	{
		"productId": "",
		"productType": "",
		"clinicSalesPrices": [
			{
				"clinicId": "",
				"clinicName": "",
				"salesPriceFlag": true,
				"salesPrice": 0
			}
		]
	}
]
```


## 修改项目-商品下发


**接口地址**:`/api/v1/catalog/product/clinic-sales-price/update`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "productId": "",
  "productType": "",
  "clinicSalesPrices": [
    {
      "clinicId": "",
      "salesPriceFlag": true,
      "salesPrice": 0
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateProductClinicSalesPriceParams|修改项目/商品下发|body|true|UpdateProductClinicSalesPriceParams|UpdateProductClinicSalesPriceParams|
|&emsp;&emsp;productId|项目/商品ID||true|string||
|&emsp;&emsp;productType|项目/商品,可用值:service,product||true|string||
|&emsp;&emsp;clinicSalesPrices|门店下发配置 空数组代表清空配置||true|array|ClinicSalesPriceParams|
|&emsp;&emsp;&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;&emsp;&emsp;salesPriceFlag|是否允许自定义价格  true时必须设置自定义价格salesPrice||true|boolean||
|&emsp;&emsp;&emsp;&emsp;salesPrice|自定义售价||false|number||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的物料类数据 - 耗材、药品、药妆等受库存管控条目


**接口地址**:`/api/v1/catalog/product/goods`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|keyword|关键字：编号/条形码/名称/拼音码/标准编码|query|false|string||
|categoryId|所属类别ID|query|false|string||
|enabled|是否有效，默认：是|query|false|boolean||
|isPharmacy|是否药品，默认：否|query|false|boolean||
|businessTypeCodes|业态标识code|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageProductSkuDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ProductSkuDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|业务编码|string||
|&emsp;&emsp;englishName|英文名称|string||
|&emsp;&emsp;formalName|正式名称|string||
|&emsp;&emsp;aliasName|产品别名|array|string|
|&emsp;&emsp;category||Category|Category|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;code|编码|string||
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;manufacturer||Manufacturer|Manufacturer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;standardCode|标准编码|string||
|&emsp;&emsp;standardName|标准名称|string||
|&emsp;&emsp;barcode|内部条形码|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;bodyPart||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;buyPrice|默认进价|number||
|&emsp;&emsp;price|零售价格|number||
|&emsp;&emsp;priceMin|零售价格-最低|number||
|&emsp;&emsp;priceMax|零售价格-最高|number||
|&emsp;&emsp;isSalable|是否可售|boolean||
|&emsp;&emsp;suppliers|供应商|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;priceRules|价格规则|array|PriceRule|
|&emsp;&emsp;&emsp;&emsp;customerClassificationCode|客户分类ID|string||
|&emsp;&emsp;&emsp;&emsp;customerClassificationName|客户分类名称|string||
|&emsp;&emsp;&emsp;&emsp;price|折扣价格|number||
|&emsp;&emsp;businessTypes|业态|array|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;extensions||object||
|&emsp;&emsp;tjfl|统计分类|string||
|&emsp;&emsp;kssbz|抗菌药物标志|string||
|&emsp;&emsp;kjywfj|抗菌药物分级管理|string||
|&emsp;&emsp;drugLevelOneCategory|药品大类|string||
|&emsp;&emsp;ynzjbz|院内自制标志|boolean||
|&emsp;&emsp;zsjbz|注射剂标志|boolean||
|&emsp;&emsp;organizations|下发的连锁门店|array|IdNameFlagStringStringBoolean|
|&emsp;&emsp;&emsp;&emsp;id|门店id|string||
|&emsp;&emsp;&emsp;&emsp;name|门店名称|string||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;tags|标签|object||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"code": "",
			"englishName": "",
			"formalName": "",
			"aliasName": [],
			"category": {
				"id": "",
				"name": "",
				"code": ""
			},
			"type": {
				"code": "",
				"name": "",
				"system": ""
			},
			"manufacturer": {
				"id": "",
				"name": ""
			},
			"standardCode": "",
			"standardName": "",
			"barcode": "",
			"spec": "",
			"unit": "",
			"bodyPart": {
				"code": "",
				"name": "",
				"system": ""
			},
			"buyPrice": 0,
			"price": 0,
			"priceMin": 0,
			"priceMax": 0,
			"isSalable": true,
			"suppliers": [
				{
					"id": "",
					"name": ""
				}
			],
			"priceRules": [
				{
					"customerClassificationCode": "",
					"customerClassificationName": "",
					"price": 0
				}
			],
			"businessTypes": [
				{
					"code": "",
					"name": "",
					"system": ""
				}
			],
			"extensions": {},
			"tjfl": "",
			"kssbz": "",
			"kjywfj": "",
			"drugLevelOneCategory": "",
			"ynzjbz": true,
			"zsjbz": true,
			"organizations": [
				{
					"id": "",
					"name": "",
					"flag": true
				}
			],
			"tags": {}
		}
	],
	"number": 0
}
```


## 新建物料类数据


**接口地址**:`/api/v1/catalog/product/goods`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "nameCHS": "",
  "aliasCHS": "",
  "standardCode": "",
  "standardName": "",
  "nameENG": "",
  "aliasENG": "",
  "type": "",
  "categoryId": "",
  "number": "",
  "spec": "",
  "unit": "",
  "brand": "",
  "manufacturer": "",
  "purchasePrice": 0,
  "sellingPrice": 0,
  "enabled": true,
  "salable": true,
  "canIssueBonusPoint": true,
  "isDeal": true,
  "note": "",
  "businessTypeCodes": [],
  "tags": [
    {
      "color": "",
      "setId": "",
      "value": "",
      "custom": true
    }
  ],
  "barcode": "",
  "tjfl": "",
  "kssbz": "",
  "kjywfj": "",
  "drugLevelOneCategory": "",
  "ynzjbz": true,
  "zsjbz": true,
  "organizations": [
    {
      "id": "",
      "name": "",
      "flag": true
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createProdSpecParams|新建商品|body|true|CreateProdSpecParams|CreateProdSpecParams|
|&emsp;&emsp;nameCHS|中文名称||true|string||
|&emsp;&emsp;aliasCHS|中文简称||false|string||
|&emsp;&emsp;standardCode|标准编码||false|string||
|&emsp;&emsp;standardName|标准名称||false|string||
|&emsp;&emsp;nameENG|英文名称||false|string||
|&emsp;&emsp;aliasENG|英文简称||false|string||
|&emsp;&emsp;type|物资类型（商品/药品）,可用值:goods,drug||true|string||
|&emsp;&emsp;categoryId|所属分类ID||true|string||
|&emsp;&emsp;number|编号||true|string||
|&emsp;&emsp;spec|规格||true|string||
|&emsp;&emsp;unit|单位||true|string||
|&emsp;&emsp;brand|品牌||false|string||
|&emsp;&emsp;manufacturer|生产厂家||false|string||
|&emsp;&emsp;purchasePrice|采购价||false|number||
|&emsp;&emsp;sellingPrice|售价||false|number||
|&emsp;&emsp;enabled|是否启用||false|boolean||
|&emsp;&emsp;salable|是否可售||false|boolean||
|&emsp;&emsp;canIssueBonusPoint|是否赠送积分||false|boolean||
|&emsp;&emsp;isDeal|是否成交||false|boolean||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;businessTypeCodes|业态标识code||false|array|string|
|&emsp;&emsp;tags|标签||false|array|Tag|
|&emsp;&emsp;&emsp;&emsp;color|标签颜色||false|string||
|&emsp;&emsp;&emsp;&emsp;setId|标签id||false|string||
|&emsp;&emsp;&emsp;&emsp;value|标签描述||false|string||
|&emsp;&emsp;&emsp;&emsp;custom|||false|boolean||
|&emsp;&emsp;barcode|条形码 多个条形码请以','隔开||false|string||
|&emsp;&emsp;tjfl|统计分类||false|string||
|&emsp;&emsp;kssbz|抗菌药物标志||false|string||
|&emsp;&emsp;kjywfj|抗菌药物分级管理||false|string||
|&emsp;&emsp;drugLevelOneCategory|药品大类||false|string||
|&emsp;&emsp;ynzjbz|院内自制标志||false|boolean||
|&emsp;&emsp;zsjbz|注射剂标志||false|boolean||
|&emsp;&emsp;organizations|下发的连锁门店||false|array|IdNameFlagStringStringBoolean|
|&emsp;&emsp;&emsp;&emsp;id|门店id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|门店名称||false|string||
|&emsp;&emsp;&emsp;&emsp;flag|||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取授权机构下的物料类数据 - 耗材、药品、药妆等受库存管控条目


**接口地址**:`/api/v1/catalog/product/goods/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ProductSkuDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|englishName|英文名称|string||
|formalName|正式名称|string||
|aliasName|产品别名|array||
|category||Category|Category|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;code|编码|string||
|type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|manufacturer||Manufacturer|Manufacturer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|standardCode|标准编码|string||
|standardName|标准名称|string||
|barcode|内部条形码|string||
|spec|规格|string||
|unit|单位|string||
|bodyPart||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|buyPrice|默认进价|number||
|price|零售价格|number||
|priceMin|零售价格-最低|number||
|priceMax|零售价格-最高|number||
|isSalable|是否可售|boolean||
|suppliers|供应商|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|priceRules|价格规则|array|PriceRule|
|&emsp;&emsp;customerClassificationCode|客户分类ID|string||
|&emsp;&emsp;customerClassificationName|客户分类名称|string||
|&emsp;&emsp;price|折扣价格|number||
|businessTypes|业态|array|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|extensions||object||
|tjfl|统计分类|string||
|kssbz|抗菌药物标志|string||
|kjywfj|抗菌药物分级管理|string||
|drugLevelOneCategory|药品大类|string||
|ynzjbz|院内自制标志|boolean||
|zsjbz|注射剂标志|boolean||
|organizations|下发的连锁门店|array|IdNameFlagStringStringBoolean|
|&emsp;&emsp;id|门店id|string||
|&emsp;&emsp;name|门店名称|string||
|&emsp;&emsp;flag||boolean||
|tags|标签|object||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"code": "",
	"englishName": "",
	"formalName": "",
	"aliasName": [],
	"category": {
		"id": "",
		"name": "",
		"code": ""
	},
	"type": {
		"code": "",
		"name": "",
		"system": ""
	},
	"manufacturer": {
		"id": "",
		"name": ""
	},
	"standardCode": "",
	"standardName": "",
	"barcode": "",
	"spec": "",
	"unit": "",
	"bodyPart": {
		"code": "",
		"name": "",
		"system": ""
	},
	"buyPrice": 0,
	"price": 0,
	"priceMin": 0,
	"priceMax": 0,
	"isSalable": true,
	"suppliers": [
		{
			"id": "",
			"name": ""
		}
	],
	"priceRules": [
		{
			"customerClassificationCode": "",
			"customerClassificationName": "",
			"price": 0
		}
	],
	"businessTypes": [
		{
			"code": "",
			"name": "",
			"system": ""
		}
	],
	"extensions": {},
	"tjfl": "",
	"kssbz": "",
	"kjywfj": "",
	"drugLevelOneCategory": "",
	"ynzjbz": true,
	"zsjbz": true,
	"organizations": [
		{
			"id": "",
			"name": "",
			"flag": true
		}
	],
	"tags": {}
}
```


## 修改物料类数据


**接口地址**:`/api/v1/catalog/product/goods/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "nameCHS": "",
  "aliasCHS": "",
  "nameENG": "",
  "standardCode": "",
  "standardName": "",
  "aliasENG": "",
  "categoryId": "",
  "number": "",
  "spec": "",
  "unit": "",
  "brand": "",
  "manufacturer": "",
  "purchasePrice": 0,
  "sellingPrice": 0,
  "enabled": true,
  "isSalable": true,
  "canIssueBonusPoint": true,
  "isDeal": true,
  "note": "",
  "priceRules": [
    {
      "customerClassificationCode": "",
      "price": 0
    }
  ],
  "businessTypeCodes": [],
  "tags": [
    {
      "color": "",
      "setId": "",
      "value": "",
      "custom": true
    }
  ],
  "barcode": "",
  "tjfl": "",
  "kjywfj": "",
  "drugLevelOneCategory": "",
  "ynzjbz": true,
  "zsjbz": true,
  "kssbz": "",
  "organizations": [
    {
      "id": "",
      "name": "",
      "flag": true
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyProdSpecParams|修改物料 - 字段不传值（null）表示不修改|body|true|ModifyProdSpecParams|ModifyProdSpecParams|
|&emsp;&emsp;nameCHS|中文名称||false|string||
|&emsp;&emsp;aliasCHS|中文简称||false|string||
|&emsp;&emsp;nameENG|英文名称||false|string||
|&emsp;&emsp;standardCode|标准编码||false|string||
|&emsp;&emsp;standardName|标准名称||false|string||
|&emsp;&emsp;aliasENG|英文简称||false|string||
|&emsp;&emsp;categoryId|所属分类ID||false|string||
|&emsp;&emsp;number|编号 - 不建议修改||false|string||
|&emsp;&emsp;spec|规格||false|string||
|&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;brand|品牌||false|string||
|&emsp;&emsp;manufacturer|生产厂家||false|string||
|&emsp;&emsp;purchasePrice|采购价||false|number||
|&emsp;&emsp;sellingPrice|售价||false|number||
|&emsp;&emsp;enabled|是否启用||false|boolean||
|&emsp;&emsp;isSalable|是否可售||false|boolean||
|&emsp;&emsp;canIssueBonusPoint|是否赠送积分||false|boolean||
|&emsp;&emsp;isDeal|是否成交||false|boolean||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;priceRules|价格规则 - 全集替换||false|array|PriceRuleParam|
|&emsp;&emsp;&emsp;&emsp;customerClassificationCode|客户分类ID - 参考字典 客户分类[customer-classification]||true|string||
|&emsp;&emsp;&emsp;&emsp;price|折后价格||true|number||
|&emsp;&emsp;businessTypeCodes|业态标识code||false|array|string|
|&emsp;&emsp;tags|标签||false|array|Tag|
|&emsp;&emsp;&emsp;&emsp;color|标签颜色||false|string||
|&emsp;&emsp;&emsp;&emsp;setId|标签id||false|string||
|&emsp;&emsp;&emsp;&emsp;value|标签描述||false|string||
|&emsp;&emsp;&emsp;&emsp;custom|||false|boolean||
|&emsp;&emsp;barcode|条形码 多个条形码请以','隔开||false|string||
|&emsp;&emsp;tjfl|统计分类||false|string||
|&emsp;&emsp;kjywfj|抗菌药物分级管理||false|string||
|&emsp;&emsp;drugLevelOneCategory|药品大类||false|string||
|&emsp;&emsp;ynzjbz|院内自制标志||false|boolean||
|&emsp;&emsp;zsjbz|注射剂标志||false|boolean||
|&emsp;&emsp;kssbz|抗菌药物标志||false|string||
|&emsp;&emsp;organizations|下发的连锁门店||false|array|IdNameFlagStringStringBoolean|
|&emsp;&emsp;&emsp;&emsp;id|门店id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|门店名称||false|string||
|&emsp;&emsp;&emsp;&emsp;flag|||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 停用、启用物料类数据


**接口地址**:`/api/v1/catalog/product/goods/{id}/active`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "isActive": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|activeParams|ActiveParams|body|true|ActiveParams|ActiveParams|
|&emsp;&emsp;isActive|启用状态||true|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的服务类项目数据 - 服务项目


**接口地址**:`/api/v1/catalog/product/service`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|ids|项目id列表|query|false|array|string|
|keyword|关键字：编号/名称/拼音码/规格|query|false|string||
|categoryId|所属类别ID|query|false|string||
|enabled|是否有效 - 默认：是|query|false|boolean||
|businessTypeCodes|业态标识code|query|false|array|string|
|liveShowFilter|是否可直播售卖|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCareServiceDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CareServiceDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|业务编码|string||
|&emsp;&emsp;englishName|英文名称|string||
|&emsp;&emsp;category||Category|Category|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;code|编码|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;courseCount|疗程次数|integer(int32)||
|&emsp;&emsp;executable|是否可执行|boolean||
|&emsp;&emsp;bodyPart||BodyPart|BodyPart|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;price|零售价格|number||
|&emsp;&emsp;children|子项目，适用于组合项目|array|BundleServiceItemDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;spec||string||
|&emsp;&emsp;&emsp;&emsp;quantity||integer||
|&emsp;&emsp;&emsp;&emsp;unitPrice||number||
|&emsp;&emsp;enable|是否有效|boolean||
|&emsp;&emsp;businessTypes|业态|array|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;deal|是否成交|boolean||
|&emsp;&emsp;materialDtos|耗材信息|array|CareServiceMaterialDto|
|&emsp;&emsp;&emsp;&emsp;id|行id|string||
|&emsp;&emsp;&emsp;&emsp;materialId|耗材id|string||
|&emsp;&emsp;&emsp;&emsp;skuId|skuId|string||
|&emsp;&emsp;&emsp;&emsp;materialName|耗材名称|string||
|&emsp;&emsp;&emsp;&emsp;spec|耗材规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|耗材单位|string||
|&emsp;&emsp;&emsp;&emsp;usedQuantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|单价|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必填(否:0,是:1)|integer||
|&emsp;&emsp;&emsp;&emsp;executionFlag|是否唯一|integer||
|&emsp;&emsp;operatorDtos|操作人信息|array|CareServiceOperatorDto|
|&emsp;&emsp;&emsp;&emsp;id|行id|string||
|&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行划扣角色code|string||
|&emsp;&emsp;&emsp;&emsp;operationFee|操作费|number||
|&emsp;&emsp;&emsp;&emsp;manhourQuantity|工时数|number||
|&emsp;&emsp;&emsp;&emsp;manhourUnitCode|工时单位code|string||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|成本单价|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必填(否:0,是:1)|integer||
|&emsp;&emsp;&emsp;&emsp;uniqueFlag|是否唯一|integer||
|&emsp;&emsp;stepDtos|操作步骤信息|array|CareServiceStepDto|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;stepId||string||
|&emsp;&emsp;&emsp;&emsp;stepName||string||
|&emsp;&emsp;&emsp;&emsp;stepTypeCode||integer||
|&emsp;&emsp;&emsp;&emsp;roleFeeInfo||array|StepRoleFeeDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行角色code|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;operationFee|操作费|number||
|&emsp;&emsp;&emsp;&emsp;manhourQuantity||number||
|&emsp;&emsp;&emsp;&emsp;manhourUnitCode||string||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice||number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag||integer||
|&emsp;&emsp;&emsp;&emsp;uniqueFlag||integer||
|&emsp;&emsp;tags|标签|array|TagDictDto|
|&emsp;&emsp;&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;&emsp;&emsp;color|标签颜色|string||
|&emsp;&emsp;treatLevel||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"code": "",
			"englishName": "",
			"category": {
				"id": "",
				"name": "",
				"code": ""
			},
			"spec": "",
			"unit": "",
			"courseCount": 0,
			"executable": true,
			"bodyPart": {
				"id": "",
				"name": ""
			},
			"price": 0,
			"children": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"quantity": 0,
					"unitPrice": 0
				}
			],
			"enable": true,
			"businessTypes": [
				{
					"code": "",
					"name": "",
					"system": ""
				}
			],
			"deal": true,
			"materialDtos": [
				{
					"id": "",
					"materialId": "",
					"skuId": "",
					"materialName": "",
					"spec": "",
					"unit": "",
					"usedQuantity": 0,
					"costUnitPrice": 0,
					"requiredFlag": 0,
					"executionFlag": 0
				}
			],
			"operatorDtos": [
				{
					"id": "",
					"executionRoleCode": "",
					"operationFee": 0,
					"manhourQuantity": 0,
					"manhourUnitCode": "",
					"costUnitPrice": 0,
					"requiredFlag": 0,
					"uniqueFlag": 0
				}
			],
			"stepDtos": [
				{
					"id": "",
					"stepId": "",
					"stepName": "",
					"stepTypeCode": 0,
					"roleFeeInfo": [
						{
							"executionRoleCode": "",
							"operationFee": 0
						}
					],
					"manhourQuantity": 0,
					"manhourUnitCode": "",
					"costUnitPrice": 0,
					"requiredFlag": 0,
					"uniqueFlag": 0
				}
			],
			"tags": [
				{
					"groupId": "",
					"groupName": "",
					"tagId": "",
					"tagName": "",
					"color": ""
				}
			],
			"treatLevel": {
				"code": "",
				"name": ""
			}
		}
	],
	"number": 0
}
```


## 新建服务项目数据


**接口地址**:`/api/v1/catalog/product/service`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "tags": [
    {
      "tagId": "",
      "setId": "",
      "value": ""
    }
  ],
  "treatLevelCode": "",
  "nameCHS": "",
  "nameENG": "",
  "categoryId": "",
  "number": "",
  "bodyPartId": "",
  "spec": "",
  "unit": "",
  "standardCode": "",
  "standardName": "",
  "medicalDepartmentId": "",
  "sellingPrice": 0,
  "isMedical": true,
  "isCourse": true,
  "courseCount": 0,
  "isExecutable": true,
  "enabled": true,
  "sellingScope": "",
  "note": "",
  "businessTypeCodes": [],
  "deal": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createServiceParams|新建项目|body|true|CreateServiceParams|CreateServiceParams|
|&emsp;&emsp;tags|标签||false|array|TagDictParams|
|&emsp;&emsp;&emsp;&emsp;tagId|标签ID 优先使用该参数||false|string||
|&emsp;&emsp;&emsp;&emsp;setId|标签组ID 配合value参数一起使用||false|string||
|&emsp;&emsp;&emsp;&emsp;value|标签名称||false|string||
|&emsp;&emsp;treatLevelCode|执行资质 参考字典分类(execution-qualification)||false|string||
|&emsp;&emsp;nameCHS|中文名称||true|string||
|&emsp;&emsp;nameENG|英文名称||false|string||
|&emsp;&emsp;categoryId|所属分类ID||true|string||
|&emsp;&emsp;number|编号||true|string||
|&emsp;&emsp;bodyPartId|身体部位ID||false|string||
|&emsp;&emsp;spec|规格||false|string||
|&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;standardCode|标准编码||false|string||
|&emsp;&emsp;standardName|标准名称||false|string||
|&emsp;&emsp;medicalDepartmentId|所属科室，参考 基础数据-组织架构||false|string||
|&emsp;&emsp;sellingPrice|售价||false|number||
|&emsp;&emsp;isMedical|是否医疗项目||false|boolean||
|&emsp;&emsp;isCourse|是否疗程项目||false|boolean||
|&emsp;&emsp;courseCount|疗程次数||false|integer(int32)||
|&emsp;&emsp;isExecutable|是否可执行||false|boolean||
|&emsp;&emsp;enabled|是否启用||false|boolean||
|&emsp;&emsp;sellingScope|可售范围（不限/只能单卖/只能活动）,可用值:free,single,promotion||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;businessTypeCodes|业态标识code||false|array|string|
|&emsp;&emsp;deal|是否成交||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 添加项目的使用耗材


**接口地址**:`/api/v1/catalog/product/service/addMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "materialParams": [
    {
      "skuId": "",
      "materialName": "",
      "spec": "",
      "unit": "",
      "usedQuantity": 0,
      "costUnitPrice": 0,
      "requiredFlag": 0,
      "executionFlag": 0
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createCareServiceMaterialParam|CreateCareServiceMaterialParam|body|true|CreateCareServiceMaterialParam|CreateCareServiceMaterialParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;materialParams|耗材||false|array|CommonCareServiceMaterialParam|
|&emsp;&emsp;&emsp;&emsp;skuId|skuId||false|string||
|&emsp;&emsp;&emsp;&emsp;materialName|耗材名称||false|string||
|&emsp;&emsp;&emsp;&emsp;spec|耗材规格||false|string||
|&emsp;&emsp;&emsp;&emsp;unit|耗材单位||false|string||
|&emsp;&emsp;&emsp;&emsp;usedQuantity|数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|单价||false|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必填(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;executionFlag|划扣是否默认带出耗材(0:否,1:是)||false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 添加项目的操作人员


**接口地址**:`/api/v1/catalog/product/service/addOperator`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "operatorParams": [
    {
      "executionRoleCode": "",
      "operationFee": 0,
      "manhourQuantity": 0,
      "manhourUnitCode": "",
      "costUnitPrice": 0,
      "requiredFlag": 0,
      "uniqueFlag": 0
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createCareServiceOperatorParam|CreateCareServiceOperatorParam|body|true|CreateCareServiceOperatorParam|CreateCareServiceOperatorParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;operatorParams|操作人||false|array|CommonCareServiceOperatorParam|
|&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行划扣角色code||false|string||
|&emsp;&emsp;&emsp;&emsp;operationFee|操作费||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourQuantity|工时数||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourUnitCode|工时单位code (hour:小时,minute:分钟)||false|string||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|成本单价||false|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必填(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;uniqueFlag|是否唯一(0:否,1:是)||false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 添加项目的操作步骤


**接口地址**:`/api/v1/catalog/product/service/addStep`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "stepParams": [
    {
      "stepId": "",
      "stepName": "",
      "stepTypeCode": 0,
      "roleFeeInfo": [
        {
          "executionRoleCode": "",
          "operationFee": 0
        }
      ],
      "manhourQuantity": 0,
      "manhourUnitCode": "",
      "costUnitPrice": 0,
      "requiredFlag": 0
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createCareServiceStepParam|CreateCareServiceStepParam|body|true|CreateCareServiceStepParam|CreateCareServiceStepParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;stepParams|操作人||false|array|CommonCareServiceStepParam|
|&emsp;&emsp;&emsp;&emsp;stepId|步骤id||false|string||
|&emsp;&emsp;&emsp;&emsp;stepName|步骤名称||false|string||
|&emsp;&emsp;&emsp;&emsp;stepTypeCode|步骤类型 -1:操作前准备，0：操作项目,1:操作后护理||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleFeeInfo|划扣角色、费用信息||false|array|StepRoleFeeDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行角色code||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;operationFee|操作费||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourQuantity|工时数||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourUnitCode|工时单位 (hour:小时,minute:分钟)||false|string||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|成本数||false|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必选(0:否,1:是)||false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除项目的使用耗材


**接口地址**:`/api/v1/catalog/product/service/deleteMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "careServiceMaterialIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|deleteCareServiceMaterialParam|DeleteCareServiceMaterialParam|body|true|DeleteCareServiceMaterialParam|DeleteCareServiceMaterialParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;careServiceMaterialIds|项目耗材行Id||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除项目的操作人员


**接口地址**:`/api/v1/catalog/product/service/deleteOperator`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "careServiceOperatorIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|deleteCareServiceOperatorParam|DeleteCareServiceOperatorParam|body|true|DeleteCareServiceOperatorParam|DeleteCareServiceOperatorParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;careServiceOperatorIds|项目操作人行Id||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除项目的操作步骤


**接口地址**:`/api/v1/catalog/product/service/deleteStep`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "careServiceStepIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|deleteCareServiceStepParam|DeleteCareServiceStepParam|body|true|DeleteCareServiceStepParam|DeleteCareServiceStepParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;careServiceStepIds|项目操作步骤行Id||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询操作人员职位


**接口地址**:`/api/v1/catalog/product/service/findExecutionRole`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ExecutionRoleDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|执行角色code|string||
|display|执行角色名称|string||


**响应示例**:
```javascript
[
	{
		"code": "",
		"display": ""
	}
]
```


## 查询操作步骤


**接口地址**:`/api/v1/catalog/product/service/getOperationStepDictPageList`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|keyword|根据步骤名称搜索|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageOperationStepDictListDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|OperationStepDictListDto|
|&emsp;&emsp;id|步骤id|string||
|&emsp;&emsp;stepCode|步骤编号，BZ+年月日时分秒+四位随机数|string||
|&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;stepTypeCode|步骤类型, -1:操作前准备，0：操作项目,1:操作后护理|integer(int32)||
|&emsp;&emsp;stepTypeName|执行角色code|string||
|&emsp;&emsp;roleFeeInfo|划扣角色、费用信息|array|StepRoleFeeDTO|
|&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行角色code|string||
|&emsp;&emsp;&emsp;&emsp;operationFee|操作费|number||
|&emsp;&emsp;manhourQuantity|工时数|number||
|&emsp;&emsp;manhourUnitCode|工时单位|string||
|&emsp;&emsp;manhourUnitName|工时单位名称|string||
|&emsp;&emsp;costUnitPrice|成本数|number||
|&emsp;&emsp;enable|是否启用：0 未启用，1 启用|integer(int32)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"stepCode": "",
			"stepName": "",
			"stepTypeCode": 0,
			"stepTypeName": "",
			"roleFeeInfo": [
				{
					"executionRoleCode": "",
					"operationFee": 0
				}
			],
			"manhourQuantity": 0,
			"manhourUnitCode": "",
			"manhourUnitName": "",
			"costUnitPrice": 0,
			"enable": 0
		}
	],
	"number": 0
}
```


## 获取授权机构下的服务类项目数据 - 服务项目价格规则


**接口地址**:`/api/v1/catalog/product/service/price-rule`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|项目id列表, 不填写时，查询全部项目|query|false|array|string|
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCareServicePriceRuleDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CareServicePriceRuleDto|
|&emsp;&emsp;careServiceId|项目id|string||
|&emsp;&emsp;careServiceName|项目名称|string||
|&emsp;&emsp;priceRules|价格规则|array|PriceRuleDto|
|&emsp;&emsp;&emsp;&emsp;customerClassificationId|客户类别id|string||
|&emsp;&emsp;&emsp;&emsp;customerClassificationName|客户类别名称|string||
|&emsp;&emsp;&emsp;&emsp;price|单价,单位：元|number||
|&emsp;&emsp;&emsp;&emsp;validityStart|有效期--开始|string||
|&emsp;&emsp;&emsp;&emsp;validityEnd|有效期--结束|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"careServiceId": "",
			"careServiceName": "",
			"priceRules": [
				{
					"customerClassificationId": "",
					"customerClassificationName": "",
					"price": 0,
					"validityStart": "",
					"validityEnd": ""
				}
			]
		}
	],
	"number": 0
}
```


## 修改服务类项目价格规则


**接口地址**:`/api/v1/catalog/product/service/price-rule/update`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "priceRules": [
    {
      "customerClassificationId": "",
      "price": 0,
      "validityStart": "",
      "validityEnd": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateCareServicePriceRuleParams|UpdateCareServicePriceRuleParams|body|true|UpdateCareServicePriceRuleParams|UpdateCareServicePriceRuleParams|
|&emsp;&emsp;careServiceId|项目id||true|string||
|&emsp;&emsp;priceRules|价格规则||false|array|PriceRuleParams|
|&emsp;&emsp;&emsp;&emsp;customerClassificationId|客户类别id||true|string||
|&emsp;&emsp;&emsp;&emsp;price|单价, 单位：元||false|number||
|&emsp;&emsp;&emsp;&emsp;validityStart|有效期--开始, 格式：yyyy-MM-dd||false|string||
|&emsp;&emsp;&emsp;&emsp;validityEnd|有效期--结束, 格式：yyyy-MM-dd||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CareServicePriceRuleModifyResultDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|result||CareServicePriceRuleDto|CareServicePriceRuleDto|
|&emsp;&emsp;careServiceId|项目id|string||
|&emsp;&emsp;careServiceName|项目名称|string||
|&emsp;&emsp;priceRules|价格规则|array|PriceRuleDto|
|&emsp;&emsp;&emsp;&emsp;customerClassificationId|客户类别id|string||
|&emsp;&emsp;&emsp;&emsp;customerClassificationName|客户类别名称|string||
|&emsp;&emsp;&emsp;&emsp;price|单价,单位：元|number||
|&emsp;&emsp;&emsp;&emsp;validityStart|有效期--开始|string||
|&emsp;&emsp;&emsp;&emsp;validityEnd|有效期--结束|string||
|success|是否成功|boolean||


**响应示例**:
```javascript
{
	"result": {
		"careServiceId": "",
		"careServiceName": "",
		"priceRules": [
			{
				"customerClassificationId": "",
				"customerClassificationName": "",
				"price": 0,
				"validityStart": "",
				"validityEnd": ""
			}
		]
	},
	"success": true
}
```


## 修改项目的使用耗材


**接口地址**:`/api/v1/catalog/product/service/updateMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "materialParams": [
    {
      "skuId": "",
      "materialName": "",
      "spec": "",
      "unit": "",
      "usedQuantity": 0,
      "costUnitPrice": 0,
      "requiredFlag": 0,
      "executionFlag": 0,
      "id": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateCareServiceMaterialParam|UpdateCareServiceMaterialParam|body|true|UpdateCareServiceMaterialParam|UpdateCareServiceMaterialParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;materialParams|耗材||false|array|CareServiceMaterialParam|
|&emsp;&emsp;&emsp;&emsp;skuId|skuId||false|string||
|&emsp;&emsp;&emsp;&emsp;materialName|耗材名称||false|string||
|&emsp;&emsp;&emsp;&emsp;spec|耗材规格||false|string||
|&emsp;&emsp;&emsp;&emsp;unit|耗材单位||false|string||
|&emsp;&emsp;&emsp;&emsp;usedQuantity|数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|单价||false|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必填(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;executionFlag|划扣是否默认带出耗材(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|项目耗材行Id||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改项目的操作人员


**接口地址**:`/api/v1/catalog/product/service/updateOperator`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "operatorParams": [
    {
      "executionRoleCode": "",
      "operationFee": 0,
      "manhourQuantity": 0,
      "manhourUnitCode": "",
      "costUnitPrice": 0,
      "requiredFlag": 0,
      "uniqueFlag": 0,
      "id": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateCareServiceOperatorParam|UpdateCareServiceOperatorParam|body|true|UpdateCareServiceOperatorParam|UpdateCareServiceOperatorParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;operatorParams|操作人||false|array|CareServiceOperatorParam|
|&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行划扣角色code||false|string||
|&emsp;&emsp;&emsp;&emsp;operationFee|操作费||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourQuantity|工时数||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourUnitCode|工时单位code (hour:小时,minute:分钟)||false|string||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|成本单价||false|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必填(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;uniqueFlag|是否唯一(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|项目操作人行Id||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改项目的操作步骤


**接口地址**:`/api/v1/catalog/product/service/updateStep`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "careServiceId": "",
  "stepParams": [
    {
      "stepId": "",
      "stepName": "",
      "stepTypeCode": 0,
      "roleFeeInfo": [
        {
          "executionRoleCode": "",
          "operationFee": 0
        }
      ],
      "manhourQuantity": 0,
      "manhourUnitCode": "",
      "costUnitPrice": 0,
      "requiredFlag": 0,
      "id": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|updateCareServiceStepParam|UpdateCareServiceStepParam|body|true|UpdateCareServiceStepParam|UpdateCareServiceStepParam|
|&emsp;&emsp;careServiceId|项目Id||false|string||
|&emsp;&emsp;stepParams|操作步骤||false|array|CareServiceStepParam|
|&emsp;&emsp;&emsp;&emsp;stepId|步骤id||false|string||
|&emsp;&emsp;&emsp;&emsp;stepName|步骤名称||false|string||
|&emsp;&emsp;&emsp;&emsp;stepTypeCode|步骤类型 -1:操作前准备，0：操作项目,1:操作后护理||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleFeeInfo|划扣角色、费用信息||false|array|StepRoleFeeDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行角色code||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;operationFee|操作费||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourQuantity|工时数||false|number||
|&emsp;&emsp;&emsp;&emsp;manhourUnitCode|工时单位 (hour:小时,minute:分钟)||false|string||
|&emsp;&emsp;&emsp;&emsp;costUnitPrice|成本数||false|number||
|&emsp;&emsp;&emsp;&emsp;requiredFlag|是否必选(0:否,1:是)||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|操作步骤行id||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的服务类项目数据 - 单个项目


**接口地址**:`/api/v1/catalog/product/service/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CareServiceDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|englishName|英文名称|string||
|category||Category|Category|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;code|编码|string||
|spec|规格|string||
|unit|单位|string||
|courseCount|疗程次数|integer(int32)|integer(int32)|
|executable|是否可执行|boolean||
|bodyPart||BodyPart|BodyPart|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|price|零售价格|number||
|children|子项目，适用于组合项目|array|BundleServiceItemDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;spec||string||
|&emsp;&emsp;quantity||integer(int32)||
|&emsp;&emsp;unitPrice||number||
|enable|是否有效|boolean||
|businessTypes|业态|array|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|deal|是否成交|boolean||
|materialDtos|耗材信息|array|CareServiceMaterialDto|
|&emsp;&emsp;id|行id|string||
|&emsp;&emsp;materialId|耗材id|string||
|&emsp;&emsp;skuId|skuId|string||
|&emsp;&emsp;materialName|耗材名称|string||
|&emsp;&emsp;spec|耗材规格|string||
|&emsp;&emsp;unit|耗材单位|string||
|&emsp;&emsp;usedQuantity|数量|integer(int32)||
|&emsp;&emsp;costUnitPrice|单价|number||
|&emsp;&emsp;requiredFlag|是否必填(否:0,是:1)|integer(int32)||
|&emsp;&emsp;executionFlag|是否唯一|integer(int32)||
|operatorDtos|操作人信息|array|CareServiceOperatorDto|
|&emsp;&emsp;id|行id|string||
|&emsp;&emsp;executionRoleCode|执行划扣角色code|string||
|&emsp;&emsp;operationFee|操作费|number||
|&emsp;&emsp;manhourQuantity|工时数|number||
|&emsp;&emsp;manhourUnitCode|工时单位code|string||
|&emsp;&emsp;costUnitPrice|成本单价|number||
|&emsp;&emsp;requiredFlag|是否必填(否:0,是:1)|integer(int32)||
|&emsp;&emsp;uniqueFlag|是否唯一|integer(int32)||
|stepDtos|操作步骤信息|array|CareServiceStepDto|
|&emsp;&emsp;id||string||
|&emsp;&emsp;stepId||string||
|&emsp;&emsp;stepName||string||
|&emsp;&emsp;stepTypeCode||integer(int32)||
|&emsp;&emsp;roleFeeInfo||array|StepRoleFeeDTO|
|&emsp;&emsp;&emsp;&emsp;executionRoleCode|执行角色code|string||
|&emsp;&emsp;&emsp;&emsp;operationFee|操作费|number||
|&emsp;&emsp;manhourQuantity||number||
|&emsp;&emsp;manhourUnitCode||string||
|&emsp;&emsp;costUnitPrice||number||
|&emsp;&emsp;requiredFlag||integer(int32)||
|&emsp;&emsp;uniqueFlag||integer(int32)||
|tags|标签|array|TagDictDto|
|&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;color|标签颜色|string||
|treatLevel||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"code": "",
	"englishName": "",
	"category": {
		"id": "",
		"name": "",
		"code": ""
	},
	"spec": "",
	"unit": "",
	"courseCount": 0,
	"executable": true,
	"bodyPart": {
		"id": "",
		"name": ""
	},
	"price": 0,
	"children": [
		{
			"id": "",
			"name": "",
			"spec": "",
			"quantity": 0,
			"unitPrice": 0
		}
	],
	"enable": true,
	"businessTypes": [
		{
			"code": "",
			"name": "",
			"system": ""
		}
	],
	"deal": true,
	"materialDtos": [
		{
			"id": "",
			"materialId": "",
			"skuId": "",
			"materialName": "",
			"spec": "",
			"unit": "",
			"usedQuantity": 0,
			"costUnitPrice": 0,
			"requiredFlag": 0,
			"executionFlag": 0
		}
	],
	"operatorDtos": [
		{
			"id": "",
			"executionRoleCode": "",
			"operationFee": 0,
			"manhourQuantity": 0,
			"manhourUnitCode": "",
			"costUnitPrice": 0,
			"requiredFlag": 0,
			"uniqueFlag": 0
		}
	],
	"stepDtos": [
		{
			"id": "",
			"stepId": "",
			"stepName": "",
			"stepTypeCode": 0,
			"roleFeeInfo": [
				{
					"executionRoleCode": "",
					"operationFee": 0
				}
			],
			"manhourQuantity": 0,
			"manhourUnitCode": "",
			"costUnitPrice": 0,
			"requiredFlag": 0,
			"uniqueFlag": 0
		}
	],
	"tags": [
		{
			"groupId": "",
			"groupName": "",
			"tagId": "",
			"tagName": "",
			"color": ""
		}
	],
	"treatLevel": {
		"code": "",
		"name": ""
	}
}
```


## 根据服务项目id更新服务项目


**接口地址**:`/api/v1/catalog/product/service/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "tags": [
    {
      "tagId": "",
      "setId": "",
      "value": ""
    }
  ],
  "treatLevelCode": "",
  "categoryId": "",
  "nameCHS": "",
  "nameENG": "",
  "number": "",
  "bodyPartId": "",
  "spec": "",
  "unit": "",
  "standardCode": "",
  "standardName": "",
  "medicalDepartmentId": "",
  "sellingPrice": 0,
  "isMedical": true,
  "isCourse": true,
  "courseCount": 0,
  "isExecutable": true,
  "enabled": true,
  "sellingScope": "",
  "note": "",
  "businessTypeCodes": [],
  "deal": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyServiceParams|修改服务项目|body|true|ModifyServiceParams|ModifyServiceParams|
|&emsp;&emsp;tags|标签||false|array|TagDictParams|
|&emsp;&emsp;&emsp;&emsp;tagId|标签ID 优先使用该参数||false|string||
|&emsp;&emsp;&emsp;&emsp;setId|标签组ID 配合value参数一起使用||false|string||
|&emsp;&emsp;&emsp;&emsp;value|标签名称||false|string||
|&emsp;&emsp;treatLevelCode|执行资质 参考字典分类(execution-qualification)||false|string||
|&emsp;&emsp;categoryId|所属分类ID||true|string||
|&emsp;&emsp;nameCHS|中文名称||true|string||
|&emsp;&emsp;nameENG|英文名称||false|string||
|&emsp;&emsp;number|编号||true|string||
|&emsp;&emsp;bodyPartId|身体部位ID||false|string||
|&emsp;&emsp;spec|规格||false|string||
|&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;standardCode|标准编码||false|string||
|&emsp;&emsp;standardName|标准名称||false|string||
|&emsp;&emsp;medicalDepartmentId|所属科室，参考 基础数据-组织架构||false|string||
|&emsp;&emsp;sellingPrice|售价||false|number||
|&emsp;&emsp;isMedical|是否医疗项目||false|boolean||
|&emsp;&emsp;isCourse|是否疗程项目||false|boolean||
|&emsp;&emsp;courseCount|疗程次数||false|integer(int32)||
|&emsp;&emsp;isExecutable|是否可执行||false|boolean||
|&emsp;&emsp;enabled|是否启用||false|boolean||
|&emsp;&emsp;sellingScope|可售范围（不限/只能单卖/只能活动）,可用值:free,single,promotion||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;businessTypeCodes|业态标识code||false|array|string|
|&emsp;&emsp;deal|是否成交||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 暂停-启用服务项目


**接口地址**:`/api/v1/catalog/product/service/{id}/active`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "isActive": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|activeParams|ActiveParams|body|true|ActiveParams|ActiveParams|
|&emsp;&emsp;isActive|启用状态||true|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 04. 诊疗服务流程


## 获取授权机构下的预约数据 - 列表


**接口地址**:`/api/v1/workflow/appointment`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|clinicId|诊所Id|query|false|string||
|customerId|顾客ID|query|false|string||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|ownerId|医生/辅助人员ID|query|false|string||
|serviceKeyword|项目关键字|query|false|string||
|cancelled|是否包含已取消(默认-否)|query|false|boolean||
|careClass|预约类型(first,recurring,check,procedure,consume)|query|false|array|string|
|specialty|就诊类型(参考系统配置/字典管理)|query|false|array|string|
|operatorId|创建人|query|false|string||
|createStart|创建日期 - 开始，如 2018-11-11|query|false|string(date-time)||
|createEnd|创建日期 - 结束，如 2018-12-11|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageAppointmentDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|AppointmentDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;room||Room|Room|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;assistants|辅助人员|array|IdNameRoleDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;careClass||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;specialty||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;services|预约项目列表|array|IdNameTypeDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目|integer||
|&emsp;&emsp;intentions|预约意向项目列表|array|IdNameTypeDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目|integer||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;operator||Operator|Operator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;isPay|是否成交|boolean||
|&emsp;&emsp;start|开始时间|string(date-time)||
|&emsp;&emsp;end|结束时间|string(date-time)||
|&emsp;&emsp;createdAt|创建时间|string(date-time)||
|&emsp;&emsp;appointmentNo|预约编号|string||
|&emsp;&emsp;lastModifiedDate|最后修改时间|string(date-time)||
|&emsp;&emsp;lastModifiedUserId|最后修改人id|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"room": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"assistants": [
				{
					"id": "",
					"name": "",
					"role": {
						"code": "",
						"name": "",
						"system": ""
					}
				}
			],
			"careClass": {
				"code": "",
				"name": "",
				"system": ""
			},
			"specialty": {
				"code": "",
				"name": "",
				"system": ""
			},
			"services": [
				{
					"id": "",
					"name": "",
					"type": 0
				}
			],
			"intentions": [
				{
					"id": "",
					"name": "",
					"type": 0
				}
			],
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"note": "",
			"operator": {
				"id": "",
				"name": ""
			},
			"isPay": true,
			"start": "",
			"end": "",
			"createdAt": "",
			"appointmentNo": "",
			"lastModifiedDate": "",
			"lastModifiedUserId": ""
		}
	],
	"number": 0
}
```


## 创建预约


**接口地址**:`/api/v1/workflow/appointment`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "customerId": "",
  "clinicId": "",
  "start": "",
  "end": "",
  "doctorId": "",
  "nurseId": "",
  "consultantId": "",
  "beauticianId": "",
  "roomId": "",
  "medicalDepartmentId": "",
  "careClass": "",
  "specialty": "",
  "intentionsId": [],
  "serviceIds": [],
  "serviceList": [
    {
      "id": "",
      "name": "",
      "type": 0
    }
  ],
  "intentions": [],
  "note": "",
  "externalId": "",
  "source": "",
  "operatorId": "",
  "ignoreRest": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createAppointmentParams|CreateAppointmentParams|body|true|CreateAppointmentParams|CreateAppointmentParams|
|&emsp;&emsp;customerId|客人ID||true|string||
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;start|预约开始时间(ISO-8601标志格式，注意时区)||true|string(date-time)||
|&emsp;&emsp;end|预约结束时间(ISO-8601标志格式)||false|string(date-time)||
|&emsp;&emsp;doctorId|医生ID||false|string||
|&emsp;&emsp;nurseId|护士ID||false|string||
|&emsp;&emsp;consultantId|咨询师ID||false|string||
|&emsp;&emsp;beauticianId|美容师ID||false|string||
|&emsp;&emsp;roomId|诊室ID||false|string||
|&emsp;&emsp;medicalDepartmentId|医疗科室ID||false|string||
|&emsp;&emsp;careClass|预约类别(初诊，复诊，复查，疗程内，再消费),可用值:first,recurring,check,procedure,consume||false|string||
|&emsp;&emsp;specialty|就诊类型(参考系统配置/字典管理/就诊类型-specialty)||false|string||
|&emsp;&emsp;intentionsId|就诊意向项目分类||false|array|string|
|&emsp;&emsp;serviceIds|就诊实际项目||false|array|string|
|&emsp;&emsp;serviceList|就诊实际项目（新）||false|array|IdNameTypeDto|
|&emsp;&emsp;&emsp;&emsp;id|ID||false|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目||false|integer||
|&emsp;&emsp;intentions|||false|array|object|
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;externalId|外部预约单ID||false|string||
|&emsp;&emsp;source|外部来源代码(参考系统配置/字典管理/预约来源-appointment-source)||false|string||
|&emsp;&emsp;operatorId|创建员工Id||false|string||
|&emsp;&emsp;ignoreRest|有休息班/日程是否创建预约||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取预约空闲时间段


**接口地址**:`/api/v1/workflow/appointment/getAppointmentFreeList`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "organizationId": "",
  "employeeId": "",
  "roleCode": "",
  "scheduleDate": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|appointmentFreeParams|AppointmentFreeParams|body|true|AppointmentFreeParams|AppointmentFreeParams|
|&emsp;&emsp;organizationId|门店id||true|string||
|&emsp;&emsp;employeeId|员工id||true|string||
|&emsp;&emsp;roleCode|岗位编码(doctor医生、nurse护士、beautician美容师、consultant咨询师)||true|string||
|&emsp;&emsp;scheduleDate|日期||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AppointmentFreeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|scheduleDate|日期|string||
|orginazationId|门店id|string||
|roleCode|岗位编号|string||
|employeeId|员工id|string||
|freeTimeList|空闲时间列表|array|TimeRangeDto|
|&emsp;&emsp;beginTime|开始时间|string||
|&emsp;&emsp;endTime|结束时间|string||


**响应示例**:
```javascript
{
	"scheduleDate": "",
	"orginazationId": "",
	"roleCode": "",
	"employeeId": "",
	"freeTimeList": [
		{
			"beginTime": "",
			"endTime": ""
		}
	]
}
```


## 获取授权机构下的预约数据 - 单个


**接口地址**:`/api/v1/workflow/appointment/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AppointmentDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|clinic||Clinic|Clinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|room||Room|Room|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|doctor||Doctor|Doctor|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|assistants|辅助人员|array|IdNameRoleDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|careClass||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|specialty||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|services|预约项目列表|array|IdNameTypeDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目|integer(int32)||
|intentions|预约意向项目列表|array|IdNameTypeDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目|integer(int32)||
|status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|note|备注|string||
|operator||Operator|Operator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|isPay|是否成交|boolean||
|start|开始时间|string(date-time)|string(date-time)|
|end|结束时间|string(date-time)|string(date-time)|
|createdAt|创建时间|string(date-time)|string(date-time)|
|appointmentNo|预约编号|string||
|lastModifiedDate|最后修改时间|string(date-time)|string(date-time)|
|lastModifiedUserId|最后修改人id|string||


**响应示例**:
```javascript
{
	"id": "",
	"customer": {
		"id": "",
		"name": ""
	},
	"clinic": {
		"id": "",
		"name": ""
	},
	"medicalDepartment": {
		"id": "",
		"name": ""
	},
	"room": {
		"id": "",
		"name": ""
	},
	"doctor": {
		"id": "",
		"name": ""
	},
	"assistants": [
		{
			"id": "",
			"name": "",
			"role": {
				"code": "",
				"name": "",
				"system": ""
			}
		}
	],
	"careClass": {
		"code": "",
		"name": "",
		"system": ""
	},
	"specialty": {
		"code": "",
		"name": "",
		"system": ""
	},
	"services": [
		{
			"id": "",
			"name": "",
			"type": 0
		}
	],
	"intentions": [
		{
			"id": "",
			"name": "",
			"type": 0
		}
	],
	"status": {
		"code": "",
		"name": "",
		"system": ""
	},
	"note": "",
	"operator": {
		"id": "",
		"name": ""
	},
	"isPay": true,
	"start": "",
	"end": "",
	"createdAt": "",
	"appointmentNo": "",
	"lastModifiedDate": "",
	"lastModifiedUserId": ""
}
```


## 取消预约


**接口地址**:`/api/v1/workflow/appointment/{id}/cancel`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "note": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|cancelAppointmentParams|CancelAppointmentParams|body|true|CancelAppointmentParams|CancelAppointmentParams|
|&emsp;&emsp;note|备注||true|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 确认预约


**接口地址**:`/api/v1/workflow/appointment/{id}/confirm`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "note": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|conformAppointmentParams|确认预约参数|body|true|ConformAppointmentParams|ConformAppointmentParams|
|&emsp;&emsp;note|备注信息||false|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改预约


**接口地址**:`/api/v1/workflow/appointment/{id}/partial`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "doctorId": "",
  "start": "",
  "end": "",
  "careClass": "",
  "specialty": "",
  "note": "",
  "roomId": {
    "present": true,
    "value": ""
  },
  "consultantId": {
    "present": true,
    "value": ""
  },
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyAppointmentParams|ModifyAppointmentParams|body|true|ModifyAppointmentParams|ModifyAppointmentParams|
|&emsp;&emsp;clinicId|诊所ID||false|string||
|&emsp;&emsp;doctorId|医生ID||false|string||
|&emsp;&emsp;start|预约开始时间(ISO-8601标志格式)||false|string(date-time)||
|&emsp;&emsp;end|预约结束时间(ISO-8601标志格式)||false|string(date-time)||
|&emsp;&emsp;careClass|预约类别(初诊，复诊，复查，疗程内，再消费),可用值:first,recurring,check,procedure,consume||false|string||
|&emsp;&emsp;specialty|就诊类型(参考系统配置/字典管理/就诊类型-specialty)||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;roomId|||false|OptionalValueString|OptionalValueString|
|&emsp;&emsp;&emsp;&emsp;present|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;value|||false|string||
|&emsp;&emsp;consultantId|||false|OptionalValueString|OptionalValueString|
|&emsp;&emsp;&emsp;&emsp;present|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;value|||false|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 上传档案文件


**接口地址**:`/api/v1/workflow/archives/document/upload`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId|客户ID|query|true|string||
|categoryType|文件类型(检测报告:TestReport,诊断结果:diagnosisResults,处方:prescription,病历:medicalecord,知情同意书:informedConsent),可用值:TestReport,diagnosisResults,prescription,medicalecord,informedConsent|query|true|string||
|organizationId|门店Id|query|true|string||
|file||query|true|file||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DocumentUploadDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|fileId||string||


**响应示例**:
```javascript
{
	"fileId": ""
}
```


## 获取授权机构下的咨询数据


**接口地址**:`/api/v1/workflow/consultation`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|clinicId|诊所Id|query|false|string||
|customerId|顾客ID|query|false|string||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|methodCodes|咨询方式代码 - 列表|query|false|array|string|
|associatedId|相关人ID|query|false|string||
|creatorId|创建人ID|query|false|string||
|deal|是否成交|query|false|boolean||
|arrive|是否到访|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageConsultationDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ConsultationDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;content|咨询内容|string||
|&emsp;&emsp;neededServiceCategories|咨询项目类别 - 列表|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;recommendedServices|潜在项目 - 列表|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;description|未成交原因|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createdAt|创建时间|string(date-time)||
|&emsp;&emsp;deal|当日是否有成交并支付|boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"method": {
				"code": "",
				"name": "",
				"system": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"content": "",
			"neededServiceCategories": [
				{
					"id": "",
					"name": ""
				}
			],
			"recommendedServices": [
				{
					"id": "",
					"name": ""
				}
			],
			"description": "",
			"note": "",
			"creator": {
				"id": "",
				"name": ""
			},
			"createdAt": "",
			"deal": true
		}
	],
	"number": 0
}
```


## 创建咨询


**接口地址**:`/api/v1/workflow/consultation`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "customerId": "",
  "methodCode": "",
  "neededServiceCategoryIds": [],
  "recommendedServiceIds": [],
  "content": "",
  "medicalDepartmentId": "",
  "description": "",
  "note": "",
  "creatorId": "",
  "createdAt": "",
  "referralServiceIds": [],
  "opportunityPromotionIds": [],
  "dealIntention": 0,
  "willingVisit": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createConsultationParams|CreateConsultationParams|body|true|CreateConsultationParams|CreateConsultationParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;customerId|客户ID||true|string||
|&emsp;&emsp;methodCode|咨询方式代码(参考系统配置/字典管理/咨询方式 consultation-method)||true|string||
|&emsp;&emsp;neededServiceCategoryIds|咨询项目类别 - ID列表||false|array|string|
|&emsp;&emsp;recommendedServiceIds|潜在项目 - ID列表||false|array|string|
|&emsp;&emsp;content|咨询内容||false|string||
|&emsp;&emsp;medicalDepartmentId|科室ID||false|string||
|&emsp;&emsp;description|未成交原因||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;creatorId|咨询师ID||true|string||
|&emsp;&emsp;createdAt|咨询时间(ISO-8601标志格式)||false|string(date-time)||
|&emsp;&emsp;referralServiceIds|推荐项目 - ID列表||false|array|string|
|&emsp;&emsp;opportunityPromotionIds|关注活动 - ID列表||false|array|string|
|&emsp;&emsp;dealIntention|成交意愿 1-高 2-中 3-低 4-已成交||false|integer(int32)||
|&emsp;&emsp;willingVisit|是否愿意上门||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 修改咨询


**接口地址**:`/api/v1/workflow/modify/consultation`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "id": "",
  "clinicId": "",
  "customerId": "",
  "methodCode": "",
  "neededServiceCategoryIds": [],
  "recommendedServiceIds": [],
  "content": "",
  "medicalDepartmentId": "",
  "description": "",
  "note": "",
  "creatorId": "",
  "createdAt": "",
  "referralServiceIds": [],
  "opportunityPromotionIds": [],
  "dealIntention": 0,
  "willingVisit": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|modifyConsultationParams|ModifyConsultationParams|body|true|ModifyConsultationParams|ModifyConsultationParams|
|&emsp;&emsp;id|咨询id||true|string||
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;customerId|客户ID||true|string||
|&emsp;&emsp;methodCode|咨询方式代码(参考系统配置/字典管理/咨询方式 consultation-method)||true|string||
|&emsp;&emsp;neededServiceCategoryIds|咨询项目类别 - ID列表||false|array|string|
|&emsp;&emsp;recommendedServiceIds|潜在项目 - ID列表||false|array|string|
|&emsp;&emsp;content|咨询内容||false|string||
|&emsp;&emsp;medicalDepartmentId|科室ID||false|string||
|&emsp;&emsp;description|未成交原因||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;creatorId|咨询师ID||true|string||
|&emsp;&emsp;createdAt|咨询时间(ISO-8601标志格式)||false|string(date-time)||
|&emsp;&emsp;referralServiceIds|推荐项目 - ID列表||false|array|string|
|&emsp;&emsp;opportunityPromotionIds|关注活动 - ID列表||false|array|string|
|&emsp;&emsp;dealIntention|成交意愿 1-高 2-中 3-低 4-已成交||false|integer(int32)||
|&emsp;&emsp;willingVisit|是否愿意上门||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的现场人员空闲状态 - Experimental


**接口地址**:`/api/v1/workflow/participant/status`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|clinicId|诊所Id|query|true|string||
|roleCode|角色代码,可用值:consultant,doctor|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ParticipantStatusDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|participant||Participant|Participant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|isFree|是否空闲 - 忙碌为否|boolean||
|temporaryFrees|临时空闲队列|array|TemporaryFree|
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;pauseAt|暂停开始时间|string(date-time)||
|&emsp;&emsp;resumeAt|暂停结束时间 - 计划或实际时间|string(date-time)||
|&emsp;&emsp;note|备注|string||


**响应示例**:
```javascript
[
	{
		"participant": {
			"id": "",
			"name": ""
		},
		"isFree": true,
		"temporaryFrees": [
			{
				"customer": {
					"id": "",
					"name": ""
				},
				"pauseAt": "",
				"resumeAt": "",
				"note": ""
			}
		]
	}
]
```


## 获取前后对比照数据


**接口地址**:`/api/v1/workflow/photoCompares`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|customerId|客户ID|query|false|string||
|organizationId|机构ID|query|false|string||
|startTime|开始时间|query|false|string(date-time)||
|endTime|结束时间|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PagePhotoCompareDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|PhotoCompareDto|
|&emsp;&emsp;customer||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;organization||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;compareGroupId|项目对比组ID|string||
|&emsp;&emsp;item||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;before|术前照片文件信息|array|PhotoCompareFileDto|
|&emsp;&emsp;&emsp;&emsp;fileId|照片id|string||
|&emsp;&emsp;&emsp;&emsp;fileName|照片名称|string||
|&emsp;&emsp;&emsp;&emsp;createTime|上传时间|string||
|&emsp;&emsp;&emsp;&emsp;comparePictureId|图片集id|string||
|&emsp;&emsp;after|术后照片文件信息|array|PhotoCompareFileDto|
|&emsp;&emsp;&emsp;&emsp;fileId|照片id|string||
|&emsp;&emsp;&emsp;&emsp;fileName|照片名称|string||
|&emsp;&emsp;&emsp;&emsp;createTime|上传时间|string||
|&emsp;&emsp;&emsp;&emsp;comparePictureId|图片集id|string||
|&emsp;&emsp;reference|参考类型照片文件信息|array|PhotoCompareFileDto|
|&emsp;&emsp;&emsp;&emsp;fileId|照片id|string||
|&emsp;&emsp;&emsp;&emsp;fileName|照片名称|string||
|&emsp;&emsp;&emsp;&emsp;createTime|上传时间|string||
|&emsp;&emsp;&emsp;&emsp;comparePictureId|图片集id|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"customer": {
				"id": "",
				"name": ""
			},
			"organization": {
				"id": "",
				"name": ""
			},
			"compareGroupId": "",
			"item": {
				"id": "",
				"name": ""
			},
			"before": [
				{
					"fileId": "",
					"fileName": "",
					"createTime": "",
					"comparePictureId": ""
				}
			],
			"after": [
				{
					"fileId": "",
					"fileName": "",
					"createTime": "",
					"comparePictureId": ""
				}
			],
			"reference": [
				{
					"fileId": "",
					"fileName": "",
					"createTime": "",
					"comparePictureId": ""
				}
			]
		}
	],
	"number": 0
}
```


## 分页获取授权机构下的排班数据


**接口地址**:`/api/v1/workflow/schedule`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所ID|query|false|string||
|employeeId|员工ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageScheduleItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ScheduleItemDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;date|日期|string||
|&emsp;&emsp;employee||IdNameRoleDto|IdNameRoleDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;rule||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;start||ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;hour|小时|integer||
|&emsp;&emsp;&emsp;&emsp;minute|分钟|integer||
|&emsp;&emsp;end||ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;hour|小时|integer||
|&emsp;&emsp;&emsp;&emsp;minute|分钟|integer||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"clinic": {
				"id": "",
				"name": ""
			},
			"date": "",
			"employee": {
				"id": "",
				"name": "",
				"role": {
					"code": "",
					"name": "",
					"system": ""
				}
			},
			"rule": {
				"id": "",
				"name": ""
			},
			"start": {
				"hour": 0,
				"minute": 0
			},
			"end": {
				"hour": 0,
				"minute": 0
			}
		}
	],
	"number": 0
}
```


## 在授权机构下创建排班


**接口地址**:`/api/v1/workflow/schedule`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "date": "",
  "organizationId": "",
  "scheduleRuleId": "",
  "employeeId": "",
  "targetType": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createScheduleParams|CreateScheduleParams|body|true|CreateScheduleParams|CreateScheduleParams|
|&emsp;&emsp;date|日期||true|string(date-time)||
|&emsp;&emsp;organizationId|门店ID||true|string||
|&emsp;&emsp;scheduleRuleId|班次ID||true|string||
|&emsp;&emsp;employeeId|员工ID||true|string||
|&emsp;&emsp;targetType|资源类型，1：员工；2：设备。未填则默认为员工||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 分页获取授权机构下的班次信息


**接口地址**:`/api/v1/workflow/schedule-rule`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|clinicId|诊所ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageScheduleRuleDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ScheduleRuleDto|
|&emsp;&emsp;organization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;rules|班次|array|Rule|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;start||ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|小时|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|分钟|integer||
|&emsp;&emsp;&emsp;&emsp;end||ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;hour|小时|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;minute|分钟|integer||
|&emsp;&emsp;&emsp;&emsp;color|16色字符串，如 #c87d0e|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"organization": {
				"id": "",
				"name": ""
			},
			"rules": [
				{
					"id": "",
					"name": "",
					"start": {
						"hour": 0,
						"minute": 0
					},
					"end": {
						"hour": 0,
						"minute": 0
					},
					"color": ""
				}
			]
		}
	],
	"number": 0
}
```


## 在授权机构下创建班次


**接口地址**:`/api/v1/workflow/schedule-rule`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "organizationId": "",
  "name": "",
  "start": {
    "hour": 0,
    "minute": 0
  },
  "end": {
    "hour": 0,
    "minute": 0
  },
  "color": "",
  "note": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createScheduleRuleParams|CreateScheduleRuleParams|body|true|CreateScheduleRuleParams|CreateScheduleRuleParams|
|&emsp;&emsp;organizationId|门店ID||true|string||
|&emsp;&emsp;name|班次名称||true|string||
|&emsp;&emsp;start|||true|ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;hour|小时||false|integer||
|&emsp;&emsp;&emsp;&emsp;minute|分钟||false|integer||
|&emsp;&emsp;end|||true|ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;hour|小时||false|integer||
|&emsp;&emsp;&emsp;&emsp;minute|分钟||false|integer||
|&emsp;&emsp;color|16色字符串，如 #c87d0e||true|string||
|&emsp;&emsp;note|备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 在授权机构下修改班次


**接口地址**:`/api/v1/workflow/schedule-rule/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "organizationId": "",
  "name": "",
  "start": {
    "hour": 0,
    "minute": 0
  },
  "end": {
    "hour": 0,
    "minute": 0
  },
  "color": "",
  "note": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|updateScheduleRuleParams|UpdateScheduleRuleParams|body|true|UpdateScheduleRuleParams|UpdateScheduleRuleParams|
|&emsp;&emsp;organizationId|门店ID||true|string||
|&emsp;&emsp;name|班次名称||true|string||
|&emsp;&emsp;start|||true|ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;hour|小时||false|integer||
|&emsp;&emsp;&emsp;&emsp;minute|分钟||false|integer||
|&emsp;&emsp;end|||true|ScheduleTimeDto|ScheduleTimeDto|
|&emsp;&emsp;&emsp;&emsp;hour|小时||false|integer||
|&emsp;&emsp;&emsp;&emsp;minute|分钟||false|integer||
|&emsp;&emsp;color|16色字符串，如 #c87d0e||true|string||
|&emsp;&emsp;note|备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 创建签到


**接口地址**:`/api/v1/workflow/sign-in`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "customerId": "",
  "clinicId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|signInParams|创建签到|body|true|SignInParams|SignInParams|
|&emsp;&emsp;customerId|用户id||true|string||
|&emsp;&emsp;clinicId|门店id||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SignInDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|signInId||string||
|clinicId||string||
|customerId||string||
|signInNo||integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"signInId": "",
	"clinicId": "",
	"customerId": "",
	"signInNo": 0
}
```


## 获取授权机构下的到访数据


**接口地址**:`/api/v1/workflow/visit`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|clinicId|诊所Id|query|false|string||
|customerId|顾客ID|query|false|string||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|status|状态,可用值:in,out|query|false|string||
|appointmentId|预约ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageVisitDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|VisitDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;room||Room|Room|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;assistants|辅助人员|array|IdNameRoleDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;careClass||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;specialty||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;services|预约项目列表|array|IdNameTypeDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目|integer||
|&emsp;&emsp;intentions|预约意向项目列表|array|IdNameTypeDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目|integer||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;operator||Operator|Operator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;isPay|是否成交|boolean||
|&emsp;&emsp;appointmentId|关联预约ID|string||
|&emsp;&emsp;number|就诊号|string||
|&emsp;&emsp;arrivedAt|到达时间|string(date-time)||
|&emsp;&emsp;leftAt|离店时间|string(date-time)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"room": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"assistants": [
				{
					"id": "",
					"name": "",
					"role": {
						"code": "",
						"name": "",
						"system": ""
					}
				}
			],
			"careClass": {
				"code": "",
				"name": "",
				"system": ""
			},
			"specialty": {
				"code": "",
				"name": "",
				"system": ""
			},
			"services": [
				{
					"id": "",
					"name": "",
					"type": 0
				}
			],
			"intentions": [
				{
					"id": "",
					"name": "",
					"type": 0
				}
			],
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"note": "",
			"operator": {
				"id": "",
				"name": ""
			},
			"isPay": true,
			"appointmentId": "",
			"number": "",
			"arrivedAt": "",
			"leftAt": ""
		}
	],
	"number": 0
}
```


## 创建到访


**接口地址**:`/api/v1/workflow/visit`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "token": "",
  "customerId": "",
  "clinicId": "",
  "careClass": "",
  "specialty": "",
  "doctorId": "",
  "nurseId": "",
  "consultantId": "",
  "beauticianId": "",
  "roomId": "",
  "medicalDepartmentId": "",
  "serviceIds": [],
  "serviceList": [
    {
      "id": "",
      "name": "",
      "type": 0
    }
  ],
  "note": "",
  "operatorId": "",
  "intentionsId": [],
  "intentions": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createVisitParams|CreateVisitParams|body|true|CreateVisitParams|CreateVisitParams|
|&emsp;&emsp;token|操作token||true|string||
|&emsp;&emsp;customerId|客人ID||true|string||
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;careClass|预约类别(初诊，复诊，复查，疗程内，再消费)||true|string||
|&emsp;&emsp;specialty|就诊类型(参考系统配置/字典管理/就诊类型-specialty)||true|string||
|&emsp;&emsp;doctorId|医生ID||false|string||
|&emsp;&emsp;nurseId|护士ID||false|string||
|&emsp;&emsp;consultantId|咨询师ID||false|string||
|&emsp;&emsp;beauticianId|美容师ID||false|string||
|&emsp;&emsp;roomId|诊室ID||false|string||
|&emsp;&emsp;medicalDepartmentId|医疗科室ID||false|string||
|&emsp;&emsp;serviceIds|项目||false|array|string|
|&emsp;&emsp;serviceList|就诊实际项目（新）||false|array|IdNameTypeDto|
|&emsp;&emsp;&emsp;&emsp;id|ID||false|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型：1意向项目，2疗程项目，3复查项目||false|integer||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;operatorId|创建员工Id||false|string||
|&emsp;&emsp;intentionsId|项目分类||false|array|string|
|&emsp;&emsp;intentions|||false|array|object|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 到访客户信息


**接口地址**:`/api/v1/workflow/visit/customer-info`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerNumber|会员号|query|false|string||
|phoneNumber|手机号码|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ApiResultTodayVisitCustomerDTO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|description||string||
|errorCode||string||
|requestId||string||
|data||TodayVisitCustomerDTO|TodayVisitCustomerDTO|
|&emsp;&emsp;customerId|客户Id|string||
|&emsp;&emsp;customerName|客户姓名|string||
|&emsp;&emsp;customerNumber|会员编号|string||
|&emsp;&emsp;gender|性别（M/F）|string||
|&emsp;&emsp;phones|手机号码|array|string|
|&emsp;&emsp;age|年龄|integer(int32)||
|&emsp;&emsp;birthDay|生日|string||
|&emsp;&emsp;mail|邮箱|array|string|
|&emsp;&emsp;address|联系地址|string||
|&emsp;&emsp;wechat|微信号|string||
|&emsp;&emsp;visitOrganization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;visitId|到访Id|string||
|code||integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"description": "",
	"errorCode": "",
	"requestId": "",
	"data": {
		"customerId": "",
		"customerName": "",
		"customerNumber": "",
		"gender": "",
		"phones": [],
		"age": 0,
		"birthDay": "",
		"mail": [],
		"address": "",
		"wechat": "",
		"visitOrganization": {
			"id": "",
			"name": ""
		},
		"visitId": ""
	},
	"code": 0
}
```


## 到访操作token


**接口地址**:`/api/v1/workflow/visit/{customerId}/operation/token`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|TokenDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|token||string||


**响应示例**:
```javascript
{
	"token": ""
}
```


# 05. 客户关系管理


## 获取授权机构下的客户数据


**接口地址**:`/api/v1/crm/customer`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|birthday|生日|query|false|Birthday|Birthday|
|&emsp;&emsp;year|年||false|integer(int32)||
|&emsp;&emsp;month|月||false|integer(int32)||
|&emsp;&emsp;day|日||false|integer(int32)||
|keyword|关键字: 姓名/手机号/会员号/病历号/证件号|query|false|string||
|groupIds|客户分群分组Id - 列表|query|false|array|string|
|secondLevelChannelId|二级渠道Id|query|false|string||
|queryBinding|是否包含绑定关系|query|false|boolean||
|includeUnbound|是否包含已解绑的关系 - 仅包含绑定查询时生效|query|false|boolean||
|bindingType|指定绑定类型 - 仅包含绑定查询时生效,可用值:wx,minpro,h5,line,facebook|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCustomerDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CustomerDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;gender|性别（M/F）|string||
|&emsp;&emsp;email|Email|string||
|&emsp;&emsp;mobile|手机号 - 主号码|string||
|&emsp;&emsp;phones|手机号 - 列表（包含主号码）|array|PhoneDto|
|&emsp;&emsp;&emsp;&emsp;ownerType||OwnerType|OwnerType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;number|号码|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家代码， like +86|string||
|&emsp;&emsp;&emsp;&emsp;isPrimary|是否主号码 - 同时仅有一个主号码|boolean||
|&emsp;&emsp;&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;birthday||Birthday|Birthday|
|&emsp;&emsp;&emsp;&emsp;year|年|integer||
|&emsp;&emsp;&emsp;&emsp;month|月|integer||
|&emsp;&emsp;&emsp;&emsp;day|日|integer||
|&emsp;&emsp;maritalStatus||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;idCard||IdCardDto|IdCardDto|
|&emsp;&emsp;&emsp;&emsp;type|类型,参考系统设置：字典-证件类型-idcard-categories|string||
|&emsp;&emsp;&emsp;&emsp;number|号码|string||
|&emsp;&emsp;idCards|证件列表|array|IdCardDto|
|&emsp;&emsp;&emsp;&emsp;type|类型,参考系统设置：字典-证件类型-idcard-categories|string||
|&emsp;&emsp;&emsp;&emsp;number|号码|string||
|&emsp;&emsp;membershipLevel||MembershipLevel|MembershipLevel|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;expireDate|会员入会时间|string(date-time)||
|&emsp;&emsp;obtainedDate|会员失效时间|string(date-time)||
|&emsp;&emsp;creditBalance|积分余额|integer(int64)||
|&emsp;&emsp;isShared|是否共享客户|boolean||
|&emsp;&emsp;type||CustomerType|CustomerType|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;profileTags|动态标签|array|ProfileTag|
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;code|标签code|string||
|&emsp;&emsp;&emsp;&emsp;color|颜色值|string||
|&emsp;&emsp;classification||Classification|Classification|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;socialMediaAccounts|社交帐号|object||
|&emsp;&emsp;address||Address|Address|
|&emsp;&emsp;&emsp;&emsp;street|街道/门牌号|string||
|&emsp;&emsp;&emsp;&emsp;district|市区|string||
|&emsp;&emsp;&emsp;&emsp;city|城市|string||
|&emsp;&emsp;&emsp;&emsp;province|省/市|string||
|&emsp;&emsp;&emsp;&emsp;country|国家/地区|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家/地区的英文代码，参照ISO标准国家中英文对照表填写|string||
|&emsp;&emsp;&emsp;&emsp;postalCode|邮编|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultAssistant||ConsultAssistant|ConsultAssistant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;beautician||Beautician|Beautician|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;serviceConsultant||ServiceConsultant|ServiceConsultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;customerService||CustomerService|CustomerService|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developerAssistant||DeveloperAssistant|DeveloperAssistant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;referrer||ReferrerDto|ReferrerDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;channelCategory||ChannelCategory|ChannelCategory|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;channel||ChannelInfo|ChannelInfo|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;contact|联系人|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;organization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createdAt|创建日期|string(date-time)||
|&emsp;&emsp;createdBy||CreatedBy|CreatedBy|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;bindings|社交账号绑定关系|array|Binding|
|&emsp;&emsp;&emsp;&emsp;appId|绑定应用ID|string||
|&emsp;&emsp;&emsp;&emsp;appType|绑定应用类型|string||
|&emsp;&emsp;&emsp;&emsp;openId|openId|string||
|&emsp;&emsp;&emsp;&emsp;unbound|是否已解绑|boolean||
|&emsp;&emsp;&emsp;&emsp;boundAt|绑定日期|string||
|&emsp;&emsp;&emsp;&emsp;unboundAt|解绑日期|string||
|&emsp;&emsp;nativeProvince|籍贯（省份）|string||
|&emsp;&emsp;ethnicity||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;occupation||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;patients|病历号|array|CustomerPatient|
|&emsp;&emsp;&emsp;&emsp;organizationId|门店id|string||
|&emsp;&emsp;&emsp;&emsp;recordNumber|病历号|string||
|&emsp;&emsp;deleted|是否被作废|boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"number": "",
			"gender": "",
			"email": "",
			"mobile": "",
			"phones": [
				{
					"ownerType": {
						"code": "",
						"name": "",
						"system": ""
					},
					"number": "",
					"countryCode": "",
					"isPrimary": true,
					"type": {
						"code": "",
						"name": "",
						"system": ""
					}
				}
			],
			"note": "",
			"birthday": {
				"year": 1987,
				"month": 6,
				"day": 18
			},
			"maritalStatus": {
				"code": "",
				"name": "",
				"system": ""
			},
			"idCard": {
				"type": "",
				"number": ""
			},
			"idCards": [
				{
					"type": "",
					"number": ""
				}
			],
			"membershipLevel": {
				"id": "",
				"name": ""
			},
			"expireDate": "",
			"obtainedDate": "",
			"creditBalance": 0,
			"isShared": true,
			"type": {
				"code": "",
				"name": "",
				"system": ""
			},
			"profileTags": [
				{
					"name": "",
					"code": "",
					"color": ""
				}
			],
			"classification": {
				"id": "",
				"name": ""
			},
			"socialMediaAccounts": {},
			"address": {
				"street": "",
				"district": "",
				"city": "",
				"province": "",
				"country": "",
				"countryCode": "",
				"postalCode": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"consultAssistant": {
				"id": "",
				"name": ""
			},
			"beautician": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"serviceConsultant": {
				"id": "",
				"name": ""
			},
			"customerService": {
				"id": "",
				"name": ""
			},
			"developerAssistant": {
				"id": "",
				"name": ""
			},
			"referrer": {
				"id": "",
				"name": "",
				"channelCategory": {
					"id": "",
					"name": ""
				},
				"channel": {
					"id": "",
					"name": "",
					"contact": "",
					"phone": "",
					"note": ""
				}
			},
			"organization": {
				"id": "",
				"name": ""
			},
			"createdAt": "",
			"createdBy": {
				"id": "",
				"name": ""
			},
			"bindings": [
				{
					"appId": "",
					"appType": "",
					"openId": "",
					"unbound": true,
					"boundAt": "",
					"unboundAt": ""
				}
			],
			"nativeProvince": "",
			"ethnicity": {
				"code": "",
				"name": "",
				"system": ""
			},
			"occupation": {
				"code": "",
				"name": "",
				"system": ""
			},
			"patients": [
				{
					"organizationId": "",
					"recordNumber": ""
				}
			],
			"deleted": true
		}
	],
	"number": 0
}
```


## 在授权机构下创建新客户


**接口地址**:`/api/v1/crm/customer`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "number": "",
  "organizationId": "",
  "consultantId": "",
  "beauticianId": "",
  "doctorId": "",
  "customerServiceId": "",
  "serviceConsultantId": "",
  "consultAssistantId": "",
  "serviceConsultantEmployeeNumber": "",
  "developerAssistantId": "",
  "gender": "",
  "birthday": {
    "year": 1987,
    "month": 6,
    "day": 18
  },
  "maritalStatusCode": "",
  "mobile": "",
  "phones": [
    {
      "ownerTypeCode": "",
      "number": "",
      "countryCode": "+86",
      "isPrimary": true
    }
  ],
  "email": "",
  "socialMediaAccount": {
    "qq": "",
    "weChat": ""
  },
  "idCard": {
    "categoryCode": "",
    "number": ""
  },
  "address": {
    "street": "",
    "district": "",
    "city": "",
    "province": "",
    "country": "",
    "countryCode": "",
    "postalCode": ""
  },
  "referrer": {
    "referrerId": "",
    "internal": true
  },
  "note": "",
  "operatorId": "",
  "isShared": true,
  "tags": [
    {
      "setId": "",
      "value": ""
    }
  ],
  "nativeProvince": "",
  "ethnicity": "",
  "occupationCode": "",
  "classificationId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createCustomerParams|创建客户参数|body|true|CreateCustomerParams|CreateCustomerParams|
|&emsp;&emsp;name|姓名||true|string||
|&emsp;&emsp;number|会员编号||false|string||
|&emsp;&emsp;organizationId|归属门店ID||false|string||
|&emsp;&emsp;consultantId|归属咨询师ID||false|string||
|&emsp;&emsp;beauticianId|归属美容师ID||false|string||
|&emsp;&emsp;doctorId|归属医生ID||false|string||
|&emsp;&emsp;customerServiceId|归属客服ID||false|string||
|&emsp;&emsp;serviceConsultantId|归属电网咨询师ID||false|string||
|&emsp;&emsp;consultAssistantId|所属咨询助理ID||false|string||
|&emsp;&emsp;serviceConsultantEmployeeNumber|归属电网咨询师员工号||false|string||
|&emsp;&emsp;developerAssistantId|客户开发人||false|string||
|&emsp;&emsp;gender|性别,可用值:M,F||true|string||
|&emsp;&emsp;birthday|||false|Birthday|Birthday|
|&emsp;&emsp;&emsp;&emsp;year|年||false|integer||
|&emsp;&emsp;&emsp;&emsp;month|月||false|integer||
|&emsp;&emsp;&emsp;&emsp;day|日||false|integer||
|&emsp;&emsp;maritalStatusCode|婚姻状况 - 参考字典代码:婚姻状况||false|string||
|&emsp;&emsp;mobile|手机，本人主号码 - 同时仅允许一个主号码||false|string||
|&emsp;&emsp;phones|手机号列表 - 整体替换已有列表（包含主号码）||false|array|Phone|
|&emsp;&emsp;&emsp;&emsp;ownerTypeCode|手机号所有类型 - 本人，朋友，家人,可用值:self,friend,family||false|string||
|&emsp;&emsp;&emsp;&emsp;number|号码||true|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家代码||false|string||
|&emsp;&emsp;&emsp;&emsp;isPrimary|是否主号码 - 同时仅允许一个主号码||false|boolean||
|&emsp;&emsp;email|Email||false|string||
|&emsp;&emsp;socialMediaAccount|||false|SocialMediaAccount|SocialMediaAccount|
|&emsp;&emsp;&emsp;&emsp;qq|QQ||false|string||
|&emsp;&emsp;&emsp;&emsp;weChat|微信||false|string||
|&emsp;&emsp;idCard|||false|IdCard|IdCard|
|&emsp;&emsp;&emsp;&emsp;categoryCode|参考字典，证件类型 - idcard-categories||false|string||
|&emsp;&emsp;&emsp;&emsp;number|证件号||false|string||
|&emsp;&emsp;address|||false|Address|Address|
|&emsp;&emsp;&emsp;&emsp;street|街道/门牌号||false|string||
|&emsp;&emsp;&emsp;&emsp;district|市区||false|string||
|&emsp;&emsp;&emsp;&emsp;city|城市||true|string||
|&emsp;&emsp;&emsp;&emsp;province|省/市||false|string||
|&emsp;&emsp;&emsp;&emsp;country|国家/地区||false|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家/地区的英文代码，参照ISO标准国家中英文对照表填写||false|string||
|&emsp;&emsp;&emsp;&emsp;postalCode|邮编||false|string||
|&emsp;&emsp;referrer|||false|ReferrerParam|ReferrerParam|
|&emsp;&emsp;&emsp;&emsp;referrerId|二级渠道ID||true|string||
|&emsp;&emsp;&emsp;&emsp;internal|是否内部渠道(referrerId是否会员ID)||false|boolean||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;operatorId|登记人||false|string||
|&emsp;&emsp;isShared|是否共享客户（默认否）||false|boolean||
|&emsp;&emsp;tags|印象标签||false|array|TagParam|
|&emsp;&emsp;&emsp;&emsp;setId|标签组ID||true|string||
|&emsp;&emsp;&emsp;&emsp;value|标签值||true|string||
|&emsp;&emsp;nativeProvince|籍贯（省份）||false|string||
|&emsp;&emsp;ethnicity|民族（Code）- 参考字典代码:ethnicity（民族）||false|string||
|&emsp;&emsp;occupationCode|职业- 参考字典代码:occupation（职业）||false|string||
|&emsp;&emsp;classificationId|客户类别id，传参参考系统配置-客户分类,字典[customer-classification]||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据手机号码查询客户数据


**接口地址**:`/api/v1/crm/customer/findByMobile`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|mobile|手机号码|query|false|string||
|queryBinding|是否包含绑定关系|query|false|boolean||
|includeUnbound|是否包含已解绑的关系 - 仅包含绑定查询时生效|query|false|boolean||
|bindingType|指定绑定类型 - 仅包含绑定查询时生效,可用值:wx,minpro,h5,line,facebook|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCustomerDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CustomerDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;gender|性别（M/F）|string||
|&emsp;&emsp;email|Email|string||
|&emsp;&emsp;mobile|手机号 - 主号码|string||
|&emsp;&emsp;phones|手机号 - 列表（包含主号码）|array|PhoneDto|
|&emsp;&emsp;&emsp;&emsp;ownerType||OwnerType|OwnerType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;number|号码|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家代码， like +86|string||
|&emsp;&emsp;&emsp;&emsp;isPrimary|是否主号码 - 同时仅有一个主号码|boolean||
|&emsp;&emsp;&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;birthday||Birthday|Birthday|
|&emsp;&emsp;&emsp;&emsp;year|年|integer||
|&emsp;&emsp;&emsp;&emsp;month|月|integer||
|&emsp;&emsp;&emsp;&emsp;day|日|integer||
|&emsp;&emsp;maritalStatus||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;idCard||IdCardDto|IdCardDto|
|&emsp;&emsp;&emsp;&emsp;type|类型,参考系统设置：字典-证件类型-idcard-categories|string||
|&emsp;&emsp;&emsp;&emsp;number|号码|string||
|&emsp;&emsp;idCards|证件列表|array|IdCardDto|
|&emsp;&emsp;&emsp;&emsp;type|类型,参考系统设置：字典-证件类型-idcard-categories|string||
|&emsp;&emsp;&emsp;&emsp;number|号码|string||
|&emsp;&emsp;membershipLevel||MembershipLevel|MembershipLevel|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;expireDate|会员入会时间|string(date-time)||
|&emsp;&emsp;obtainedDate|会员失效时间|string(date-time)||
|&emsp;&emsp;creditBalance|积分余额|integer(int64)||
|&emsp;&emsp;isShared|是否共享客户|boolean||
|&emsp;&emsp;type||CustomerType|CustomerType|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;profileTags|动态标签|array|ProfileTag|
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;code|标签code|string||
|&emsp;&emsp;&emsp;&emsp;color|颜色值|string||
|&emsp;&emsp;classification||Classification|Classification|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;socialMediaAccounts|社交帐号|object||
|&emsp;&emsp;address||Address|Address|
|&emsp;&emsp;&emsp;&emsp;street|街道/门牌号|string||
|&emsp;&emsp;&emsp;&emsp;district|市区|string||
|&emsp;&emsp;&emsp;&emsp;city|城市|string||
|&emsp;&emsp;&emsp;&emsp;province|省/市|string||
|&emsp;&emsp;&emsp;&emsp;country|国家/地区|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家/地区的英文代码，参照ISO标准国家中英文对照表填写|string||
|&emsp;&emsp;&emsp;&emsp;postalCode|邮编|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultAssistant||ConsultAssistant|ConsultAssistant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;beautician||Beautician|Beautician|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;serviceConsultant||ServiceConsultant|ServiceConsultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;customerService||CustomerService|CustomerService|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developerAssistant||DeveloperAssistant|DeveloperAssistant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;referrer||ReferrerDto|ReferrerDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;channelCategory||ChannelCategory|ChannelCategory|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;channel||ChannelInfo|ChannelInfo|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;contact|联系人|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;organization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createdAt|创建日期|string(date-time)||
|&emsp;&emsp;createdBy||CreatedBy|CreatedBy|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;bindings|社交账号绑定关系|array|Binding|
|&emsp;&emsp;&emsp;&emsp;appId|绑定应用ID|string||
|&emsp;&emsp;&emsp;&emsp;appType|绑定应用类型|string||
|&emsp;&emsp;&emsp;&emsp;openId|openId|string||
|&emsp;&emsp;&emsp;&emsp;unbound|是否已解绑|boolean||
|&emsp;&emsp;&emsp;&emsp;boundAt|绑定日期|string||
|&emsp;&emsp;&emsp;&emsp;unboundAt|解绑日期|string||
|&emsp;&emsp;nativeProvince|籍贯（省份）|string||
|&emsp;&emsp;ethnicity||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;occupation||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;patients|病历号|array|CustomerPatient|
|&emsp;&emsp;&emsp;&emsp;organizationId|门店id|string||
|&emsp;&emsp;&emsp;&emsp;recordNumber|病历号|string||
|&emsp;&emsp;deleted|是否被作废|boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"number": "",
			"gender": "",
			"email": "",
			"mobile": "",
			"phones": [
				{
					"ownerType": {
						"code": "",
						"name": "",
						"system": ""
					},
					"number": "",
					"countryCode": "",
					"isPrimary": true,
					"type": {
						"code": "",
						"name": "",
						"system": ""
					}
				}
			],
			"note": "",
			"birthday": {
				"year": 1987,
				"month": 6,
				"day": 18
			},
			"maritalStatus": {
				"code": "",
				"name": "",
				"system": ""
			},
			"idCard": {
				"type": "",
				"number": ""
			},
			"idCards": [
				{
					"type": "",
					"number": ""
				}
			],
			"membershipLevel": {
				"id": "",
				"name": ""
			},
			"expireDate": "",
			"obtainedDate": "",
			"creditBalance": 0,
			"isShared": true,
			"type": {
				"code": "",
				"name": "",
				"system": ""
			},
			"profileTags": [
				{
					"name": "",
					"code": "",
					"color": ""
				}
			],
			"classification": {
				"id": "",
				"name": ""
			},
			"socialMediaAccounts": {},
			"address": {
				"street": "",
				"district": "",
				"city": "",
				"province": "",
				"country": "",
				"countryCode": "",
				"postalCode": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"consultAssistant": {
				"id": "",
				"name": ""
			},
			"beautician": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"serviceConsultant": {
				"id": "",
				"name": ""
			},
			"customerService": {
				"id": "",
				"name": ""
			},
			"developerAssistant": {
				"id": "",
				"name": ""
			},
			"referrer": {
				"id": "",
				"name": "",
				"channelCategory": {
					"id": "",
					"name": ""
				},
				"channel": {
					"id": "",
					"name": "",
					"contact": "",
					"phone": "",
					"note": ""
				}
			},
			"organization": {
				"id": "",
				"name": ""
			},
			"createdAt": "",
			"createdBy": {
				"id": "",
				"name": ""
			},
			"bindings": [
				{
					"appId": "",
					"appType": "",
					"openId": "",
					"unbound": true,
					"boundAt": "",
					"unboundAt": ""
				}
			],
			"nativeProvince": "",
			"ethnicity": {
				"code": "",
				"name": "",
				"system": ""
			},
			"occupation": {
				"code": "",
				"name": "",
				"system": ""
			},
			"patients": [
				{
					"organizationId": "",
					"recordNumber": ""
				}
			],
			"deleted": true
		}
	],
	"number": 0
}
```


## 查询客户修改日志


**接口地址**:`/api/v1/crm/customer/getOperatorLog`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId||query|true|string||
|operatorBeginDate||query|true|string||
|operatorEndDate||query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|TaskSnapshotOperateLogVo|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|customerId|客户id|string||
|operator|操作人|string||
|operateTime|操作时间|string||
|operateOrganizationName|操作门店|string||
|detailList|操作内容|array|OperateLogDetailBo|
|&emsp;&emsp;key|变更类型|string||
|&emsp;&emsp;before|变更前内容|string||
|&emsp;&emsp;after|变更后内容|string||


**响应示例**:
```javascript
[
	{
		"customerId": "",
		"operator": "",
		"operateTime": "",
		"operateOrganizationName": "",
		"detailList": [
			{
				"key": "",
				"before": "",
				"after": ""
			}
		]
	}
]
```


## 增值金调整


**接口地址**:`/api/v1/crm/customer/gift/add`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "accountId": "",
  "amount": 0,
  "note": "",
  "clinicId": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|addGiftReq|AddGiftReq|body|true|AddGiftReq|AddGiftReq|
|&emsp;&emsp;accountId|客户ID||true|string||
|&emsp;&emsp;amount|金额，单位元||true|number||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;clinicId|目标诊所ID,(说明:传值按当前所传门店操作处理；若不传值按客户归属门店操作处理；若客户也无归属门店则按总部操作处理)||false|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的客户的分群标签


**接口地址**:`/api/v1/crm/customer/group`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|客户ids|query|true|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取授权机构下的客户分群分组定义 - 分页


**接口地址**:`/api/v1/crm/customer/group-definition`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|name|组名|query|false|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCustomerGroupInfo|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CustomerGroupInfo|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;desc|描述|string||
|&emsp;&emsp;tags|标签|array|string|
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"desc": "",
			"tags": []
		}
	],
	"number": 0
}
```


## 修改客户会员等级


**接口地址**:`/api/v1/crm/customer/membershipLevel`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId||query|false|string||
|membershipLevel||query|false|string||
|note||query|false|string||
|obtainedDate||query|false|string||
|expireDate||query|false|string||
|give||query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取会员等级目录


**接口地址**:`/api/v1/crm/customer/membershipLevel/list`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|membershipLevelStatus||query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|MembershipDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|membershipLevelId|会员等级id|string||
|membershipLevel|会员等级编号|integer(int32)|integer(int32)|
|membershipLevelName|会员等级名称|string||
|membershipLevelStatus|会员等级状态,1:启用,2:禁用|integer(int32)|integer(int32)|


**响应示例**:
```javascript
[
	{
		"membershipLevelId": "",
		"membershipLevel": 0,
		"membershipLevelName": "",
		"membershipLevelStatus": 0
	}
]
```


## 获取授权机构下的客户合并数据


**接口地址**:`/api/v1/crm/customer/merge-log`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|source|源客户ID|query|false|string||
|target|目标客户ID|query|false|string||
|status|状态,可用值:pending,done|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageMergeLogDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|MergeLogDto|
|&emsp;&emsp;source|源客户ID|string||
|&emsp;&emsp;target|目标客户ID|string||
|&emsp;&emsp;mergedAt|合并时间|string(date-time)||
|&emsp;&emsp;status||Status|Status|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"source": "",
			"target": "",
			"mergedAt": "",
			"status": {
				"code": "",
				"name": "",
				"system": ""
			}
		}
	],
	"number": 0
}
```


## 根据客户Id获取授权机构下的客户数据


**接口地址**:`/api/v1/crm/customer/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|queryBinding|是否包含绑定关系|query|false|boolean||
|includeUnbound|是否包含已解绑的关系 - 仅包含绑定查询时生效|query|false|boolean||
|bindingType|指定绑定类型 - 仅包含绑定查询时生效,可用值:wx,minpro,h5,line,facebook|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CustomerDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|gender|性别（M/F）|string||
|email|Email|string||
|mobile|手机号 - 主号码|string||
|phones|手机号 - 列表（包含主号码）|array|PhoneDto|
|&emsp;&emsp;ownerType||OwnerType|OwnerType|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;number|号码|string||
|&emsp;&emsp;countryCode|国家代码， like +86|string||
|&emsp;&emsp;isPrimary|是否主号码 - 同时仅有一个主号码|boolean||
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|note|备注|string||
|birthday||Birthday|Birthday|
|&emsp;&emsp;year|年|integer(int32)||
|&emsp;&emsp;month|月|integer(int32)||
|&emsp;&emsp;day|日|integer(int32)||
|maritalStatus||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|idCard||IdCardDto|IdCardDto|
|&emsp;&emsp;type|类型,参考系统设置：字典-证件类型-idcard-categories|string||
|&emsp;&emsp;number|号码|string||
|idCards|证件列表|array|IdCardDto|
|&emsp;&emsp;type|类型,参考系统设置：字典-证件类型-idcard-categories|string||
|&emsp;&emsp;number|号码|string||
|membershipLevel||MembershipLevel|MembershipLevel|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|expireDate|会员入会时间|string(date-time)|string(date-time)|
|obtainedDate|会员失效时间|string(date-time)|string(date-time)|
|creditBalance|积分余额|integer(int64)|integer(int64)|
|isShared|是否共享客户|boolean||
|type||CustomerType|CustomerType|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|profileTags|动态标签|array|ProfileTag|
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|标签code|string||
|&emsp;&emsp;color|颜色值|string||
|classification||Classification|Classification|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|socialMediaAccounts|社交帐号|object||
|address||Address|Address|
|&emsp;&emsp;street|街道/门牌号|string||
|&emsp;&emsp;district|市区|string||
|&emsp;&emsp;city|城市|string||
|&emsp;&emsp;province|省/市|string||
|&emsp;&emsp;country|国家/地区|string||
|&emsp;&emsp;countryCode|国家/地区的英文代码，参照ISO标准国家中英文对照表填写|string||
|&emsp;&emsp;postalCode|邮编|string||
|consultant||Consultant|Consultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|consultAssistant||ConsultAssistant|ConsultAssistant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|beautician||Beautician|Beautician|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|doctor||Doctor|Doctor|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|serviceConsultant||ServiceConsultant|ServiceConsultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|customerService||CustomerService|CustomerService|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|developerAssistant||DeveloperAssistant|DeveloperAssistant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|referrer||ReferrerDto|ReferrerDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;channelCategory||ChannelCategory|ChannelCategory|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;channel||ChannelInfo|ChannelInfo|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;contact|联系人|string||
|&emsp;&emsp;&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|organization||Organization|Organization|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|createdAt|创建日期|string(date-time)|string(date-time)|
|createdBy||CreatedBy|CreatedBy|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|bindings|社交账号绑定关系|array|Binding|
|&emsp;&emsp;appId|绑定应用ID|string||
|&emsp;&emsp;appType|绑定应用类型|string||
|&emsp;&emsp;openId|openId|string||
|&emsp;&emsp;unbound|是否已解绑|boolean||
|&emsp;&emsp;boundAt|绑定日期|string(date-time)||
|&emsp;&emsp;unboundAt|解绑日期|string(date-time)||
|nativeProvince|籍贯（省份）|string||
|ethnicity||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|occupation||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|patients|病历号|array|CustomerPatient|
|&emsp;&emsp;organizationId|门店id|string||
|&emsp;&emsp;recordNumber|病历号|string||
|deleted|是否被作废|boolean||
|patientNumber|病历号|array|PatientNumber|
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;number|病历号|string||
|keyFigure||KeyFigureDto|KeyFigureDto|
|&emsp;&emsp;events|关键事件|array|Event|
|&emsp;&emsp;&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;when||string||
|tags|印象标签|array|TagDto|
|&emsp;&emsp;setId|标签组ID|string||
|&emsp;&emsp;value|标签|string||
|&emsp;&emsp;color|颜色|string||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"number": "",
	"gender": "",
	"email": "",
	"mobile": "",
	"phones": [
		{
			"ownerType": {
				"code": "",
				"name": "",
				"system": ""
			},
			"number": "",
			"countryCode": "",
			"isPrimary": true,
			"type": {
				"code": "",
				"name": "",
				"system": ""
			}
		}
	],
	"note": "",
	"birthday": {
		"year": 1987,
		"month": 6,
		"day": 18
	},
	"maritalStatus": {
		"code": "",
		"name": "",
		"system": ""
	},
	"idCard": {
		"type": "",
		"number": ""
	},
	"idCards": [
		{
			"type": "",
			"number": ""
		}
	],
	"membershipLevel": {
		"id": "",
		"name": ""
	},
	"expireDate": "",
	"obtainedDate": "",
	"creditBalance": 0,
	"isShared": true,
	"type": {
		"code": "",
		"name": "",
		"system": ""
	},
	"profileTags": [
		{
			"name": "",
			"code": "",
			"color": ""
		}
	],
	"classification": {
		"id": "",
		"name": ""
	},
	"socialMediaAccounts": {},
	"address": {
		"street": "",
		"district": "",
		"city": "",
		"province": "",
		"country": "",
		"countryCode": "",
		"postalCode": ""
	},
	"consultant": {
		"id": "",
		"name": ""
	},
	"consultAssistant": {
		"id": "",
		"name": ""
	},
	"beautician": {
		"id": "",
		"name": ""
	},
	"doctor": {
		"id": "",
		"name": ""
	},
	"serviceConsultant": {
		"id": "",
		"name": ""
	},
	"customerService": {
		"id": "",
		"name": ""
	},
	"developerAssistant": {
		"id": "",
		"name": ""
	},
	"referrer": {
		"id": "",
		"name": "",
		"channelCategory": {
			"id": "",
			"name": ""
		},
		"channel": {
			"id": "",
			"name": "",
			"contact": "",
			"phone": "",
			"note": ""
		}
	},
	"organization": {
		"id": "",
		"name": ""
	},
	"createdAt": "",
	"createdBy": {
		"id": "",
		"name": ""
	},
	"bindings": [
		{
			"appId": "",
			"appType": "",
			"openId": "",
			"unbound": true,
			"boundAt": "",
			"unboundAt": ""
		}
	],
	"nativeProvince": "",
	"ethnicity": {
		"code": "",
		"name": "",
		"system": ""
	},
	"occupation": {
		"code": "",
		"name": "",
		"system": ""
	},
	"patients": [
		{
			"organizationId": "",
			"recordNumber": ""
		}
	],
	"deleted": true,
	"patientNumber": [
		{
			"clinic": {
				"id": "",
				"name": ""
			},
			"number": ""
		}
	],
	"keyFigure": {
		"events": [
			{
				"type": {
					"code": "",
					"name": "",
					"system": ""
				},
				"when": ""
			}
		]
	},
	"tags": [
		{
			"setId": "",
			"value": "",
			"color": ""
		}
	]
}
```


## 在授权机构下修改客户


**接口地址**:`/api/v1/crm/customer/{id}`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "name": "",
  "organizationId": "",
  "consultantId": "",
  "beauticianId": "",
  "doctorId": "",
  "customerServiceId": "",
  "serviceConsultantId": "",
  "developerAssistantId": "",
  "consultAssistantId": "",
  "gender": "",
  "birthday": {
    "year": 1987,
    "month": 6,
    "day": 18
  },
  "maritalStatusCode": "",
  "mobile": "",
  "phones": [
    {
      "ownerTypeCode": "",
      "number": "",
      "countryCode": "+86",
      "isPrimary": true
    }
  ],
  "email": "",
  "qq": "",
  "weChat": "",
  "idCards": [
    {
      "categoryCode": "",
      "number": ""
    }
  ],
  "address": {
    "street": "",
    "district": "",
    "city": "",
    "province": "",
    "country": "",
    "countryCode": "",
    "postalCode": ""
  },
  "referrer": {
    "referrerId": "",
    "internal": true
  },
  "note": "",
  "isShared": true,
  "nativeProvince": "",
  "ethnicity": "",
  "occupation": "",
  "classificationId": {
    "present": true,
    "value": ""
  }
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|modifyCustomerParams|修改客户信息 - 不传值字段默认不改动|body|true|ModifyCustomerParams|ModifyCustomerParams|
|&emsp;&emsp;name|姓名||true|string||
|&emsp;&emsp;organizationId|归属组织ID||false|string||
|&emsp;&emsp;consultantId|归属咨询师ID||false|string||
|&emsp;&emsp;beauticianId|归属美容师ID||false|string||
|&emsp;&emsp;doctorId|归属医生ID||false|string||
|&emsp;&emsp;customerServiceId|归属客服ID||false|string||
|&emsp;&emsp;serviceConsultantId|归属电网咨询师ID||false|string||
|&emsp;&emsp;developerAssistantId|客户开发人||false|string||
|&emsp;&emsp;consultAssistantId|所属咨询助理ID||false|string||
|&emsp;&emsp;gender|性别,可用值:M,F||true|string||
|&emsp;&emsp;birthday|||false|Birthday|Birthday|
|&emsp;&emsp;&emsp;&emsp;year|年||false|integer||
|&emsp;&emsp;&emsp;&emsp;month|月||false|integer||
|&emsp;&emsp;&emsp;&emsp;day|日||false|integer||
|&emsp;&emsp;maritalStatusCode|婚姻状态 - 参考字典：婚姻状态||false|string||
|&emsp;&emsp;mobile|手机，本人主号码 - 同时仅允许一个主号码||false|string||
|&emsp;&emsp;phones|手机号列表 - 整体替换已有列表（包含主号码）||false|array|Phone|
|&emsp;&emsp;&emsp;&emsp;ownerTypeCode|手机号所有类型 - 本人，朋友，家人,可用值:self,friend,family||false|string||
|&emsp;&emsp;&emsp;&emsp;number|号码||true|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家代码||false|string||
|&emsp;&emsp;&emsp;&emsp;isPrimary|是否主号码 - 同时仅允许一个主号码||false|boolean||
|&emsp;&emsp;email|Email||false|string||
|&emsp;&emsp;qq|QQ||false|string||
|&emsp;&emsp;weChat|微信||false|string||
|&emsp;&emsp;idCards|证件 - 全集替换已有证件||false|array|IdCard|
|&emsp;&emsp;&emsp;&emsp;categoryCode|参考字典，证件类型 - idcard-categories||false|string||
|&emsp;&emsp;&emsp;&emsp;number|证件号||false|string||
|&emsp;&emsp;address|||false|Address|Address|
|&emsp;&emsp;&emsp;&emsp;street|街道/门牌号||false|string||
|&emsp;&emsp;&emsp;&emsp;district|市区||false|string||
|&emsp;&emsp;&emsp;&emsp;city|城市||true|string||
|&emsp;&emsp;&emsp;&emsp;province|省/市||false|string||
|&emsp;&emsp;&emsp;&emsp;country|国家/地区||false|string||
|&emsp;&emsp;&emsp;&emsp;countryCode|国家/地区的英文代码，参照ISO标准国家中英文对照表填写||false|string||
|&emsp;&emsp;&emsp;&emsp;postalCode|邮编||false|string||
|&emsp;&emsp;referrer|||false|ReferrerParam|ReferrerParam|
|&emsp;&emsp;&emsp;&emsp;referrerId|二级渠道ID||true|string||
|&emsp;&emsp;&emsp;&emsp;internal|是否内部渠道(referrerId是否会员ID)||false|boolean||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;isShared|是否共享客户（默认否）||false|boolean||
|&emsp;&emsp;nativeProvince|籍贯（省份）||false|string||
|&emsp;&emsp;ethnicity|民族（Code）- 参考字典代码:ethnicity（民族）||false|string||
|&emsp;&emsp;occupation|职业- 参考字典代码:occupation（职业）||false|string||
|&emsp;&emsp;classificationId|||false|OptionalValueString|OptionalValueString|
|&emsp;&emsp;&emsp;&emsp;present|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;value|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 在授权机构下删除客户


**接口地址**:`/api/v1/crm/customer/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据客户Id获取授权机构下的账户余额


**接口地址**:`/api/v1/crm/customer/{id}/account`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AccountDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|balance|可用余额|number||
|gift|可用增值金|number||
|credit|可用积分|integer(int64)|integer(int64)|
|prepaid|预定金|number||


**响应示例**:
```javascript
{
	"balance": 0,
	"gift": 0,
	"credit": 0,
	"prepaid": 0
}
```


## 根据客户ID绑定优惠券 - 返回账户未启用券列表


**接口地址**:`/api/v1/crm/customer/{id}/account/coupon`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "couponId": "",
  "fixedAmount": 0,
  "clinicId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|bindCouponParams|BindCouponParams|body|true|BindCouponParams|BindCouponParams|
|&emsp;&emsp;couponId|券种ID||true|string||
|&emsp;&emsp;fixedAmount|指定券面金额 - optional,不定额券指定券面金额||false|number||
|&emsp;&emsp;clinicId|目标诊所ID,(说明:传值按当前所传门店操作处理；若不传值按客户归属门店操作处理；若客户也无归属门店则按总部操作处理)||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|AccountCouponDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|券权益ID|string||
|ownerStoreId|当前归属门店|string||
|type|券类型|string||
|multiplePayment|单次/多次使用限制，默认false单次使用|boolean||
|number|券权益编号|string||
|invitationRightsFlag|是否初始请客权益|boolean||
|couponId|券定义ID|string||
|amount|券余额|number||
|name|名称|string||
|expireDate|过期时间|string(date-time)|string(date-time)|
|gotTime|获取时间|string(date-time)|string(date-time)|
|expired|已过期|boolean||
|restriction|使用范围(空则无限制)|array|CouponRestriction|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型(项目、商品、项目类别、商品类别、项目标签、商品标签、促销标签、卡项标签),可用值:service,product,serviceCategory,productCategory,serviceTag,productTag,promotionTag,cardTag|string||
|status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"ownerStoreId": "",
		"type": "",
		"multiplePayment": true,
		"number": "",
		"invitationRightsFlag": true,
		"couponId": "",
		"amount": 0,
		"name": "",
		"expireDate": "",
		"gotTime": "",
		"expired": true,
		"restriction": [
			{
				"id": "",
				"name": "",
				"type": ""
			}
		],
		"status": {
			"code": "",
			"name": ""
		}
	}
]
```


## 根据客户ID查询券余


**接口地址**:`/api/v1/crm/customer/{id}/account/coupon/_list`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|status|状态,可用值:unused,used,overdue,disabled|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AccountCouponDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|券权益ID|string||
|ownerStoreId|当前归属门店|string||
|type|券类型|string||
|multiplePayment|单次/多次使用限制，默认false单次使用|boolean||
|number|券权益编号|string||
|invitationRightsFlag|是否初始请客权益|boolean||
|couponId|券定义ID|string||
|amount|券余额|number||
|name|名称|string||
|expireDate|过期时间|string(date-time)|string(date-time)|
|gotTime|获取时间|string(date-time)|string(date-time)|
|expired|已过期|boolean||
|restriction|使用范围(空则无限制)|array|CouponRestriction|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型(项目、商品、项目类别、商品类别、项目标签、商品标签、促销标签、卡项标签),可用值:service,product,serviceCategory,productCategory,serviceTag,productTag,promotionTag,cardTag|string||
|status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"ownerStoreId": "",
		"type": "",
		"multiplePayment": true,
		"number": "",
		"invitationRightsFlag": true,
		"couponId": "",
		"amount": 0,
		"name": "",
		"expireDate": "",
		"gotTime": "",
		"expired": true,
		"restriction": [
			{
				"id": "",
				"name": "",
				"type": ""
			}
		],
		"status": {
			"code": "",
			"name": ""
		}
	}
]
```


## 根据客户ID解绑优惠券 - 返回账户未启用券列表


**接口地址**:`/api/v1/crm/customer/{id}/account/coupon/_unbind`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "couponItemId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|unbindCouponParams|UnbindCouponParams|body|true|UnbindCouponParams|UnbindCouponParams|
|&emsp;&emsp;couponItemId|券权益ID/券实体ID||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|AccountCouponDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|券权益ID|string||
|ownerStoreId|当前归属门店|string||
|type|券类型|string||
|multiplePayment|单次/多次使用限制，默认false单次使用|boolean||
|number|券权益编号|string||
|invitationRightsFlag|是否初始请客权益|boolean||
|couponId|券定义ID|string||
|amount|券余额|number||
|name|名称|string||
|expireDate|过期时间|string(date-time)|string(date-time)|
|gotTime|获取时间|string(date-time)|string(date-time)|
|expired|已过期|boolean||
|restriction|使用范围(空则无限制)|array|CouponRestriction|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型(项目、商品、项目类别、商品类别、项目标签、商品标签、促销标签、卡项标签),可用值:service,product,serviceCategory,productCategory,serviceTag,productTag,promotionTag,cardTag|string||
|status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"ownerStoreId": "",
		"type": "",
		"multiplePayment": true,
		"number": "",
		"invitationRightsFlag": true,
		"couponId": "",
		"amount": 0,
		"name": "",
		"expireDate": "",
		"gotTime": "",
		"expired": true,
		"restriction": [
			{
				"id": "",
				"name": "",
				"type": ""
			}
		],
		"status": {
			"code": "",
			"name": ""
		}
	}
]
```


## 根据客户ID进行积分增减操作


**接口地址**:`/api/v1/crm/customer/{id}/account/credit`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "amount": 0,
  "externalOrderNo": "",
  "note": "",
  "clinicId": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|changeCreditParams|ChangeCreditParams|body|true|ChangeCreditParams|ChangeCreditParams|
|&emsp;&emsp;amount|增减积分点数 - 正负表示增减||false|integer(int32)||
|&emsp;&emsp;externalOrderNo|外部交易单号||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;clinicId|目标诊所ID,(说明:传值按当前所传门店操作处理；若不传值按客户归属门店操作处理；若客户也无归属门店则按总部操作处理)||false|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据客户Id获取授权机构下的账户余额变动数据


**接口地址**:`/api/v1/crm/customer/{id}/account/journal`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|clinicId||query|false|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageAccountJournalDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|AccountJournalDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;accountType||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;income|收入数额(元/积分点)|number||
|&emsp;&emsp;outcome|支出数额(元/积分点)|number||
|&emsp;&emsp;balance|变动后数额(元/积分点)|number||
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;createdAt|变动时间|string(date-time)||
|&emsp;&emsp;operator||Operator|Operator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;note|备注|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"accountType": {
				"code": "",
				"name": "",
				"system": ""
			},
			"income": 0,
			"outcome": 0,
			"balance": 0,
			"type": {
				"code": "",
				"name": "",
				"system": ""
			},
			"createdAt": "",
			"operator": {
				"id": "",
				"name": ""
			},
			"note": ""
		}
	],
	"number": 0
}
```


## 获取授权机构下根据客户Id获取客户当日到访类型


**接口地址**:`/api/v1/crm/customer/{id}/careClass`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CareClassDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|客户类型code|string||
|description|客户类型描述|string||


**响应示例**:
```javascript
[
	{
		"code": "",
		"description": ""
	}
]
```


## 根据客户ID获取客户汇总消费金额


**接口地址**:`/api/v1/crm/customer/{id}/expense/summary`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CustomerSummaryDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|customerId|会员ID|string||
|customerName|会员姓名|string||
|totalExpense|累计消费|number||
|totalCheckout|累计现款支付|number||
|executionMoney|累计划扣|number||


**响应示例**:
```javascript
{
	"customerId": "",
	"customerName": "",
	"totalExpense": 0,
	"totalCheckout": 0,
	"executionMoney": 0
}
```


## 在授权机构下根据客户ID添加自定义标签


**接口地址**:`/api/v1/crm/customer/{id}/tag`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "value": "",
  "setId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|addCustomerTagParam|AddCustomerTagParam|body|true|AddCustomerTagParam|AddCustomerTagParam|
|&emsp;&emsp;value|标签值||true|string||
|&emsp;&emsp;setId|标签组ID，为空的话，该标签为自由标签，非空为预设标签||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 在授权机构下根据客户ID删除标签


**接口地址**:`/api/v1/crm/customer/{id}/tag`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "value": "",
  "setId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|deleteCustomerTagParam|DeleteCustomerTagParam|body|true|DeleteCustomerTagParam|DeleteCustomerTagParam|
|&emsp;&emsp;value|标签值||true|string||
|&emsp;&emsp;setId|标签组ID，为空的话，该标签为自由标签，非空为预设标签||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据客户Id获取授权机构下的客户简单数据


**接口地址**:`/api/v1/crm/customerDetail`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId||query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CustomerSimpleDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|gender|性别（M/F）|string||
|mobile|手机号 - 主号码|string||
|birthday||Birthday|Birthday|
|&emsp;&emsp;year|年|integer(int32)||
|&emsp;&emsp;month|月|integer(int32)||
|&emsp;&emsp;day|日|integer(int32)||
|referrer||ReferrerDto|ReferrerDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;channelCategory||ChannelCategory|ChannelCategory|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;channel||ChannelInfo|ChannelInfo|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;contact|联系人|string||
|&emsp;&emsp;&emsp;&emsp;phone|手机号|string||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|createdAt|创建日期|string(date-time)|string(date-time)|
|deleted|是否被作废|boolean||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"number": "",
	"gender": "",
	"mobile": "",
	"birthday": {
		"year": 1987,
		"month": 6,
		"day": 18
	},
	"referrer": {
		"id": "",
		"name": "",
		"channelCategory": {
			"id": "",
			"name": ""
		},
		"channel": {
			"id": "",
			"name": "",
			"contact": "",
			"phone": "",
			"note": ""
		}
	},
	"createdAt": "",
	"deleted": true
}
```


## 获取授权机构下的客户列表数据


**接口地址**:`/api/v1/crm/customerList`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|birthday|生日|query|false|Birthday|Birthday|
|&emsp;&emsp;year|年||false|integer(int32)||
|&emsp;&emsp;month|月||false|integer(int32)||
|&emsp;&emsp;day|日||false|integer(int32)||
|keyword|关键字: 姓名/手机号/会员号/病历号/证件号|query|false|string||
|groupIds|客户分群分组Id - 列表|query|false|array|string|
|secondLevelChannelId|二级渠道Id|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCustomerSimpleListDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CustomerSimpleListDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;gender|性别（M/F）|string||
|&emsp;&emsp;mobile|手机号|string||
|&emsp;&emsp;deleted|是否被作废|boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"number": "",
			"gender": "",
			"mobile": "",
			"deleted": true
		}
	],
	"number": 0
}
```


# 06. 销售财务数据


## 储值金退款


**接口地址**:`/api/v1/account-item/balance/refund`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "customerId": "",
  "clinicId": "",
  "operatorId": "",
  "bankPayee": "",
  "bankAccountNumber": "",
  "bankName": "",
  "bankBranchName": "",
  "amount": 0,
  "note": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createAccountRefundParams|账户退款申请参数|body|true|CreateAccountRefundParams|CreateAccountRefundParams|
|&emsp;&emsp;customerId|客户Id||true|string||
|&emsp;&emsp;clinicId|退款操作门店Id||true|string||
|&emsp;&emsp;operatorId|创建人员工ID||true|string||
|&emsp;&emsp;bankPayee|银行卡-收款方||true|string||
|&emsp;&emsp;bankAccountNumber|银行卡-账户号||true|string||
|&emsp;&emsp;bankName|银行卡-开户行||true|string||
|&emsp;&emsp;bankBranchName|银行卡-开户支行||true|string||
|&emsp;&emsp;amount|退款金额(单位:元)||true|number||
|&emsp;&emsp;note|备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 查询权益 - 按ID查询卡项权益详情


**接口地址**:`/api/v1/account-item/card/detail`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|卡项权益ID|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CardItemDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|权益ID|string||
|amount|成交金额|number||
|remainAmount|剩余金额|number||
|availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|product||IdNameDto|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|orderId|订单ID|string||
|orderNumber|订单NO.|string||
|creator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|createTime|创建时间(格式：yyyy-MM-dd HH:mm:ss)|string||
|bundles|卡项组（含已兑换条目）|array|BundleItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;type|兑换组规则类型(固定组：package, N先M：combination, 点卡：point),可用值:package,combination,point|string||
|&emsp;&emsp;redeemOptions|卡项组兑换选项|array|RedeemOptionDto|
|&emsp;&emsp;&emsp;&emsp;index|索引|string||
|&emsp;&emsp;&emsp;&emsp;type|兑换实体类型|string||
|&emsp;&emsp;&emsp;&emsp;itemId|对应范围实体ID|string||
|&emsp;&emsp;&emsp;&emsp;itemName|对应范围实体名称|string||
|&emsp;&emsp;&emsp;&emsp;activated|是否激活使用|boolean||
|&emsp;&emsp;&emsp;&emsp;totalQty|总数|integer||
|&emsp;&emsp;&emsp;&emsp;remainQty|剩余数量|integer||
|&emsp;&emsp;&emsp;&emsp;avgDeduction|平均兑换价值-点数 - 仅点卡|number||
|&emsp;&emsp;&emsp;&emsp;subItems|已兑换品项|array|BundleSubItemDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型,可用值:service,product|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;product||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|成交数量|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;remainQuantity|剩余数量（扣除已使用/退款等，含锁定）|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createTime|确认品项时间(格式：yyyy-MM-dd HH:mm:ss)|string||
|&emsp;&emsp;thresholdTotalQty|组阈值 - 点卡总点数/N选M可选组数|number||
|&emsp;&emsp;thresholdRemainQty|组阈值 - 剩余点卡总点数/剩余N选M可选组数|number||
|depositMoney||CardMonetaryItemDto|CardMonetaryItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;type|权益类型(deposit:储值金,gift:增值金,coupon:代金券),可用值:deposit,gift,coupon|string||
|&emsp;&emsp;usageScopes|使用范围/打折范围&折扣|array|UsageScopeItemDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,serviceCategory,ProductCategory,serviceTag,productTag|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;discountPercent|折扣 - 仅打折权益|integer||
|giftMoney||CardMonetaryItemDto|CardMonetaryItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;type|权益类型(deposit:储值金,gift:增值金,coupon:代金券),可用值:deposit,gift,coupon|string||
|&emsp;&emsp;usageScopes|使用范围/打折范围&折扣|array|UsageScopeItemDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,serviceCategory,ProductCategory,serviceTag,productTag|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;discountPercent|折扣 - 仅打折权益|integer||
|discountItem||CardMonetaryItemDto|CardMonetaryItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;type|权益类型(deposit:储值金,gift:增值金,coupon:代金券),可用值:deposit,gift,coupon|string||
|&emsp;&emsp;usageScopes|使用范围/打折范围&折扣|array|UsageScopeItemDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,serviceCategory,ProductCategory,serviceTag,productTag|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;discountPercent|折扣 - 仅打折权益|integer||
|couponItems|赠券权益|array|CardMonetaryItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;type|权益类型(deposit:储值金,gift:增值金,coupon:代金券),可用值:deposit,gift,coupon|string||
|&emsp;&emsp;usageScopes|使用范围/打折范围&折扣|array|UsageScopeItemDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,serviceCategory,ProductCategory,serviceTag,productTag|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;discountPercent|折扣 - 仅打折权益|integer||


**响应示例**:
```javascript
{
	"id": "",
	"amount": 0,
	"remainAmount": 0,
	"availableDate": "",
	"expireDate": "",
	"status": "",
	"product": {
		"id": "",
		"name": ""
	},
	"orderId": "",
	"orderNumber": "",
	"creator": {
		"id": "",
		"name": ""
	},
	"createTime": "",
	"bundles": [
		{
			"id": "",
			"amount": 0,
			"remainAmount": 0,
			"availableDate": "",
			"expireDate": "",
			"status": "",
			"type": "",
			"redeemOptions": [
				{
					"index": "",
					"type": "",
					"itemId": "",
					"itemName": "",
					"activated": true,
					"totalQty": 0,
					"remainQty": 0,
					"avgDeduction": 0,
					"subItems": [
						{
							"id": "",
							"amount": 0,
							"remainAmount": 0,
							"availableDate": "",
							"expireDate": "",
							"status": "",
							"type": "",
							"product": {
								"id": "",
								"name": ""
							},
							"quantity": 0,
							"remainQuantity": 0,
							"creator": {
								"id": "",
								"name": ""
							},
							"createTime": ""
						}
					]
				}
			],
			"thresholdTotalQty": 0,
			"thresholdRemainQty": 0
		}
	],
	"depositMoney": {
		"id": "",
		"amount": 0,
		"remainAmount": 0,
		"availableDate": "",
		"expireDate": "",
		"status": "",
		"type": "",
		"usageScopes": [
			{
				"id": "",
				"type": "",
				"name": "",
				"discountPercent": 0
			}
		]
	},
	"giftMoney": {
		"id": "",
		"amount": 0,
		"remainAmount": 0,
		"availableDate": "",
		"expireDate": "",
		"status": "",
		"type": "",
		"usageScopes": [
			{
				"id": "",
				"type": "",
				"name": "",
				"discountPercent": 0
			}
		]
	},
	"discountItem": {
		"id": "",
		"amount": 0,
		"remainAmount": 0,
		"availableDate": "",
		"expireDate": "",
		"status": "",
		"type": "",
		"usageScopes": [
			{
				"id": "",
				"type": "",
				"name": "",
				"discountPercent": 0
			}
		]
	},
	"couponItems": [
		{
			"id": "",
			"amount": 0,
			"remainAmount": 0,
			"availableDate": "",
			"expireDate": "",
			"status": "",
			"type": "",
			"usageScopes": [
				{
					"id": "",
					"type": "",
					"name": "",
					"discountPercent": 0
				}
			]
		}
	]
}
```


## 查询权益 - 按客户ID查询可用卡项


**接口地址**:`/api/v1/account-item/card/page`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId|客户ID|query|true|string||
|clinicId|门点ID(不填则默认为登录门店资产共享组)|query|false|string||
|orderId|订单ID|query|false|string||
|status|状态,可用值:all,pending,effective,expired,transferred|query|false|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCardItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CardItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;availableDate|生效日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;expireDate|到期日期(格式：yyyy-MM-dd) - 可能为空|string||
|&emsp;&emsp;status|状态 - pending待生效,effective生效中,completed已完成,transferred已转赠,expired已过期,invalid已失效,可用值:pending,effective,completed,transferred,expired,invalid|string||
|&emsp;&emsp;product||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;orderNumber|订单NO.|string||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createTime|创建时间(格式：yyyy-MM-dd HH:mm:ss)|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"amount": 0,
			"remainAmount": 0,
			"availableDate": "",
			"expireDate": "",
			"status": "",
			"product": {
				"id": "",
				"name": ""
			},
			"orderId": "",
			"orderNumber": "",
			"creator": {
				"id": "",
				"name": ""
			},
			"createTime": ""
		}
	],
	"number": 0
}
```


## 卡项确认品项


**接口地址**:`/api/v1/account-item/card/redeem`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "customerId": "",
  "clinicId": "",
  "operatorId": "",
  "cardId": "",
  "bundleId": "",
  "redeemItems": [
    {
      "redeemOptionIndex": "",
      "quantity": 0,
      "itemId": "",
      "type": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bundleItemRedeemParam|卡项确认品项参数|body|true|BundleItemRedeemParam|BundleItemRedeemParam|
|&emsp;&emsp;customerId|客户Id||true|string||
|&emsp;&emsp;clinicId|操作门店Id||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||true|string||
|&emsp;&emsp;cardId|卡权益ID||true|string||
|&emsp;&emsp;bundleId|兑换组ID||true|string||
|&emsp;&emsp;redeemItems|兑换条目||true|array|RedeemItemParam|
|&emsp;&emsp;&emsp;&emsp;redeemOptionIndex|兑换选项索引||true|string||
|&emsp;&emsp;&emsp;&emsp;quantity|兑换数量||true|integer||
|&emsp;&emsp;&emsp;&emsp;itemId|兑换目标品项ID||true|string||
|&emsp;&emsp;&emsp;&emsp;type|兑换条目类型,可用值:service,product||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AccProductItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|权益ID|string||
|type|权益类型|string||
|store||Clinic|Clinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|rootId|权益RootId|string||
|envelopType|营销分类类型,可用值:card,promotion,combination|string||
|envelopProductId|营销分类ID|string||
|envelopProductName|营销分类名称|string||
|product||IdNameDto|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|orderId|订单ID|string||
|orderNumber|订单NO.|string||
|quantity|成交数量|integer(int64)|integer(int64)|
|remainQuantity|剩余数量（扣除已使用/退款等，含锁定）|integer(int64)|integer(int64)|
|amount|成交金额|number||
|remainAmount|剩余金额|number||
|creator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|createTime|确认品项时间|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"type": "",
		"store": {
			"id": "",
			"name": ""
		},
		"customer": {
			"id": "",
			"name": ""
		},
		"rootId": "",
		"envelopType": "",
		"envelopProductId": "",
		"envelopProductName": "",
		"product": {
			"id": "",
			"name": ""
		},
		"orderId": "",
		"orderNumber": "",
		"quantity": 0,
		"remainQuantity": 0,
		"amount": 0,
		"remainAmount": 0,
		"creator": {
			"id": "",
			"name": ""
		},
		"createTime": ""
	}
]
```


## 卡项作废确认品项


**接口地址**:`/api/v1/account-item/card/redeem-revoke`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "operatorId": "",
  "cardId": "",
  "redeemItemIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bundleItemRedeemRevokeParam|卡项作废确认品项参数|body|true|BundleItemRedeemRevokeParam|BundleItemRedeemRevokeParam|
|&emsp;&emsp;clinicId|操作门店Id||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||true|string||
|&emsp;&emsp;cardId|卡权益ID||true|string||
|&emsp;&emsp;redeemItemIds|品项权益ID||true|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询权益 - 支持查询卡项已兑换的单品权益


**接口地址**:`/api/v1/account-item/card/redeemed/page`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|customerId|客户ID - 客户ID/rootId/日期至少填一个|query|false|string||
|storeId|门店ID|query|false|string||
|rootId|权益rootId|query|false|string||
|includeCompleted|是否包含已耗尽，默认否|query|false|boolean||
|start|开始日期 - 包含该日期（无客户ID条件时，时间跨度不允许超过一天），如 yyyy-MM-dd|query|false|string(date)||
|end|结束日期 - 包含该日期，如 yyyy-MM-dd|query|false|string(date)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageAccProductItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|AccProductItemDto|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;type|权益类型|string||
|&emsp;&emsp;store||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;rootId|权益RootId|string||
|&emsp;&emsp;envelopType|营销分类类型,可用值:card,promotion,combination|string||
|&emsp;&emsp;envelopProductId|营销分类ID|string||
|&emsp;&emsp;envelopProductName|营销分类名称|string||
|&emsp;&emsp;product||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;orderNumber|订单NO.|string||
|&emsp;&emsp;quantity|成交数量|integer(int64)||
|&emsp;&emsp;remainQuantity|剩余数量（扣除已使用/退款等，含锁定）|integer(int64)||
|&emsp;&emsp;amount|成交金额|number||
|&emsp;&emsp;remainAmount|剩余金额|number||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createTime|确认品项时间|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"type": "",
			"store": {
				"id": "",
				"name": ""
			},
			"customer": {
				"id": "",
				"name": ""
			},
			"rootId": "",
			"envelopType": "",
			"envelopProductId": "",
			"envelopProductName": "",
			"product": {
				"id": "",
				"name": ""
			},
			"orderId": "",
			"orderNumber": "",
			"quantity": 0,
			"remainQuantity": 0,
			"amount": 0,
			"remainAmount": 0,
			"creator": {
				"id": "",
				"name": ""
			},
			"createTime": ""
		}
	],
	"number": 0
}
```


## 查询权益 - 按ID查询单品权益


**接口地址**:`/api/v1/account-item/product-item/byId`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|权益ID|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AccProductItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|权益ID|string||
|type|权益类型|string||
|store||Clinic|Clinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|rootId|权益RootId|string||
|envelopType|营销分类类型,可用值:card,promotion,combination|string||
|envelopProductId|营销分类ID|string||
|envelopProductName|营销分类名称|string||
|product||IdNameDto|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|orderId|订单ID|string||
|orderNumber|订单NO.|string||
|quantity|成交数量|integer(int64)|integer(int64)|
|remainQuantity|剩余数量（扣除已使用/退款等，含锁定）|integer(int64)|integer(int64)|
|amount|成交金额|number||
|remainAmount|剩余金额|number||
|creator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|createTime|确认品项时间|string||


**响应示例**:
```javascript
{
	"id": "",
	"type": "",
	"store": {
		"id": "",
		"name": ""
	},
	"customer": {
		"id": "",
		"name": ""
	},
	"rootId": "",
	"envelopType": "",
	"envelopProductId": "",
	"envelopProductName": "",
	"product": {
		"id": "",
		"name": ""
	},
	"orderId": "",
	"orderNumber": "",
	"quantity": 0,
	"remainQuantity": 0,
	"amount": 0,
	"remainAmount": 0,
	"creator": {
		"id": "",
		"name": ""
	},
	"createTime": ""
}
```


## 增值金余额调整


**接口地址**:`/api/v1/account-item/reward/adjust`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "customerId": "",
  "clinicId": "",
  "operatorId": "",
  "amount": 0,
  "externalOrderNo": "",
  "note": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|balanceAdjustParams|储值金/增值金余额调整参数|body|true|BalanceAdjustParams|BalanceAdjustParams|
|&emsp;&emsp;customerId|客户Id||true|string||
|&emsp;&emsp;clinicId|操作门店Id||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||true|string||
|&emsp;&emsp;amount|金额(单位:元)||true|number||
|&emsp;&emsp;externalOrderNo|外部单据/流水号(只能用一次)||true|string||
|&emsp;&emsp;note|备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AccountJournalEntryInfo|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||
|debit||AmountTypeUnitLongCodedValueCodedValue|AmountTypeUnitLongCodedValueCodedValue|
|&emsp;&emsp;amount||integer(int64)||
|&emsp;&emsp;type||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|&emsp;&emsp;unit||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|credit||AmountTypeUnitLongCodedValueCodedValue|AmountTypeUnitLongCodedValueCodedValue|
|&emsp;&emsp;amount||integer(int64)||
|&emsp;&emsp;type||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|&emsp;&emsp;unit||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|balance||AmountTypeUnitLongCodedValueCodedValue|AmountTypeUnitLongCodedValueCodedValue|
|&emsp;&emsp;amount||integer(int64)||
|&emsp;&emsp;type||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|&emsp;&emsp;unit||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|description||CodableValue|CodableValue|
|&emsp;&emsp;codes||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|&emsp;&emsp;text||string||
|&emsp;&emsp;empty||boolean||
|note||string||
|timestamp||string(date-time)|string(date-time)|
|type||CodedValue|CodedValue|
|&emsp;&emsp;displayText||string||
|&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;family||string||
|&emsp;&emsp;version||string||
|&emsp;&emsp;enable||boolean||
|&emsp;&emsp;order||integer(int32)||
|&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;default||boolean||
|&emsp;&emsp;codeValue||string||
|creator||IdNameStringString|IdNameStringString|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|transactionId||string||
|servicesName||string||
|orderId||string||
|store||IdNameStringString|IdNameStringString|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||


**响应示例**:
```javascript
{
	"id": "",
	"debit": {
		"amount": 0,
		"type": {
			"displayText": "",
			"abbreviationText": "",
			"family": "",
			"version": "",
			"enable": true,
			"order": 0,
			"relevance": [
				{
					"displayText": "",
					"abbreviationText": "",
					"family": "",
					"version": "",
					"enable": true,
					"order": 0,
					"relevance": [
						{}
					],
					"systemCfg": true,
					"vocabularyName": "",
					"default": true,
					"codeValue": ""
				}
			],
			"systemCfg": true,
			"vocabularyName": "",
			"default": true,
			"codeValue": ""
		},
		"unit": {}
	},
	"credit": {
		"amount": 0,
		"type": {
			"displayText": "",
			"abbreviationText": "",
			"family": "",
			"version": "",
			"enable": true,
			"order": 0,
			"relevance": [
				{
					"displayText": "",
					"abbreviationText": "",
					"family": "",
					"version": "",
					"enable": true,
					"order": 0,
					"relevance": [
						{}
					],
					"systemCfg": true,
					"vocabularyName": "",
					"default": true,
					"codeValue": ""
				}
			],
			"systemCfg": true,
			"vocabularyName": "",
			"default": true,
			"codeValue": ""
		},
		"unit": {}
	},
	"balance": {
		"amount": 0,
		"type": {
			"displayText": "",
			"abbreviationText": "",
			"family": "",
			"version": "",
			"enable": true,
			"order": 0,
			"relevance": [
				{
					"displayText": "",
					"abbreviationText": "",
					"family": "",
					"version": "",
					"enable": true,
					"order": 0,
					"relevance": [
						{}
					],
					"systemCfg": true,
					"vocabularyName": "",
					"default": true,
					"codeValue": ""
				}
			],
			"systemCfg": true,
			"vocabularyName": "",
			"default": true,
			"codeValue": ""
		},
		"unit": {}
	},
	"description": {
		"codes": [
			{
				"displayText": "",
				"abbreviationText": "",
				"family": "",
				"version": "",
				"enable": true,
				"order": 0,
				"relevance": [
					{
						"displayText": "",
						"abbreviationText": "",
						"family": "",
						"version": "",
						"enable": true,
						"order": 0,
						"relevance": [
							{}
						],
						"systemCfg": true,
						"vocabularyName": "",
						"default": true,
						"codeValue": ""
					}
				],
				"systemCfg": true,
				"vocabularyName": "",
				"default": true,
				"codeValue": ""
			}
		],
		"text": "",
		"empty": true
	},
	"note": "",
	"timestamp": "",
	"type": {
		"displayText": "",
		"abbreviationText": "",
		"family": "",
		"version": "",
		"enable": true,
		"order": 0,
		"relevance": [
			{
				"displayText": "",
				"abbreviationText": "",
				"family": "",
				"version": "",
				"enable": true,
				"order": 0,
				"relevance": [
					{}
				],
				"systemCfg": true,
				"vocabularyName": "",
				"default": true,
				"codeValue": ""
			}
		],
		"systemCfg": true,
		"vocabularyName": "",
		"default": true,
		"codeValue": ""
	},
	"creator": {
		"id": "",
		"name": ""
	},
	"transactionId": "",
	"servicesName": "",
	"orderId": "",
	"store": {
		"id": "",
		"name": ""
	}
}
```


## 操作客户转疗（自动同意转疗）


**接口地址**:`/api/v1/billing/customer/transfer/product-item`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "accountItemIds": [],
  "toClinicId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|transferCustomerProductItemReqParams|TransferCustomerProductItemReqParams|body|true|TransferCustomerProductItemReqParams|TransferCustomerProductItemReqParams|
|&emsp;&emsp;accountItemIds|要转疗的权益ID||true|array|string|
|&emsp;&emsp;toClinicId|要转入的门店ID||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取客户美学评估单特征


**接口地址**:`/api/v1/billing/customer/{id}/esthetics/estimate-item`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|organizationIdList|门店ID|query|true|array|string|
|estimateId|评估单Id|query|false|string||
|estimateDateStart|日期开始|query|false|string(date-time)||
|estimateDateEnd|日期结束|query|false|string(date-time)||
|statusList|评估单状态 待跟进(wait-follow), 跟进中(following), 已开单(order), 已收款(paid)|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|QueryEstimateListDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|estimateId|评估单ID|string||
|estimateNumber|评估单号|string||
|customerId|客户ID|string||
|customerName|客户名|string||
|estimateDate|评估单创建时间|string(date-time)|string(date-time)|
|estimateOrganizationId|评估单门店ID|string||
|estimateOrganizationName|评估单创建门店名|string||
|status|评估单状态 待跟进(wait-follow), 跟进中(following), 已开单(order), 已收款(paid)|string||
|enabled|是否有效|boolean||
|estimateItemList|评估单条目|array|EstimateItem|
|&emsp;&emsp;characteristicId|美学特征ID|string||
|&emsp;&emsp;characteristicName|美学特征名称|string||
|&emsp;&emsp;levelSerialNumber|美学特征等级序号|integer(int32)||
|&emsp;&emsp;levelCustomName|美学特征等级名称|string||


**响应示例**:
```javascript
[
	{
		"estimateId": "",
		"estimateNumber": "",
		"customerId": "",
		"customerName": "",
		"estimateDate": "",
		"estimateOrganizationId": "",
		"estimateOrganizationName": "",
		"status": "",
		"enabled": true,
		"estimateItemList": [
			{
				"characteristicId": "",
				"characteristicName": "",
				"levelSerialNumber": 0,
				"levelCustomName": ""
			}
		]
	}
]
```


## 根据客户Id获取授权机构下的客户项目执行数据


**接口地址**:`/api/v1/billing/customer/{id}/execution-record`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageExecutionRecordDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ExecutionRecordDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|单号|string||
|&emsp;&emsp;itemId|可执行条目ID|string||
|&emsp;&emsp;orderId|销售单ID|string||
|&emsp;&emsp;stepList|操作步骤|array|ExecutionStepDTO|
|&emsp;&emsp;&emsp;&emsp;stepId|步骤id|string||
|&emsp;&emsp;&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;&emsp;&emsp;stepTypeCode|步骤类型code -1:操作前准备，0：操作项目,1:操作后护理|integer||
|&emsp;&emsp;&emsp;&emsp;stepTypeName|步骤类型|string||
|&emsp;&emsp;bodyPartName|执行部位名称|string||
|&emsp;&emsp;bodyPartId|执行部位ID|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||ExecutionClinic|ExecutionClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;serviceConsultant||ExecutionConsultant|ExecutionConsultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;executedDate|执行时间|string(date-time)||
|&emsp;&emsp;service||Service|Service|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;spec||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;quantity|执行数量|integer(int32)||
|&emsp;&emsp;amount|执行金额|number||
|&emsp;&emsp;arrearsAmount|当前欠费金额|number||
|&emsp;&emsp;participants|参与人|array|ParticipantDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;durationInMin|操作时长|integer||
|&emsp;&emsp;&emsp;&emsp;stepId|步骤id|string||
|&emsp;&emsp;&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;&emsp;&emsp;operationFeeTotal|操作费|number||
|&emsp;&emsp;deviceDtoList|治疗参数|array|DeviceDto|
|&emsp;&emsp;&emsp;&emsp;deviceName|设备|string||
|&emsp;&emsp;&emsp;&emsp;parameterName|参数名|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;reference|参考值|string||
|&emsp;&emsp;&emsp;&emsp;actual|实际值|string||
|&emsp;&emsp;costItems|耗用品|array|ExecutionCostItemDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次号|string||
|&emsp;&emsp;&emsp;&emsp;expirationDate|有效期|string||
|&emsp;&emsp;&emsp;&emsp;warehouse||Warehouse|Warehouse|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;cancelled|已作废|boolean||
|&emsp;&emsp;revoked|已撤回|boolean||
|&emsp;&emsp;refunded|已退款|boolean||
|&emsp;&emsp;salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;salesConsultant||SalesConsultant|SalesConsultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;salesDate|销售时间|string(date-time)||
|&emsp;&emsp;cancelledDate|作废/撤回时间|string(date-time)||
|&emsp;&emsp;refundedDate|退款时间|string(date-time)||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;remainNumber|权益剩余执行数量（划扣后）|integer(int32)||
|&emsp;&emsp;courseNumber|权益总次数|integer(int32)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"itemId": "",
			"orderId": "",
			"stepList": [
				{
					"stepId": "",
					"stepName": "",
					"stepTypeCode": 0,
					"stepTypeName": ""
				}
			],
			"bodyPartName": "",
			"bodyPartId": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"serviceConsultant": {
				"id": "",
				"name": ""
			},
			"executedDate": "",
			"service": {
				"id": "",
				"name": "",
				"spec": "",
				"unit": ""
			},
			"quantity": 0,
			"amount": 0,
			"arrearsAmount": 0,
			"participants": [
				{
					"id": "",
					"name": "",
					"role": {
						"code": "",
						"name": "",
						"system": ""
					},
					"durationInMin": 0,
					"stepId": "",
					"stepName": "",
					"operationFeeTotal": 0
				}
			],
			"deviceDtoList": [
				{
					"deviceName": "",
					"parameterName": "",
					"unit": "",
					"reference": "",
					"actual": ""
				}
			],
			"costItems": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"unit": "",
					"quantity": 0,
					"batchNo": "",
					"expirationDate": "",
					"warehouse": {
						"id": "",
						"name": ""
					}
				}
			],
			"cancelled": true,
			"revoked": true,
			"refunded": true,
			"salesClinic": {
				"id": "",
				"name": ""
			},
			"salesConsultant": {
				"id": "",
				"name": ""
			},
			"salesDate": "",
			"cancelledDate": "",
			"refundedDate": "",
			"creator": {
				"id": "",
				"name": ""
			},
			"note": "",
			"remainNumber": 0,
			"courseNumber": 0
		}
	],
	"number": 0
}
```


## 根据客户Id获取授权机构下的客户充值订单数据


**接口地址**:`/api/v1/billing/customer/{id}/prepaid-order`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageSalesOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|SalesOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;external||External|External|
|&emsp;&emsp;&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]|string||
|&emsp;&emsp;&emsp;&emsp;number|外部订单号|string||
|&emsp;&emsp;salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;referrer||Referrer|Referrer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;retailAmount|零售价金额，原价|number||
|&emsp;&emsp;transactionAmount|成交价金额，原价|number||
|&emsp;&emsp;totalArrears|当前欠款金额|number||
|&emsp;&emsp;items|销售订单条目信息|array|SimpleOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;id|SKU ID|string||
|&emsp;&emsp;&emsp;&emsp;name|SKU 名称|string||
|&emsp;&emsp;&emsp;&emsp;number|SKU 编号|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,promotion,card,card-service,card-product,balance,reward,prepay|string||
|&emsp;&emsp;&emsp;&emsp;index|序号|string||
|&emsp;&emsp;&emsp;&emsp;lineId|行/条目 id|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;aptitude|资质|string||
|&emsp;&emsp;&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;&emsp;&emsp;totalTransactionPrice|成交价总金额|number||
|&emsp;&emsp;&emsp;&emsp;arrears|当前欠款金额|number||
|&emsp;&emsp;&emsp;&emsp;subItems|子条目(组合项目)|array|SimpleOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;sourceId|来源条目ID - 卡项定义ID/已购买卡项条目ID|string||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;sales||Sales|Sales|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developer||Developer|Developer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;beautician||Beautician|Beautician|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;operator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;status|状态，参考wiki/补充文档/状态一览,可用值:draft,submitted,paying,partial-paid,paid,refunded,discarded,arrears-clear,orderItem-arrears-clear|string||
|&emsp;&emsp;approvalStatus|审批状态,可用值:approving,approved,rejected|string||
|&emsp;&emsp;type|类型,可用值:retail,medical,free,charge,prepay,spa,exchange,medical-transfer,prepay-transfer,charge-transfer|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;visitId|关联到访ID|string||
|&emsp;&emsp;createdAt|开单时间|string(date-time)||
|&emsp;&emsp;freeReason||FreeReason|FreeReason|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developers|共同开发人|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"external": {
				"system": "",
				"number": ""
			},
			"salesClinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"referrer": {
				"id": "",
				"name": ""
			},
			"retailAmount": 0,
			"transactionAmount": 0,
			"totalArrears": 0,
			"items": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"index": "",
					"lineId": "",
					"unit": "",
					"aptitude": "",
					"specification": "",
					"quantity": 0,
					"unitRetailPrice": 0,
					"totalTransactionPrice": 0,
					"arrears": 0,
					"subItems": [
						{
							"id": "",
							"name": "",
							"number": "",
							"type": "",
							"index": "",
							"lineId": "",
							"unit": "",
							"aptitude": "",
							"specification": "",
							"quantity": 0,
							"unitRetailPrice": 0,
							"totalTransactionPrice": 0,
							"arrears": 0,
							"subItems": [
								{}
							],
							"sourceId": "",
							"note": ""
						}
					],
					"sourceId": "",
					"note": ""
				}
			],
			"customer": {
				"id": "",
				"name": ""
			},
			"sales": {
				"id": "",
				"name": ""
			},
			"developer": {
				"id": "",
				"name": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"beautician": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"operator": {
				"id": "",
				"name": ""
			},
			"status": "",
			"approvalStatus": "",
			"type": "",
			"note": "",
			"visitId": "",
			"createdAt": "",
			"freeReason": {
				"id": "",
				"name": ""
			},
			"developers": [
				{
					"id": "",
					"name": ""
				}
			]
		}
	],
	"number": 0
}
```


## 根据客户Id获取授权机构下的客户销售订单数据


**接口地址**:`/api/v1/billing/customer/{id}/sales-order`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageSalesOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|SalesOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;external||External|External|
|&emsp;&emsp;&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]|string||
|&emsp;&emsp;&emsp;&emsp;number|外部订单号|string||
|&emsp;&emsp;salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;referrer||Referrer|Referrer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;retailAmount|零售价金额，原价|number||
|&emsp;&emsp;transactionAmount|成交价金额，原价|number||
|&emsp;&emsp;totalArrears|当前欠款金额|number||
|&emsp;&emsp;items|销售订单条目信息|array|SimpleOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;id|SKU ID|string||
|&emsp;&emsp;&emsp;&emsp;name|SKU 名称|string||
|&emsp;&emsp;&emsp;&emsp;number|SKU 编号|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,promotion,card,card-service,card-product,balance,reward,prepay|string||
|&emsp;&emsp;&emsp;&emsp;index|序号|string||
|&emsp;&emsp;&emsp;&emsp;lineId|行/条目 id|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;aptitude|资质|string||
|&emsp;&emsp;&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;&emsp;&emsp;totalTransactionPrice|成交价总金额|number||
|&emsp;&emsp;&emsp;&emsp;arrears|当前欠款金额|number||
|&emsp;&emsp;&emsp;&emsp;subItems|子条目(组合项目)|array|SimpleOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;sourceId|来源条目ID - 卡项定义ID/已购买卡项条目ID|string||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;sales||Sales|Sales|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developer||Developer|Developer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;beautician||Beautician|Beautician|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;operator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;status|状态，参考wiki/补充文档/状态一览,可用值:draft,submitted,paying,partial-paid,paid,refunded,discarded,arrears-clear,orderItem-arrears-clear|string||
|&emsp;&emsp;approvalStatus|审批状态,可用值:approving,approved,rejected|string||
|&emsp;&emsp;type|类型,可用值:retail,medical,free,charge,prepay,spa,exchange,medical-transfer,prepay-transfer,charge-transfer|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;visitId|关联到访ID|string||
|&emsp;&emsp;createdAt|开单时间|string(date-time)||
|&emsp;&emsp;freeReason||FreeReason|FreeReason|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developers|共同开发人|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"external": {
				"system": "",
				"number": ""
			},
			"salesClinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"referrer": {
				"id": "",
				"name": ""
			},
			"retailAmount": 0,
			"transactionAmount": 0,
			"totalArrears": 0,
			"items": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"index": "",
					"lineId": "",
					"unit": "",
					"aptitude": "",
					"specification": "",
					"quantity": 0,
					"unitRetailPrice": 0,
					"totalTransactionPrice": 0,
					"arrears": 0,
					"subItems": [
						{
							"id": "",
							"name": "",
							"number": "",
							"type": "",
							"index": "",
							"lineId": "",
							"unit": "",
							"aptitude": "",
							"specification": "",
							"quantity": 0,
							"unitRetailPrice": 0,
							"totalTransactionPrice": 0,
							"arrears": 0,
							"subItems": [
								{}
							],
							"sourceId": "",
							"note": ""
						}
					],
					"sourceId": "",
					"note": ""
				}
			],
			"customer": {
				"id": "",
				"name": ""
			},
			"sales": {
				"id": "",
				"name": ""
			},
			"developer": {
				"id": "",
				"name": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"beautician": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"operator": {
				"id": "",
				"name": ""
			},
			"status": "",
			"approvalStatus": "",
			"type": "",
			"note": "",
			"visitId": "",
			"createdAt": "",
			"freeReason": {
				"id": "",
				"name": ""
			},
			"developers": [
				{
					"id": "",
					"name": ""
				}
			]
		}
	],
	"number": 0
}
```


## 获取客户可转疗项目


**接口地址**:`/api/v1/billing/customer/{id}/transfer/product-item`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CustomerTransferProductItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|customerId|客户id|string||
|customerName|客户名|string||
|productItems|可转疗品项|array|TransferProductItem|
|&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;clinicId|开单门店ID|string||
|&emsp;&emsp;timestamp|开单时间|string(date-time)||
|&emsp;&emsp;executableQty|可执行数量|integer(int64)||
|&emsp;&emsp;productId|项目ID|string||
|&emsp;&emsp;productName|项目名称|string||


**响应示例**:
```javascript
{
	"customerId": "",
	"customerName": "",
	"productItems": [
		{
			"id": "",
			"orderId": "",
			"clinicId": "",
			"timestamp": "",
			"executableQty": 0,
			"productId": "",
			"productName": ""
		}
	]
}
```


## 获取订单与美学规划关联关系


**接口地址**:`/api/v1/billing/esthetics/order-relation`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|estimateId|美学评估单ID，与订单ID必传一个|query|false|string||
|orderId|订单ID, 与评估单ID必传一个|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|QueryEstimateItemOrderLineRelationDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|estimateId|评估单ID|string||
|orderList|评估单关联的订单|array|Order|
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;orderLineList|订单行关联评估条目|array|OrderLine|
|&emsp;&emsp;&emsp;&emsp;orderLineId|订单行ID|string||
|&emsp;&emsp;&emsp;&emsp;estimateItemIdList|特征ID|array|string|


**响应示例**:
```javascript
{
	"estimateId": "",
	"orderList": [
		{
			"orderId": "",
			"orderLineList": [
				{
					"orderLineId": "",
					"estimateItemIdList": []
				}
			]
		}
	]
}
```


## 修改订单与美学规划关联关系


**接口地址**:`/api/v1/billing/esthetics/order-relation`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "estimateId": "",
  "orderId": "",
  "orderLineList": [
    {
      "orderLineId": "",
      "estimateItemIdList": []
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|saveEstimateOrderLineRelationParams|SaveEstimateOrderLineRelationParams|body|true|SaveEstimateOrderLineRelationParams|SaveEstimateOrderLineRelationParams|
|&emsp;&emsp;estimateId|美学评估单ID||true|string||
|&emsp;&emsp;orderId|订单ID||true|string||
|&emsp;&emsp;orderLineList|订单行关联的评估特征||true|array|OrderLine|
|&emsp;&emsp;&emsp;&emsp;orderLineId|订单行ID||true|string||
|&emsp;&emsp;&emsp;&emsp;estimateItemIdList|特征ID||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取客户美学方案


**接口地址**:`/api/v1/billing/esthetics/plan`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "customerId": "",
  "organizationId": "",
  "estheticsPlanId": "",
  "estimateId": "",
  "estimateNumber": "",
  "planDateStart": "",
  "planDateEnd": "",
  "statusList": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|queryEstheticsPlanParams|QueryEstheticsPlanParams|body|true|QueryEstheticsPlanParams|QueryEstheticsPlanParams|
|&emsp;&emsp;customerId|客户ID||true|string||
|&emsp;&emsp;organizationId|创建门店ID||false|string||
|&emsp;&emsp;estheticsPlanId|美学方案ID||false|string||
|&emsp;&emsp;estimateId|美学评估单ID||false|string||
|&emsp;&emsp;estimateNumber|美学评估单号||false|string||
|&emsp;&emsp;planDateStart|美学方案创建开始时间||false|string(date-time)||
|&emsp;&emsp;planDateEnd|美学方案创建结束日期||false|string(date-time)||
|&emsp;&emsp;statusList|美学方案状态（支持多选，待跟进(wait-follow), 跟进中(following), 已开单(order), 已收款(paid)）||false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|QueryEstheticsPlanProductDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|estheticsPlanId|方案ID|string||
|estheticsPlanNumber|方案编号|string||
|createTime|方案创建时间|string(date-time)|string(date-time)|
|status|方案状态|string||
|estimateId|评估单ID|string||
|estimateNumber|评估单编号|string||
|customerId|客户ID|string||
|customerName|客户名|string||
|organizationId|门店ID|string||
|organizationName|门店名|string||
|productList|关联品项明细列表|array|Product|
|&emsp;&emsp;productType|品项目类型（区分分类、项目、商品、促销、卡项）|string||
|&emsp;&emsp;productId|品项ID|string||
|&emsp;&emsp;productName|品项名|string||
|&emsp;&emsp;productQuantity|品项数量|integer(int32)||
|&emsp;&emsp;estimateItemList|特征明细列表|array|EstimateItem|
|&emsp;&emsp;&emsp;&emsp;characteristicId|美学特征ID|string||
|&emsp;&emsp;&emsp;&emsp;characteristicName|美学特征名称|string||
|&emsp;&emsp;&emsp;&emsp;levelSerialNumber|美学特征等级序号|integer||
|&emsp;&emsp;&emsp;&emsp;levelCustomName|美学特征等级名称|string||


**响应示例**:
```javascript
[
	{
		"estheticsPlanId": "",
		"estheticsPlanNumber": "",
		"createTime": "",
		"status": "",
		"estimateId": "",
		"estimateNumber": "",
		"customerId": "",
		"customerName": "",
		"organizationId": "",
		"organizationName": "",
		"productList": [
			{
				"productType": "",
				"productId": "",
				"productName": "",
				"productQuantity": 0,
				"estimateItemList": [
					{
						"characteristicId": "",
						"characteristicName": "",
						"levelSerialNumber": 0,
						"levelCustomName": ""
					}
				]
			}
		]
	}
]
```


## 换入订单ID查询换购记录


**接口地址**:`/api/v1/billing/exchange/list-by-target-ids`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|targetOrderIds|换入订单ID|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ExchangeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|换购ID|string||
|customerId|客户ID|string||
|clinicId|门店ID|string||
|totalAmount|总金额|number||
|supplementAmount|补缴金额|number||
|exchangeStatus|换购状态,可用值:completed,approving,cancel,reject|string||
|bizTime|业务时间|string(date-time)|string(date-time)|
|createTime|创建时间|string(date-time)|string(date-time)|
|inItems|换入信息|array|ExchangeInItemDto|
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;accountItemId|权益ID|string||
|&emsp;&emsp;accountItemType|权益类型|string||
|&emsp;&emsp;skuId|skuId|string||
|&emsp;&emsp;quantity|数量|integer(int64)||
|&emsp;&emsp;amount|金额|number||
|outItems|换出信息|array|ExchangeOutItemDto|
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;accountItemId|权益ID|string||
|&emsp;&emsp;accountItemType|权益类型|string||
|&emsp;&emsp;skuId|skuId|string||
|&emsp;&emsp;quantity|数量|integer(int64)||
|&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;refundOrderId|换出退款单ID|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"customerId": "",
		"clinicId": "",
		"totalAmount": 0,
		"supplementAmount": 0,
		"exchangeStatus": "",
		"bizTime": "",
		"createTime": "",
		"inItems": [
			{
				"orderId": "",
				"clinicId": "",
				"accountItemId": "",
				"accountItemType": "",
				"skuId": "",
				"quantity": 0,
				"amount": 0
			}
		],
		"outItems": [
			{
				"orderId": "",
				"clinicId": "",
				"accountItemId": "",
				"accountItemType": "",
				"skuId": "",
				"quantity": 0,
				"amount": 0,
				"refundOrderId": ""
			}
		]
	}
]
```


## 获取换购记录


**接口地址**:`/api/v1/billing/exchange/page`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|customerId|客户ID|query|false|string||
|clinicIds|门店ID|query|false|array|string|
|exchangeStatuses|换购状态,可用值:completed,approving,cancel,reject|query|false|array|string|
|start|业务时间(ISO-8601标准格式) yyyy-MM-dd 格式|query|false|string(date-time)||
|end|业务时间(ISO-8601标准格式) yyyy-MM-dd 格式|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageExchangeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ExchangeDto|
|&emsp;&emsp;id|换购ID|string||
|&emsp;&emsp;customerId|客户ID|string||
|&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;totalAmount|总金额|number||
|&emsp;&emsp;supplementAmount|补缴金额|number||
|&emsp;&emsp;exchangeStatus|换购状态,可用值:completed,approving,cancel,reject|string||
|&emsp;&emsp;bizTime|业务时间|string(date-time)||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;inItems|换入信息|array|ExchangeInItemDto|
|&emsp;&emsp;&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;&emsp;&emsp;accountItemId|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;accountItemType|权益类型|string||
|&emsp;&emsp;&emsp;&emsp;skuId|skuId|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;outItems|换出信息|array|ExchangeOutItemDto|
|&emsp;&emsp;&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;&emsp;&emsp;accountItemId|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;accountItemType|权益类型|string||
|&emsp;&emsp;&emsp;&emsp;skuId|skuId|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;refundOrderId|换出退款单ID|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"customerId": "",
			"clinicId": "",
			"totalAmount": 0,
			"supplementAmount": 0,
			"exchangeStatus": "",
			"bizTime": "",
			"createTime": "",
			"inItems": [
				{
					"orderId": "",
					"clinicId": "",
					"accountItemId": "",
					"accountItemType": "",
					"skuId": "",
					"quantity": 0,
					"amount": 0
				}
			],
			"outItems": [
				{
					"orderId": "",
					"clinicId": "",
					"accountItemId": "",
					"accountItemType": "",
					"skuId": "",
					"quantity": 0,
					"amount": 0,
					"refundOrderId": ""
				}
			]
		}
	],
	"number": 0
}
```


## 获取授权机构下的可执行条目信息 - 订单中的项目条目


**接口地址**:`/api/v1/billing/execution-item`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所ID|query|false|string||
|customerId|顾客ID|query|false|string||
|ids|ID - 列表|query|false|array|string|
|status|状态(pending,executing,completion,cancelled)|query|false|array|string|
|keyword|关键字（消费项目）|query|false|string||
|orderId|订单ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageExecutionItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ExecutionItemDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;lineIndex|订单行Index|string||
|&emsp;&emsp;lineId|订单行Id|string||
|&emsp;&emsp;lineItemIndex|订单条目Index|string||
|&emsp;&emsp;lineItemId|订单条目Id|string||
|&emsp;&emsp;skuInfo||SkuInfo|SkuInfo|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;transferId|转赠记录ID|string||
|&emsp;&emsp;type|类型(项目、套餐项目、卡项项目),可用值:service,promotion,card-service|string||
|&emsp;&emsp;item||LineItemInfo|LineItemInfo|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;courseNumber||integer||
|&emsp;&emsp;createdAt|开单日期|string(date-time)||
|&emsp;&emsp;amount|可执行总金额|number||
|&emsp;&emsp;remain|剩余可执行金额|number||
|&emsp;&emsp;arrears|欠费金额|number||
|&emsp;&emsp;totalTimes|可执行总次数  剩余可执行次数+已执行次数+已退次数+锁定次数|integer(int32)||
|&emsp;&emsp;leftTimes|剩余可执行次数 不包含锁定次数|integer(int32)||
|&emsp;&emsp;executedTimes|已执行次数|integer(int32)||
|&emsp;&emsp;refundedTimes|已退次数|integer(int32)||
|&emsp;&emsp;lockedTimes|锁定次数 退款/转赠/换购场景过程中锁定的次数|integer(int32)||
|&emsp;&emsp;status|状态|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"orderId": "",
			"lineIndex": "",
			"lineId": "",
			"lineItemIndex": "",
			"lineItemId": "",
			"skuInfo": {
				"id": "",
				"name": ""
			},
			"transferId": "",
			"type": "",
			"item": {
				"id": "",
				"name": "",
				"courseNumber": 0
			},
			"createdAt": "",
			"amount": 0,
			"remain": 0,
			"arrears": 0,
			"totalTimes": 0,
			"leftTimes": 0,
			"executedTimes": 0,
			"refundedTimes": 0,
			"lockedTimes": 0,
			"status": ""
		}
	],
	"number": 0
}
```


## 获取授权机构下的可执行条目转赠记录


**接口地址**:`/api/v1/billing/execution-item/transfer`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|giverId|转赠客户ID|query|false|string||
|receiverId|受赠客户ID|query|false|string||
|sourceClinicId|转出门诊ID|query|false|string||
|targetClinicId|转入门诊ID|query|false|string||
|status|状态(approving(待审核), completed(已完成), cancel(已作废), reject(已拒绝), exception(异常)),可用值:approving,completed,cancel,reject,exception|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageItemTransferDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ItemTransferDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;number|转赠单号|string||
|&emsp;&emsp;giver||Giver|Giver|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;sourceClinic||SourceClinic|SourceClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;receiver||Receiver|Receiver|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;targetClinic||TargetClinic|TargetClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;orderId|关联订单ID（已废弃）|string||
|&emsp;&emsp;status||CodedValue|CodedValue|
|&emsp;&emsp;&emsp;&emsp;displayText||string||
|&emsp;&emsp;&emsp;&emsp;abbreviationText||string||
|&emsp;&emsp;&emsp;&emsp;family||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;enable||boolean||
|&emsp;&emsp;&emsp;&emsp;order||integer||
|&emsp;&emsp;&emsp;&emsp;relevance||array|CodedValue|
|&emsp;&emsp;&emsp;&emsp;systemCfg||boolean||
|&emsp;&emsp;&emsp;&emsp;vocabularyName||string||
|&emsp;&emsp;&emsp;&emsp;default||boolean||
|&emsp;&emsp;&emsp;&emsp;codeValue||string||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createdAt|创建时间|string(date-time)||
|&emsp;&emsp;details|具体项目|array|ItemTransferLineDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;spec||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;&emsp;&emsp;type|转赠类型(项目/产品/代金券/卡项/积分/增值金/储值金),可用值:service,product,coupon,card,point,balance,reward|string||
|&emsp;&emsp;&emsp;&emsp;sourceItemId|转赠原记录ID - 项目类型则对应可执行记录|string||
|&emsp;&emsp;&emsp;&emsp;sourceOrderId|原订单ID|string||
|&emsp;&emsp;&emsp;&emsp;sourceOrderLineItemId|原订单条目ID|string||
|&emsp;&emsp;&emsp;&emsp;targetItemId|受赠后记录ID - 项目类型则对应可执行记录|string||
|&emsp;&emsp;&emsp;&emsp;targetOrderId|受赠后订单id|string||
|&emsp;&emsp;&emsp;&emsp;targetOrderLineItemId|转入订单条目ID|string||
|&emsp;&emsp;&emsp;&emsp;refundOrderId|原订单转赠退款单ID|string||
|&emsp;&emsp;&emsp;&emsp;unitTransactionPrice|成交单价|number||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|零售单价 (已废弃)|number||
|&emsp;&emsp;&emsp;&emsp;unitTransferPrice|转赠单件价值(成交价/疗程数) (已废弃)|number||
|&emsp;&emsp;&emsp;&emsp;quantity|转赠数量|integer||
|&emsp;&emsp;totalAmount|总金额|number||
|&emsp;&emsp;note|备注|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"giver": {
				"id": "",
				"name": ""
			},
			"sourceClinic": {
				"id": "",
				"name": ""
			},
			"receiver": {
				"id": "",
				"name": ""
			},
			"targetClinic": {
				"id": "",
				"name": ""
			},
			"orderId": "",
			"status": {
				"displayText": "",
				"abbreviationText": "",
				"family": "",
				"version": "",
				"enable": true,
				"order": 0,
				"relevance": [
					{
						"displayText": "",
						"abbreviationText": "",
						"family": "",
						"version": "",
						"enable": true,
						"order": 0,
						"relevance": [
							{}
						],
						"systemCfg": true,
						"vocabularyName": "",
						"default": true,
						"codeValue": ""
					}
				],
				"systemCfg": true,
				"vocabularyName": "",
				"default": true,
				"codeValue": ""
			},
			"creator": {
				"id": "",
				"name": ""
			},
			"createdAt": "",
			"details": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"unit": "",
					"type": "",
					"sourceItemId": "",
					"sourceOrderId": "",
					"sourceOrderLineItemId": "",
					"targetItemId": "",
					"targetOrderId": "",
					"targetOrderLineItemId": "",
					"refundOrderId": "",
					"unitTransactionPrice": 0,
					"unitRetailPrice": 0,
					"unitTransferPrice": 0,
					"quantity": 0
				}
			],
			"totalAmount": 0,
			"note": ""
		}
	],
	"number": 0
}
```


## 获取授权机构下的客户项目执行数据


**接口地址**:`/api/v1/billing/execution-record`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所ID|query|false|string||
|customerId|顾客ID|query|false|string||
|cancelled|是否已作废|query|false|boolean||
|status|状态:正常(已完成)/已撤回（completion,revoked），默认仅查询正常状态；,可用值:completion,revoked|query|false|array|string|
|itemIds|可执行订单条目ID - 列表|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageExecutionRecordDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ExecutionRecordDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|单号|string||
|&emsp;&emsp;itemId|可执行条目ID|string||
|&emsp;&emsp;orderId|销售单ID|string||
|&emsp;&emsp;stepList|操作步骤|array|ExecutionStepDTO|
|&emsp;&emsp;&emsp;&emsp;stepId|步骤id|string||
|&emsp;&emsp;&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;&emsp;&emsp;stepTypeCode|步骤类型code -1:操作前准备，0：操作项目,1:操作后护理|integer||
|&emsp;&emsp;&emsp;&emsp;stepTypeName|步骤类型|string||
|&emsp;&emsp;bodyPartName|执行部位名称|string||
|&emsp;&emsp;bodyPartId|执行部位ID|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||ExecutionClinic|ExecutionClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;serviceConsultant||ExecutionConsultant|ExecutionConsultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;executedDate|执行时间|string(date-time)||
|&emsp;&emsp;service||Service|Service|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;spec||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;quantity|执行数量|integer(int32)||
|&emsp;&emsp;amount|执行金额|number||
|&emsp;&emsp;arrearsAmount|当前欠费金额|number||
|&emsp;&emsp;participants|参与人|array|ParticipantDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;durationInMin|操作时长|integer||
|&emsp;&emsp;&emsp;&emsp;stepId|步骤id|string||
|&emsp;&emsp;&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;&emsp;&emsp;operationFeeTotal|操作费|number||
|&emsp;&emsp;deviceDtoList|治疗参数|array|DeviceDto|
|&emsp;&emsp;&emsp;&emsp;deviceName|设备|string||
|&emsp;&emsp;&emsp;&emsp;parameterName|参数名|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;reference|参考值|string||
|&emsp;&emsp;&emsp;&emsp;actual|实际值|string||
|&emsp;&emsp;costItems|耗用品|array|ExecutionCostItemDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次号|string||
|&emsp;&emsp;&emsp;&emsp;expirationDate|有效期|string||
|&emsp;&emsp;&emsp;&emsp;warehouse||Warehouse|Warehouse|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;cancelled|已作废|boolean||
|&emsp;&emsp;revoked|已撤回|boolean||
|&emsp;&emsp;refunded|已退款|boolean||
|&emsp;&emsp;salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;salesConsultant||SalesConsultant|SalesConsultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;salesDate|销售时间|string(date-time)||
|&emsp;&emsp;cancelledDate|作废/撤回时间|string(date-time)||
|&emsp;&emsp;refundedDate|退款时间|string(date-time)||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;remainNumber|权益剩余执行数量（划扣后）|integer(int32)||
|&emsp;&emsp;courseNumber|权益总次数|integer(int32)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"itemId": "",
			"orderId": "",
			"stepList": [
				{
					"stepId": "",
					"stepName": "",
					"stepTypeCode": 0,
					"stepTypeName": ""
				}
			],
			"bodyPartName": "",
			"bodyPartId": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"serviceConsultant": {
				"id": "",
				"name": ""
			},
			"executedDate": "",
			"service": {
				"id": "",
				"name": "",
				"spec": "",
				"unit": ""
			},
			"quantity": 0,
			"amount": 0,
			"arrearsAmount": 0,
			"participants": [
				{
					"id": "",
					"name": "",
					"role": {
						"code": "",
						"name": "",
						"system": ""
					},
					"durationInMin": 0,
					"stepId": "",
					"stepName": "",
					"operationFeeTotal": 0
				}
			],
			"deviceDtoList": [
				{
					"deviceName": "",
					"parameterName": "",
					"unit": "",
					"reference": "",
					"actual": ""
				}
			],
			"costItems": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"unit": "",
					"quantity": 0,
					"batchNo": "",
					"expirationDate": "",
					"warehouse": {
						"id": "",
						"name": ""
					}
				}
			],
			"cancelled": true,
			"revoked": true,
			"refunded": true,
			"salesClinic": {
				"id": "",
				"name": ""
			},
			"salesConsultant": {
				"id": "",
				"name": ""
			},
			"salesDate": "",
			"cancelledDate": "",
			"refundedDate": "",
			"creator": {
				"id": "",
				"name": ""
			},
			"note": "",
			"remainNumber": 0,
			"courseNumber": 0
		}
	],
	"number": 0
}
```


## 在授权机构下创建项目执行记录数据


**接口地址**:`/api/v1/billing/execution-record`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "itemId": "",
  "medicalDepartmentId": "",
  "times": 0,
  "participants": [
    {
      "employeeId": "",
      "roleCode": "",
      "durationInMin": 0
    }
  ],
  "costs": [
    {
      "id": "",
      "quantity": 0,
      "batchNo": "",
      "expirationDate": "",
      "warehouseId": "",
      "drug": true
    }
  ],
  "operatorId": "",
  "note": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createExecutionParams|CreateExecutionParams|body|true|CreateExecutionParams|CreateExecutionParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;itemId|执行条目ID||true|string||
|&emsp;&emsp;medicalDepartmentId|划扣科室ID，参考 基础数据-组织架构||false|string||
|&emsp;&emsp;times|本次执行次数||false|integer(int32)||
|&emsp;&emsp;participants|参与人||false|array|ParticipantParams|
|&emsp;&emsp;&emsp;&emsp;employeeId|参与员工ID||true|string||
|&emsp;&emsp;&emsp;&emsp;roleCode|参与人划扣角色Code,可用值:doctor,assistant,nurse,beautician,anesthetist||true|string||
|&emsp;&emsp;&emsp;&emsp;durationInMin|参与时长 - 分钟||false|integer||
|&emsp;&emsp;costs|耗材||false|array|CostItemParams|
|&emsp;&emsp;&emsp;&emsp;id|耗材ID||true|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量||true|integer||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次号||false|string||
|&emsp;&emsp;&emsp;&emsp;expirationDate|有效期||false|string||
|&emsp;&emsp;&emsp;&emsp;warehouseId|库房信息||true|string||
|&emsp;&emsp;&emsp;&emsp;drug|||false|boolean||
|&emsp;&emsp;operatorId|操作人||false|string||
|&emsp;&emsp;note|备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 作废执行记录


**接口地址**:`/api/v1/billing/execution-record/cancel`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "recordId": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|revokeCancelExecutionParams|RevokeCancelExecutionParams|body|true|RevokeCancelExecutionParams|RevokeCancelExecutionParams|
|&emsp;&emsp;recordId|执行记录id||true|string||
|&emsp;&emsp;operatorId|操作人id||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content|ExecutionRecordRevokeResult|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|result||integer(int32)|integer(int32)|
|message||string||


**响应示例**:
```javascript
{
	"result": 0,
	"message": ""
}
```


## 查询执行记录的履约明细


**接口地址**:`/api/v1/billing/execution-record/fulfillment/detail`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
[]
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|strings|string|body|true|array||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|FulfillmentDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|executionRecordId|执行记录ID|string||
|accountItemId|权益ID|string||
|totalAmount|核销总金额|number||
|totalCredit|核销总积分数量|integer(int64)|integer(int64)|
|amounts|核销金额明细|array|FulfillmentAmountDto|
|&emsp;&emsp;billingMethodCode|支付方式|string||
|&emsp;&emsp;amount|核销金额|number||
|&emsp;&emsp;credit|核销积分数量|integer(int64)||


**响应示例**:
```javascript
[
	{
		"executionRecordId": "",
		"accountItemId": "",
		"totalAmount": 0,
		"totalCredit": 0,
		"amounts": [
			{
				"billingMethodCode": "",
				"amount": 0,
				"credit": 0
			}
		]
	}
]
```


## 撤回执行记录


**接口地址**:`/api/v1/billing/execution-record/revoke`


**请求方式**:`PUT`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "recordId": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|revokeCancelExecutionParams|RevokeCancelExecutionParams|body|true|RevokeCancelExecutionParams|RevokeCancelExecutionParams|
|&emsp;&emsp;recordId|执行记录id||true|string||
|&emsp;&emsp;operatorId|操作人id||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content|ExecutionRecordRevokeResult|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|result||integer(int32)|integer(int32)|
|message||string||


**响应示例**:
```javascript
{
	"result": 0,
	"message": ""
}
```


## 获取授权机构下的客户项目执行数据


**接口地址**:`/api/v1/billing/execution-record/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ExecutionRecordDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|number|单号|string||
|itemId|可执行条目ID|string||
|orderId|销售单ID|string||
|stepList|操作步骤|array|ExecutionStepDTO|
|&emsp;&emsp;stepId|步骤id|string||
|&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;stepTypeCode|步骤类型code -1:操作前准备，0：操作项目,1:操作后护理|integer(int32)||
|&emsp;&emsp;stepTypeName|步骤类型|string||
|bodyPartName|执行部位名称|string||
|bodyPartId|执行部位ID|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|clinic||ExecutionClinic|ExecutionClinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|serviceConsultant||ExecutionConsultant|ExecutionConsultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|executedDate|执行时间|string(date-time)|string(date-time)|
|service||Service|Service|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;spec||string||
|&emsp;&emsp;unit||string||
|quantity|执行数量|integer(int32)|integer(int32)|
|amount|执行金额|number||
|arrearsAmount|当前欠费金额|number||
|participants|参与人|array|ParticipantDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;role||JobRoleDto|JobRoleDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;durationInMin|操作时长|integer(int32)||
|&emsp;&emsp;stepId|步骤id|string||
|&emsp;&emsp;stepName|步骤名称|string||
|&emsp;&emsp;operationFeeTotal|操作费|number||
|deviceDtoList|治疗参数|array|DeviceDto|
|&emsp;&emsp;deviceName|设备|string||
|&emsp;&emsp;parameterName|参数名|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;reference|参考值|string||
|&emsp;&emsp;actual|实际值|string||
|costItems|耗用品|array|ExecutionCostItemDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;quantity|数量|integer(int32)||
|&emsp;&emsp;batchNo|批次号|string||
|&emsp;&emsp;expirationDate|有效期|string(date-time)||
|&emsp;&emsp;warehouse||Warehouse|Warehouse|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|cancelled|已作废|boolean||
|revoked|已撤回|boolean||
|refunded|已退款|boolean||
|salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|salesConsultant||SalesConsultant|SalesConsultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|salesDate|销售时间|string(date-time)|string(date-time)|
|cancelledDate|作废/撤回时间|string(date-time)|string(date-time)|
|refundedDate|退款时间|string(date-time)|string(date-time)|
|creator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|note|备注|string||
|remainNumber|权益剩余执行数量（划扣后）|integer(int32)|integer(int32)|
|courseNumber|权益总次数|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"id": "",
	"number": "",
	"itemId": "",
	"orderId": "",
	"stepList": [
		{
			"stepId": "",
			"stepName": "",
			"stepTypeCode": 0,
			"stepTypeName": ""
		}
	],
	"bodyPartName": "",
	"bodyPartId": "",
	"customer": {
		"id": "",
		"name": ""
	},
	"clinic": {
		"id": "",
		"name": ""
	},
	"medicalDepartment": {
		"id": "",
		"name": ""
	},
	"serviceConsultant": {
		"id": "",
		"name": ""
	},
	"executedDate": "",
	"service": {
		"id": "",
		"name": "",
		"spec": "",
		"unit": ""
	},
	"quantity": 0,
	"amount": 0,
	"arrearsAmount": 0,
	"participants": [
		{
			"id": "",
			"name": "",
			"role": {
				"code": "",
				"name": "",
				"system": ""
			},
			"durationInMin": 0,
			"stepId": "",
			"stepName": "",
			"operationFeeTotal": 0
		}
	],
	"deviceDtoList": [
		{
			"deviceName": "",
			"parameterName": "",
			"unit": "",
			"reference": "",
			"actual": ""
		}
	],
	"costItems": [
		{
			"id": "",
			"name": "",
			"spec": "",
			"unit": "",
			"quantity": 0,
			"batchNo": "",
			"expirationDate": "",
			"warehouse": {
				"id": "",
				"name": ""
			}
		}
	],
	"cancelled": true,
	"revoked": true,
	"refunded": true,
	"salesClinic": {
		"id": "",
		"name": ""
	},
	"salesConsultant": {
		"id": "",
		"name": ""
	},
	"salesDate": "",
	"cancelledDate": "",
	"refundedDate": "",
	"creator": {
		"id": "",
		"name": ""
	},
	"note": "",
	"remainNumber": 0,
	"courseNumber": 0
}
```


## 获取收退款分摊信息


**接口地址**:`/api/v1/billing/financial/billing-apportion`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|billingId|收退款支付ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|BillingApportionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|orderId|关联订单/退款单ID|string||
|orderType|关联订单/退款单 类型|string||
|salesOrderId|源订单id|string||
|salesOrderLineId|关联订单行id|string||
|salesOrderLineItemId|关联订单条目id|string||
|billingId|收退款支付ID|string||
|billingType|收退款类型 正常付费/收欠款/退款|string||
|billingMethod|支付方式|string||
|billingItemId|收退款条目ID|string||
|billingAccountItemId|支付权益ID|string||
|amount|支付金额|number||
|customerId|客户ID|string||
|accountItemId|权益ID|string||
|accountItemType|权益类型|string||
|accountItemSkuId|权益SKU|string||
|rootAccountItemId|根权益ID|string||
|rootAccountItemSkuId|根权益SKU|string||
|rootAccountItemType|根权益类型|string||
|creditQuantity|积分数|integer(int64)|integer(int64)|
|orderLineIndex|订单行index|string||
|billingMethodGroup|支付方式组|string||


**响应示例**:
```javascript
[
	{
		"orderId": "",
		"orderType": "",
		"salesOrderId": "",
		"salesOrderLineId": "",
		"salesOrderLineItemId": "",
		"billingId": "",
		"billingType": "",
		"billingMethod": "",
		"billingItemId": "",
		"billingAccountItemId": "",
		"amount": 0,
		"customerId": "",
		"accountItemId": "",
		"accountItemType": "",
		"accountItemSkuId": "",
		"rootAccountItemId": "",
		"rootAccountItemSkuId": "",
		"rootAccountItemType": "",
		"creditQuantity": 0,
		"orderLineIndex": "",
		"billingMethodGroup": ""
	}
]
```


## 获取退款订单分摊信息


**接口地址**:`/api/v1/billing/financial/refund-order-billing-apportion`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|refundOrderId|退款ID|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|BillingApportionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|orderId|关联订单/退款单ID|string||
|orderType|关联订单/退款单 类型|string||
|salesOrderId|源订单id|string||
|salesOrderLineId|关联订单行id|string||
|salesOrderLineItemId|关联订单条目id|string||
|billingId|收退款支付ID|string||
|billingType|收退款类型 正常付费/收欠款/退款|string||
|billingMethod|支付方式|string||
|billingItemId|收退款条目ID|string||
|billingAccountItemId|支付权益ID|string||
|amount|支付金额|number||
|customerId|客户ID|string||
|accountItemId|权益ID|string||
|accountItemType|权益类型|string||
|accountItemSkuId|权益SKU|string||
|rootAccountItemId|根权益ID|string||
|rootAccountItemSkuId|根权益SKU|string||
|rootAccountItemType|根权益类型|string||
|creditQuantity|积分数|integer(int64)|integer(int64)|
|orderLineIndex|订单行index|string||
|billingMethodGroup|支付方式组|string||


**响应示例**:
```javascript
[
	{
		"orderId": "",
		"orderType": "",
		"salesOrderId": "",
		"salesOrderLineId": "",
		"salesOrderLineItemId": "",
		"billingId": "",
		"billingType": "",
		"billingMethod": "",
		"billingItemId": "",
		"billingAccountItemId": "",
		"amount": 0,
		"customerId": "",
		"accountItemId": "",
		"accountItemType": "",
		"accountItemSkuId": "",
		"rootAccountItemId": "",
		"rootAccountItemSkuId": "",
		"rootAccountItemType": "",
		"creditQuantity": 0,
		"orderLineIndex": "",
		"billingMethodGroup": ""
	}
]
```


## 创建免单订单，创建后为支付完成，忽略所有审批流程


**接口地址**:`/api/v1/billing/free-order`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "customerId": "",
  "participants": {
    "developerId": "",
    "doctorId": "",
    "beauticianId": "",
    "nurseId": "",
    "departmentId": "",
    "consultantId": ""
  },
  "external": {
    "system": "",
    "number": ""
  },
  "referrer": {
    "referrerId": "",
    "internal": true
  },
  "details": [
    {
      "itemType": "",
      "itemId": "",
      "unitRetailPrice": 0,
      "transactionTotalPrice": 0,
      "quantity": 0
    }
  ],
  "createdAt": "",
  "operatorId": "",
  "note": "",
  "orderType": "",
  "reductionId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createFreeOrderParams|创建销售订单参数|body|true|CreateFreeOrderParams|CreateFreeOrderParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;customerId|顾客信息||true|string||
|&emsp;&emsp;participants|||false|Participants|Participants|
|&emsp;&emsp;&emsp;&emsp;developerId|开发人||false|string||
|&emsp;&emsp;&emsp;&emsp;doctorId|医生||false|string||
|&emsp;&emsp;&emsp;&emsp;beauticianId|美容师||false|string||
|&emsp;&emsp;&emsp;&emsp;nurseId|护士||false|string||
|&emsp;&emsp;&emsp;&emsp;departmentId|开单科室||false|string||
|&emsp;&emsp;&emsp;&emsp;consultantId|开单咨询师||false|string||
|&emsp;&emsp;external|||false|NotRequiredExternal|NotRequiredExternal|
|&emsp;&emsp;&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]||false|string||
|&emsp;&emsp;&emsp;&emsp;number|外部订单号||false|string||
|&emsp;&emsp;referrer|||false|ReferrerParam|ReferrerParam|
|&emsp;&emsp;&emsp;&emsp;referrerId|二级渠道ID||true|string||
|&emsp;&emsp;&emsp;&emsp;internal|是否内部渠道(referrerId是否会员ID)||false|boolean||
|&emsp;&emsp;details|订单Item详情||true|array|OrderItemLine|
|&emsp;&emsp;&emsp;&emsp;itemType|Item类型,可用值:service,product,promotion,coupon-card||true|string||
|&emsp;&emsp;&emsp;&emsp;itemId|Item ID||true|string||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|单个零售价||false|number||
|&emsp;&emsp;&emsp;&emsp;transactionTotalPrice|成交总金额||false|number||
|&emsp;&emsp;&emsp;&emsp;quantity|数量||true|integer||
|&emsp;&emsp;createdAt|创建时间(ISO-8601标准格式) - 仅允许指定过去时间||false|string(date-time)||
|&emsp;&emsp;operatorId|创建人员工ID(开单人)||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;orderType|订单类型(零售、医美),可用值:retail,medical,free||true|string||
|&emsp;&emsp;reductionId|免单原因ID，参考字典代码:free-order-option（免单原因）||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 订单业绩分配


**接口地址**:`/api/v1/billing/order/performance-allocation`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "paymentId": "",
  "details": [
    {
      "employeeId": "",
      "employeeName": "",
      "amount": 0
    }
  ],
  "itemDetails": [
    {
      "itemId": "",
      "details": [
        {
          "employeeId": "",
          "employeeName": "",
          "amount": 0
        }
      ]
    }
  ],
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|orderPerformanceAllocationParams|订单业绩分配|body|true|OrderPerformanceAllocationParams|OrderPerformanceAllocationParams|
|&emsp;&emsp;paymentId|支付ID||true|string||
|&emsp;&emsp;details|不按条目分配明细||false|array|Detail|
|&emsp;&emsp;&emsp;&emsp;employeeId|员工ID||true|string||
|&emsp;&emsp;&emsp;&emsp;employeeName|员工姓名||false|string||
|&emsp;&emsp;&emsp;&emsp;amount|业绩金额（元）||true|number||
|&emsp;&emsp;itemDetails|按条目分配明细||false|array|ItemDetail|
|&emsp;&emsp;&emsp;&emsp;itemId|条目ID||true|string||
|&emsp;&emsp;&emsp;&emsp;details|分配明细||false|array|Detail|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;employeeId|员工ID||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;employeeName|员工姓名||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|业绩金额（元）||true|number||
|&emsp;&emsp;operatorId|创建人员工ID||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdString|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 订单退款V2，仅支持原路退，忽略审批流程


**接口地址**:`/api/v1/billing/order/refund`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "operatorId": "",
  "orderId": "",
  "items": [
    {
      "itemId": "",
      "orderLineItemId": "",
      "quantity": 0,
      "amount": 0,
      "note": ""
    }
  ],
  "payments": [
    {
      "type": "",
      "amount": 0,
      "creditQuantity": 0,
      "accountItemId": "",
      "note": ""
    }
  ],
  "bizTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createRefundOrderParams|订单退款申请参数v2|body|true|CreateRefundOrderParams|CreateRefundOrderParams|
|&emsp;&emsp;clinicId|退款操作门店Id||true|string||
|&emsp;&emsp;operatorId|创建人员工ID||true|string||
|&emsp;&emsp;orderId|订单ID - 目标订单id||true|string||
|&emsp;&emsp;items|退款条目||true|array|RefundItemV2|
|&emsp;&emsp;&emsp;&emsp;itemId|权益ID||false|string||
|&emsp;&emsp;&emsp;&emsp;orderLineItemId|订单条目id||false|string||
|&emsp;&emsp;&emsp;&emsp;quantity|订单条目退款数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;amount|订单条目退款金额（单位元）||false|number||
|&emsp;&emsp;&emsp;&emsp;note|订单条目退款备注信息||false|string||
|&emsp;&emsp;payments|退款支付条目 - 限原订单支付方式||true|array|RefundPaymentItem|
|&emsp;&emsp;&emsp;&emsp;type|订单条目退款支付方式code值||true|string||
|&emsp;&emsp;&emsp;&emsp;amount|订单条目退款金额（单位元）||true|number||
|&emsp;&emsp;&emsp;&emsp;creditQuantity|订单条目退积分数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;accountItemId|退回抵扣权益ID、券实例ID，支付方式为券时券实例ID必填||false|string||
|&emsp;&emsp;&emsp;&emsp;note|订单条目退款支付备注信息||false|string||
|&emsp;&emsp;bizTime|指定业务日期 - 仅允许指定到过去时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdString|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 订单退款V3，支持统一退。忽略审批流程


**接口地址**:`/api/v1/billing/order/refund/v3`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "operatorId": "",
  "orderId": "",
  "items": [
    {
      "itemId": "",
      "orderLineItemId": "",
      "quantity": 0,
      "amount": 0,
      "note": ""
    }
  ],
  "payments": [
    {
      "type": "",
      "unified": true,
      "amount": 0,
      "creditQuantity": 0,
      "accountItemId": "",
      "bankAccount": {
        "name": "",
        "account": "",
        "bankName": "",
        "bankBranch": ""
      },
      "note": ""
    }
  ],
  "bizTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createRefundOrderParamsV3|订单退款申请参数v3|body|true|CreateRefundOrderParamsV3|CreateRefundOrderParamsV3|
|&emsp;&emsp;clinicId|退款操作门店Id||true|string||
|&emsp;&emsp;operatorId|创建人员工ID||true|string||
|&emsp;&emsp;orderId|订单ID - 目标订单id||true|string||
|&emsp;&emsp;items|退款条目||true|array|RefundItemV3|
|&emsp;&emsp;&emsp;&emsp;itemId|权益ID||false|string||
|&emsp;&emsp;&emsp;&emsp;orderLineItemId|订单条目id||false|string||
|&emsp;&emsp;&emsp;&emsp;quantity|订单条目退款数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;amount|订单条目退款金额（单位元）||false|number||
|&emsp;&emsp;&emsp;&emsp;note|订单条目退款备注信息||false|string||
|&emsp;&emsp;payments|退款支付条目||true|array|RefundPaymentItemV3|
|&emsp;&emsp;&emsp;&emsp;type|订单条目退款支付方式code值||true|string||
|&emsp;&emsp;&emsp;&emsp;unified|是否统一退方式（仅可支持一种统一退方式）||true|boolean||
|&emsp;&emsp;&emsp;&emsp;amount|订单条目退款金额（单位元）||true|number||
|&emsp;&emsp;&emsp;&emsp;creditQuantity|订单条目退积分数量（如退款方式为积分必填）||false|integer||
|&emsp;&emsp;&emsp;&emsp;accountItemId|退回抵扣权益ID、券实例ID，支付方式为券时券实例ID必填||false|string||
|&emsp;&emsp;&emsp;&emsp;bankAccount|||false|BankAccount|BankAccount|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|银行卡-收款方||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;account|银行卡-账户号||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;bankName|银行卡-开户行||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;bankBranch|银行卡-开户支行||false|string||
|&emsp;&emsp;&emsp;&emsp;note|订单条目退款支付备注信息||false|string||
|&emsp;&emsp;bizTime|指定业务日期 - 仅允许指定到过去时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdString|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取授权机构下的收银摘要数据 - 收银摘要列表


**接口地址**:`/api/v1/billing/payment`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所ID|query|false|string||
|customerId|顾客ID|query|false|string||
|orderNumber|订单号|query|false|string||
|orderIds|订单ID - 列表(优先于订单号)|query|false|array|string|
|includeRefund|是否包含退款单,默认(false)|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PagePaymentDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|PaymentDetailDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;orderId|订单Id|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;totalAmount|支付总额|number||
|&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;operator||Cashier|Cashier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;effectiveTime|生效时间，如非特殊修改，等同于数据创建时间|string(date-time)||
|&emsp;&emsp;status|支付记录状态,可用值:issue,fail,success,refund,cancel|string||
|&emsp;&emsp;type|支付记录类型(正常，付欠费),可用值:normal,due|string||
|&emsp;&emsp;orderType|订单类型,可用值:medical,spa,retail,medicine,repair,free,charge,prepay,inpatient,exchange,charge-transfer,prepay-transfer,medicine-transfer,transfer-out,exchange-out|string||
|&emsp;&emsp;processingType|收款单处理中类型(cancelling:撤销中, none:未在处理中),可用值:cancelling,none|string||
|&emsp;&emsp;reduction||ReductionDto|ReductionDto|
|&emsp;&emsp;&emsp;&emsp;amount|减免金额|number||
|&emsp;&emsp;&emsp;&emsp;reason|减免原因|string||
|&emsp;&emsp;credit||CreditPayDto|CreditPayDto|
|&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;&emsp;&emsp;details|门店分摊明细|array|CreditPayDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;&emsp;&emsp;accounts|抵扣权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;coupons|券支付信息|array|CouponItemDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;&emsp;&emsp;type|券类型,可用值:voucher,paper|string||
|&emsp;&emsp;&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;items|普通支付条目信息|array|PaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;&emsp;&emsp;source||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;ext|扩展字段:1、payTool:支付宝、微信、POS|object||
|&emsp;&emsp;&emsp;&emsp;details|门店分摊明细|array|PaymentItemDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;accounts|权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;lineItems|按项目支付条目信息|array|LinePaymentDto|
|&emsp;&emsp;&emsp;&emsp;orderItemIndex|对应订单行|string||
|&emsp;&emsp;&emsp;&emsp;credit||CreditPayDto|CreditPayDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;details|门店分摊明细|array|CreditPayDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;accounts|抵扣权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;coupons|券支付信息|array|CouponItemDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|券类型,可用值:voucher,paper|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;items|普通支付条目|array|PaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;source||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ext|扩展字段:1、payTool:支付宝、微信、POS|object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;details|门店分摊明细|array|PaymentItemDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;accounts|权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"orderId": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"totalAmount": 0,
			"netAmount": 0,
			"operator": {
				"id": "",
				"name": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"createTime": "",
			"effectiveTime": "",
			"status": "",
			"type": "",
			"orderType": "",
			"processingType": "",
			"reduction": {
				"amount": 0,
				"reason": ""
			},
			"credit": {
				"billingItemId": "",
				"credit": 0,
				"payAmount": 0,
				"details": [
					{
						"payAmount": 0,
						"clinicId": "",
						"credit": 0
					}
				],
				"accounts": [
					{
						"id": "",
						"type": 0,
						"amount": 0,
						"quantity": 0
					}
				]
			},
			"coupons": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"payAmount": 0,
					"netAmount": 0,
					"billingItemId": ""
				}
			],
			"items": [
				{
					"billingItemId": "",
					"method": {
						"code": "",
						"name": "",
						"system": ""
					},
					"payAmount": 0,
					"netAmount": 0,
					"note": "",
					"source": {
						"id": "",
						"name": ""
					},
					"ext": {},
					"details": [
						{
							"payAmount": 0,
							"clinicId": ""
						}
					],
					"accounts": [
						{
							"id": "",
							"type": 0,
							"amount": 0,
							"quantity": 0
						}
					]
				}
			],
			"lineItems": [
				{
					"orderItemIndex": "",
					"credit": {},
					"coupons": [
						{
							"id": "",
							"name": "",
							"number": "",
							"type": "",
							"payAmount": 0,
							"netAmount": 0,
							"billingItemId": ""
						}
					],
					"items": [
						{}
					]
				}
			]
		}
	],
	"number": 0
}
```


## 获取授权机构下的支付方式


**接口地址**:`/api/v1/billing/payment-method`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PaymentMethodDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|代码|string||
|name|名称|string||
|system|编码系统|string||
|id|唯一ID|string||
|enable|是否启用状态|boolean||
|checkoutAmount|是否计入收银业绩|boolean||
|executionPerformance|是否计入执行业绩|boolean||
|refundToAccount|是否退款到系统账户(已废弃)|boolean||
|groupCode|收款类型code|string||
|groupName|收款类型名称|string||


**响应示例**:
```javascript
[
	{
		"code": "",
		"name": "",
		"system": "",
		"id": "",
		"enable": true,
		"checkoutAmount": true,
		"executionPerformance": true,
		"refundToAccount": true,
		"groupCode": "",
		"groupName": ""
	}
]
```


## 作废收款单


**接口地址**:`/api/v1/billing/payment/discard`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "paymentId": "",
  "operatorId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|billingPaymentDiscardParam|作废收款单请求参数|body|true|BillingPaymentDiscardParam|BillingPaymentDiscardParam|
|&emsp;&emsp;paymentId|收款单ID||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取支付的签名图片（包含无有效签名结果）


**接口地址**:`/api/v1/billing/payment/list-signature`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "billingIds": [],
  "includeNull": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|listBillingSignatureParams|批量获取收款单签名图片|body|true|ListBillingSignatureParams|ListBillingSignatureParams|
|&emsp;&emsp;billingIds|收款单id - 列表||true|array|string|
|&emsp;&emsp;includeNull|是否包含无签名数据的结果, 默认false||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PaymentSignatureDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|signatureId|签名唯一ID - null则无签名|string||
|imageBase64|图片base64字符串 - null则无签名|string||
|signTime|签名时间 - null则无签名|string(date-time)|string(date-time)|
|billingId||string||


**响应示例**:
```javascript
[
	{
		"signatureId": "",
		"imageBase64": "",
		"signTime": "",
		"billingId": ""
	}
]
```


## 获取授权机构下的收银摘要数据 - 收银详细信息


**接口地址**:`/api/v1/billing/payment/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PaymentDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|orderId|订单Id|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|clinic||Clinic|Clinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|totalAmount|支付总额|number||
|netAmount|支付净额|number||
|operator||Cashier|Cashier|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|consultant||Consultant|Consultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|createTime|创建时间|string(date-time)|string(date-time)|
|effectiveTime|生效时间，如非特殊修改，等同于数据创建时间|string(date-time)|string(date-time)|
|status|支付记录状态,可用值:issue,fail,success,refund,cancel|string||
|type|支付记录类型(正常，付欠费),可用值:normal,due|string||
|orderType|订单类型,可用值:medical,spa,retail,medicine,repair,free,charge,prepay,inpatient,exchange,charge-transfer,prepay-transfer,medicine-transfer,transfer-out,exchange-out|string||
|processingType|收款单处理中类型(cancelling:撤销中, none:未在处理中),可用值:cancelling,none|string||
|reduction||ReductionDto|ReductionDto|
|&emsp;&emsp;amount|减免金额|number||
|&emsp;&emsp;reason|减免原因|string||
|credit||CreditPayDto|CreditPayDto|
|&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;credit|消耗积分点数|integer(int64)||
|&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;details|门店分摊明细|array|CreditPayDetailDto|
|&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;accounts|抵扣权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|coupons|券支付信息|array|CouponItemDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;type|券类型,可用值:voucher,paper|string||
|&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;billingItemId|支付条目ID|string||
|items|普通支付条目信息|array|PaymentItemDto|
|&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;source||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;ext|扩展字段:1、payTool:支付宝、微信、POS|object||
|&emsp;&emsp;details|门店分摊明细|array|PaymentItemDetailDto|
|&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;accounts|权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|lineItems|按项目支付条目信息|array|LinePaymentDto|
|&emsp;&emsp;orderItemIndex|对应订单行|string||
|&emsp;&emsp;credit||CreditPayDto|CreditPayDto|
|&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;&emsp;&emsp;details|门店分摊明细|array|CreditPayDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;credit|消耗积分点数|integer||
|&emsp;&emsp;&emsp;&emsp;accounts|抵扣权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;coupons|券支付信息|array|CouponItemDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;&emsp;&emsp;type|券类型,可用值:voucher,paper|string||
|&emsp;&emsp;&emsp;&emsp;payAmount|支付面额|number||
|&emsp;&emsp;&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;items|普通支付条目|array|PaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;billingItemId|支付条目ID|string||
|&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;&emsp;&emsp;source||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;ext|扩展字段:1、payTool:支付宝、微信、POS|object||
|&emsp;&emsp;&emsp;&emsp;details|门店分摊明细|array|PaymentItemDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;payAmount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;clinicId|门店|string||
|&emsp;&emsp;&emsp;&emsp;accounts|权益信息|array|AccountDetailDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|权益ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|权益类型|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||


**响应示例**:
```javascript
{
	"id": "",
	"number": "",
	"orderId": "",
	"customer": {
		"id": "",
		"name": ""
	},
	"clinic": {
		"id": "",
		"name": ""
	},
	"totalAmount": 0,
	"netAmount": 0,
	"operator": {
		"id": "",
		"name": ""
	},
	"consultant": {
		"id": "",
		"name": ""
	},
	"createTime": "",
	"effectiveTime": "",
	"status": "",
	"type": "",
	"orderType": "",
	"processingType": "",
	"reduction": {
		"amount": 0,
		"reason": ""
	},
	"credit": {
		"billingItemId": "",
		"credit": 0,
		"payAmount": 0,
		"details": [
			{
				"payAmount": 0,
				"clinicId": "",
				"credit": 0
			}
		],
		"accounts": [
			{
				"id": "",
				"type": 0,
				"amount": 0,
				"quantity": 0
			}
		]
	},
	"coupons": [
		{
			"id": "",
			"name": "",
			"number": "",
			"type": "",
			"payAmount": 0,
			"netAmount": 0,
			"billingItemId": ""
		}
	],
	"items": [
		{
			"billingItemId": "",
			"method": {
				"code": "",
				"name": "",
				"system": ""
			},
			"payAmount": 0,
			"netAmount": 0,
			"note": "",
			"source": {
				"id": "",
				"name": ""
			},
			"ext": {},
			"details": [
				{
					"payAmount": 0,
					"clinicId": ""
				}
			],
			"accounts": [
				{
					"id": "",
					"type": 0,
					"amount": 0,
					"quantity": 0
				}
			]
		}
	],
	"lineItems": [
		{
			"orderItemIndex": "",
			"credit": {},
			"coupons": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"payAmount": 0,
					"netAmount": 0,
					"billingItemId": ""
				}
			],
			"items": [
				{}
			]
		}
	]
}
```


## 创建储值金订单，创建后为待支付订单，忽略所有审批流程


**接口地址**:`/api/v1/billing/prepaid-order`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "customerId": "",
  "participants": {
    "developerId": "",
    "doctorId": "",
    "beauticianId": "",
    "nurseId": "",
    "departmentId": "",
    "consultantId": ""
  },
  "external": {
    "system": "",
    "number": ""
  },
  "referrer": {
    "referrerId": "",
    "internal": true
  },
  "createdAt": "",
  "operatorId": "",
  "note": "",
  "orderType": "",
  "rechargeItem": {
    "amount": 0,
    "giftcash": 0
  },
  "promotion": [
    {
      "id": "",
      "quantity": 0,
      "qty": 0
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createPrepaidOrderParams|创建销售订单参数|body|true|CreatePrepaidOrderParams|CreatePrepaidOrderParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;customerId|顾客信息||true|string||
|&emsp;&emsp;participants|||false|Participants|Participants|
|&emsp;&emsp;&emsp;&emsp;developerId|开发人||false|string||
|&emsp;&emsp;&emsp;&emsp;doctorId|医生||false|string||
|&emsp;&emsp;&emsp;&emsp;beauticianId|美容师||false|string||
|&emsp;&emsp;&emsp;&emsp;nurseId|护士||false|string||
|&emsp;&emsp;&emsp;&emsp;departmentId|开单科室||false|string||
|&emsp;&emsp;&emsp;&emsp;consultantId|开单咨询师||false|string||
|&emsp;&emsp;external|||false|External|External|
|&emsp;&emsp;&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]||true|string||
|&emsp;&emsp;&emsp;&emsp;number|外部订单号||true|string||
|&emsp;&emsp;referrer|||false|ReferrerParam|ReferrerParam|
|&emsp;&emsp;&emsp;&emsp;referrerId|二级渠道ID||true|string||
|&emsp;&emsp;&emsp;&emsp;internal|是否内部渠道(referrerId是否会员ID)||false|boolean||
|&emsp;&emsp;createdAt|创建时间(ISO-8601标准格式)，仅允许指定到过去时间||false|string(date-time)||
|&emsp;&emsp;operatorId|创建人员工ID(开单人)||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;orderType|订单类型(储值金，预充值),可用值:charge,prepay||true|string||
|&emsp;&emsp;rechargeItem|||false|RechargeItem|RechargeItem|
|&emsp;&emsp;&emsp;&emsp;amount|充值或者预付金额||false|number||
|&emsp;&emsp;&emsp;&emsp;giftcash|赠送增值金，默认为0,当orderType为prepay时选填||false|number||
|&emsp;&emsp;promotion|促销活动，可多选||false|array|PromotionActivity|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID||false|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;qty|||false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取授权机构下的退款数据 - 退款列表


**接口地址**:`/api/v1/billing/refund`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所ID|query|false|string||
|customerId|顾客ID|query|false|string||
|status|状态(apply,wait-finance-operation,success)|query|false|array|string|
|type|账户类型(sys-account,other-account)|query|false|array|string|
|bizType|退款类型(订单/账户),可用值:order,account|query|false|string||
|withLinePayment|是否包含项目内支付明细(默认否)|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageRefundDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|RefundDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;number|退款单号|string||
|&emsp;&emsp;orderId|订单ID|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;type|退款方式（线上退款，线下退款）,可用值:sys-account,other-account|string||
|&emsp;&emsp;bizType|退款类型（订单/账户）,可用值:order,account|string||
|&emsp;&emsp;refundType|退款单类型（普通退款/换购换出退款/转赠转出退款）,可用值:refund,exchange-out,transfer-out|string||
|&emsp;&emsp;status|状态，参考wiki/补充文档/状态一览,可用值:apply申请退款,success退款成功,fail退款失败,finance-operation等待财务确认,cancelled退款取消,deleted退款作废|string||
|&emsp;&emsp;amount|退款总额|number||
|&emsp;&emsp;items|退单项目|array|RefundItemDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,combination,promotion,card,card-service,card-product,balance,prepay,reward|string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;amount|退款金额(实退金额)|number||
|&emsp;&emsp;&emsp;&emsp;transactionAmount|抵扣销售金额|number||
|&emsp;&emsp;&emsp;&emsp;executionRecordId|关联已执行记录ID，service专有，纠纷退款|string||
|&emsp;&emsp;&emsp;&emsp;envelopeName|营销分类名称|string||
|&emsp;&emsp;&emsp;&emsp;envelopeType|营销分类类型,可用值:card,promotion,combination|string||
|&emsp;&emsp;&emsp;&emsp;subItems|子条目(组合项目)，promotion专有|array|RefundItemDto|
|&emsp;&emsp;&emsp;&emsp;payments|支付分摊明细|array|RefundPaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;&emsp;&emsp;orderLineIndex||string||
|&emsp;&emsp;payments|支付明细|array|RefundPaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;bankPayment||RefundToBankDetailDto|RefundToBankDetailDto|
|&emsp;&emsp;&emsp;&emsp;name|收款方名称|string||
|&emsp;&emsp;&emsp;&emsp;account|账户号|string||
|&emsp;&emsp;&emsp;&emsp;bankName|开户行|string||
|&emsp;&emsp;&emsp;&emsp;branchName|开户支行|string||
|&emsp;&emsp;&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;createdAt|退款发起时间|string(date-time)||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;refundedAt|退款时间|string(date-time)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"orderId": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"type": "",
			"bizType": "",
			"refundType": "",
			"status": "",
			"amount": 0,
			"items": [
				{
					"id": "",
					"name": "",
					"type": "",
					"spec": "",
					"unit": "",
					"quantity": 0,
					"amount": 0,
					"transactionAmount": 0,
					"executionRecordId": "",
					"envelopeName": "",
					"envelopeType": "",
					"subItems": [
						{
							"id": "",
							"name": "",
							"type": "",
							"spec": "",
							"unit": "",
							"quantity": 0,
							"amount": 0,
							"transactionAmount": 0,
							"executionRecordId": "",
							"envelopeName": "",
							"envelopeType": "",
							"subItems": [
								{}
							],
							"payments": [
								{
									"method": {
										"code": "",
										"name": "",
										"system": ""
									},
									"amount": 0,
									"note": ""
								}
							],
							"orderLineIndex": ""
						}
					],
					"payments": [
						{}
					],
					"orderLineIndex": ""
				}
			],
			"payments": [
				{}
			],
			"bankPayment": {
				"name": "",
				"account": "",
				"bankName": "",
				"branchName": "",
				"amount": 0,
				"note": ""
			},
			"createdAt": "",
			"creator": {
				"id": "",
				"name": ""
			},
			"refundedAt": ""
		}
	],
	"number": 0
}
```


## 获取授权机构下的退款数据 - 单个退款


**接口地址**:`/api/v1/billing/refund/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|RefundDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|ID|string||
|number|退款单号|string||
|orderId|订单ID|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|clinic||Clinic|Clinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|type|退款方式（线上退款，线下退款）,可用值:sys-account,other-account|string||
|bizType|退款类型（订单/账户）,可用值:order,account|string||
|refundType|退款单类型（普通退款/换购换出退款/转赠转出退款）,可用值:refund,exchange-out,transfer-out|string||
|status|状态，参考wiki/补充文档/状态一览,可用值:apply申请退款,success退款成功,fail退款失败,finance-operation等待财务确认,cancelled退款取消,deleted退款作废|string||
|amount|退款总额|number||
|items|退单项目|array|RefundItemDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型,可用值:service,product,combination,promotion,card,card-service,card-product,balance,prepay,reward|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;quantity|数量|integer(int32)||
|&emsp;&emsp;amount|退款金额(实退金额)|number||
|&emsp;&emsp;transactionAmount|抵扣销售金额|number||
|&emsp;&emsp;executionRecordId|关联已执行记录ID，service专有，纠纷退款|string||
|&emsp;&emsp;envelopeName|营销分类名称|string||
|&emsp;&emsp;envelopeType|营销分类类型,可用值:card,promotion,combination|string||
|&emsp;&emsp;subItems|子条目(组合项目)，promotion专有|array|RefundItemDto|
|&emsp;&emsp;payments|支付分摊明细|array|RefundPaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;orderLineIndex||string||
|payments|支付明细|array|RefundPaymentItemDto|
|&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;note|备注|string||
|bankPayment||RefundToBankDetailDto|RefundToBankDetailDto|
|&emsp;&emsp;name|收款方名称|string||
|&emsp;&emsp;account|账户号|string||
|&emsp;&emsp;bankName|开户行|string||
|&emsp;&emsp;branchName|开户支行|string||
|&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;note|备注|string||
|createdAt|退款发起时间|string(date-time)|string(date-time)|
|creator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|refundedAt|退款时间|string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"id": "",
	"number": "",
	"orderId": "",
	"customer": {
		"id": "",
		"name": ""
	},
	"clinic": {
		"id": "",
		"name": ""
	},
	"type": "",
	"bizType": "",
	"refundType": "",
	"status": "",
	"amount": 0,
	"items": [
		{
			"id": "",
			"name": "",
			"type": "",
			"spec": "",
			"unit": "",
			"quantity": 0,
			"amount": 0,
			"transactionAmount": 0,
			"executionRecordId": "",
			"envelopeName": "",
			"envelopeType": "",
			"subItems": [
				{
					"id": "",
					"name": "",
					"type": "",
					"spec": "",
					"unit": "",
					"quantity": 0,
					"amount": 0,
					"transactionAmount": 0,
					"executionRecordId": "",
					"envelopeName": "",
					"envelopeType": "",
					"subItems": [
						{}
					],
					"payments": [
						{
							"method": {
								"code": "",
								"name": "",
								"system": ""
							},
							"amount": 0,
							"note": ""
						}
					],
					"orderLineIndex": ""
				}
			],
			"payments": [
				{}
			],
			"orderLineIndex": ""
		}
	],
	"payments": [
		{
			"method": {
				"code": "",
				"name": "",
				"system": ""
			},
			"amount": 0,
			"note": ""
		}
	],
	"bankPayment": {
		"name": "",
		"account": "",
		"bankName": "",
		"branchName": "",
		"amount": 0,
		"note": ""
	},
	"createdAt": "",
	"creator": {
		"id": "",
		"name": ""
	},
	"refundedAt": ""
}
```


## 获取授权机构下的销售订单摘要数据 - 订单摘要信息


**接口地址**:`/api/v1/billing/sales-order`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所ID|query|false|string||
|customerId|顾客ID|query|false|string||
|number|订单号|query|false|string||
|status|状态(paying,paid,refunded)|query|false|array|string|
|type|类型(retail,medical,free,charge,prepay,spa)|query|false|array|string|
|visitId|关联到访ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageSalesOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|SalesOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;external||External|External|
|&emsp;&emsp;&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]|string||
|&emsp;&emsp;&emsp;&emsp;number|外部订单号|string||
|&emsp;&emsp;salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;referrer||Referrer|Referrer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;retailAmount|零售价金额，原价|number||
|&emsp;&emsp;transactionAmount|成交价金额，原价|number||
|&emsp;&emsp;totalArrears|当前欠款金额|number||
|&emsp;&emsp;items|销售订单条目信息|array|SimpleOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;id|SKU ID|string||
|&emsp;&emsp;&emsp;&emsp;name|SKU 名称|string||
|&emsp;&emsp;&emsp;&emsp;number|SKU 编号|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:service,product,promotion,card,card-service,card-product,balance,reward,prepay|string||
|&emsp;&emsp;&emsp;&emsp;index|序号|string||
|&emsp;&emsp;&emsp;&emsp;lineId|行/条目 id|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;aptitude|资质|string||
|&emsp;&emsp;&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;&emsp;&emsp;totalTransactionPrice|成交价总金额|number||
|&emsp;&emsp;&emsp;&emsp;arrears|当前欠款金额|number||
|&emsp;&emsp;&emsp;&emsp;subItems|子条目(组合项目)|array|SimpleOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;sourceId|来源条目ID - 卡项定义ID/已购买卡项条目ID|string||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;sales||Sales|Sales|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developer||Developer|Developer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;beautician||Beautician|Beautician|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;operator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;status|状态，参考wiki/补充文档/状态一览,可用值:draft,submitted,paying,partial-paid,paid,refunded,discarded,arrears-clear,orderItem-arrears-clear|string||
|&emsp;&emsp;approvalStatus|审批状态,可用值:approving,approved,rejected|string||
|&emsp;&emsp;type|类型,可用值:retail,medical,free,charge,prepay,spa,exchange,medical-transfer,prepay-transfer,charge-transfer|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;visitId|关联到访ID|string||
|&emsp;&emsp;createdAt|开单时间|string(date-time)||
|&emsp;&emsp;freeReason||FreeReason|FreeReason|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;developers|共同开发人|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"external": {
				"system": "",
				"number": ""
			},
			"salesClinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"referrer": {
				"id": "",
				"name": ""
			},
			"retailAmount": 0,
			"transactionAmount": 0,
			"totalArrears": 0,
			"items": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"index": "",
					"lineId": "",
					"unit": "",
					"aptitude": "",
					"specification": "",
					"quantity": 0,
					"unitRetailPrice": 0,
					"totalTransactionPrice": 0,
					"arrears": 0,
					"subItems": [
						{
							"id": "",
							"name": "",
							"number": "",
							"type": "",
							"index": "",
							"lineId": "",
							"unit": "",
							"aptitude": "",
							"specification": "",
							"quantity": 0,
							"unitRetailPrice": 0,
							"totalTransactionPrice": 0,
							"arrears": 0,
							"subItems": [
								{}
							],
							"sourceId": "",
							"note": ""
						}
					],
					"sourceId": "",
					"note": ""
				}
			],
			"customer": {
				"id": "",
				"name": ""
			},
			"sales": {
				"id": "",
				"name": ""
			},
			"developer": {
				"id": "",
				"name": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"beautician": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"operator": {
				"id": "",
				"name": ""
			},
			"status": "",
			"approvalStatus": "",
			"type": "",
			"note": "",
			"visitId": "",
			"createdAt": "",
			"freeReason": {
				"id": "",
				"name": ""
			},
			"developers": [
				{
					"id": "",
					"name": ""
				}
			]
		}
	],
	"number": 0
}
```


## 创建销售订单，创建后为待支付订单，忽略所有审批流程


**接口地址**:`/api/v1/billing/sales-order`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "customerId": "",
  "participants": {
    "developerId": "",
    "doctorId": "",
    "beauticianId": "",
    "nurseId": "",
    "departmentId": "",
    "consultantId": ""
  },
  "external": {
    "system": "",
    "number": ""
  },
  "referrer": {
    "referrerId": "",
    "internal": true
  },
  "details": [
    {
      "itemType": "",
      "itemId": "",
      "unitRetailPrice": 0,
      "transactionTotalPrice": 0,
      "quantity": 0
    }
  ],
  "createdAt": "",
  "operatorId": "",
  "note": "",
  "orderType": "",
  "reductionId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createSalesOrderParams|创建销售订单参数|body|true|CreateSalesOrderParams|CreateSalesOrderParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;customerId|顾客信息||true|string||
|&emsp;&emsp;participants|||false|Participants|Participants|
|&emsp;&emsp;&emsp;&emsp;developerId|开发人||false|string||
|&emsp;&emsp;&emsp;&emsp;doctorId|医生||false|string||
|&emsp;&emsp;&emsp;&emsp;beauticianId|美容师||false|string||
|&emsp;&emsp;&emsp;&emsp;nurseId|护士||false|string||
|&emsp;&emsp;&emsp;&emsp;departmentId|开单科室||false|string||
|&emsp;&emsp;&emsp;&emsp;consultantId|开单咨询师||false|string||
|&emsp;&emsp;external|||false|External|External|
|&emsp;&emsp;&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]||true|string||
|&emsp;&emsp;&emsp;&emsp;number|外部订单号||true|string||
|&emsp;&emsp;referrer|||false|ReferrerParam|ReferrerParam|
|&emsp;&emsp;&emsp;&emsp;referrerId|二级渠道ID||true|string||
|&emsp;&emsp;&emsp;&emsp;internal|是否内部渠道(referrerId是否会员ID)||false|boolean||
|&emsp;&emsp;details|订单Item详情||true|array|OrderItemLine|
|&emsp;&emsp;&emsp;&emsp;itemType|Item类型,可用值:service,product,promotion,coupon-card||true|string||
|&emsp;&emsp;&emsp;&emsp;itemId|Item ID||true|string||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|单个零售价||false|number||
|&emsp;&emsp;&emsp;&emsp;transactionTotalPrice|成交总金额||false|number||
|&emsp;&emsp;&emsp;&emsp;quantity|数量||true|integer||
|&emsp;&emsp;createdAt|创建时间(ISO-8601标准格式) - 仅允许指定过去时间||false|string(date-time)||
|&emsp;&emsp;operatorId|创建人员工ID(开单人)||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;orderType|订单类型(零售、医美),可用值:retail,medical,free||true|string||
|&emsp;&emsp;reductionId|免单原因ID，参考字典代码:free-order-option（免单原因）||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 根据订单ID获取销售订单发票明细


**接口地址**:`/api/v1/billing/sales-order/list-invoices`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "orderIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|listInvoiceParams|批量获取订单发票|body|true|ListInvoiceParams|ListInvoiceParams|
|&emsp;&emsp;orderIds|订单id-列表||true|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SalesOrderInvoiceDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|发票记录唯一ID|string||
|orderId|所属订单ID|string||
|orderLineId|所属订单行ID|string||
|skuInfo||OrderLineItem|OrderLineItem|
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;unitPrice|单价|number||
|quantity|购买数量|integer(int32)|integer(int32)|
|totalRetailPrice|总价|number||
|discount|折扣|number||
|transactionAmount|成交价|number||
|totalCourseQty|总疗程数|integer(int32)|integer(int32)|
|invoiceNumber|发票号码|string||
|invoiceAmount|发票金额|number||
|invoiceTime|开票时间|string(date-time)|string(date-time)|
|invoiceBy|开票员工id|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"orderId": "",
		"orderLineId": "",
		"skuInfo": {
			"name": "",
			"spec": "",
			"unit": "",
			"unitPrice": 0
		},
		"quantity": 0,
		"totalRetailPrice": 0,
		"discount": 0,
		"transactionAmount": 0,
		"totalCourseQty": 0,
		"invoiceNumber": "",
		"invoiceAmount": 0,
		"invoiceTime": "",
		"invoiceBy": ""
	}
]
```


## 根据订单ID获取销售订单详细数据 - 订单详细信息


**接口地址**:`/api/v1/billing/sales-order/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SalesOrderDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|external||External|External|
|&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]|string||
|&emsp;&emsp;number|外部订单号|string||
|salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|referrer||Referrer|Referrer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|retailAmount|零售价金额，原价|number||
|transactionAmount|成交价金额，原价|number||
|totalArrears|当前欠款金额|number||
|items|销售订单条目信息|array|SimpleOrderItemDto|
|&emsp;&emsp;id|SKU ID|string||
|&emsp;&emsp;name|SKU 名称|string||
|&emsp;&emsp;number|SKU 编号|string||
|&emsp;&emsp;type|类型,可用值:service,product,promotion,card,card-service,card-product,balance,reward,prepay|string||
|&emsp;&emsp;index|序号|string||
|&emsp;&emsp;lineId|行/条目 id|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;aptitude|资质|string||
|&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;quantity|数量|integer(int32)||
|&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;totalTransactionPrice|成交价总金额|number||
|&emsp;&emsp;arrears|当前欠款金额|number||
|&emsp;&emsp;subItems|子条目(组合项目)|array|SimpleOrderItemDto|
|&emsp;&emsp;sourceId|来源条目ID - 卡项定义ID/已购买卡项条目ID|string||
|&emsp;&emsp;note|备注|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|sales||Sales|Sales|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|developer||Developer|Developer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|consultant||Consultant|Consultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|beautician||Beautician|Beautician|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|doctor||Doctor|Doctor|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|operator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|status|状态，参考wiki/补充文档/状态一览,可用值:draft,submitted,paying,partial-paid,paid,refunded,discarded,arrears-clear,orderItem-arrears-clear|string||
|approvalStatus|审批状态,可用值:approving,approved,rejected|string||
|type|类型,可用值:retail,medical,free,charge,prepay,spa,exchange,medical-transfer,prepay-transfer,charge-transfer|string||
|note|备注|string||
|visitId|关联到访ID|string||
|createdAt|开单时间|string(date-time)|string(date-time)|
|freeReason||FreeReason|FreeReason|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|developers|共同开发人|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|payments|历史支付信息|array|PaymentDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;orderId|订单Id|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;totalAmount|支付总额|number||
|&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;operator||Cashier|Cashier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;effectiveTime|生效时间，如非特殊修改，等同于数据创建时间|string(date-time)||
|&emsp;&emsp;status|支付记录状态,可用值:issue,fail,success,refund,cancel|string||
|&emsp;&emsp;type|支付记录类型(正常，付欠费),可用值:normal,due|string||
|&emsp;&emsp;orderType|订单类型,可用值:medical,spa,retail,medicine,repair,free,charge,prepay,inpatient,exchange,charge-transfer,prepay-transfer,medicine-transfer,transfer-out,exchange-out|string||
|&emsp;&emsp;processingType|收款单处理中类型(cancelling:撤销中, none:未在处理中),可用值:cancelling,none|string||
|netAmount|净价金额，扣除优惠券、积分等不计入财务收入部分|number||
|extensions|其他扩展信息|object||
|origin||Origin|Origin|
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;value||string||


**响应示例**:
```javascript
{
	"id": "",
	"number": "",
	"external": {
		"system": "",
		"number": ""
	},
	"salesClinic": {
		"id": "",
		"name": ""
	},
	"medicalDepartment": {
		"id": "",
		"name": ""
	},
	"referrer": {
		"id": "",
		"name": ""
	},
	"retailAmount": 0,
	"transactionAmount": 0,
	"totalArrears": 0,
	"items": [
		{
			"id": "",
			"name": "",
			"number": "",
			"type": "",
			"index": "",
			"lineId": "",
			"unit": "",
			"aptitude": "",
			"specification": "",
			"quantity": 0,
			"unitRetailPrice": 0,
			"totalTransactionPrice": 0,
			"arrears": 0,
			"subItems": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"index": "",
					"lineId": "",
					"unit": "",
					"aptitude": "",
					"specification": "",
					"quantity": 0,
					"unitRetailPrice": 0,
					"totalTransactionPrice": 0,
					"arrears": 0,
					"subItems": [
						{}
					],
					"sourceId": "",
					"note": ""
				}
			],
			"sourceId": "",
			"note": ""
		}
	],
	"customer": {
		"id": "",
		"name": ""
	},
	"sales": {
		"id": "",
		"name": ""
	},
	"developer": {
		"id": "",
		"name": ""
	},
	"consultant": {
		"id": "",
		"name": ""
	},
	"beautician": {
		"id": "",
		"name": ""
	},
	"doctor": {
		"id": "",
		"name": ""
	},
	"operator": {
		"id": "",
		"name": ""
	},
	"status": "",
	"approvalStatus": "",
	"type": "",
	"note": "",
	"visitId": "",
	"createdAt": "",
	"freeReason": {
		"id": "",
		"name": ""
	},
	"developers": [
		{
			"id": "",
			"name": ""
		}
	],
	"payments": [
		{
			"id": "",
			"number": "",
			"orderId": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"totalAmount": 0,
			"netAmount": 0,
			"operator": {
				"id": "",
				"name": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"createTime": "",
			"effectiveTime": "",
			"status": "",
			"type": "",
			"orderType": "",
			"processingType": ""
		}
	],
	"netAmount": 0,
	"extensions": {},
	"origin": {
		"type": {
			"code": "",
			"name": "",
			"system": ""
		},
		"value": ""
	}
}
```


## 销售订单废弃，未支付订单可废弃，废弃后订单不可操作


**接口地址**:`/api/v1/billing/sales-order/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 销售订单支付，支付后为已支付订单，忽略所有审批流程


**接口地址**:`/api/v1/billing/sales-order/{id}/payment`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "credit": 0,
  "arrears": 0,
  "methods": [
    {
      "methodCode": "",
      "amount": 0,
      "note": ""
    }
  ],
  "clinicId": "",
  "consultantId": "",
  "operatorId": "",
  "effectiveTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|payOrderParam|支付订单参数|body|true|PayOrderParam|PayOrderParam|
|&emsp;&emsp;credit|用于抵扣积分点数（1.仅支持医美订单；2.确保能被'兑换基数'整除，默认'1000'兑1元，具体请参考"系统参数设置"）||false|integer(int64)||
|&emsp;&emsp;arrears|欠费||false|number||
|&emsp;&emsp;methods|支付详情||false|array|MethodParam|
|&emsp;&emsp;&emsp;&emsp;methodCode|支付方式Code，参考系统支付方式配置；||true|string||
|&emsp;&emsp;&emsp;&emsp;amount|支付金额，元||true|number||
|&emsp;&emsp;&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;clinicId|操作门店ID||false|string||
|&emsp;&emsp;consultantId|收款咨询师ID||false|string||
|&emsp;&emsp;operatorId|操作员工ID||false|string||
|&emsp;&emsp;effectiveTime|支付生效时间，不指定则为当前时间(格式参照ISO-8601, 如 '2019-08-08')||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|SalesOrderDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|external||External|External|
|&emsp;&emsp;system|外部系统代号 参考系统配置-电商平台设置，字典[business-platform]|string||
|&emsp;&emsp;number|外部订单号|string||
|salesClinic||SalesClinic|SalesClinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|referrer||Referrer|Referrer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|retailAmount|零售价金额，原价|number||
|transactionAmount|成交价金额，原价|number||
|totalArrears|当前欠款金额|number||
|items|销售订单条目信息|array|SimpleOrderItemDto|
|&emsp;&emsp;id|SKU ID|string||
|&emsp;&emsp;name|SKU 名称|string||
|&emsp;&emsp;number|SKU 编号|string||
|&emsp;&emsp;type|类型,可用值:service,product,promotion,card,card-service,card-product,balance,reward,prepay|string||
|&emsp;&emsp;index|序号|string||
|&emsp;&emsp;lineId|行/条目 id|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;aptitude|资质|string||
|&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;quantity|数量|integer(int32)||
|&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;totalTransactionPrice|成交价总金额|number||
|&emsp;&emsp;arrears|当前欠款金额|number||
|&emsp;&emsp;subItems|子条目(组合项目)|array|SimpleOrderItemDto|
|&emsp;&emsp;sourceId|来源条目ID - 卡项定义ID/已购买卡项条目ID|string||
|&emsp;&emsp;note|备注|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|sales||Sales|Sales|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|developer||Developer|Developer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|consultant||Consultant|Consultant|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|beautician||Beautician|Beautician|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|doctor||Doctor|Doctor|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|operator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|status|状态，参考wiki/补充文档/状态一览,可用值:draft,submitted,paying,partial-paid,paid,refunded,discarded,arrears-clear,orderItem-arrears-clear|string||
|approvalStatus|审批状态,可用值:approving,approved,rejected|string||
|type|类型,可用值:retail,medical,free,charge,prepay,spa,exchange,medical-transfer,prepay-transfer,charge-transfer|string||
|note|备注|string||
|visitId|关联到访ID|string||
|createdAt|开单时间|string(date-time)|string(date-time)|
|freeReason||FreeReason|FreeReason|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|developers|共同开发人|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|payments|历史支付信息|array|PaymentDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;orderId|订单Id|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;totalAmount|支付总额|number||
|&emsp;&emsp;netAmount|支付净额|number||
|&emsp;&emsp;operator||Cashier|Cashier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;consultant||Consultant|Consultant|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createTime|创建时间|string(date-time)||
|&emsp;&emsp;effectiveTime|生效时间，如非特殊修改，等同于数据创建时间|string(date-time)||
|&emsp;&emsp;status|支付记录状态,可用值:issue,fail,success,refund,cancel|string||
|&emsp;&emsp;type|支付记录类型(正常，付欠费),可用值:normal,due|string||
|&emsp;&emsp;orderType|订单类型,可用值:medical,spa,retail,medicine,repair,free,charge,prepay,inpatient,exchange,charge-transfer,prepay-transfer,medicine-transfer,transfer-out,exchange-out|string||
|&emsp;&emsp;processingType|收款单处理中类型(cancelling:撤销中, none:未在处理中),可用值:cancelling,none|string||
|netAmount|净价金额，扣除优惠券、积分等不计入财务收入部分|number||
|extensions|其他扩展信息|object||
|origin||Origin|Origin|
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;value||string||


**响应示例**:
```javascript
{
	"id": "",
	"number": "",
	"external": {
		"system": "",
		"number": ""
	},
	"salesClinic": {
		"id": "",
		"name": ""
	},
	"medicalDepartment": {
		"id": "",
		"name": ""
	},
	"referrer": {
		"id": "",
		"name": ""
	},
	"retailAmount": 0,
	"transactionAmount": 0,
	"totalArrears": 0,
	"items": [
		{
			"id": "",
			"name": "",
			"number": "",
			"type": "",
			"index": "",
			"lineId": "",
			"unit": "",
			"aptitude": "",
			"specification": "",
			"quantity": 0,
			"unitRetailPrice": 0,
			"totalTransactionPrice": 0,
			"arrears": 0,
			"subItems": [
				{
					"id": "",
					"name": "",
					"number": "",
					"type": "",
					"index": "",
					"lineId": "",
					"unit": "",
					"aptitude": "",
					"specification": "",
					"quantity": 0,
					"unitRetailPrice": 0,
					"totalTransactionPrice": 0,
					"arrears": 0,
					"subItems": [
						{}
					],
					"sourceId": "",
					"note": ""
				}
			],
			"sourceId": "",
			"note": ""
		}
	],
	"customer": {
		"id": "",
		"name": ""
	},
	"sales": {
		"id": "",
		"name": ""
	},
	"developer": {
		"id": "",
		"name": ""
	},
	"consultant": {
		"id": "",
		"name": ""
	},
	"beautician": {
		"id": "",
		"name": ""
	},
	"doctor": {
		"id": "",
		"name": ""
	},
	"operator": {
		"id": "",
		"name": ""
	},
	"status": "",
	"approvalStatus": "",
	"type": "",
	"note": "",
	"visitId": "",
	"createdAt": "",
	"freeReason": {
		"id": "",
		"name": ""
	},
	"developers": [
		{
			"id": "",
			"name": ""
		}
	],
	"payments": [
		{
			"id": "",
			"number": "",
			"orderId": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"totalAmount": 0,
			"netAmount": 0,
			"operator": {
				"id": "",
				"name": ""
			},
			"consultant": {
				"id": "",
				"name": ""
			},
			"createTime": "",
			"effectiveTime": "",
			"status": "",
			"type": "",
			"orderType": "",
			"processingType": ""
		}
	],
	"netAmount": 0,
	"extensions": {},
	"origin": {
		"type": {
			"code": "",
			"name": "",
			"system": ""
		},
		"value": ""
	}
}
```


## 销售订单分行支付，支付后为已支付订单，忽略所有审批流程


**接口地址**:`/api/v1/billing/sales-order/{id}/payment/by-line`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "consultantId": "",
  "operatorId": "",
  "effectiveTime": "",
  "lineParams": [
    {
      "credit": 0,
      "arrears": 0,
      "methods": [
        {
          "methodCode": "",
          "amount": 0,
          "note": "",
          "accountItemId": ""
        }
      ],
      "index": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||
|payOrderByLineParam|分行支付订单参数|body|true|PayOrderByLineParam|PayOrderByLineParam|
|&emsp;&emsp;clinicId|操作门店ID||false|string||
|&emsp;&emsp;consultantId|收款咨询师ID||false|string||
|&emsp;&emsp;operatorId|操作员工ID||false|string||
|&emsp;&emsp;effectiveTime|支付生效时间，不指定则为当前时间(格式参照ISO-8601, 如 '2019-08-08')||false|string(date-time)||
|&emsp;&emsp;lineParams|按行支付参数||true|array|ByLinePayParam|
|&emsp;&emsp;&emsp;&emsp;credit|用于抵扣积分点数（1.仅支持医美订单；2.确保能被'兑换基数'整除，默认'1000'兑1元，具体请参考"系统参数设置"）||false|integer||
|&emsp;&emsp;&emsp;&emsp;arrears|欠费||false|number||
|&emsp;&emsp;&emsp;&emsp;methods|支付详情||false|array|ByLineMethodParam|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;methodCode|支付方式Code，参考系统支付方式配置；||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;amount|支付金额，元||true|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;accountItemId|抵扣/折让权益id，如电子券权益/实例id||false|string||
|&emsp;&emsp;&emsp;&emsp;index|订单行编号||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 根据订单ID获取销售订单退款详细数据 - 订单退款详细信息


**接口地址**:`/api/v1/billing/sales-order/{id}/refund`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|RefundDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|ID|string||
|number|退款单号|string||
|orderId|订单ID|string||
|customer||Customer|Customer|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|clinic||Clinic|Clinic|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|type|退款方式（线上退款，线下退款）,可用值:sys-account,other-account|string||
|bizType|退款类型（订单/账户）,可用值:order,account|string||
|refundType|退款单类型（普通退款/换购换出退款/转赠转出退款）,可用值:refund,exchange-out,transfer-out|string||
|status|状态，参考wiki/补充文档/状态一览,可用值:apply申请退款,success退款成功,fail退款失败,finance-operation等待财务确认,cancelled退款取消,deleted退款作废|string||
|amount|退款总额|number||
|items|退单项目|array|RefundItemDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型,可用值:service,product,combination,promotion,card,card-service,card-product,balance,prepay,reward|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;quantity|数量|integer(int32)||
|&emsp;&emsp;amount|退款金额(实退金额)|number||
|&emsp;&emsp;transactionAmount|抵扣销售金额|number||
|&emsp;&emsp;executionRecordId|关联已执行记录ID，service专有，纠纷退款|string||
|&emsp;&emsp;envelopeName|营销分类名称|string||
|&emsp;&emsp;envelopeType|营销分类类型,可用值:card,promotion,combination|string||
|&emsp;&emsp;subItems|子条目(组合项目)，promotion专有|array|RefundItemDto|
|&emsp;&emsp;payments|支付分摊明细|array|RefundPaymentItemDto|
|&emsp;&emsp;&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;orderLineIndex||string||
|payments|支付明细|array|RefundPaymentItemDto|
|&emsp;&emsp;method||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;note|备注|string||
|bankPayment||RefundToBankDetailDto|RefundToBankDetailDto|
|&emsp;&emsp;name|收款方名称|string||
|&emsp;&emsp;account|账户号|string||
|&emsp;&emsp;bankName|开户行|string||
|&emsp;&emsp;branchName|开户支行|string||
|&emsp;&emsp;amount|支付金额|number||
|&emsp;&emsp;note|备注|string||
|createdAt|退款发起时间|string(date-time)|string(date-time)|
|creator||Creator|Creator|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|refundedAt|退款时间|string(date-time)|string(date-time)|


**响应示例**:
```javascript
[
	{
		"id": "",
		"number": "",
		"orderId": "",
		"customer": {
			"id": "",
			"name": ""
		},
		"clinic": {
			"id": "",
			"name": ""
		},
		"type": "",
		"bizType": "",
		"refundType": "",
		"status": "",
		"amount": 0,
		"items": [
			{
				"id": "",
				"name": "",
				"type": "",
				"spec": "",
				"unit": "",
				"quantity": 0,
				"amount": 0,
				"transactionAmount": 0,
				"executionRecordId": "",
				"envelopeName": "",
				"envelopeType": "",
				"subItems": [
					{
						"id": "",
						"name": "",
						"type": "",
						"spec": "",
						"unit": "",
						"quantity": 0,
						"amount": 0,
						"transactionAmount": 0,
						"executionRecordId": "",
						"envelopeName": "",
						"envelopeType": "",
						"subItems": [
							{}
						],
						"payments": [
							{
								"method": {
									"code": "",
									"name": "",
									"system": ""
								},
								"amount": 0,
								"note": ""
							}
						],
						"orderLineIndex": ""
					}
				],
				"payments": [
					{}
				],
				"orderLineIndex": ""
			}
		],
		"payments": [
			{
				"method": {
					"code": "",
					"name": "",
					"system": ""
				},
				"amount": 0,
				"note": ""
			}
		],
		"bankPayment": {
			"name": "",
			"account": "",
			"bankName": "",
			"branchName": "",
			"amount": 0,
			"note": ""
		},
		"createdAt": "",
		"creator": {
			"id": "",
			"name": ""
		},
		"refundedAt": ""
	}
]
```


## 根据订单ID查询服务费


**接口地址**:`/api/v1/billing/service-fee/order`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "orderId": "",
  "includeCancelled": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|serviceFeeByOrderQueryParams|按订单ID查询服务费参数|body|true|ServiceFeeByOrderQueryParams|ServiceFeeByOrderQueryParams|
|&emsp;&emsp;orderId|服务费订单ID||true|string||
|&emsp;&emsp;includeCancelled|包含已作废的服务费, 默认: 包含 true||false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ServiceFeeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|clinicId|服务费门店ID|string||
|number|服务费明细记录编号|string||
|serviceFeeAmount|服务费金额|number||
|bizTime|业务时间|string(date-time)|string(date-time)|
|orderId|服务费订单ID|string||
|orderLineId|对应订单行ID|string||
|orderLineItemId|对应订单条目ID|string||
|refundOrderId|来源退款单id|string||
|refundOrderLineId|来源退款单行id|string||
|cancelled|已作废|boolean||


**响应示例**:
```javascript
[
	{
		"id": "",
		"clinicId": "",
		"number": "",
		"serviceFeeAmount": 0,
		"bizTime": "",
		"orderId": "",
		"orderLineId": "",
		"orderLineItemId": "",
		"refundOrderId": "",
		"refundOrderLineId": "",
		"cancelled": true
	}
]
```


## 分页查询服务费


**接口地址**:`/api/v1/billing/service-fee/page`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "start": "",
  "end": "",
  "includeCancelled": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|serviceFeeQueryParams|查询服务费参数|body|true|ServiceFeeQueryParams|ServiceFeeQueryParams|
|&emsp;&emsp;clinicId|服务费门店ID||true|string||
|&emsp;&emsp;start|业务时间(ISO-8601标准格式) yyyy-MM-dd 格式||true|string(date-time)||
|&emsp;&emsp;end|业务时间(ISO-8601标准格式) yyyy-MM-dd 格式||true|string(date-time)||
|&emsp;&emsp;includeCancelled|包含已作废的服务费, 默认: 包含 true||false|boolean||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageServiceFeeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|ServiceFeeDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;clinicId|服务费门店ID|string||
|&emsp;&emsp;number|服务费明细记录编号|string||
|&emsp;&emsp;serviceFeeAmount|服务费金额|number||
|&emsp;&emsp;bizTime|业务时间|string(date-time)||
|&emsp;&emsp;orderId|服务费订单ID|string||
|&emsp;&emsp;orderLineId|对应订单行ID|string||
|&emsp;&emsp;orderLineItemId|对应订单条目ID|string||
|&emsp;&emsp;refundOrderId|来源退款单id|string||
|&emsp;&emsp;refundOrderLineId|来源退款单行id|string||
|&emsp;&emsp;cancelled|已作废|boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"clinicId": "",
			"number": "",
			"serviceFeeAmount": 0,
			"bizTime": "",
			"orderId": "",
			"orderLineId": "",
			"orderLineItemId": "",
			"refundOrderId": "",
			"refundOrderLineId": "",
			"cancelled": true
		}
	],
	"number": 0
}
```


## 获取授权机构下转诊-转疗数据


**接口地址**:`/api/v1/billing/transfer`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|fromClinicId|转出门店ID|query|false|string||
|toClinicId|转入门店ID|query|false|string||
|customerId|客户ID|query|false|string||
|type|类型(转诊，转疗, 项目转疗),可用值:customer,order,product-item|query|false|string||
|status|状态编码(submitted,accepted,rejected,cancelled)|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageTransferRecordDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|TransferRecordDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;source||TransferSource|TransferSource|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;target||TransferTarget|TransferTarget|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;occurredAt|生效时间|string(date-time)||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;type||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;orderIds|关联订单列表|array|string|
|&emsp;&emsp;accountItemIds|关联权益列表|array|string|
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"customer": {
				"id": "",
				"name": ""
			},
			"source": {
				"id": "",
				"name": ""
			},
			"target": {
				"id": "",
				"name": ""
			},
			"occurredAt": "",
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"type": {
				"code": "",
				"name": "",
				"system": ""
			},
			"note": "",
			"orderIds": [],
			"accountItemIds": []
		}
	],
	"number": 0
}
```


# 07. 市场营销集成


## 查询授权机构下的卡项信息


**接口地址**:`/api/v1/market/card`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|clinicId|诊所ID|query|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|keyword|关键字（名称）|query|false|string||
|status|销售状态（已作废/销售中/已过期/已下架）,可用值:disabled,sales,overdue,off-shelves|query|false|string||
|liveShowFilter|是否可直播售卖|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageFusionCardDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|FusionCardDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;allowedClinics|归属门店（为空则没有限制）|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;start|发行日期 - 起始|string(date-time)||
|&emsp;&emsp;end|发行日期 - 结束|string(date-time)||
|&emsp;&emsp;scope||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;description|备注|string||
|&emsp;&emsp;status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;quantity|发行数（0为不限）|integer(int32)||
|&emsp;&emsp;cardTags|卡项标签集合|array|TagDictDto|
|&emsp;&emsp;&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;&emsp;&emsp;color|标签颜色|string||
|&emsp;&emsp;price|售价|number||
|&emsp;&emsp;groups|内容条目|array|CardGroupDto|
|&emsp;&emsp;&emsp;&emsp;index|卡内组序号|string||
|&emsp;&emsp;&emsp;&emsp;type|类型(固定项目，N选M，次卡，账户权益，打折权益，代金券权益),可用值:package,combination,point,store,discount,coupon|string||
|&emsp;&emsp;&emsp;&emsp;items|条目信息|array|CardGroupItemDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型(项目,商品,项目类别,商品类别,券,项目标签,商品标签,卡项,卡项标签),可用值:service,product,serviceCategory,productCategory,coupon,serviceTag,productTag,card,cardTag|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;salableQuantity|可售数量（为空则不限）- 非次卡|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;performanceQuantity|业绩计提次数 - 非次卡|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unitCostPoints|单次耗费点数 - 次卡|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;percent|折扣 - 折扣权益|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shareAmount|分摊金额|number||
|&emsp;&emsp;&emsp;&emsp;validity||CardValidityDto|CardValidityDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型,可用值:fixed,byOrder,byExecution|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fixedStart|a，固定时段 - 起始|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fixedEnd|b，固定时段 - 结束|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;frozenDays|x，购买后激活等待天数（0为当天）|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;availableDays|y/z，激活后有效天数|integer||
|&emsp;&emsp;&emsp;&emsp;optionQuantity|可选数量（M值）- N选M|integer||
|&emsp;&emsp;&emsp;&emsp;totalPoints|总点数 - 次卡|number||
|&emsp;&emsp;&emsp;&emsp;deposit|账户权益 - 账户金额|number||
|&emsp;&emsp;&emsp;&emsp;giftMoney|增值金 - 账户金额|number||
|&emsp;&emsp;&emsp;&emsp;periodsCount|期数 - 时间卡|integer||
|&emsp;&emsp;&emsp;&emsp;name|权益组名称|string||
|&emsp;&emsp;&emsp;&emsp;shareAmount|分摊金额|number||
|&emsp;&emsp;remain|可售数量|integer(int32)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"allowedClinics": [
				{
					"id": "",
					"name": ""
				}
			],
			"start": "",
			"end": "",
			"scope": {
				"code": "",
				"name": ""
			},
			"description": "",
			"status": {
				"code": "",
				"name": ""
			},
			"quantity": 0,
			"cardTags": [
				{
					"groupId": "",
					"groupName": "",
					"tagId": "",
					"tagName": "",
					"color": ""
				}
			],
			"price": 0,
			"groups": [
				{
					"index": "",
					"type": "",
					"items": [
						{
							"id": "",
							"name": "",
							"type": "",
							"salableQuantity": 0,
							"performanceQuantity": 0,
							"unitCostPoints": 0,
							"percent": 0,
							"shareAmount": 0
						}
					],
					"validity": {
						"type": "",
						"fixedStart": "",
						"fixedEnd": "",
						"frozenDays": 0,
						"availableDays": 0
					},
					"optionQuantity": 0,
					"totalPoints": 0,
					"deposit": 0,
					"giftMoney": 0,
					"periodsCount": 0,
					"name": "",
					"shareAmount": 0
				}
			],
			"remain": 0
		}
	],
	"number": 0
}
```


## 根据条件查询可用卡项信息


**接口地址**:`/api/v1/market/card/prompt`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|customerId|客户ID|query|true|string||
|clinicId|诊所ID|query|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|keyword|关键字(名称，描述)|query|false|string||
|orderTypes|订单类型(medical,retail,spa,free,prepay,charge)|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageFusionCardDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|FusionCardDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;allowedClinics|归属门店（为空则没有限制）|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;start|发行日期 - 起始|string(date-time)||
|&emsp;&emsp;end|发行日期 - 结束|string(date-time)||
|&emsp;&emsp;scope||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;description|备注|string||
|&emsp;&emsp;status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;quantity|发行数（0为不限）|integer(int32)||
|&emsp;&emsp;cardTags|卡项标签集合|array|TagDictDto|
|&emsp;&emsp;&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;&emsp;&emsp;color|标签颜色|string||
|&emsp;&emsp;price|售价|number||
|&emsp;&emsp;groups|内容条目|array|CardGroupDto|
|&emsp;&emsp;&emsp;&emsp;index|卡内组序号|string||
|&emsp;&emsp;&emsp;&emsp;type|类型(固定项目，N选M，次卡，账户权益，打折权益，代金券权益),可用值:package,combination,point,store,discount,coupon|string||
|&emsp;&emsp;&emsp;&emsp;items|条目信息|array|CardGroupItemDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型(项目,商品,项目类别,商品类别,券,项目标签,商品标签,卡项,卡项标签),可用值:service,product,serviceCategory,productCategory,coupon,serviceTag,productTag,card,cardTag|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;salableQuantity|可售数量（为空则不限）- 非次卡|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;performanceQuantity|业绩计提次数 - 非次卡|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unitCostPoints|单次耗费点数 - 次卡|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;percent|折扣 - 折扣权益|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;shareAmount|分摊金额|number||
|&emsp;&emsp;&emsp;&emsp;validity||CardValidityDto|CardValidityDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型,可用值:fixed,byOrder,byExecution|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fixedStart|a，固定时段 - 起始|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fixedEnd|b，固定时段 - 结束|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;frozenDays|x，购买后激活等待天数（0为当天）|integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;availableDays|y/z，激活后有效天数|integer||
|&emsp;&emsp;&emsp;&emsp;optionQuantity|可选数量（M值）- N选M|integer||
|&emsp;&emsp;&emsp;&emsp;totalPoints|总点数 - 次卡|number||
|&emsp;&emsp;&emsp;&emsp;deposit|账户权益 - 账户金额|number||
|&emsp;&emsp;&emsp;&emsp;giftMoney|增值金 - 账户金额|number||
|&emsp;&emsp;&emsp;&emsp;periodsCount|期数 - 时间卡|integer||
|&emsp;&emsp;&emsp;&emsp;name|权益组名称|string||
|&emsp;&emsp;&emsp;&emsp;shareAmount|分摊金额|number||
|&emsp;&emsp;remain|可售数量|integer(int32)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"allowedClinics": [
				{
					"id": "",
					"name": ""
				}
			],
			"start": "",
			"end": "",
			"scope": {
				"code": "",
				"name": ""
			},
			"description": "",
			"status": {
				"code": "",
				"name": ""
			},
			"quantity": 0,
			"cardTags": [
				{
					"groupId": "",
					"groupName": "",
					"tagId": "",
					"tagName": "",
					"color": ""
				}
			],
			"price": 0,
			"groups": [
				{
					"index": "",
					"type": "",
					"items": [
						{
							"id": "",
							"name": "",
							"type": "",
							"salableQuantity": 0,
							"performanceQuantity": 0,
							"unitCostPoints": 0,
							"percent": 0,
							"shareAmount": 0
						}
					],
					"validity": {
						"type": "",
						"fixedStart": "",
						"fixedEnd": "",
						"frozenDays": 0,
						"availableDays": 0
					},
					"optionQuantity": 0,
					"totalPoints": 0,
					"deposit": 0,
					"giftMoney": 0,
					"periodsCount": 0,
					"name": "",
					"shareAmount": 0
				}
			],
			"remain": 0
		}
	],
	"number": 0
}
```


## 精确获取授权机构下的卡项信息


**接口地址**:`/api/v1/market/card/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|FusionCardDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|allowedClinics|归属门店（为空则没有限制）|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|start|发行日期 - 起始|string(date-time)|string(date-time)|
|end|发行日期 - 结束|string(date-time)|string(date-time)|
|scope||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||
|description|备注|string||
|status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||
|quantity|发行数（0为不限）|integer(int32)|integer(int32)|
|cardTags|卡项标签集合|array|TagDictDto|
|&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;color|标签颜色|string||
|price|售价|number||
|groups|内容条目|array|CardGroupDto|
|&emsp;&emsp;index|卡内组序号|string||
|&emsp;&emsp;type|类型(固定项目，N选M，次卡，账户权益，打折权益，代金券权益),可用值:package,combination,point,store,discount,coupon|string||
|&emsp;&emsp;items|条目信息|array|CardGroupItemDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;type|类型(项目,商品,项目类别,商品类别,券,项目标签,商品标签,卡项,卡项标签),可用值:service,product,serviceCategory,productCategory,coupon,serviceTag,productTag,card,cardTag|string||
|&emsp;&emsp;&emsp;&emsp;salableQuantity|可售数量（为空则不限）- 非次卡|integer||
|&emsp;&emsp;&emsp;&emsp;performanceQuantity|业绩计提次数 - 非次卡|integer||
|&emsp;&emsp;&emsp;&emsp;unitCostPoints|单次耗费点数 - 次卡|number||
|&emsp;&emsp;&emsp;&emsp;percent|折扣 - 折扣权益|integer||
|&emsp;&emsp;&emsp;&emsp;shareAmount|分摊金额|number||
|&emsp;&emsp;validity||CardValidityDto|CardValidityDto|
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:fixed,byOrder,byExecution|string||
|&emsp;&emsp;&emsp;&emsp;fixedStart|a，固定时段 - 起始|string||
|&emsp;&emsp;&emsp;&emsp;fixedEnd|b，固定时段 - 结束|string||
|&emsp;&emsp;&emsp;&emsp;frozenDays|x，购买后激活等待天数（0为当天）|integer||
|&emsp;&emsp;&emsp;&emsp;availableDays|y/z，激活后有效天数|integer||
|&emsp;&emsp;optionQuantity|可选数量（M值）- N选M|integer(int32)||
|&emsp;&emsp;totalPoints|总点数 - 次卡|number||
|&emsp;&emsp;deposit|账户权益 - 账户金额|number||
|&emsp;&emsp;giftMoney|增值金 - 账户金额|number||
|&emsp;&emsp;periodsCount|期数 - 时间卡|integer(int32)||
|&emsp;&emsp;name|权益组名称|string||
|&emsp;&emsp;shareAmount|分摊金额|number||
|remain|可售数量|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"allowedClinics": [
		{
			"id": "",
			"name": ""
		}
	],
	"start": "",
	"end": "",
	"scope": {
		"code": "",
		"name": ""
	},
	"description": "",
	"status": {
		"code": "",
		"name": ""
	},
	"quantity": 0,
	"cardTags": [
		{
			"groupId": "",
			"groupName": "",
			"tagId": "",
			"tagName": "",
			"color": ""
		}
	],
	"price": 0,
	"groups": [
		{
			"index": "",
			"type": "",
			"items": [
				{
					"id": "",
					"name": "",
					"type": "",
					"salableQuantity": 0,
					"performanceQuantity": 0,
					"unitCostPoints": 0,
					"percent": 0,
					"shareAmount": 0
				}
			],
			"validity": {
				"type": "",
				"fixedStart": "",
				"fixedEnd": "",
				"frozenDays": 0,
				"availableDays": 0
			},
			"optionQuantity": 0,
			"totalPoints": 0,
			"deposit": 0,
			"giftMoney": 0,
			"periodsCount": 0,
			"name": "",
			"shareAmount": 0
		}
	],
	"remain": 0
}
```


## 获取授权机构下的优惠券信息


**接口地址**:`/api/v1/market/coupon`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|type|券类型（线下券、代金券、不定额代金券、请客券）,可用值:offline,voucher,un-quota,invitation|query|true|string||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|clinicId|可用诊所ID - 默认不限制|query|false|string||
|keyword|关键字（名称）|query|false|string||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|status|销售状态（销售中/已过期/已下架）,可用值:sales,overdue,disabled|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageCouponDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|CouponDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;allowedClinics|归属门店（为空则没有限制）|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;start|发行日期 - 起始|string(date-time)||
|&emsp;&emsp;end|发行日期 - 结束|string(date-time)||
|&emsp;&emsp;scope||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;description|备注|string||
|&emsp;&emsp;status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;quantity|发行数（0为不限）|integer(int32)||
|&emsp;&emsp;cardTags|卡项标签集合|array|TagDictDto|
|&emsp;&emsp;&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;&emsp;&emsp;color|标签颜色|string||
|&emsp;&emsp;amount|面额|number||
|&emsp;&emsp;multipleUse|允许多次支付|boolean||
|&emsp;&emsp;restriction|使用范围(空则无限制)|array|CouponRestriction|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;type|类型(项目、商品、项目类别、商品类别、项目标签、商品标签、促销标签、卡项标签),可用值:service,product,serviceCategory,productCategory,serviceTag,productTag,promotionTag,cardTag|string||
|&emsp;&emsp;remain|可发行数量|integer(int32)||
|&emsp;&emsp;receiverRestriction||CouponReceiverRestriction|CouponReceiverRestriction|
|&emsp;&emsp;&emsp;&emsp;customerGroups|客户分群标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;customerTags|客户印象标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;customerDynamicTags|客户动态标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;membershipTypes|会员等级|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"allowedClinics": [
				{
					"id": "",
					"name": ""
				}
			],
			"start": "",
			"end": "",
			"scope": {
				"code": "",
				"name": ""
			},
			"description": "",
			"status": {
				"code": "",
				"name": ""
			},
			"quantity": 0,
			"cardTags": [
				{
					"groupId": "",
					"groupName": "",
					"tagId": "",
					"tagName": "",
					"color": ""
				}
			],
			"amount": 0,
			"multipleUse": true,
			"restriction": [
				{
					"id": "",
					"name": "",
					"type": ""
				}
			],
			"remain": 0,
			"receiverRestriction": {
				"customerGroups": [
					{
						"id": "",
						"name": ""
					}
				],
				"customerTags": [
					{
						"id": "",
						"name": ""
					}
				],
				"customerDynamicTags": [
					{
						"id": "",
						"name": ""
					}
				],
				"membershipTypes": [
					{
						"id": "",
						"name": ""
					}
				]
			}
		}
	],
	"number": 0
}
```


## 精确获取授权机构下的优惠券信息


**接口地址**:`/api/v1/market/coupon/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CouponDetailDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|allowedClinics|归属门店（为空则没有限制）|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|start|发行日期 - 起始|string(date-time)|string(date-time)|
|end|发行日期 - 结束|string(date-time)|string(date-time)|
|scope||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||
|description|备注|string||
|status||CodeNameDto|CodeNameDto|
|&emsp;&emsp;code|Code|string||
|&emsp;&emsp;name|名称/姓名|string||
|quantity|发行数（0为不限）|integer(int32)|integer(int32)|
|cardTags|卡项标签集合|array|TagDictDto|
|&emsp;&emsp;groupId|标签组ID|string||
|&emsp;&emsp;groupName|标签组名称|string||
|&emsp;&emsp;tagId|标签ID|string||
|&emsp;&emsp;tagName|标签名称|string||
|&emsp;&emsp;color|标签颜色|string||
|amount|面额|number||
|multipleUse|允许多次支付|boolean||
|restriction|使用范围(空则无限制)|array|CouponRestriction|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型(项目、商品、项目类别、商品类别、项目标签、商品标签、促销标签、卡项标签),可用值:service,product,serviceCategory,productCategory,serviceTag,productTag,promotionTag,cardTag|string||
|remain|可发行数量|integer(int32)|integer(int32)|
|receiverRestriction||CouponReceiverRestriction|CouponReceiverRestriction|
|&emsp;&emsp;customerGroups|客户分群标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;customerTags|客户印象标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;customerDynamicTags|客户动态标签|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;membershipTypes|会员等级|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"allowedClinics": [
		{
			"id": "",
			"name": ""
		}
	],
	"start": "",
	"end": "",
	"scope": {
		"code": "",
		"name": ""
	},
	"description": "",
	"status": {
		"code": "",
		"name": ""
	},
	"quantity": 0,
	"cardTags": [
		{
			"groupId": "",
			"groupName": "",
			"tagId": "",
			"tagName": "",
			"color": ""
		}
	],
	"amount": 0,
	"multipleUse": true,
	"restriction": [
		{
			"id": "",
			"name": "",
			"type": ""
		}
	],
	"remain": 0,
	"receiverRestriction": {
		"customerGroups": [
			{
				"id": "",
				"name": ""
			}
		],
		"customerTags": [
			{
				"id": "",
				"name": ""
			}
		],
		"customerDynamicTags": [
			{
				"id": "",
				"name": ""
			}
		],
		"membershipTypes": [
			{
				"id": "",
				"name": ""
			}
		]
	}
}
```


## 获取授权机构下的促销信息


**接口地址**:`/api/v1/market/promotion`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所|query|false|string||
|type|类型(套餐/规则),可用值:bundle,rule|query|false|string||
|status|状态(未开始,进行中,暂停中,已结束),可用值:pending,active,suspend,end|query|false|string||
|minPrice|价格区间 - 最低价|query|false|number||
|maxPrice|价格区间 - 最高价|query|false|number||
|keyword|关键字（名称）|query|false|string||
|liveShowFilter|是否可直播售卖|query|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PagePromotionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|PromotionDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;start|开始时间(含)|string(date-time)||
|&emsp;&emsp;end|结束时间(含)|string(date-time)||
|&emsp;&emsp;clinics|归属门店|array|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;type|类型(套餐/规则),可用值:bundle,rule|string||
|&emsp;&emsp;active|是否激活|boolean||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;price|销售价格|number||
|&emsp;&emsp;bundles|套餐内容(仅套餐类型)|array|PromotionBundleDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;type|类型,可用值:product,service|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;&emsp;&emsp;transactionPrice|折后总价(0代表赠品)|number||
|&emsp;&emsp;rules|规则内容(仅规则类型)|array|PromotionRuleDto|
|&emsp;&emsp;&emsp;&emsp;conditions||array|object|
|&emsp;&emsp;&emsp;&emsp;actions||array|object|
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"start": "",
			"end": "",
			"clinics": [
				{
					"id": "",
					"name": ""
				}
			],
			"type": "",
			"active": true,
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"price": 0,
			"bundles": [
				{
					"id": "",
					"name": "",
					"type": "",
					"quantity": 0,
					"unitRetailPrice": 0,
					"transactionPrice": 0
				}
			],
			"rules": [
				{
					"conditions": [],
					"actions": []
				}
			]
		}
	],
	"number": 0
}
```


## 促销启用-停用


**接口地址**:`/api/v1/market/promotion/active`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "active": true,
  "id": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|salesPromotionActiveParam|促销启用/停用-请求参数|body|true|SalesPromotionActiveParam|SalesPromotionActiveParam|
|&emsp;&emsp;active|启用状态||true|boolean||
|&emsp;&emsp;id|促销ID||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|204|No Content||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据ID获取促销信息


**接口地址**:`/api/v1/market/promotion/{id}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PromotionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|start|开始时间(含)|string(date-time)|string(date-time)|
|end|结束时间(含)|string(date-time)|string(date-time)|
|clinics|归属门店|array|IdNameDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|type|类型(套餐/规则),可用值:bundle,rule|string||
|active|是否激活|boolean||
|status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;code|代码|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;system|编码系统|string||
|price|销售价格|number||
|bundles|套餐内容(仅套餐类型)|array|PromotionBundleDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;type|类型,可用值:product,service|string||
|&emsp;&emsp;quantity|数量|integer(int32)||
|&emsp;&emsp;unitRetailPrice|销售单价|number||
|&emsp;&emsp;transactionPrice|折后总价(0代表赠品)|number||
|rules|规则内容(仅规则类型)|array|PromotionRuleDto|
|&emsp;&emsp;conditions||array|object|
|&emsp;&emsp;actions||array|object|


**响应示例**:
```javascript
{
	"id": "",
	"name": "",
	"start": "",
	"end": "",
	"clinics": [
		{
			"id": "",
			"name": ""
		}
	],
	"type": "",
	"active": true,
	"status": {
		"code": "",
		"name": "",
		"system": ""
	},
	"price": 0,
	"bundles": [
		{
			"id": "",
			"name": "",
			"type": "",
			"quantity": 0,
			"unitRetailPrice": 0,
			"transactionPrice": 0
		}
	],
	"rules": [
		{
			"conditions": [],
			"actions": []
		}
	]
}
```


# 08. 库存物料集成


## 获取授权机构下出-入库类别，bizType参数: stock-in(入库), stock-out(出库)


**接口地址**:`/api/v1/inventory/change-type/{bizType}`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bizType||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChangeTypeDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|类别编码|string||
|name|类别名称|string||
|active|是否启用|boolean||
|selectable|是否可选用（否则仅为系统自动操作用）|boolean||
|asCost|是否计入成本|boolean||
|isBuiltIn|是否系统内置|boolean||
|needConfirm|是否需要二次确认|boolean||


**响应示例**:
```javascript
[
	{
		"code": "",
		"name": "",
		"active": true,
		"selectable": true,
		"asCost": true,
		"isBuiltIn": true,
		"needConfirm": true
	}
]
```


## 获取提货单信息 - 翻页


**接口地址**:`/api/v1/inventory/outbound/all`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|organizationId|门店的id|query|false|string||
|customerId|客户id|query|false|string||
|orderTimeStart|开单开始时间 - 包含该日期，如 2024-11-26T06:07:15.870Z|query|false|string(date-time)||
|orderTimeEnd|开单结束时间 - 包含该日期，如 2024-11-26T06:07:15.870Z|query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageOutboundRequisitionInfoDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|OutboundRequisitionInfoDto|
|&emsp;&emsp;id|提货单id|string||
|&emsp;&emsp;customerId|客户id|string||
|&emsp;&emsp;customerName|客户姓名|string||
|&emsp;&emsp;organizationId|门店id|string||
|&emsp;&emsp;organizationName|门店名称|string||
|&emsp;&emsp;orderTime|开单时间|string(date-time)||
|&emsp;&emsp;orderId|订单号|string||
|&emsp;&emsp;outboundItems||array|OutboundRequestItem|
|&emsp;&emsp;&emsp;&emsp;skuId|商品id|string||
|&emsp;&emsp;&emsp;&emsp;name|商品名称|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;accountItemId|权益id|string||
|&emsp;&emsp;&emsp;&emsp;orderLineId|订单行id|string||
|&emsp;&emsp;&emsp;&emsp;orderLineIndex|订单行号|string||
|&emsp;&emsp;&emsp;&emsp;orderLineItemId|订单条目id|string||
|&emsp;&emsp;&emsp;&emsp;orderLineItemIndex|订单条目号|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"customerId": "",
			"customerName": "",
			"organizationId": "",
			"organizationName": "",
			"orderTime": "",
			"orderId": "",
			"outboundItems": [
				{
					"skuId": "",
					"name": "",
					"quantity": 0,
					"accountItemId": "",
					"orderLineId": "",
					"orderLineIndex": "",
					"orderLineItemId": "",
					"orderLineItemIndex": ""
				}
			]
		}
	],
	"number": 0
}
```


## 物资采购订单


**接口地址**:`/api/v1/inventory/purchaseOrder`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|操作日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|操作日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|门店ID|query|false|string||
|id|采购订单ID|query|false|string||
|supplierId|供应商ID|query|false|string||
|status|交货状态， 0:待审核；1:采购中；2:已拒绝；3:部分入库；4:已入库：|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PagePurchaseOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|PurchaseOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|编码，通常用于：1）三方集成使用，2）快速甄别查找|string||
|&emsp;&emsp;supplier||Supplier|Supplier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;organization||Organization|Organization|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;creator||Creator|Creator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;createdAt|创建时间|string(date-time)||
|&emsp;&emsp;financialNote|财务信息|string||
|&emsp;&emsp;note|采购原因|string||
|&emsp;&emsp;purchaseAmount|采购金额|number||
|&emsp;&emsp;receiptAmount|入库金额|number||
|&emsp;&emsp;status|交货状态， 0:待审核；1:采购中；2:已拒绝；3:部分入库；4:已入库：,可用值:0,1,2,3,4|string||
|&emsp;&emsp;details|订单条目信息|array|SimplePurchaseOrderItemDto|
|&emsp;&emsp;&emsp;&emsp;id|SKU ID|string||
|&emsp;&emsp;&emsp;&emsp;name|SKU 名称|string||
|&emsp;&emsp;&emsp;&emsp;number|SKU 编号|string||
|&emsp;&emsp;&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;manufacturer|生产厂商|string||
|&emsp;&emsp;&emsp;&emsp;licenseNumber|批准文号|string||
|&emsp;&emsp;&emsp;&emsp;unitPrice|单价|number||
|&emsp;&emsp;&emsp;&emsp;quantity|采购数量|integer||
|&emsp;&emsp;&emsp;&emsp;receiptQuantity|入库数量|integer||
|&emsp;&emsp;&emsp;&emsp;purchaseApplyId|采购申请单ID|string||
|&emsp;&emsp;&emsp;&emsp;purchaseApplyNumber|采购申请单编号|string||
|&emsp;&emsp;workflows|审批记录详情|array|ReviewedWorkflow|
|&emsp;&emsp;&emsp;&emsp;reviewedBy||ReviewedBy|ReviewedBy|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;reviewedDate|审核时间|string||
|&emsp;&emsp;&emsp;&emsp;comment|审核意见|string||
|&emsp;&emsp;&emsp;&emsp;reviewedStatus||ReviewedStatus|ReviewedStatus|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|审批状态|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;text|审批状态描述|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"supplier": {
				"id": "",
				"name": ""
			},
			"organization": {
				"id": "",
				"name": ""
			},
			"creator": {
				"id": "",
				"name": ""
			},
			"createdAt": "",
			"financialNote": "",
			"note": "",
			"purchaseAmount": 0,
			"receiptAmount": 0,
			"status": "",
			"details": [
				{
					"id": "",
					"name": "",
					"number": "",
					"specification": "",
					"unit": "",
					"manufacturer": "",
					"licenseNumber": "",
					"unitPrice": 0,
					"quantity": 0,
					"receiptQuantity": 0,
					"purchaseApplyId": "",
					"purchaseApplyNumber": ""
				}
			],
			"workflows": [
				{
					"reviewedBy": {
						"id": "",
						"name": ""
					},
					"reviewedDate": "",
					"comment": "",
					"reviewedStatus": {
						"code": "",
						"text": ""
					}
				}
			]
		}
	],
	"number": 0
}
```


## 获取授权机构下的所有库存条目信息


**接口地址**:`/api/v1/inventory/stock-item`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|categoryId|物料类别ID|query|false|string||
|branchId|所属分支结构ID|query|false|string||
|warehouseId|库房ID|query|false|string||
|hasStock|是否有库存|query|false|boolean||
|isDrug|是否药品（默认否）|query|false|boolean||
|isShortage|是否缺货|query|false|boolean||
|isEnabled|是否启用|query|false|boolean||
|keyword|模糊搜索关键字（商品名称、规格、条码、批次）|query|false|string||
|ids|物料Id - 列表|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageStockItemDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|StockItemDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;name|名称|string||
|&emsp;&emsp;code|业务编码|string||
|&emsp;&emsp;warehouse||Stock|Stock|
|&emsp;&emsp;category||Category|Category|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;code|编码|string||
|&emsp;&emsp;quantity|库存总数|integer(int32)||
|&emsp;&emsp;manufacturer|制造商|string||
|&emsp;&emsp;supplier||Supplier|Supplier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;licenseNumber|批准文号|string||
|&emsp;&emsp;batches|批次详情|array|BatchDto|
|&emsp;&emsp;&emsp;&emsp;number|批次号|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|到期日期|string||
|&emsp;&emsp;&emsp;&emsp;quantity|剩余数量|integer||
|&emsp;&emsp;&emsp;&emsp;unitPrice|单价|number||
|&emsp;&emsp;enabled||boolean||
|&emsp;&emsp;shortage||boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"code": "",
			"warehouse": "",
			"category": {
				"id": "",
				"name": "",
				"code": ""
			},
			"quantity": 0,
			"manufacturer": "",
			"supplier": {
				"id": "",
				"name": ""
			},
			"spec": "",
			"unit": "",
			"licenseNumber": "",
			"batches": [
				{
					"number": "",
					"expiredAt": "",
					"quantity": 0,
					"unitPrice": 0
				}
			],
			"enabled": true,
			"shortage": true
		}
	],
	"number": 0
}
```


## 物料入库记录


**接口地址**:`/api/v1/inventory/stock-item/stock-in`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|操作日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|操作日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|门店ID|query|false|string||
|warehouseId|仓库ID|query|false|string||
|isPharmacy|是否药品库(默认否)|query|false|boolean||
|supplierId|供应商ID|query|false|string||
|categoryIds|物料类别ID - 列表|query|false|array|string|
|id|单据ID|query|false|string||
|includeRollback|是否包含回冲单|query|false|boolean||
|changeTypeCode|入库类别|query|false|string||
|number|入库单号|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageStockInOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|StockInOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|单号|string||
|&emsp;&emsp;operator||Operator|Operator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;occurredAt|生效时间|string(date-time)||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;warehouse||Warehouse|Warehouse|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;supplier||Supplier|Supplier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;changeType||ChangeType|ChangeType|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;relatedOrder||RelatedOrder|RelatedOrder|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;number||string||
|&emsp;&emsp;totalAmount|总金额|number||
|&emsp;&emsp;orderId|关联订单ID|string||
|&emsp;&emsp;purchaseOrderId|采购订单ID|string||
|&emsp;&emsp;details|明细|array|StockInOutProduct|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次号|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|有效日期|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;lineId|关联订单行/条目id（仅出库列表有值）|string||
|&emsp;&emsp;&emsp;&emsp;totalAmount|成本总价|number||
|&emsp;&emsp;&emsp;&emsp;unitPrice|成本单价|number||
|&emsp;&emsp;&emsp;&emsp;zqerProductCodes|追溯码|array|string|
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"operator": {
				"id": "",
				"name": ""
			},
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"occurredAt": "",
			"note": "",
			"warehouse": {
				"id": "",
				"name": ""
			},
			"supplier": {
				"id": "",
				"name": ""
			},
			"changeType": {
				"code": "",
				"name": ""
			},
			"relatedOrder": {
				"id": "",
				"number": ""
			},
			"totalAmount": 0,
			"orderId": "",
			"purchaseOrderId": "",
			"details": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"unit": "",
					"batchNo": "",
					"expiredAt": "",
					"quantity": 0,
					"lineId": "",
					"totalAmount": 0,
					"unitPrice": 0,
					"zqerProductCodes": []
				}
			]
		}
	],
	"number": 0
}
```


## 物料入库操作


**接口地址**:`/api/v1/inventory/stock-item/stock-in`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "number": "",
  "warehouseId": "",
  "type": "",
  "supplierId": "",
  "operatorId": "",
  "note": "",
  "externalType": "",
  "products": [
    {
      "id": "",
      "price": 0,
      "quantity": 0,
      "batchNo": "",
      "expiredAt": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|stockInParams|入库操作|body|true|StockInParams|StockInParams|
|&emsp;&emsp;number|入库单号(留空则自动生成) - 根据单号唯一实现幂等性||false|string||
|&emsp;&emsp;warehouseId|仓库ID||true|string||
|&emsp;&emsp;type|入库类别Code, 参照 /change-type/stock-in||true|string||
|&emsp;&emsp;supplierId|供应商ID||false|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;externalType|订单来源||false|string||
|&emsp;&emsp;products|出库明细||true|array|StockInProduct|
|&emsp;&emsp;&emsp;&emsp;id|商品ID||true|string||
|&emsp;&emsp;&emsp;&emsp;price|进价||false|number||
|&emsp;&emsp;&emsp;&emsp;quantity|出库数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次||false|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|有效期，yyyy-MM-dd||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|
|201|Created|IdDto|


**响应状态码-200**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


**响应状态码-201**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 作废物料入库记录


**接口地址**:`/api/v1/inventory/stock-item/stock-in/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|
|204|No Content||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 物料出库记录


**接口地址**:`/api/v1/inventory/stock-item/stock-out`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|操作日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|操作日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|门店ID|query|false|string||
|warehouseId|仓库ID|query|false|string||
|isPharmacy|是否药品库(默认否)|query|false|boolean||
|supplierId|供应商ID|query|false|string||
|categoryIds|物料类别ID - 列表|query|false|array|string|
|id|单据ID|query|false|string||
|includeRollback|是否包含回冲单|query|false|boolean||
|changeTypeCode|出库类别|query|false|string||
|number|出库单号|query|false|string||
|takeUserId|领用人|query|false|string||
|customerId|客户Id|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageStockOutOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|StockOutOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|单号|string||
|&emsp;&emsp;operator||Operator|Operator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;occurredAt|生效时间|string(date-time)||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;warehouse||Warehouse|Warehouse|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;supplier||Supplier|Supplier|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;changeType||ChangeType|ChangeType|
|&emsp;&emsp;&emsp;&emsp;code|Code|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;relatedOrder||RelatedOrder|RelatedOrder|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;number||string||
|&emsp;&emsp;totalAmount|总金额|number||
|&emsp;&emsp;details|明细|array|StockInOutProduct|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次号|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|有效日期|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;lineId|关联订单行/条目id（仅出库列表有值）|string||
|&emsp;&emsp;&emsp;&emsp;totalAmount|成本总价|number||
|&emsp;&emsp;&emsp;&emsp;unitPrice|成本单价|number||
|&emsp;&emsp;&emsp;&emsp;zqerProductCodes|追溯码|array|string|
|&emsp;&emsp;customer||Customer|Customer|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;takeUser||TakeUser|TakeUser|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;orderId|关联订单ID|string||
|&emsp;&emsp;executionId|关联划扣ID|string||
|&emsp;&emsp;performancePreAllocations|业绩明细|array|OutStockPerformancePreAllocationInfo|
|&emsp;&emsp;&emsp;&emsp;outStockId|出库单id|string||
|&emsp;&emsp;&emsp;&emsp;skuId|商品id|string||
|&emsp;&emsp;&emsp;&emsp;percent|业绩比例|number||
|&emsp;&emsp;&emsp;&emsp;employeeId|业绩员工ID|string||
|&emsp;&emsp;&emsp;&emsp;allocateType|业绩分配类型：0 整单 ，1 按条目|integer||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"operator": {
				"id": "",
				"name": ""
			},
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"occurredAt": "",
			"note": "",
			"warehouse": {
				"id": "",
				"name": ""
			},
			"supplier": {
				"id": "",
				"name": ""
			},
			"changeType": {
				"code": "",
				"name": ""
			},
			"relatedOrder": {
				"id": "",
				"number": ""
			},
			"totalAmount": 0,
			"details": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"unit": "",
					"batchNo": "",
					"expiredAt": "",
					"quantity": 0,
					"lineId": "",
					"totalAmount": 0,
					"unitPrice": 0,
					"zqerProductCodes": []
				}
			],
			"customer": {
				"id": "",
				"name": ""
			},
			"takeUser": {
				"id": "",
				"name": ""
			},
			"orderId": "",
			"executionId": "",
			"performancePreAllocations": [
				{
					"outStockId": "",
					"skuId": "",
					"percent": 0,
					"employeeId": "",
					"allocateType": 0
				}
			]
		}
	],
	"number": 0
}
```


## 物料出库操作


**接口地址**:`/api/v1/inventory/stock-item/stock-out`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "number": "",
  "warehouseId": "",
  "type": "",
  "supplierId": "",
  "recipientEmployeeId": "",
  "recipientOrganizationId": "",
  "medicalDepartmentIds": [],
  "customerId": "",
  "operatorId": "",
  "note": "",
  "externalType": "",
  "outboundRequisitionId": "",
  "warehouseManageId": "",
  "products": [
    {
      "id": "",
      "batchNo": "",
      "expiredAt": "",
      "quantity": 0,
      "accountItemId": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|stockOutParams|出库操作|body|true|StockOutParams|StockOutParams|
|&emsp;&emsp;number|出库单号(留空则自动生成) - 根据单号唯一实现幂等性||false|string||
|&emsp;&emsp;warehouseId|仓库ID||true|string||
|&emsp;&emsp;type|出库类别Code, 参照 /change-type/stock-out||true|string||
|&emsp;&emsp;supplierId|供应商ID||false|string||
|&emsp;&emsp;recipientEmployeeId|领用员工ID||false|string||
|&emsp;&emsp;recipientOrganizationId|领用部门ID||false|string||
|&emsp;&emsp;medicalDepartmentIds|医疗科室ID（列表）||false|array|string|
|&emsp;&emsp;customerId|客户ID||false|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;externalType|订单来源||false|string||
|&emsp;&emsp;outboundRequisitionId|提货单id||false|string||
|&emsp;&emsp;warehouseManageId|库管员Id||false|string||
|&emsp;&emsp;products|出库明细||true|array|StockOutProductInParam|
|&emsp;&emsp;&emsp;&emsp;id|商品ID||true|string||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次||false|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|有效期，yyyy-MM-dd||false|string||
|&emsp;&emsp;&emsp;&emsp;quantity|出库数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;accountItemId|权益id||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|
|201|Created|IdDto|


**响应状态码-200**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


**响应状态码-201**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 作废物料出库记录


**接口地址**:`/api/v1/inventory/stock-item/stock-out/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|
|204|No Content||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 物料调拨记录


**接口地址**:`/api/v1/inventory/stock-item/transfer`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|操作日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|操作日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|id|id|query|false|string||
|number|调拨单号|query|false|string||
|isPharmacy|是否药品库（默认否）|query|false|boolean||
|fromWarehouseId|调出仓库ID|query|false|string||
|toWarehouseId|调入仓库ID|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageStockTransferOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|StockTransferOrderDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|单号|string||
|&emsp;&emsp;operator||Operator|Operator|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;occurredAt|生效时间|string(date-time)||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;details|明细|array|CommonProduct|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次号|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|有效日期|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;lineId|关联订单行/条目id（仅出库列表有值）|string||
|&emsp;&emsp;&emsp;&emsp;totalAmount|成本总价|number||
|&emsp;&emsp;fromWarehouse||FromWarehouse|FromWarehouse|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;toWarehouse||ToWarehouse|ToWarehouse|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;takeUser||TakeUser|TakeUser|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"operator": {
				"id": "",
				"name": ""
			},
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"occurredAt": "",
			"note": "",
			"details": [
				{
					"id": "",
					"name": "",
					"spec": "",
					"unit": "",
					"batchNo": "",
					"expiredAt": "",
					"quantity": 0,
					"lineId": "",
					"totalAmount": 0
				}
			],
			"fromWarehouse": {
				"id": "",
				"name": ""
			},
			"toWarehouse": {
				"id": "",
				"name": ""
			},
			"takeUser": {
				"id": "",
				"name": ""
			}
		}
	],
	"number": 0
}
```


## 物料库存调拨


**接口地址**:`/api/v1/inventory/stock-item/transfer`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "fromWarehouseId": "",
  "toWarehouseId": "",
  "operatorId": "",
  "note": "",
  "number": "",
  "products": [
    {
      "id": "",
      "quantity": 0,
      "batchNo": "",
      "expiredAt": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|stockTransferParams|调拨操作|body|true|StockTransferParams|StockTransferParams|
|&emsp;&emsp;fromWarehouseId|调出仓库ID||true|string||
|&emsp;&emsp;toWarehouseId|调入仓库ID||true|string||
|&emsp;&emsp;operatorId|操作人ID||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;number|单号（不提供则自动生成） - 根据单号唯一实现幂等性||false|string||
|&emsp;&emsp;products|调拨明细||true|array|StockTransferProduct|
|&emsp;&emsp;&emsp;&emsp;id|商品ID||true|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;batchNo|批次||false|string||
|&emsp;&emsp;&emsp;&emsp;expiredAt|有效期, yyyy-MM-dd||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|
|201|Created|IdDto|


**响应状态码-200**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


**响应状态码-201**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 作废物料调拨记录


**接口地址**:`/api/v1/inventory/stock-item/transfer/{id}`


**请求方式**:`DELETE`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IdDto|
|204|No Content||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取供应商信息 - 翻页


**接口地址**:`/api/v1/inventory/supplier`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageSupplierDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|SupplierDto|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;type||IdNameDto|IdNameDto|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;enable|是否有效|boolean||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"name": "",
			"type": {
				"id": "",
				"name": ""
			},
			"enable": true
		}
	],
	"number": 0
}
```


## 获取授权机构下的所有库房信息


**接口地址**:`/api/v1/inventory/warehouse`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|WarehouseDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|name|名称|string||
|code|业务编码|string||
|branch||Organization|Organization|
|&emsp;&emsp;id|ID|string||
|&emsp;&emsp;name|名称/姓名|string||
|description|备注|string||
|type|库房类型(HIS物资库，药品库),可用值:his,drug,可用值:his,drug|array||
|executionOnlyManager|是否仅库管操作|boolean||
|managers|库管员信息|array|WarehouseEmployee|
|&emsp;&emsp;employeeId|库管员id|string||
|&emsp;&emsp;employeeName|库管员名称|string||


**响应示例**:
```javascript
[
	{
		"id": "",
		"name": "",
		"code": "",
		"branch": {
			"id": "",
			"name": ""
		},
		"description": "",
		"type": [],
		"executionOnlyManager": true,
		"managers": [
			{
				"employeeId": "",
				"employeeName": ""
			}
		]
	}
]
```


# 10. 业务事件订阅


## 获取历史事件分页列表


**接口地址**:`/api/v1/event/event-history`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|startTime|创建时间开始（包含，仅支持近3个月内事件历史），如 2022-07-19T00:00:00|query|true|string(date-time)||
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|endTime|创建时间结束(不包含)，如 2022-07-20T00:00:00，默认为当前时间|query|false|string(date-time)||
|topics|事件主题 - 列表|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageEventHistoryDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|EventHistoryDto|
|&emsp;&emsp;uuid|消息UUID|string||
|&emsp;&emsp;bizEntityId|关联业务实体ID|string||
|&emsp;&emsp;topic|topic关联主题|string||
|&emsp;&emsp;rawJson|json原文|string||
|&emsp;&emsp;bizTime|业务发生时间|string(date-time)||
|&emsp;&emsp;createTime|历史记录创建时间|string(date-time)||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"uuid": "",
			"bizEntityId": "",
			"topic": "",
			"rawJson": "",
			"bizTime": "",
			"createTime": ""
		}
	],
	"number": 0
}
```


## 获取特定业务实体对应的历史事件列表


**接口地址**:`/api/v1/event/event-history/single-entity`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bizEntityId|业务实体id|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|EventHistoryDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|uuid|消息UUID|string||
|bizEntityId|关联业务实体ID|string||
|topic|topic关联主题|string||
|rawJson|json原文|string||
|bizTime|业务发生时间|string(date-time)|string(date-time)|
|createTime|历史记录创建时间|string(date-time)|string(date-time)|


**响应示例**:
```javascript
[
	{
		"uuid": "",
		"bizEntityId": "",
		"topic": "",
		"rawJson": "",
		"bizTime": "",
		"createTime": ""
	}
]
```


## 获取当前订阅列表


**接口地址**:`/api/v1/event/subscribe`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|TopicSubscriptionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|topics|监听列表|array||
|callbackUrl|回调地址|string||
|status|订阅状态,可用值:Subscribed,Listening,Unsubscribed,Removed|string||
|createdAt|创建时间|string(date-time)|string(date-time)|
|lastModifiedAt|最近修改时间|string(date-time)|string(date-time)|
|timeToLive|生存时间（毫秒值，过期后删除），-1为永久保存|integer(int64)|integer(int64)|


**响应示例**:
```javascript
[
	{
		"id": "",
		"topics": [],
		"callbackUrl": "",
		"status": "",
		"createdAt": "",
		"lastModifiedAt": "",
		"timeToLive": 0
	}
]
```


## 订阅系统业务事件主题，结果返回当前订阅


**接口地址**:`/api/v1/event/subscribe`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "callbackUrl": "",
  "topics": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createSubscriptionParams|CreateSubscriptionParams|body|true|CreateSubscriptionParams|CreateSubscriptionParams|
|&emsp;&emsp;callbackUrl|回调完整url，不允许包含'?'，'&'等参数分隔符||false|string||
|&emsp;&emsp;topics|监听的事件列表||true|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|TopicSubscriptionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|topics|监听列表|array||
|callbackUrl|回调地址|string||
|status|订阅状态,可用值:Subscribed,Listening,Unsubscribed,Removed|string||
|createdAt|创建时间|string(date-time)|string(date-time)|
|lastModifiedAt|最近修改时间|string(date-time)|string(date-time)|
|timeToLive|生存时间（毫秒值，过期后删除），-1为永久保存|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"id": "",
	"topics": [],
	"callbackUrl": "",
	"status": "",
	"createdAt": "",
	"lastModifiedAt": "",
	"timeToLive": 0
}
```


## 获取当前系统支持的事件主题


**接口地址**:`/api/v1/event/topic`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|EventTopicDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code|编码|string||
|name|名称|string||
|description|描述|string||
|model|回调数据结构说明|string||


**响应示例**:
```javascript
[
	{
		"code": "",
		"name": "",
		"description": "",
		"model": ""
	}
]
```


## 取消订阅系统业务事件主题


**接口地址**:`/api/v1/event/unsubscribe/{id}`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id||path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|202|Accepted|TopicSubscriptionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|唯一ID|string||
|topics|监听列表|array||
|callbackUrl|回调地址|string||
|status|订阅状态,可用值:Subscribed,Listening,Unsubscribed,Removed|string||
|createdAt|创建时间|string(date-time)|string(date-time)|
|lastModifiedAt|最近修改时间|string(date-time)|string(date-time)|
|timeToLive|生存时间（毫秒值，过期后删除），-1为永久保存|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"id": "",
	"topics": [],
	"callbackUrl": "",
	"status": "",
	"createdAt": "",
	"lastModifiedAt": "",
	"timeToLive": 0
}
```


# 11. 电子健康档案


## 在授权机构下的创建患者诊疗计划


**接口地址**:`/api/v1/ehr/care-plan`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "title": "",
  "subject": {
    "reference": "",
    "type": "",
    "identifier": "",
    "display": ""
  },
  "description": "",
  "author": {
    "reference": "",
    "type": "",
    "identifier": "",
    "display": ""
  },
  "note": "",
  "activity": [
    {
      "detail": {
        "location": {
          "reference": "",
          "type": "",
          "identifier": "",
          "display": ""
        },
        "performer": [
          {
            "reference": "",
            "type": "",
            "identifier": "",
            "display": ""
          }
        ],
        "productReference": {
          "reference": "",
          "type": "",
          "identifier": "",
          "display": ""
        },
        "quantity": 0
      },
      "scheduledTiming": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createCarePlanParams|CreateCarePlanParams|body|true|CreateCarePlanParams|CreateCarePlanParams|
|&emsp;&emsp;title|标题||false|string||
|&emsp;&emsp;subject|||true|EhrRefParam|EhrRefParam|
|&emsp;&emsp;&emsp;&emsp;reference|引用来源(URI)，比如 employee/231123||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型，比如 doctor||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|唯一编号，比如 231123||false|string||
|&emsp;&emsp;&emsp;&emsp;display|简单描述||false|string||
|&emsp;&emsp;description|描述||false|string||
|&emsp;&emsp;author|||false|EhrRefParam|EhrRefParam|
|&emsp;&emsp;&emsp;&emsp;reference|引用来源(URI)，比如 employee/231123||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型，比如 doctor||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|唯一编号，比如 231123||false|string||
|&emsp;&emsp;&emsp;&emsp;display|简单描述||false|string||
|&emsp;&emsp;note|备注||false|string||
|&emsp;&emsp;activity|明细||true|array|ActivityParam|
|&emsp;&emsp;&emsp;&emsp;detail|||true|ActivityDetailParam|ActivityDetailParam|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;location|||true|EhrRefParam|EhrRefParam|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;reference|引用来源(URI)，比如 employee/231123||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型，比如 doctor||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier|唯一编号，比如 231123||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;display|简单描述||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;performer|执行人||false|array|EhrRefParam|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;reference|引用来源(URI)，比如 employee/231123||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型，比如 doctor||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier|唯一编号，比如 231123||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;display|简单描述||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;productReference|||true|ProductRefParam|ProductRefParam|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;reference|引用来源(URI)，比如 employee/231123||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|类型，比如 doctor||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier|唯一编号，比如 231123||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;display|简单描述||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;quantity|数量||true|integer||
|&emsp;&emsp;&emsp;&emsp;scheduledTiming|日期，格式：yyyy-MM-dd||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|IdDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||string||


**响应示例**:
```javascript
{
	"id": ""
}
```


## 获取授权机构下的处方数据


**接口地址**:`/api/v1/ehr/prescription`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|页码(从0开始)|query|false|integer(int32)||
|size|分页大小(默认20)|query|false|integer(int32)||
|start|开始日期 - 包含该日期，如 2018-11-11|query|false|string(date-time)||
|end|结束日期 - 包含该日期，如 2018-12-11|query|false|string(date-time)||
|clinicId|诊所Id|query|false|string||
|patientId|患者ID - customer id|query|false|string||
|type|处方类型(参考系统配置/字典管理/处方类型-medical-prescription-type)|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PagePrescriptionDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|PrescriptionDto|
|&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;number|处方流水号|string||
|&emsp;&emsp;visitNumber|就诊流水号|string||
|&emsp;&emsp;type||PrescriptionType|PrescriptionType|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;patient||Patient|Patient|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;&emsp;&emsp;number|病历号|string||
|&emsp;&emsp;clinic||Clinic|Clinic|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;medicalDepartment||MedicalDepartment|MedicalDepartment|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;doctor||Doctor|Doctor|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;auditPharmacist||AuditPharmacist|AuditPharmacist|
|&emsp;&emsp;&emsp;&emsp;id|ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称/姓名|string||
|&emsp;&emsp;clinicalDiagnose|临床诊断|string||
|&emsp;&emsp;createdAt|处方时间|string(date-time)||
|&emsp;&emsp;auditedAt|审核时间|string(date-time)||
|&emsp;&emsp;medicines|药品列表|array|PrescriptionMedicineDto|
|&emsp;&emsp;&emsp;&emsp;id|唯一ID|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;dose|剂量|string||
|&emsp;&emsp;&emsp;&emsp;doseUnit||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;duration|天数|integer||
|&emsp;&emsp;&emsp;&emsp;frequency||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;&emsp;&emsp;instruction|使用方法|string||
|&emsp;&emsp;&emsp;&emsp;specification|规格|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量|integer||
|&emsp;&emsp;&emsp;&emsp;note|备注|string||
|&emsp;&emsp;status||CodeValueDto|CodeValueDto|
|&emsp;&emsp;&emsp;&emsp;code|代码|string||
|&emsp;&emsp;&emsp;&emsp;name|名称|string||
|&emsp;&emsp;&emsp;&emsp;system|编码系统|string||
|&emsp;&emsp;note|备注|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"number": "",
			"visitNumber": "",
			"type": {
				"id": "",
				"name": ""
			},
			"patient": {
				"id": "",
				"name": "",
				"number": ""
			},
			"clinic": {
				"id": "",
				"name": ""
			},
			"medicalDepartment": {
				"id": "",
				"name": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"auditPharmacist": {
				"id": "",
				"name": ""
			},
			"clinicalDiagnose": "",
			"createdAt": "",
			"auditedAt": "",
			"medicines": [
				{
					"id": "",
					"name": "",
					"dose": "",
					"doseUnit": {
						"code": "",
						"name": "",
						"system": ""
					},
					"duration": 0,
					"frequency": {
						"code": "",
						"name": "",
						"system": ""
					},
					"instruction": "",
					"specification": "",
					"unit": "",
					"quantity": 0,
					"note": ""
				}
			],
			"status": {
				"code": "",
				"name": "",
				"system": ""
			},
			"note": ""
		}
	],
	"number": 0
}
```


## 获取授权机构下的新版本医嘱服务的处方数据


**接口地址**:`/api/v1/ehr/prescriptionNew`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|clinicId|诊所Id 必填|query|true|string||
|page|当前页码，如果不传默认为0，0为第一页|query|true|integer(int32)||
|size|每页大小，如果不传默认为20，最大值200|query|true|integer(int32)||
|start|开始日期，必填，包含该日期，如 2018-11-11，开始到结束日期最大为三个月|query|true|string(date-time)||
|end|结束日期，必填，包含该日期，如 2018-12-11，开始到结束日期最大为三个月|query|true|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageSupervisionDataOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|SupervisionDataOrderDto|
|&emsp;&emsp;prescriptionType||string||
|&emsp;&emsp;prescriptionNo||string||
|&emsp;&emsp;date||string||
|&emsp;&emsp;customer||SupervisionCustomerDataDto|SupervisionCustomerDataDto|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;mrn||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;gender||integer||
|&emsp;&emsp;&emsp;&emsp;age||string||
|&emsp;&emsp;&emsp;&emsp;weight||string||
|&emsp;&emsp;&emsp;&emsp;mobile||string||
|&emsp;&emsp;&emsp;&emsp;allergyInfo||string||
|&emsp;&emsp;doctor||SupervisionDoctorDataDto|SupervisionDoctorDataDto|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;department||SupervisionDataDepartmentDto|SupervisionDataDepartmentDto|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;diagnosis||array|SupervisionDataDiagnosisDto|
|&emsp;&emsp;&emsp;&emsp;diagnosisCode||string||
|&emsp;&emsp;&emsp;&emsp;diagnosisName||string||
|&emsp;&emsp;&emsp;&emsp;isMain||string||
|&emsp;&emsp;medicinal||array|SupervisionDataMedicinalDto|
|&emsp;&emsp;&emsp;&emsp;code|药品代码|string||
|&emsp;&emsp;&emsp;&emsp;name|药品名称|string||
|&emsp;&emsp;&emsp;&emsp;orderNo|医嘱编码 成组药的医嘱编码相同|string||
|&emsp;&emsp;&emsp;&emsp;orderSlaveNo|明细编码|string||
|&emsp;&emsp;&emsp;&emsp;orderTypeCodeName|医嘱类型 药品、检验、检查等|string||
|&emsp;&emsp;&emsp;&emsp;groupName||string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;dose|剂量|number||
|&emsp;&emsp;&emsp;&emsp;doseUnit|剂量单位|string||
|&emsp;&emsp;&emsp;&emsp;price|单价|number||
|&emsp;&emsp;&emsp;&emsp;totalPrice|金额|number||
|&emsp;&emsp;&emsp;&emsp;frequencyCode||string||
|&emsp;&emsp;&emsp;&emsp;frequencyName|频次名称|string||
|&emsp;&emsp;&emsp;&emsp;routeCode||string||
|&emsp;&emsp;&emsp;&emsp;routeName|途径名称|string||
|&emsp;&emsp;&emsp;&emsp;drippingSpeed|滴速|integer||
|&emsp;&emsp;&emsp;&emsp;quantity|发药数量|integer||
|&emsp;&emsp;&emsp;&emsp;quantityUnit|发药单位|string||
|&emsp;&emsp;&emsp;&emsp;innerBarCode|内部条形码|string||
|&emsp;&emsp;&emsp;&emsp;note|医嘱备注|string||
|&emsp;&emsp;&emsp;&emsp;createOn|下嘱时间|string||
|&emsp;&emsp;&emsp;&emsp;externalDispensingFlag|是否是外配药|boolean||
|&emsp;&emsp;&emsp;&emsp;duration|持续时间（天数）|integer||
|&emsp;&emsp;&emsp;&emsp;practiceExecuteCount|诊所内执行次数|integer||
|&emsp;&emsp;&emsp;&emsp;orderedById|下嘱医生代码|string||
|&emsp;&emsp;&emsp;&emsp;orderedBy|下嘱医生名称|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"prescriptionType": "",
			"prescriptionNo": "",
			"date": "",
			"customer": {
				"id": "",
				"mrn": "",
				"name": "",
				"gender": 0,
				"age": "",
				"weight": "",
				"mobile": "",
				"allergyInfo": ""
			},
			"doctor": {
				"id": "",
				"name": ""
			},
			"department": {
				"id": "",
				"name": ""
			},
			"diagnosis": [
				{
					"diagnosisCode": "",
					"diagnosisName": "",
					"isMain": ""
				}
			],
			"medicinal": [
				{
					"code": "",
					"name": "",
					"orderNo": "",
					"orderSlaveNo": "",
					"orderTypeCodeName": "",
					"groupName": "",
					"spec": "",
					"dose": 0,
					"doseUnit": "",
					"price": 0,
					"totalPrice": 0,
					"frequencyCode": "",
					"frequencyName": "",
					"routeCode": "",
					"routeName": "",
					"drippingSpeed": 0,
					"quantity": 0,
					"quantityUnit": "",
					"innerBarCode": "",
					"note": "",
					"createOn": "",
					"externalDispensingFlag": true,
					"duration": 0,
					"practiceExecuteCount": 0,
					"orderedById": "",
					"orderedBy": ""
				}
			]
		}
	],
	"number": 0
}
```


## 获取授权机构下医嘱服务的医嘱数据


**接口地址**:`/api/v1/ehr/queryAdvicesOrderList`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|page|当前页码，如果不传默认为0，0为第一页|query|true|integer(int32)||
|size|每页大小，如果不传默认为20，最大值200|query|true|integer(int32)||
|start|开始日期，必填，包含该日期，如 2018-11-11，开始到结束日期最大为三个月|query|true|string(date-time)||
|end|结束日期，必填，包含该日期，如 2018-12-11，开始到结束日期最大为三个月|query|true|string(date-time)||
|clinicId|诊所Id，当医嘱编号为空时，诊所Id必填|query|false|string||
|orderNoList|医嘱编号 - orderNo，当诊所Id为空时，医嘱编号必填 |query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageSupervisionAdvicesOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|SupervisionAdvicesOrderDto|
|&emsp;&emsp;patientName|姓名|string||
|&emsp;&emsp;patientBirthday|生日|string||
|&emsp;&emsp;patientSex|性别 1女，2男，3未知|integer(int32)||
|&emsp;&emsp;patientMrn|患者病历号|string||
|&emsp;&emsp;patientId|患者ID|string||
|&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;visitId|到访ID|string||
|&emsp;&emsp;visitDate|到访时间|string||
|&emsp;&emsp;advicesOrderList|医嘱列表|array|SupervisionDataMedicinalDto|
|&emsp;&emsp;&emsp;&emsp;code|药品代码|string||
|&emsp;&emsp;&emsp;&emsp;name|药品名称|string||
|&emsp;&emsp;&emsp;&emsp;orderNo|医嘱编码 成组药的医嘱编码相同|string||
|&emsp;&emsp;&emsp;&emsp;orderSlaveNo|明细编码|string||
|&emsp;&emsp;&emsp;&emsp;orderTypeCodeName|医嘱类型 药品、检验、检查等|string||
|&emsp;&emsp;&emsp;&emsp;groupName||string||
|&emsp;&emsp;&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;&emsp;&emsp;dose|剂量|number||
|&emsp;&emsp;&emsp;&emsp;doseUnit|剂量单位|string||
|&emsp;&emsp;&emsp;&emsp;price|单价|number||
|&emsp;&emsp;&emsp;&emsp;totalPrice|金额|number||
|&emsp;&emsp;&emsp;&emsp;frequencyCode||string||
|&emsp;&emsp;&emsp;&emsp;frequencyName|频次名称|string||
|&emsp;&emsp;&emsp;&emsp;routeCode||string||
|&emsp;&emsp;&emsp;&emsp;routeName|途径名称|string||
|&emsp;&emsp;&emsp;&emsp;drippingSpeed|滴速|integer||
|&emsp;&emsp;&emsp;&emsp;quantity|发药数量|integer||
|&emsp;&emsp;&emsp;&emsp;quantityUnit|发药单位|string||
|&emsp;&emsp;&emsp;&emsp;innerBarCode|内部条形码|string||
|&emsp;&emsp;&emsp;&emsp;note|医嘱备注|string||
|&emsp;&emsp;&emsp;&emsp;createOn|下嘱时间|string||
|&emsp;&emsp;&emsp;&emsp;externalDispensingFlag|是否是外配药|boolean||
|&emsp;&emsp;&emsp;&emsp;duration|持续时间（天数）|integer||
|&emsp;&emsp;&emsp;&emsp;practiceExecuteCount|诊所内执行次数|integer||
|&emsp;&emsp;&emsp;&emsp;orderedById|下嘱医生代码|string||
|&emsp;&emsp;&emsp;&emsp;orderedBy|下嘱医生名称|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"patientName": "",
			"patientBirthday": "",
			"patientSex": 0,
			"patientMrn": "",
			"patientId": "",
			"clinicId": "",
			"visitId": "",
			"visitDate": "",
			"advicesOrderList": [
				{
					"code": "",
					"name": "",
					"orderNo": "",
					"orderSlaveNo": "",
					"orderTypeCodeName": "",
					"groupName": "",
					"spec": "",
					"dose": 0,
					"doseUnit": "",
					"price": 0,
					"totalPrice": 0,
					"frequencyCode": "",
					"frequencyName": "",
					"routeCode": "",
					"routeName": "",
					"drippingSpeed": 0,
					"quantity": 0,
					"quantityUnit": "",
					"innerBarCode": "",
					"note": "",
					"createOn": "",
					"externalDispensingFlag": true,
					"duration": 0,
					"practiceExecuteCount": 0,
					"orderedById": "",
					"orderedBy": ""
				}
			]
		}
	],
	"number": 0
}
```


## 获取授权机构下客户的医嘱服务的医嘱数据


**接口地址**:`/api/v1/ehr/queryAdvicesOrderListByPatientId`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|patientId|患者ID - customer id|query|false|string||
|orderNoList|医嘱编号 - orderNo|query|false|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SupervisionAdvicesOrderDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|patientName|姓名|string||
|patientBirthday|生日|string||
|patientSex|性别 1女，2男，3未知|integer(int32)|integer(int32)|
|patientMrn|患者病历号|string||
|patientId|患者ID|string||
|clinicId|门店ID|string||
|visitId|到访ID|string||
|visitDate|到访时间|string||
|advicesOrderList|医嘱列表|array|SupervisionDataMedicinalDto|
|&emsp;&emsp;code|药品代码|string||
|&emsp;&emsp;name|药品名称|string||
|&emsp;&emsp;orderNo|医嘱编码 成组药的医嘱编码相同|string||
|&emsp;&emsp;orderSlaveNo|明细编码|string||
|&emsp;&emsp;orderTypeCodeName|医嘱类型 药品、检验、检查等|string||
|&emsp;&emsp;groupName||string||
|&emsp;&emsp;spec|规格|string||
|&emsp;&emsp;dose|剂量|number||
|&emsp;&emsp;doseUnit|剂量单位|string||
|&emsp;&emsp;price|单价|number||
|&emsp;&emsp;totalPrice|金额|number||
|&emsp;&emsp;frequencyCode||string||
|&emsp;&emsp;frequencyName|频次名称|string||
|&emsp;&emsp;routeCode||string||
|&emsp;&emsp;routeName|途径名称|string||
|&emsp;&emsp;drippingSpeed|滴速|integer(int32)||
|&emsp;&emsp;quantity|发药数量|integer(int32)||
|&emsp;&emsp;quantityUnit|发药单位|string||
|&emsp;&emsp;innerBarCode|内部条形码|string||
|&emsp;&emsp;note|医嘱备注|string||
|&emsp;&emsp;createOn|下嘱时间|string||
|&emsp;&emsp;externalDispensingFlag|是否是外配药|boolean||
|&emsp;&emsp;duration|持续时间（天数）|integer(int32)||
|&emsp;&emsp;practiceExecuteCount|诊所内执行次数|integer(int32)||
|&emsp;&emsp;orderedById|下嘱医生代码|string||
|&emsp;&emsp;orderedBy|下嘱医生名称|string||


**响应示例**:
```javascript
[
	{
		"patientName": "",
		"patientBirthday": "",
		"patientSex": 0,
		"patientMrn": "",
		"patientId": "",
		"clinicId": "",
		"visitId": "",
		"visitDate": "",
		"advicesOrderList": [
			{
				"code": "",
				"name": "",
				"orderNo": "",
				"orderSlaveNo": "",
				"orderTypeCodeName": "",
				"groupName": "",
				"spec": "",
				"dose": 0,
				"doseUnit": "",
				"price": 0,
				"totalPrice": 0,
				"frequencyCode": "",
				"frequencyName": "",
				"routeCode": "",
				"routeName": "",
				"drippingSpeed": 0,
				"quantity": 0,
				"quantityUnit": "",
				"innerBarCode": "",
				"note": "",
				"createOn": "",
				"externalDispensingFlag": true,
				"duration": 0,
				"practiceExecuteCount": 0,
				"orderedById": "",
				"orderedBy": ""
			}
		]
	}
]
```


## 获取授权机构下医嘱服务的病历数据明细


**接口地址**:`/api/v1/ehr/queryMedicalRecordDetail`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|medicalRecordNo|病历记录编码 - medical record no|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PatientMedicalRecordDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|patientName|姓名|string||
|patientSex|性别 1女，2男，3未知|integer(int32)|integer(int32)|
|patientMrn|患者病历号|string||
|patientId|患者ID|string||
|patientBirthday|生日|string||
|visitId|到访ID|string||
|visitDate|到访时间|string||
|detailContent|病历Html|string||
|medicalRecordNo|病历ID|string||
|medicalTemplateName|病历模板名称|string||
|createBy|创建医生|string||
|createOn|创建时间|string||
|signStatusName|病历状态|string||
|signBy|签署医生|string||
|signOn|签署时间|string||
|clinicId|门店ID|string||
|clinicName|门店名称|string||
|itemParamList|当前病历控件的值信息|array|MedicalRecordItemBo|
|&emsp;&emsp;key|控件ID|string||
|&emsp;&emsp;value|控件值|string||
|&emsp;&emsp;desc|控件描述|string||


**响应示例**:
```javascript
{
	"patientName": "",
	"patientSex": 0,
	"patientMrn": "",
	"patientId": "",
	"patientBirthday": "",
	"visitId": "",
	"visitDate": "",
	"detailContent": "",
	"medicalRecordNo": "",
	"medicalTemplateName": "",
	"createBy": "",
	"createOn": "",
	"signStatusName": "",
	"signBy": "",
	"signOn": "",
	"clinicId": "",
	"clinicName": "",
	"itemParamList": [
		{
			"key": "",
			"value": "",
			"desc": ""
		}
	]
}
```


## 获取授权机构下医嘱服务的病历数据


**接口地址**:`/api/v1/ehr/queryMedicalRecordList`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|clinicId|诊所Id 必填|query|true|string||
|page|当前页码，如果不传默认为0，0为第一页|query|true|integer(int32)||
|size|每页大小，如果不传默认为20，最大值200|query|true|integer(int32)||
|start|开始日期，必填，包含该日期，如 2018-11-11，开始到结束日期最大为三个月|query|true|string(date-time)||
|end|结束日期，必填，包含该日期，如 2018-12-11，开始到结束日期最大为三个月|query|true|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageMedicalRecordPatientListDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|MedicalRecordPatientListDto|
|&emsp;&emsp;clinicId|门店ID|string||
|&emsp;&emsp;visitId|到访ID|string||
|&emsp;&emsp;visitDate|到访时间|string||
|&emsp;&emsp;medicalRecordNo|病历ID|string||
|&emsp;&emsp;patientId|患者ID|string||
|&emsp;&emsp;patientName|姓名|string||
|&emsp;&emsp;patientMrn|患者病历号|string||
|&emsp;&emsp;patientBirthday|生日|string||
|&emsp;&emsp;patientSex|性别 1女，2男，3未知|integer(int32)||
|&emsp;&emsp;createBy|创建医生|string||
|&emsp;&emsp;createOn|创建时间|string||
|&emsp;&emsp;signStatus||integer(int32)||
|&emsp;&emsp;signStatusName|病历状态|string||
|&emsp;&emsp;signBy|签署医生|string||
|&emsp;&emsp;signOn|签署时间|string||
|&emsp;&emsp;medicalTemplateName|病历模板名称|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"clinicId": "",
			"visitId": "",
			"visitDate": "",
			"medicalRecordNo": "",
			"patientId": "",
			"patientName": "",
			"patientMrn": "",
			"patientBirthday": "",
			"patientSex": 0,
			"createBy": "",
			"createOn": "",
			"signStatus": 0,
			"signStatusName": "",
			"signBy": "",
			"signOn": "",
			"medicalTemplateName": ""
		}
	],
	"number": 0
}
```


## 获取授权机构下客户的医嘱服务的病历数据


**接口地址**:`/api/v1/ehr/queryMedicalRecordListByPatientId`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|patientId|患者ID - customer id|query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|MedicalRecordPatientListDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|clinicId|门店ID|string||
|visitId|到访ID|string||
|visitDate|到访时间|string||
|medicalRecordNo|病历ID|string||
|patientId|患者ID|string||
|patientName|姓名|string||
|patientMrn|患者病历号|string||
|patientBirthday|生日|string||
|patientSex|性别 1女，2男，3未知|integer(int32)|integer(int32)|
|createBy|创建医生|string||
|createOn|创建时间|string||
|signStatus||integer(int32)|integer(int32)|
|signStatusName|病历状态|string||
|signBy|签署医生|string||
|signOn|签署时间|string||
|medicalTemplateName|病历模板名称|string||


**响应示例**:
```javascript
[
	{
		"clinicId": "",
		"visitId": "",
		"visitDate": "",
		"medicalRecordNo": "",
		"patientId": "",
		"patientName": "",
		"patientMrn": "",
		"patientBirthday": "",
		"patientSex": 0,
		"createBy": "",
		"createOn": "",
		"signStatus": 0,
		"signStatusName": "",
		"signBy": "",
		"signOn": "",
		"medicalTemplateName": ""
	}
]
```


# 12. 云晰系统集成


## 多品项开单，按品项拆分多个订单，成功后为已支付订单，忽略所有审批流程


**接口地址**:`/api/v1/integration/yunxi/create-order`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "operatorId": "",
  "customerId": "",
  "yunxiOrderNo": "",
  "orderTime": "",
  "lines": [
    {
      "yunxiOrderLineIndex": "1",
      "skuType": "",
      "skuId": "",
      "quantity": 5,
      "amount": 300.78
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|yunxiCreateOrderParams|多品项开单，按品项拆分多个订单参数|body|true|YunxiCreateOrderParams|YunxiCreateOrderParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||true|string||
|&emsp;&emsp;customerId|客户ID||true|string||
|&emsp;&emsp;yunxiOrderNo|云晰订单号||true|string||
|&emsp;&emsp;orderTime|下单时间(ISO-8601标准格式) - 仅允许指定过去时间||false|string(date-time)||
|&emsp;&emsp;lines|云晰订单行信息||true|array|YunxiCreateOrderLineParams|
|&emsp;&emsp;&emsp;&emsp;yunxiOrderLineIndex|云晰订单行号||true|string||
|&emsp;&emsp;&emsp;&emsp;skuType|品项类型 必须是service、promotion或card,可用值:service,promotion,card||true|string||
|&emsp;&emsp;&emsp;&emsp;skuId|品项ID 不允许重复||true|string||
|&emsp;&emsp;&emsp;&emsp;quantity|数量(卡项最大50)||true|integer||
|&emsp;&emsp;&emsp;&emsp;amount|成交金额||true|number||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|提交成功|YunxiCreateOrderResponse|
|400|无效的请求参数|YunxiCreateOrderResponse|


**响应状态码-200**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|message|失败原因 - 失败时必填|string||
|orders|订单拆分结果|array|CreateOrderDto|
|&emsp;&emsp;status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|&emsp;&emsp;message|失败原因 - 失败时必填|string||
|&emsp;&emsp;yunxiOrderLineIndex|云晰订单行号|string||
|&emsp;&emsp;skuId|品项ID|string||
|&emsp;&emsp;orderNo|医美订单号(仅成功订单返回)|string||


**响应示例**:
```javascript
{
	"status": "",
	"message": "",
	"orders": [
		{
			"status": "",
			"message": "",
			"yunxiOrderLineIndex": "",
			"skuId": "",
			"orderNo": ""
		}
	]
}
```


**响应状态码-400**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|message|失败原因 - 失败时必填|string||
|orders|订单拆分结果|array|CreateOrderDto|
|&emsp;&emsp;status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|&emsp;&emsp;message|失败原因 - 失败时必填|string||
|&emsp;&emsp;yunxiOrderLineIndex|云晰订单行号|string||
|&emsp;&emsp;skuId|品项ID|string||
|&emsp;&emsp;orderNo|医美订单号(仅成功订单返回)|string||


**响应示例**:
```javascript
{
	"status": "",
	"message": "",
	"orders": [
		{
			"status": "",
			"message": "",
			"yunxiOrderLineIndex": "",
			"skuId": "",
			"orderNo": ""
		}
	]
}
```


## 单订单（单品项）核销状态同步


**接口地址**:`/api/v1/integration/yunxi/fulfillment`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "operatorId": "",
  "orderNo": "",
  "quantity": 3,
  "amount": 3000.5
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|yunxiFulfillmentParams|单订单（单品项）核销状态同步参数|body|true|YunxiFulfillmentParams|YunxiFulfillmentParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||true|string||
|&emsp;&emsp;orderNo|医美订单号||true|string||
|&emsp;&emsp;quantity|核销数量(需等于品项剩余数量)||true|integer(int32)||
|&emsp;&emsp;amount|核销金额（需等于剩余金额）||true|number||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|提交成功|GeneralYunxiResponse|
|400|无效的请求参数|GeneralYunxiResponse|


**响应状态码-200**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|message|失败原因 - 失败时必填|string||


**响应示例**:
```javascript
{
	"status": "",
	"message": ""
}
```


**响应状态码-400**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|message|失败原因 - 失败时必填|string||


**响应示例**:
```javascript
{
	"status": "",
	"message": ""
}
```


## 单订单（单品项）全部或部分退款


**接口地址**:`/api/v1/integration/yunxi/refund`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "clinicId": "",
  "operatorId": "",
  "yunxiRefundOrderNo": "",
  "yunxiRefundOrderLineIndex": "",
  "refundTime": "",
  "orderNo": "",
  "quantity": 5,
  "amount": 300.78,
  "allRefunded": true
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|yunxiRefundOrderParams|单品项全部/部分退款参数|body|true|YunxiRefundOrderParams|YunxiRefundOrderParams|
|&emsp;&emsp;clinicId|诊所ID||true|string||
|&emsp;&emsp;operatorId|操作人员工ID||false|string||
|&emsp;&emsp;yunxiRefundOrderNo|云晰退款单号||true|string||
|&emsp;&emsp;yunxiRefundOrderLineIndex|云晰退款行号||true|string||
|&emsp;&emsp;refundTime|退款时间(ISO-8601标准格式) - 仅允许指定过去时间||false|string(date-time)||
|&emsp;&emsp;orderNo|医美订单号||true|string||
|&emsp;&emsp;quantity|退款数量||true|integer(int32)||
|&emsp;&emsp;amount|退款金额||true|number||
|&emsp;&emsp;allRefunded|是否已退完/无剩余数量-数量已退完需传true，校验剩余数量需为0||true|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|提交成功|GeneralYunxiResponse|
|400|无效的请求参数|GeneralYunxiResponse|


**响应状态码-200**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|message|失败原因 - 失败时必填|string||


**响应示例**:
```javascript
{
	"status": "",
	"message": ""
}
```


**响应状态码-400**:


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|status|状态 S-成功，F-失败，P-部分成功(仅多行参数场景)|string||
|message|失败原因 - 失败时必填|string||


**响应示例**:
```javascript
{
	"status": "",
	"message": ""
}
```


# X1. 业务报表数据


## 查询员工销售业绩数据


**接口地址**:`/api/v1/analytic/cash/performance/page`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|startDate|业绩开始时间，必填，包含该日期，如 2018-11-11，开始到结束日期最大为三个月,不可查询1年前的数据|query|true|string(date-time)||
|endDate|业绩结束时间，默认为当前时间，包含该日期，如 2018-11-11，开始到结束日期最大为三个月,不可查询1年前的数据|query|false|string(date-time)||
|performanceOrganizationId|业绩门店id|query|false|string||
|roleCodes|业绩角色code，包括orderHeader-sales(开单人)、orderHeader-developer(开发人)、orderHeader-beautician(美容师)、orderHeader-consultant(开单咨询师)、orderHeader-doctor(分诊医生)、orderHeader-nurse(护士)、general(业绩人按比例)、billing-customer-consultant(收银时所属咨询师)、billing-customer-tmk-service(收银时所属电网咨询师)、billing-customer-consult-assistant(收银时所属咨询师助理)、billing-customer-beautician(收银时所属美容师)、billing-customer-doctor(收银时所属主诊医生)、order-customer-consultant(开单时所属咨询师)、order-customer-tmk-service(开单时所属电网咨询师)、order-customer-consult-assistant(开单时所属咨询师)、order-customer-beautician(开单时所属美容师)、order-customer-doctor(开单时所属主诊医生)|query|false|array|string|
|employeeId|员工id|query|false|string||
|page|页码|query|false|integer(int32)||
|size|单页数量|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageEmployeeCashPerformanceDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|EmployeeCashPerformanceDto|
|&emsp;&emsp;performanceDate|业绩时间(格式: yyyy-MM-dd HH:mm:ss)|string||
|&emsp;&emsp;performanceOrganizationName|业绩门店|string||
|&emsp;&emsp;employeeNo|员工号|string||
|&emsp;&emsp;employeeName|员工姓名|string||
|&emsp;&emsp;roleName|业绩角色|string||
|&emsp;&emsp;performancePercent|销售业绩比例|number||
|&emsp;&emsp;performanceAmount|销售业绩基数|number||
|&emsp;&emsp;customerNumber|会员号|string||
|&emsp;&emsp;customerName|客户名称|string||
|&emsp;&emsp;classificationName|客户类别|string||
|&emsp;&emsp;customerSource|客户来源|string||
|&emsp;&emsp;customerOrganizationName|客户所属门店|string||
|&emsp;&emsp;orderNumber|订单号|string||
|&emsp;&emsp;refundNumber|退单号|string||
|&emsp;&emsp;orderTotalTransactionAmount|订单金额|number||
|&emsp;&emsp;orderTotalRetailAmount|订单原价|number||
|&emsp;&emsp;salesOrderDiscount|订单折扣|string||
|&emsp;&emsp;orderLineIndex|订单行号|string||
|&emsp;&emsp;orderLineTypeDesc|行类型|string||
|&emsp;&emsp;lineProductName|行名称|string||
|&emsp;&emsp;itemProductTypeDesc|品项类型|string||
|&emsp;&emsp;prdSrvNumber|品项编号|string||
|&emsp;&emsp;prdSrvName|品项名称|string||
|&emsp;&emsp;itemDiscount|品项订单折扣|string||
|&emsp;&emsp;documentTypeDesc|单据类型|string||
|&emsp;&emsp;documentNumber|单据号|string||
|&emsp;&emsp;documentAmount|单据金额|number||
|&emsp;&emsp;billingMethodDetail|收款详情|string||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"performanceDate": "",
			"performanceOrganizationName": "",
			"employeeNo": "",
			"employeeName": "",
			"roleName": "",
			"performancePercent": 0,
			"performanceAmount": 0,
			"customerNumber": "",
			"customerName": "",
			"classificationName": "",
			"customerSource": "",
			"customerOrganizationName": "",
			"orderNumber": "",
			"refundNumber": "",
			"orderTotalTransactionAmount": 0,
			"orderTotalRetailAmount": 0,
			"salesOrderDiscount": "",
			"orderLineIndex": "",
			"orderLineTypeDesc": "",
			"lineProductName": "",
			"itemProductTypeDesc": "",
			"prdSrvNumber": "",
			"prdSrvName": "",
			"itemDiscount": "",
			"documentTypeDesc": "",
			"documentNumber": "",
			"documentAmount": 0,
			"billingMethodDetail": ""
		}
	],
	"number": 0
}
```


## 查询员工执行业绩数据


**接口地址**:`/api/v1/analytic/execution/performance/page`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|startDate|业绩开始时间，必填，包含该日期，如 2018-11-11，开始到结束日期最大为三个月,不可查询1年前的数据|query|true|string(date-time)||
|endDate|业绩结束时间，默认为当前时间，包含该日期，如 2018-11-11，开始到结束日期最大为三个月,不可查询1年前的数据|query|false|string(date-time)||
|performanceOrganizationId|业绩门店id|query|false|string||
|roleCodes|业绩角色code，包括orderHeader-sales(开单人)、orderHeader-developer(开发人)、orderHeader-beautician(美容师)、orderHeader-consultant(开单咨询师)、orderHeader-doctor(分诊医生)、orderHeader-nurse(护士)、general(业绩人按比例)、billing-customer-consultant(收银时所属咨询师)、billing-customer-tmk-service(收银时所属电网咨询师)、billing-customer-consult-assistant(收银时所属咨询师助理)、billing-customer-beautician(收银时所属美容师)、billing-customer-doctor(收银时所属主诊医生)、order-customer-consultant(开单时所属咨询师)、order-customer-tmk-service(开单时所属电网咨询师)、order-customer-consult-assistant(开单时所属咨询师)、order-customer-beautician(开单时所属美容师)、order-customer-doctor(开单时所属主诊医生)|query|false|array|string|
|employeeId|员工id|query|false|string||
|page|页码|query|false|integer(int32)||
|size|单页数量|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageEmployeeExecutionPerformanceDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|EmployeeExecutionPerformanceDto|
|&emsp;&emsp;performanceDate|业绩时间(格式: yyyy-MM-dd HH:mm:ss)|string||
|&emsp;&emsp;performanceOrganizationName|业绩门店|string||
|&emsp;&emsp;employeeNo|员工号|string||
|&emsp;&emsp;employeeName|员工姓名|string||
|&emsp;&emsp;roleName|业绩角色|string||
|&emsp;&emsp;performancePercent|执行业绩比例|number||
|&emsp;&emsp;performanceAmount|执行业绩|number||
|&emsp;&emsp;customerNumber|会员号|string||
|&emsp;&emsp;customerName|客户名称|string||
|&emsp;&emsp;classificationName|客户类别|string||
|&emsp;&emsp;customerSource|客户来源|string||
|&emsp;&emsp;customerOrganizationName|客户所属门店|string||
|&emsp;&emsp;orderNumber|订单号|string||
|&emsp;&emsp;refundNumber|退单号|string||
|&emsp;&emsp;orderTotalTransactionAmount|订单金额|number||
|&emsp;&emsp;orderTotalRetailAmount|订单原价|number||
|&emsp;&emsp;salesOrderDiscount|订单折扣|string||
|&emsp;&emsp;orderLineIndex|订单行号|string||
|&emsp;&emsp;orderLineTypeDesc|行类型|string||
|&emsp;&emsp;lineProductName|行名称|string||
|&emsp;&emsp;orderItemIndex|订单条目号|string||
|&emsp;&emsp;itemProductTypeDesc|品项类型|string||
|&emsp;&emsp;prdSrvNumber|品项编号|string||
|&emsp;&emsp;prdSrvName|品项名称|string||
|&emsp;&emsp;itemDiscount|品项订单折扣|string||
|&emsp;&emsp;documentTypeDesc|单据类型|string||
|&emsp;&emsp;documentNumber|单据号|string||
|&emsp;&emsp;documentAmount|单据金额|number||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"performanceDate": "",
			"performanceOrganizationName": "",
			"employeeNo": "",
			"employeeName": "",
			"roleName": "",
			"performancePercent": 0,
			"performanceAmount": 0,
			"customerNumber": "",
			"customerName": "",
			"classificationName": "",
			"customerSource": "",
			"customerOrganizationName": "",
			"orderNumber": "",
			"refundNumber": "",
			"orderTotalTransactionAmount": 0,
			"orderTotalRetailAmount": 0,
			"salesOrderDiscount": "",
			"orderLineIndex": "",
			"orderLineTypeDesc": "",
			"lineProductName": "",
			"orderItemIndex": "",
			"itemProductTypeDesc": "",
			"prdSrvNumber": "",
			"prdSrvName": "",
			"itemDiscount": "",
			"documentTypeDesc": "",
			"documentNumber": "",
			"documentAmount": 0
		}
	],
	"number": 0
}
```


## 查询往来账数据


**接口地址**:`/api/v1/analytic/financial/accountDealing/page`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|startDate|开始日期，必填，包含该日期，如 2018-11-11，开始到结束日期最大为三个月|query|true|string(date-time)||
|endDate|结束日期，必填，包含该日期，如 2018-12-11，开始到结束日期最大为三个月|query|true|string(date-time)||
|fromStoreId|应付门店ID|query|false|string||
|toStoreId|应收门店ID|query|false|string||
|customerId|客户id|query|false|string||
|page|页码|query|false|integer(int32)||
|size|单页数量|query|false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PageAccountDealingDto|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|totalElements|总数据量|integer(int64)|integer(int64)|
|totalPages|总页数|integer(int32)|integer(int32)|
|size|分页大小|integer(int32)|integer(int32)|
|content||array|AccountDealingDto|
|&emsp;&emsp;id|id|string||
|&emsp;&emsp;bizTime|往来产生日期(格式: yyyy-MM-dd HH:mm:ss)|string||
|&emsp;&emsp;fromStoreId|应付门店ID|string||
|&emsp;&emsp;fromStoreName|应付门店名称|string||
|&emsp;&emsp;toStoreId|应收门店ID|string||
|&emsp;&emsp;toStoreName|应收门店名称|string||
|&emsp;&emsp;customerId|客户ID|string||
|&emsp;&emsp;customerName|客户名称|string||
|&emsp;&emsp;documentNumber|业务单号|string||
|&emsp;&emsp;dealingType|往来类型code executed:跨店执行,transfer:跨店转赠,exchange:跨店换购,transfer_account:跨店转账,deduction:跨店资产抵扣,refund:跨店退款,sale:跨店收欠款|string||
|&emsp;&emsp;dealingTypeName|往来类型|string||
|&emsp;&emsp;orderItemNumber|关联订单条目号|string||
|&emsp;&emsp;orderLineName|关联订单条目名称|string||
|&emsp;&emsp;deltaQuantity|往来积分|integer(int32)||
|&emsp;&emsp;deltaAmountCash|现款支付|number||
|&emsp;&emsp;deltaAmountAsset|资产抵扣|number||
|&emsp;&emsp;deltaAmountPlatform|平台结算|number||
|&emsp;&emsp;deltaAmountEquity|权益折让|number||
|&emsp;&emsp;amountTotal|汇总|number||
|number|当前页码|integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"totalElements": 0,
	"totalPages": 0,
	"size": 0,
	"content": [
		{
			"id": "",
			"bizTime": "",
			"fromStoreId": "",
			"fromStoreName": "",
			"toStoreId": "",
			"toStoreName": "",
			"customerId": "",
			"customerName": "",
			"documentNumber": "",
			"dealingType": "",
			"dealingTypeName": "",
			"orderItemNumber": "",
			"orderLineName": "",
			"deltaQuantity": 0,
			"deltaAmountCash": 0,
			"deltaAmountAsset": 0,
			"deltaAmountPlatform": 0,
			"deltaAmountEquity": 0,
			"amountTotal": 0
		}
	],
	"number": 0
}
```


# X2. SCRM集成服务


## scrm服务代理


**接口地址**:`/api/v1/scrm/proxy`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "endpoint": "",
  "method": "",
  "parameters": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|scrmGatewayParams|ScrmGatewayParams|body|true|ScrmGatewayParams|ScrmGatewayParams|
|&emsp;&emsp;endpoint|请求远端URI，相对路径||true|string||
|&emsp;&emsp;method|请求HTTP方法,可用值:POST,GET||false|string||
|&emsp;&emsp;parameters|参数集合 - Map形式, 可嵌套||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|default|default response|ScrmResult|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|result||integer(int32)|integer(int32)|
|msg||string||
|body||object||


**响应示例**:
```javascript
{
	"result": 0,
	"msg": "",
	"body": {}
}
```


## 查询授权机构下的微信公众号粉丝


**接口地址**:`/api/v1/scrm/wechat-fan`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|appId|公众号ID|query|true|string||
|openId|粉丝ID|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SimpleBinding|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|appId|公众号ID|string||
|openId|粉丝ID|string||
|customerId|客户ID|string||


**响应示例**:
```javascript
[
	{
		"appId": "",
		"openId": "",
		"customerId": ""
	}
]
```


## 在授权机构下绑定微信公众号粉丝


**接口地址**:`/api/v1/scrm/wechat-fan/bind`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "appId": "",
  "openId": "",
  "customerId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBindingParams|CreateBindingParams|body|true|CreateBindingParams|CreateBindingParams|
|&emsp;&emsp;appId|公众号ID||true|string||
|&emsp;&emsp;openId|粉丝ID||true|string||
|&emsp;&emsp;customerId|客户ID||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|201|Created|SimpleBinding|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|appId|公众号ID|string||
|openId|粉丝ID|string||
|customerId|客户ID|string||


**响应示例**:
```javascript
{
	"appId": "",
	"openId": "",
	"customerId": ""
}
```