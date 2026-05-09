#### Badan Pusat Statistik

# API Documentation

The BPS APIs provides programmatic access to read BPS data. User can read about Publication, Press Release, BPS Event, and a lot of various kinds of data presented in the static table and dynamic tables. The BPS API identifies user with key token. User can get the key token from API-Portal website. Every user can get two until three key token to access the API. Responses are available in JSON.

### **Domain**

---

This service is used to displays all BPS Statistics domain website

https://webapi.bps.go.id/v1/api/domain

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| type | String | Type to show domain (all:for all domain ; prov:for province domain ; kab:for city/regency domain ; kabbyprov:for all city/regency in province) Allowed values: "all", "prov", "kab", "kabbyprov" |
| prov **optional** | String | Prov ID selected to show all city/regency domain. input this parameter when using "kabbyprov" type. Size range: 4 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list domain. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List Domain |
|     domain\_id | String | ID domain |
|     domain\_name | String | name of domain |
|     domain\_url | String | URL domain |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":1,
"total":3
},
[{
"domain_id":"0000",
"domain_name":"Pusat",
"domain_url":"https://www.bps.go.id"
},{
"domain_id":"1100",
"domain_name":"Aceh",
"domain_url":"https://aceh.bps.go.id"
},{
"domain_id":"1200",
"domain_name":"Sumatera Utara",
"domain_url":"https://sumut.bps.go.id",
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Subject**

---

##### **List of All Subject**

This service is used to displays all subject data on the website

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display Subject Data (subject) for subject is "subject" |
| lang **optional** | String | Language to display subject Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed subject (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Allowed values: 4 |
| subcat **optional** | Number | Subject categories selected to display subject data Allowed values: 1, 2, 3, 4, ..., n |
| page **optional** | Number | Page to display subject Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list subject. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List subject |
|     sub\_id | Number | ID unique of subject |
|     title | String | Title of subject |
|     subcat\_id | String | ID unique of sub category |
|     subcat | String | Name of sub category |
|     ntable | Number | Sum of table on each subject |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 5,
"per_page": 10,
"count": 10,
"total": 48
},
[
{
"sub_id": 40,
"title": "Gender",
"subcat_id": 1,
"subcat": "Sosial dan Kependudukan",
"ntabel": null
}, ...
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Subject Categories**

---

##### **List of All Subject Categories**

This service is used to displays all subject data categories on the website

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display Subject Categories (subcat) for subcat is "subcat" |
| lang **optional** | String | Language to display subject category Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed subcat (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display subcat Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list subcat. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List subcat |
|     subcat\_id | Number | ID unique of subcat |
|     title | String | Title of subcat |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 10,
"count": 4,
"total": 4
},
[
...
{
"subcat_id": 1,
"title": "Sosial dan Kependudukan"
},
...
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Dynamic Data**

---

##### **Data**

This service is used to displays data of dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display Data for variable is "data" |
| lang **optional** | String | Language to display data Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed variable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| var | Number | Variable ID selected to display data Allowed values: 1, 2, 3, 4, ..., n |
| turvar **optional** | Number | Derived Variable ID selected to display data Allowed values: 1, 2, 3, 4, ..., n |
| vervar **optional** | Number | Vertical Variable ID selected to display data Allowed values: 1, 2, 3, 4, ..., n |
| th | Number | Period data ID selected to display data Allowed values: 1, 2;3, 2:6 |
| turth **optional** | Number | Derived Period Data ID selected to display data Allowed values: 1, 2;3, 2:6 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list subject. |
| var | Number | Variable ID |
| turvar | Number | Derived Variable ID |
| labelvervar | Number | Title of Vertical Variable |
| vervar | Number | Vertical Variable ID |
| tahun | Number | Period of Data |
| turtahun | Number | Derived period data |
| datacontent | Object | Data |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"var": [
{
"val": 145,
"label": "Persentase Rumah Tangga Menurut Provinsi dan Sumber Penerangaan",
"unit": "Persen",
"subj": "Lingkungan Hidup",
"def": "",
"decimal": "",
"note": "- Sumber: Diolah dari Hasil Survei Sosial Ekonomi Nasional (Susenas), BPS.\\n<br>- Tahun 2000 Tidak termasuk Dista Aceh dan Maluku\\n<br>- Tahun 2006 Tanpa kabupaten Bantul \\n<br>-Data dikutip dari Publikasi Statistik Indonesia.\\n"
}
],
"turvar": [
{
"val": 289,
"label": "Listrik PLN"
},
...
],
"labelvervar": "Provinsi",
"vervar": [
{
"val": 9999,
"label": "INDONESIA"
},
...
],
"tahun": [
{
"val": 100,
"label": "2000"
},
...
],
"turtahun": [
{
"val": 0,
"label": "Tahun"
},
...
],
"metadata": {
"activity": null,
...
},
"datacontent": {
"99991452891000": 83.68,
...
}
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List Derived Period Data**

This service is used to displays all derived period data on dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display derived period data for derived period data is "turth" |
| lang **optional** | String | Language to display derived period data Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed derived period data (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| var **optional** | Number | Variable ID selected to display derived period data Allowed values: 1, 2, 3, 4, ..., n |
| page **optional** | Number | Page to display derived period data Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list subject. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List subject |
|     turth\_id | String | ID unique of subject |
|     turth | String | Title of subject |
|     group\_turth\_id | String | ID unique of subject |
|     name\_group\_turth | String | Title of subject |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"turth_id":0,
"turth":"Tahun",
"group_turth_id":0,
"name_group_turth":"Tahunan"
},{
"turth_id":1,
"turth":"Bulanan",
"group_turth_id":1,
"name_group_turth":"January"
},{
"turth_id":2,
"turth":"Bulanan",
"group_turth_id":2,
"name_group_turth":"February"
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List Derived Variable**

This service is used to displays all derived variable on dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display derived variable for derived variable is "turvar" |
| lang **optional** | String | Language to display derived variable Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed variable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| var **optional** | Number | Variable selected to display derived variable Allowed values: 1, 2, 3, 4, ..., n |
| group **optional** | Number | Group Vertical Variable selected to display derived variable Allowed values: 1, 2, 3, 4, ..., n |
| nopage **optional** | Boolean | param to show with no pagination (1 if want to no pagination) Allowed values: 0, 1 |
| page **optional** | Number | Page to display derived variable Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list derived variable. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List derived variable |
|     turvar\_id | Number | ID unique of derived variable |
|     turvar | String | Title of derived variable |
|     group\_turvar\_id | Number | ID unique of item group derived variable |
|     name\_group\_turvar | String | Group Name of derived variable \* |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"turvar_id":3200,
"turvar":"Title of vertical variable",
"group_turvar_id":"Group Name",
"name_group_turvar":"Wilayah Provinsi"
},{
"turvar_id":3200,
"turvar":"Title of vertical variable",
"group_turvar_id":"Group Name",
"name_group_turvar":"Wilayah Provinsi"
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List Period Data**

This service is used to displays all period data on dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display period data for variable is "th" |
| lang **optional** | String | Language to display period data Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed variable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| var **optional** | Number | Variable ID selected to display period data Allowed values: 1, 2, 3, 4, ..., n |
| page **optional** | Number | Page to display subject Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list subject. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List subject |
|     th\_id | Number | ID unique of period data |
|     th | String | Title of period data |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"th_id":117,
"th":2017
},{
"th_id":116,
"th":2016
},{
"th_id":115,
"th":2015
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List Unit Data**

This service is used to displays all unit data on dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display unit data for unit data is "unit" |
| lang **optional** | String | Language to display unit data Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed unit data(see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display unit data Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list unit data. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List unit data |
|     unit\_id | Number | ID unique of unit data |
|     unit | String | Title of unit data |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"unit_id":45678,
"unit":"Title of unit",
},{
"unit_id":45678,
"unit":"Title of unit",
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List Variable**

This service is used to displays all variable on dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display variable Data (subject) for variable is "var" |
| lang **optional** | String | Language to display variable Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed variable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Allowed values: 4 |
| subject **optional** | Number | Subject ID selected to display subject data Allowed values: 1, 2, 3, 4, ..., n |
| page **optional** | Number | Page to display subject Allowed values: 1, 2, 3, 4, ..., n |
| year **optional** | Number | Year selected to display statictable Allowed values: 1, 2, 3, 4, ..., n |
| area **optional** | Boolean | Parameter to show exist variabel on domain (1 if show exist var) Allowed values: 0, 1 |
| vervar **optional** | Number | Vertical Variabel ID selected Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list variable. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List variable |
|     var\_id | Number | ID unique of variable |
|     title | String | Title of variable |
|     sub\_id | Number | ID unique of variable |
|     sub\_name | String | Title of variable |
|     def | String | Definition of Variable |
|     notes | String | Notes for Variable |
|     vertical | Number | ID vertical variable |
|     unit | String | Unit Metric |
|     graph\_id | Number | ID graph |
|     graph\_name | String | graph name |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"var_id":45678,
"title":"Title of variable",
"sub_id":45,
"sub_name":"Subject Name",
"def":"definition",
"notes":"notes",
"vertical":3,
"unit":"Billion",
"graph_id":3,
"graph_name":"Line",
},{
"var_id":458,
"title":"Title of variable 2",
"sub_id":45,
"sub_name":"Subject Name",
"def":"definition",
"notes":"notes",
"vertical":3,
"unit":"Billion",
"graph_id":3,
"graph_name":"Line",
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List Vertical Variable**

This service is used to displays all vertical variable on dynamic table in the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display vertical variable Data for vertical variable is "vervar" |
| lang **optional** | String | Language to display vertical variable Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed variable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Allowed values: 4 |
| var **optional** | Number | Variable selected to display vertical variable Allowed values: 1, 2, 3, 4, ..., n |
| page **optional** | Number | Page to display vertical variable Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list vertical variable. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List vertical variable |
|     vervar\_id | Number | ID unique of vertical variable |
|     vervar | String | Title of vertical variable |
|     item\_ver\_id | Number | ID unique of item vertical variable |
|     group\_ver\_id | Number | ID unique of Group vertical variable |
|     name\_group\_ver\_id | String | Group Name of vertical variable \* |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"vervar_id":3200,
"vervar":"Title of vertical variable",
"item_ver_id":45,
"group_ver_id":"Group Name",
"name_group_ver_id":"Wilayah Provinsi"
},{
"vervar_id":3200,
"vervar":"Title of vertical variable",
"item_ver_id":45,
"group_ver_id":"Group Name",
"name_group_ver_id":"Wilayah Provinsi"
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Census Data** (sensus.bps.go.id)

---

##### **List of Census Events**

This service is used to return a list of events included in the Census Web

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/sensus/id/37/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| id | Number | Id number of the service. To display a list of events that is included in the Census, **use code 37\.** |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of events list |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List events |
|     id | Number | ID of Event |
|     kegiatan | String | Name of Event |
|     tahun\_kegiatan | Number | Year of Event |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
[
{
"id": {{id of event}},
"kegiatan": {{name of event}},
"tahun_kegiatan": {{year of event}}
},
…
]
]
}
```

###### **Error 4xx**

| Field | Type | Description |
| ----- | ----- | ----- |
| Status | String | Return status, OK if success and Error if any error occurred. |
| Data-availibility | String | Availability status of events list |

###### **Error Response**

```
{
"status": "Error",
"data-availability": "not-available",
"data": [
{
"page": 1,
"pages": 0,
"per_page": 25,
"count": 0,
"total": 0
},
[]
]
}
```

---

##### **Data Topics in the Census**

This service is used to display the data topics available in the census that we choose.

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/sensus/id/38/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| id | Number | Id number of the service. To display a list of data topics that is included in the Census, **use code 38\.** |
| Kegiatan | String | ID of census event that we choose to display the data topics, use service list of events to get the ID. Example: sp2020 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of Data Topics |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List Data Topics |
|     id | Number | ID of Data Topics |
|     topik | String | Name of Data Topic in Bahasa |
|     topic | String | Name of Data Topic in English |
|     id\_kegiatan | Number | ID of Events |
|     kegiatan | String | Name of event in Bahasa |
|     event | String | Name of event in English |
|     alias\_kegiatan | String | Alias of event in Bahasa |
|     alias\_event | String | Alias of event in English |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
[
{
"id": {{id of Data Topic}},
"topik": {{name of Data topic in bahasa}},
"topic": {{name of Data topic in english}},
"id_kegiatan": {{Id of event}},
"kegiatan": {{Name of event in Bahasa}},
"event": {{Name of event in English}},
"alias_kegiatan": {{Alias of event in Bahasa}},
"alias_event": {{Alias of event in English}}
}
]
]
}
```

###### **Error 4xx**

| Field | Type | Description |
| ----- | ----- | ----- |
| Status | String | Return status, OK if success and Error if any error occurred. |
| Data-availibility | String | Availability status of data topics |

###### **Error Response**

```
{
"status": "Error",
"data-availability": "not-available",
"data": [
{
"page": 1,
"pages": 0,
"per_page": 25,
"count": 0,
"total": 0
},
[]
]
}
```

---

##### **List of Census Event Areas**

This service is used to return a list of areas in the Census Event

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/sensus/id/38/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| id | Number | Id number of the service. To display a list of census event areas, **use code 39\.** |
| Kegiatan | String | ID of census event that we choose to display the census event areas, use service list of events to get the ID. Example: sp2020 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of Census Event Area |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List of Area |
|     id | Number | ID of area |
|     kode\_mfd | String | MFD Code of area |
|     nama | String | Name of area |
|     slug | String | \- |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
[
{
"id": {{ ID of Census Event Area}},
"kode_mfd": {{ MFD CODE}},
"nama": {{ Name of area }},
"slug": \-
},
```

###### **Error 4xx**

| Field | Type | Description |
| ----- | ----- | ----- |
| Status | String | Return status, OK if success and Error if any error occurred. |
| Data-availibility | String | Availability status of census event area |

###### **Error Response**

```
{
"status": "Error",
"data-availability": "not-available",
"data": [
{
"page": 1,
"pages": 0,
"per_page": 25,
"count": 0,
"total": 0
},
[]
]
}
```

---

##### **List of Available Dataset based on Event and Data Topic**

This service is used to return a list of events included in the Census

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/sensus/id/40/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| id | Number | Id number of the service. To display a list of available dataset, **use code 40\.** |
| Kegiatan | String | ID of census event that we choose to display the census dataset, use service list of events to get the ID. Example: sp2020 |
| Topik | Number | ID of Data topic, use service list of data topics to get the ID. |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of Dataset |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List of Dataset |
|     id | Number | ID of dataset |
|     id\_topik | Number | ID of data topic |
|     topic | String | Name of data topic |
|     id\_kegiatan | Number | ID of census event |
|     Nama | String | Name of dataset |
|     deskripsi | String | Description of dataset |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
[
{
"id": {{ Id of dataset }},
"id_topik": {{ Id of data topic }},
"topik": {{ Name of data topic }},
"id_kegiatan": {{ Id of Census Event }},
"nama": {{ Name of dataset }},
"deskripsi": {{ Description of dataset }}
}
]
}
```

###### **Error 4xx**

| Field | Type | Description |
| ----- | ----- | ----- |
| Status | String | Return status, OK if success and Error if any error occurred. |
| Data-availibility | String | Availability status of dataset |

###### **Error Response**

```
{
"status": "Error",
"data-availability": "not-available",
"data": [
{
"page": 1,
"pages": 0,
"per_page": 25,
"count": 0,
"total": 0
},
[]
]
}
```

---

##### **Census Data**

This service is used to return census data

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/sensus/id/41/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| id | Number | Id number of the service. To display census data based on ID of Census Event, Id of Census Area, and ID of Dataset, **use code 41\.** |
| Kegiatan | String | ID of census event that we choose to display the census dataset, use service list of events to get the ID. Example: sp2020 |
| Wilayah\_sensus | Number | ID of Census Event Area, use service list of census event area to get the ID. |
| Dataset | Number | ID of Dataset, use service list of census dataset to get the ID. |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of Data |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Data Details |
|     timestamp | date | Last Sync |
|     status | String | Status of availability |
|     data\_count | String | Count of the data |
|     data | object\[\] | Data content |
|       id\_wilayah | number | ID of area |
|       kode\_wilayah | number | Area code |
|       nama\_wilayah | string | Name of area |
|       level\_wilayah | number | Administration level of area |
|       id\_indikator | number | ID of indicator |
|       nama\_indikator | number | Name of indikator |
|       id\_kategori\_x | number | ID of indicator x-th category |
|       name\_kategori\_x | string | Name of indicator x-th category |
|       id\_item\_kategori\_x | number | ID of indicator x-th category item |
|       kode\_item\_kategori\_x | number | Code of indicator x-th category item |
|       nama\_item\_kategori\_x | string | Name of indicator x-th category item |
|       Period | number | Year of indicator |
|       nilai | number | Value of indicator |

###### **Success Response**

```
HTTP/1.1 200 OK
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
{
"timestamp": "2022-07-11T10:35:03.125",
"status": 200,
"data_count": 315,
"data": [
{
"id_wilayah": "8f42c43e-051c-482b-84cf-285bc4606075",
"kode_wilayah": "11",
"nama_wilayah": "ACEH",
"level_wilayah": 1,
"id_indikator": "4700ed90-4a9a-46a4-9ccf-54ee556e2691",
"nama_indikator": "Jumlah Penduduk Menurut Wilayah, Kesesuaian Alamat KK/KTP dengan Tempat Tinggal, dan Jenis Kelamin",
"id_kategori_1": "d1332a64-cca8-4cdf-84e6-c79ca1e66910",
"nama_kategori_1": "Klasifikasi Kesesuaian Alamat KK-KTP 2020",
"id_item_kategori_1": "982b2f23-92bc-4fdc-83ea-2ebdfd478c52",
"kode_item_kategori_1": "1",
"nama_item__kategori_1": "Ya",
"id_kategori_2": "05996fef-eaba-43ba-a917-c41108eaac6c",
"nama_kategori_2": "Klasifikasi Jenis Kelamin 2010",
"id_item_kategori_2": "3fccb669-2819-483a-8cb4-19b6aea53fe4",
"kode_item_kategori_2": "L",
"nama_item__kategori_2": "Laki-laki",
"id_kategori_3": "",
"nama_kategori_3": "",
"id_item_kategori_3": "",
"kode_item_kategori_3": "",
"nama_item__kategori_3": "",
"id_kategori_4": "",
"nama_kategori_4": "",
"id_item_kategori_4": "",
"kode_item_kategori_4": "",
"nama_item__kategori_4": "",
"period": "2020",
"nilai": "2523198.0"
},
]
```

###### **Error 4xx**

| Field | Type | Description |
| ----- | ----- | ----- |
| Status | String | Return status, OK if success and Error if any error occurred. |
| Data-availibility | String | Availability status of data |

###### **Error Response**

```
{
"status": "Error",
"data-availability": "not-available",
"data": [
{
"page": 1,
"pages": 0,
"per_page": 25,
"count": 0,
"total": 0
},
[]
]
}
```

### **SIMDASI** (Sistem Informasi Manajemen Data Statistik Terintegrasi)

Indonesian Statistics (SI) and Regional In Numbers (DDA) publications are BPS-issued publications that are of interest and attention by the public. At the moment the publication is available at www.bps.go.id. BPS continues to strive to improve the quality of SI and DDA through the Integrated Statistical Data Management Information System (SIMDASI).

---

##### **List of 7 Digit MFD Code of Province**

This service used to view the 7 Digit MFD Code of Province that is used in wilayah parameter in other SIMDASI WebAPI Parameter

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/26/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| key | String | Key app to access API |

**Send a Sample Request**

---

##### **List of 7 Digit MFD Code of Regency**

This service used to view the 7 Digit MFD Code of Regency that is used in wilayah parameter in other SIMDASI WebAPI Parameter

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/27/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| parent | String | 7 Digit MFD code of Province, use service List of 7 Digit MFD Code of Province to get the code |
| key | String | Key app to access API |

**Send a Sample Request**

---

##### **List of 7 Digit MFD Code of District**

This service used to view the 7 Digit MFD Code of District that is used in wilayah parameter in other SIMDASI WebAPI Parameter

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/28/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| parent | String | 7 Digit MFD code of Regency, use service List of 7 Digit MFD Code of Regency to get the code |
| key | String | Key app to access API |

**Send a Sample Request**

---

##### **List of SIMDASI Subject**

This service used to view a list of subjects or chapters used in SIMDASI

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/22/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| wilayah | String | 7 digit MFD Code of Area. Example for DKI Jakarta use 3100000 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Object |
|   data | Object | List of subject |
|     id | String | ID unique of subject |
|     bab | String | Name of chapter in bahasa |
|     bab\_en | String | Name of chapter in english |
|     subject | String | Name of subject in bahasa |
|     subject\_en | String | Name of subject in english |
|     mms\_id | Number | MMS ID of subject. This ID may be used in other endpoint as parameter of ID Subject. (MMS \- Metadata Management system) |
|     mms\_subject | String | CSA Subject name that is used in MMS |
|     tabel | Object | List of ID Table in this subject |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
{
"status": 200,
"condition": "OK",
"message": "-",
"created": "2022-08-01 11:33:33",
"induk": "0000000",
"wilayah": "Indonesia",
"data": [
{
"id_tabel": "UFpWMmJZOVZlZTJnc1pXaHhDV1hPQT09",
"judul": "Luas Daerah dan Jumlah Pulau Menurut Provinsi",
"judul_en": "Total Area and Number of Islands by Province",
"kode_tabel": "1.1.1",
"ketersediaan_tahun": [
2015,
2016,
2017,
2018,
2019,
2021
],
"id_subject": "OTJzVUFuRkhLQU1iTTVJUnM5Zko3QT09",
"bab": "Geografi dan Iklim",
"bab_en": "Geography and Climate",
"subject": "Keadaan Geografi",
"subject_en": "Geography Condition",
"mms_id": 516,
"mms_subject": "Statistik Lingkungan Hidup Dan Multi-domain"
},
```

---

##### **SIMDASI Master Table**

This service used to view the Master Table that is used in SIMDASI

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/34/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| key | String | Key app to access API |

**Send a Sample Request**

---

##### **Detail of SIMDASI Master Table**

This service used to view the Detail of Master Table that is used in SIMDASI

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/36/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| id\_tabel | String | ID of the Table |
| key | String | Key app to access API |

**Send a Sample Request**

---

##### **List of SIMDASI Table Based on Area**

This service used to view a list of SIMDASI Table based on Area

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/23/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| wilayah | String | 7 digit MFD Code of Area. Example for DKI Jakarta use 3100000 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Object |
|   data | Object | List of subject |
|     id\_tabel | String | ID unique of table |
|     judul | String | Table title in bahasa |
|     judul\_en | String | Table title in english |
|     kode\_tabel | String | Table code in SIMDASI |
|     ketersediaan\_tahun | String | Year availability of table |
|     id\_subject | String | ID unique of subject |
|     bab | String | Name of chapter in bahasa |
|     bab\_en | String | Name of chapter in english |
|     subject | String | Name of subject in bahasa |
|     subject\_en | String | Name of subject in english |
|     mms\_id | Number | MMS ID of subject. This ID may be used in other endpoint as parameter of ID Subject. (MMS \- Metadata Management system) |
|     mms\_subject | String | CSA Subject name that is used in MMS |
|     tabel | Object | List of ID Table in this subject |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
{
"status": 200,
"condition": "OK",
"message": "-",
"created": "2022-08-01 11:15:20",
"induk": "0000000",
"wilayah": "Indonesia",
"data": [
{
"id_tabel": "UFpWMmJZOVZlZTJnc1pXaHhDV1hPQT09",
"judul": "Luas Daerah dan Jumlah Pulau Menurut Provinsi",
"judul_en": "Total Area and Number of Islands by Province",
"kode_tabel": "1.1.1",
"ketersediaan_tahun": [
2015,
2016,
2017,
2018,
2019,
2021
],
"id_subject": "OTJzVUFuRkhLQU1iTTVJUnM5Zko3QT09",
"bab": "Geografi dan Iklim",
"bab_en": "Geography and Climate",
"subject": "Keadaan Geografi",
"subject_en": "Geography Condition",
"mms_id": 516,
"mms_subject": "Statistik Lingkungan Hidup Dan Multi-domain"
},
```

---

##### **List of SIMDASI Table Based on Area and Subject**

This service used to view a list of SIMDASI Table based on Area and Subject

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/24/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| wilayah | String | 7 digit MFD Code of Area. Example for DKI Jakarta use 3100000 |
| id\_subjek | String | MMS\_id of subject, use List of SIMDASI Subject to get the ID |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Object |
|   data | Object | List of subject |
|     id\_tabel | String | ID unique of table |
|     judul | String | Table title in bahasa |
|     judul\_en | String | Table title in english |
|     kode\_tabel | String | Table code in SIMDASI |
|     ketersediaan\_tahun | String | Year availability of table |
|     id\_subject | String | ID unique of subject |
|     bab | String | Name of chapter in bahasa |
|     bab\_en | String | Name of chapter in english |
|     subject | String | Name of subject in bahasa |
|     subject\_en | String | Name of subject in english |
|     mms\_id | Number | MMS ID of subject. This ID may be used in other endpoint as parameter of ID Subject. (MMS \- Metadata Management system) |
|     mms\_subject | String | CSA Subject name that is used in MMS |
|     tabel | Object | List of ID Table in this subject |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
{
"status": 200,
"condition": "OK",
"message": "-",
"created": "2022-08-01 11:15:20",
"induk": "0000000",
"wilayah": "Indonesia",
"data": [
{
"id_tabel": "UFpWMmJZOVZlZTJnc1pXaHhDV1hPQT09",
"judul": "Luas Daerah dan Jumlah Pulau Menurut Provinsi",
"judul_en": "Total Area and Number of Islands by Province",
"kode_tabel": "1.1.1",
"ketersediaan_tahun": [
2015,
2016,
2017,
2018,
2019,
2021
],
"id_subject": "OTJzVUFuRkhLQU1iTTVJUnM5Zko3QT09",
"bab": "Geografi dan Iklim",
"bab_en": "Geography and Climate",
"subject": "Keadaan Geografi",
"subject_en": "Geography Condition",
"mms_id": 516,
"mms_subject": "Statistik Lingkungan Hidup Dan Multi-domain"
},
```

---

##### **Detail of SIMDASI Table**

This service used to view the detail of SIMDASI Table

https://webapi.bps.go.id/v1/api/interoperabilitas/datasource/simdasi/id/25/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| wilayah | String | 7 digit MFD Code of Area. Example for DKI Jakarta use 3100000 |
| Tahun | Number | Year of the Data |
| id\_tabel | String | id\_tabel of table, use List of SIMDASI Table to get the ID |
| key | String | Key app to access API |

**Send a Sample Request**

### **Static Table**

---

##### **Detail Statictable**

This service is used to displays detail of a statictable are shown on the website

https://webapi.bps.go.id/v1/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed statictable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display statictable (statictable) for statictable is "statictable" |
| lang | String | Language to display static table Default value: ind Allowed values: "ind", "eng" |
| id | Number | statictable id to display Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list statictable. |
| data | Object | Information status |
|   table\_id | Number | ID unique of statictable |
|   subj\_id | Number | ID subject of statictable |
|   title | String | Title of statictable |
|   table | String | Title of statictable |
|   cr\_date | String | Create Date of statictable |
|   updt\_date | String | Update Date of statictable |
|   size | String | File size of statictable |
|   excel | String | Path location of statictable |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":{
"table_id": 111,
"subj_id": 23,
"title": "Inflasi data",
"table": "sample html table",
"cr_date": "2017-02-24",
"updt_date": "2017-02-24",
"excel": "http://jabar-dev.bps.go.id/new/website/tabelExcelIndo/Indo_23_3273895.xls",
"size": " MB"
}
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List All Static Table**

This service is used to displays all static table are shown on the website

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display statictable (statictable) for statictable is "statictable" |
| lang **optional** | String | Language to display static table Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed statictable (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display statictable Allowed values: 1, 2, 3, 4, ..., n |
| month **optional** | Number | Month selected to display statictable Allowed values: 1, 2, 3, 4, ..., n |
| year **optional** | Number | Year selected to display statictable Allowed values: 1, 2, 3, 4, ..., n |
| keyword **optional** | String | Keyword to search |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list statictable. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List statictable |
|     table\_id | Number | ID unique of statictable |
|     title | String | Title of statictable |
|     subj\_id | Number | ID subject of statictable |
|     subj | String | Subject of statictable |
|     updt\_date | String | Update Date of statictable |
|     size | String | File size of statictable |
|     excel | String | Path location of statictable |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"turth_id":0,
"turth":"Tahun",
"group_turth_id":0,
"name_group_turth":"Tahunan"
},{
"turth_id":1,
"turth":"Bulanan",
"group_turth_id":1,
"name_group_turth":"January"
},{
"turth_id":2,
"turth":"Bulanan",
"group_turth_id":2,
"name_group_turth":"February"
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **CSA Subject** (Classification of Statistical Activities)

CSA (Classification of Statistical Activities) was established in 2005, used as the basis for providing information in the international statistical activities database currently managed by the Conference of European Statistics (CES). In the future, BPS will adopt the CSA Subject in the new website user interface design.

---

##### **CSA Subject Categories**

This service is used to show list of CSA subject categories

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed pressrelease (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display CSA Subject Categories is "subcatcsa" |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Data List |
|     subcat\_id | Number | ID unique of CSA Subject Categories |
|     title | String | Title of CSA Subject Categories |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 10,
"count": 3,
"total": 3
},
[
{
"subcat_id": 514,
"title": "statistik demografi dan sosial"
},
{
"subcat_id": 515,
"title": "statistik ekonomi\\n"
},
{
"subcat_id": 516,
"title": "statistik lingkungan hidup dan multi-domain"
}
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **CSA Subject**

This service is used to show list of CSA subject

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed pressrelease (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display CSA Subject is "subjectcsa" |
| subcat **optional** | String | CSA Subject Categories ID, use service "CSA Subject Categories" to get the "subcat\_id" |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Data List |
|     sub\_id | Number | ID unique of CSA Subject |
|     title | String | Title of CSA Subject |
|     subcat\_id | Number | ID unique of CSA Subject Categories |
|     subcat | String | Title of CSA Subject Categories |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 2,
"per_page": 10,
"count": 10,
"total": 11
},
[
{
"sub_id": 528,
"title": "Aktivitas Politik dan Komunitas Lainnya",
"subcat_id": 514,
"subcat": "statistik demografi dan sosial"
},
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List of Table (Using CSA Subject)**

This service is used to show list of table that adopt the CSA Subject

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed pressrelease (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display List of Table is "tablestatistic" |
| subject **optional** | Number | CSA Subject ID, use service "CSA Subject" to get the "sub\_id" |
| page **optional** | Number | Page to display subject Allowed values: 1, 2, 3, 4, ..., n |
| perpage **optional** | Number | Sum of Table to display per page Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | Data List |
|     id | String | ID unique of table |
|     title | String | Title of Table |
|     id\_subject | Number | ID unique of CSA Subject |
|     subject | String | Title of CSA Subject |
|     id\_subcat | Number | ID unique of CSA Subject Categories |
|     subcat | String | Title of CSA Subject Categories |
|     tablesource | String | Source of Table 1: Static Table 2: Dynamic Table 3: SIMDASI |

---

##### **Detail of Table (Using CSA Subject)**

This service is used to show detail of table that adopt the CSA Subject

https://webapi.bps.go.id/v1/api/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed pressrelease (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display List of Table is "tablestatistic" |
| id | String | ID of table, use service "List of table" above to get the "id" |
| year **optional** | integer | a four-digit year value between oldest\_period and latest\_period |
| lang | Number | Language to display Allowed values: "ind", "eng" |
| key | String | Key app to access API |

**Send a Sample Request**

### **Press Release**

---

##### **Detail Press Release**

This service is used to displays detail of a pressrelease are shown on the website

https://webapi.bps.go.id/v1/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed pressrelease (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display pressrelease (pressrelease) for pressrelease is "pressrelease" |
| lang | String | Language to display pressrelease Allowed values: "ind", "eng" |
| id | Number | pressrelease id to display Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list pressrelease. |
| data | Object | Information status |
|   brs\_id | Number | ID unique of pressrelease |
|   title | String | Title of pressrelease |
|   abstract | String | Abstract of pressrelease |
|   rl\_date | String | Release Date of pressrelease |
|   updt\_date | String | Updated Date of pressrelease if any updated/revised pressrelease |
|   pdf | String | Path Location of pressrelease File |
|   size | String | Size File of pressrelease |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":{
"brs_id":"brs-f12345512",
"title": "Title of pressrelease",
"abstract":"Abstract of Press Release",
"rl_date": "2016-10-08",
"updt_date": null,
"pdf": "path",
"size": "1.2 MB",
}
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List All Press Release**

This service is used to displays all press release are shown on the website

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display pressrelease (pressrelease) for pressrelease is "pressrelease" |
| lang **optional** | String | Language to display pressrelease Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed pressrelease (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display pressrelease Allowed values: 1, 2, 3, 4, ..., n |
| month **optional** | Number | Month selected to display pressrelease Allowed values: 1, 2, 3, 4, ..., n |
| year **optional** | Number | Year selected to display pressrelease Allowed values: 1, 2, 3, 4, ..., n |
| keyword **optional** | String | Keyword to search |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list pressrelease. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List pressrelease |
|     brs\_id | Number | ID unique of pressrelease |
|     title | String | Title of pressrelease |
|     rl\_date | String | Release Date of pressrelease |
|     updt\_date | String | Updated Date of pressrelease if any updated/revised pressrelease |
|     pdf | String | Path Location of pressrelease File |
|     size | String | Size File of pressrelease |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"brs_id":"brs-13342312",
"title": "Title of pressrelease",
"rl_date": "2016-07-08",
"updt_date": null,
"pdf": "path",
"size": "2.1 MB",
},{
"brs_id":"brs-13344512",
"title": "Title of pressrelease now",
"rl_date": "2016-07-08",
"updt_date": null,
"pdf": "path",
"size": "2 MB",
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Publication**

---

##### **Detail Publication**

This service is used to displays detail of a publication are shown on the website

https://webapi.bps.go.id/v1/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed publication (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display publication (publication) for publication is "publication" |
| lang | String | Language to display publication Allowed values: "ind", "eng" |
| id | String | Publication id to display |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list publication. |
| data | Object | Information status |
|   pub\_id | Number | ID unique of Publication |
|   title | String | Title of Publication |
|   kat\_no | String | Category Number of Publication |
|   pub\_no | String | Publication Number of Publication |
|   issn | String | ISSN/ISBN number of Publication |
|   abstract | String | Abstract of Publication |
|   sch\_date | String | Schedule Date of Publication |
|   rl\_date | String | Release Date of Publication |
|   updt\_date | String | Updated Date of Publication if any updated/revised publication |
|   cover | String | Path Location of Publication cover |
|   pdf | String | Path Location of Publication File |
|   size | String | Size File of Publication |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":{
"pub_id":"pub-13342312",
"title": "Title of Publication",
"kat_no": "1212 1212 314",
"pub_no": "1221",
"issn": "0215-2169",
"abstract": "Abstract of Publication",
"sch_date": "2016-07-08",
"rl_date": "2016-07-08",
"updt_date": null,
"cover": "path",
"pdf": "path",
"size": "21 MB",
}
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List All Publication**

This service is used to displays all publication that are shown on the website

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display publication (publication) for publication is "publication" |
| lang **optional** | String | Language to display publication Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed publication (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display publication Allowed values: 1, 2, 3, 4, ..., n |
| month **optional** | Number | Month selected to display publication Allowed values: 1, 2, 3, 4, ..., n |
| year **optional** | Number | Year selected to display publication Allowed values: 1, 2, 3, 4, ..., n |
| keyword **optional** | String | Keyword to search |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list publication. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List publication |
|     pub\_id | Number | ID unique of Publication |
|     title | String | Title of Publication |
|     issn | String | ISSN/ISBN number of publication |
|     sch\_date | String | Schedule Date of Publication |
|     rl\_date | String | Release Date of Publication |
|     updt\_date | String | Updated Date of Publication if any updated/revised publication |
|     cover | String | Path Location of Publication cover |
|     pdf | String | Path Location of Publication File |
|     size | String | Size File of Publication |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 0,
"pages": 1,
"per_page": 10,
"count": 3,
"total": 3
},
[
{
"pub_id": "2016320000032000321313",
"title": "Indeks Pembangunan Manusia Provinsi Jawa Barat 2015",
"issn": "999-999-999-9",
"sch_date": "2016-11-28",
"rl_date": "2016-11-29",
"updt_date": null,
"cover": "http://publikasi.bps.go.id/portalpublikasi_beta/index.php/publikasi/getcover?id=2016320000032000321313",
"pdf": "http://publikasi.bps.go.id/portalpublikasi_beta/index.php/publikasi/getpdfwatermark?id=2016320000032000321313",
"size": "5 MB"
},
{
"pub_id": "20163200000320003211",
"title": "Provinsi Jawa Barat Dalam Angka 2016",
"issn": "0215-2169",
"sch_date": "2016-11-16",
"rl_date": "2016-11-16",
"updt_date": "2016-11-23",
"cover": "http://publikasi.bps.go.id/portalpublikasi_beta/index.php/publikasi/getcover?id=20163200000320003211",
"pdf": "http://publikasi.bps.go.id/portalpublikasi_beta/index.php/publikasi/getpdfwatermark?id=20163200000320003211",
"size": "2.8 MB"
},
{
"pub_id": "2016320000032000322302",
"title": "[Updated] Testing Publikasi NON-ARC",
"issn": "-",
"sch_date": null,
"rl_date": "2016-11-15",
"updt_date": "2017-01-27",
"cover": "http://publikasi.bps.go.id/portalpublikasi_beta/index.php/publikasi/getcover?id=2016320000032000322302",
"pdf": "http://www.bps.go.id",
"size": "30 MB"
}
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Strategic Indicators**

---

##### **List Strategic Indicators**

This service is used to displays all strategic indicator only for **the central and province website**

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display strategic indicators for strategic indicators is "indicators" |
| lang **optional** | String | Language to display strategic indicators Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed derived period data (see master [domain](https://webapi.bps.go.id/documentation/#domain)). Domains that allowed in this model only for central and province domain. Size range: 4 |
| var **optional** | Number | Variable ID selected to display derived period data Allowed values: 1, 2, 3, 4, ..., n |
| page **optional** | Number | Page to display derived period data Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list indicators. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List Strategic Indicators |
|     title | String | Title of Strategic Indicators |
|     desc | String | Description of Indicators |
|     data\_source | String | Data Source if Strategic Indicators |
|     value | Number | Value of Strategic Indicators |
|     unit | String | Unit Value of Strategic Indicators |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":[{
"page":1,
"pages":230,
"per_page":10,
"count":10,
"total":2300
},
[{
"turth_id":0,
"turth":"Tahun",
"group_turth_id":0,
"name_group_turth":"Tahunan"
},{
"turth_id":1,
"turth":"Bulanan",
"group_turth_id":1,
"name_group_turth":"January"
},{
"turth_id":2,
"turth":"Bulanan",
"group_turth_id":2,
"name_group_turth":"February"
}]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Infographic**

---

##### **List All Infographic**

This service is used to displays all infographic in the website

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display news (news) for infographic is "infographic" |
| lang **optional** | String | Language to display news Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed news (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display news Allowed values: 1, 2, 3, 4, ..., n |
| keyword **optional** | String | Keyword to search |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list indicators. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List Infographics |
|     inf\_id | Number | Id of Infographic |
|     title | String | Title of Infographic |
|     img | String | Thumbnail of Infographic |
|     desc | String | Description of infographic |
|     category | Number | Category id of infographic (1: Social and Population, 2: Economic and Trade, 3: Agriculture and Mining) |
|     dl | String | Download link of Infographic |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 49,
"per_page": 10,
"count": 10,
"total": 481
},
[
{
"inf_id": 527,
"title": "Transportasi Rilis Oktober 2020",
"img": "https://www.bps.go.id/website/images/Transportasi-Rilis-Oktober-2020-ind.jpg",
"desc": "",
"category": 2,
"dl": "https://www.bps.go.id/galery/download.html?asdf=NTI3\&qwer=ldjfdifsdjkfahi\&zxcv=MjAyMC0xMC0wNiAwNzozMzowMg%3D%3D"
},
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Glosarium**

---

##### **List of Glosarium**

This service is used to display list of glosarium

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display list of glosarium is "glosarium" |
| prefix **optional** | String | The first letter that the list will look for |
| page **optional** | Number | Page to display subject Allowed values: 1, 2, 3, 4, ..., n |
| perpage **optional** | Number | Sum of Table to display per page Allowed values: 1, 2, 3, 4, ..., 500 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   \_source | Object | Data List |
|     konten | String | Content: Glosarium |
|     jenis | String | Type of content: Glosarium |
|     id | Number | Unique ID of glosarium |
|     idSds | Number | Unique ID of SDS |
|     noIndikator | Number | Number of Indicator |
|     judulIndikator | String | Title of Indicator in Bahasa |
|     judulIndikator\_en | String | Title of Indicator in English |
|     konsep | String | Statistical Concept in Bahasa |
|     konsep\_en | String | Statistical Concept in English |
|     definisi | String | Definition of a Statistical Concept in Bahasa |
|     definisi\_en | String | Definition of a Statistical Concept in English |
|     namaKlasifikasi | String | Name of Classification in Bahasa |
|     namaKlasifikasi\_en | String | Name of Classification in English |
|     ukuran | String | Size in Bahasa |
|     ukuran\_en | String | Size in English |
|     satuan | String | unit in Bahasa |
|     satuan\_en | String | unit in English |
|     flagSds | String | Flag of Sds |
|     sumberKonten | String | Source of content in Bahasa |
|     sumberKonten\_en | String | Source of Content in English |
|     sumberData | String | Source of Data in Bahasa |
|     sumberData\_en | String | Source of data in English |
|     Endpoint | String | Type of ENdpoint |
|     flag | boolean |  |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 508,
"per_page": 10,
"count": 10,
"total": 5078
},
[
{
"_index": "glosarium",
"_type": "_doc",
"_id": "glosarium_4406_web",
"_score": null,
"_source": {
"konten": "glosarium",
"jenis": "glosarium",
"id": "4406",
"idSds": null,
"noIndikator": null,
"judulIndikator": "",
"judulIndikator_en": "",
"konsep": "Agama",
"konsep_en": "Religion",
"definisi": "Agama merupakan keyakinan terhadap Tuhan Yang Maha Esa yang harus dimiliki oleh setiap manusia. Agama dibedakan menjadi Islam, Kristen, Katholik, Hindu, Budha, Khong Hu Chu, dan Agama Lainnya. Agama berguna dalam menentukan kebijakan yang berkaitan dengan kerukunan umat beragama, contoh: kebijakan Kementerian Agama dalam pembangunan tempat-tempat ibadahberagama, untuk memelihara dan menyuburkan kesadaran umat dalam menghayati danmelaksanakan ajaran-ajarannya. Termasuk dalam acara agama: Sepercik Iman Pembasuh Kalbu,Terjemahan Al-Quran, Mimbar Agama Islam, Mimbar Agama Katolik, Mimbar Agama Protestan.",
"definisi_en": "Religion is belief in Almighty God that must be possessed by every human being. Religion can be divided into Muslim, Christian, Catholic, Hindu, Buddhist, Hu Khong Chu, and Other Religion. ",
"namaKlasifikasi": "",
"namaKlasifikasi_en": "",
"klasifikasi": "",
"klasifikasi_en": "",
"ukuran": "",
"ukuran_en": "",
"satuan": "",
"satuan_en": "",
"flagSds": "",
"sumberKonten": "",
"sumberKonten_en": "",
"sumberData": "",
"sumberData_en": "",
"endpoint": "web",
"flag": "t"
},
"sort": [
"agama"
]
},
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **Detail of Glosarium**

This service is used to display the detail of statistical concept

https://webapi.bps.go.id/v1/api/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display list of glosarium is "glosarium" |
| id | Number | The ID of glosarium |
| lang | String | Language to display Default value: ind Allowed values: "ind", "eng" |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   \_source | Object | Data List |
|     konten | String | Content: Glosarium |
|     jenis | String | Type of content: Glosarium |
|     id | Number | Unique ID of glosarium |
|     idSds | Number | Unique ID of SDS |
|     noIndikator | Number | Number of Indicator |
|     judulIndikator | String | Title of Indicator in Bahasa |
|     judulIndikator\_en | String | Title of Indicator in English |
|     konsep | String | Statistical Concept in Bahasa |
|     konsep\_en | String | Statistical Concept in English |
|     definisi | String | Definition of a Statistical Concept in Bahasa |
|     definisi\_en | String | Definition of a Statistical Concept in English |
|     namaKlasifikasi | String | Name of Classification in Bahasa |
|     namaKlasifikasi\_en | String | Name of Classification in English |
|     ukuran | String | Size in Bahasa |
|     ukuran\_en | String | Size in English |
|     satuan | String | unit in Bahasa |
|     satuan\_en | String | unit in English |
|     flagSds | String | Flag of Sds |
|     sumberKonten | String | Source of content in Bahasa |
|     sumberKonten\_en | String | Source of Content in English |
|     sumberData | String | Source of Data in Bahasa |
|     sumberData\_en | String | Source of data in English |
|     Endpoint | String | Type of ENdpoint |
|     flag | boolean |  |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 1,
"count": 1,
"total": 1
},
[
{
"_index": "glosarium",
"_type": "_doc",
"_id": "glosarium_4406_web",
"_score": null,
"_source": {
"konten": "glosarium",
"jenis": "glosarium",
"id": "4406",
"idSds": null,
"noIndikator": null,
"judulIndikator": "",
"judulIndikator_en": "",
"konsep": "Agama",
"konsep_en": "Religion",
"definisi": "Agama merupakan keyakinan terhadap Tuhan Yang Maha Esa yang harus dimiliki oleh setiap manusia. Agama dibedakan menjadi Islam, Kristen, Katholik, Hindu, Budha, Khong Hu Chu, dan Agama Lainnya. Agama berguna dalam menentukan kebijakan yang berkaitan dengan kerukunan umat beragama, contoh: kebijakan Kementerian Agama dalam pembangunan tempat-tempat ibadahberagama, untuk memelihara dan menyuburkan kesadaran umat dalam menghayati danmelaksanakan ajaran-ajarannya. Termasuk dalam acara agama: Sepercik Iman Pembasuh Kalbu,Terjemahan Al-Quran, Mimbar Agama Islam, Mimbar Agama Katolik, Mimbar Agama Protestan.",
"definisi_en": "Religion is belief in Almighty God that must be possessed by every human being. Religion can be divided into Muslim, Christian, Catholic, Hindu, Buddhist, Hu Khong Chu, and Other Religion. ",
"namaKlasifikasi": "",
"namaKlasifikasi_en": "",
"klasifikasi": "",
"klasifikasi_en": "",
"ukuran": "",
"ukuran_en": "",
"satuan": "",
"satuan_en": "",
"flagSds": "",
"sumberKonten": "",
"sumberKonten_en": "",
"sumberData": "",
"sumberData_en": "",
"endpoint": "web",
"flag": "t"
},
"sort": [
"agama"
]
},
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Foreign Trade Data (Export\&Import)**

This service is used to displays data of foreign trade from the website

https://webapi.bps.go.id/v1/api/dataexim/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| sumber | Number | Source of the data 1: Export 2: Import |
| periode | Number | Period of the data 1: monthly 2: annually |
| kodehs | number | HS Code of the data, use separator ; for multiple HS Code. e.g. firstHScode;secondHScode. |
| jenishs | Number | Type of HS Code 1: Two digit 2: Full HS Code If jenishs \= 1 then the kodehs is two digits. If jenishs \= 2 then the full digit kodehs follows the master hscode by year. [For more information](https://www.bps.go.id/assets/docs/HSCode%20Master%20BPS.pdf) |
| Tahun | String | Year of data |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list indicators. |
| Metadata | Object\[\] | source: source of the data value: Export/Import value in US Dollar ($) netweight: weight of Export/Import in Kilogram (Kg) kodehs: Code and Description from HS pod: Incoming/Outgoing Ports in Indonesia ctr: Country of Origin/Destination year: data year |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "not-available",
"metadata": {
"source": "Sumber : https://www.bps.go.id diakses pada 23-06-2021 12:38:14 WIB",
"value": "Nilai Ekspor/Impor dalam US Dollar ($)",
"netweight": "Berat Ekspor/Impor dalam Kilogram (KG)",
"kodehs": "Kode dan Deskripsi dari HS",
"pod": "Pelabuhan Masuk/Keluar di Indonesia",
"ctr": "Negara Asal/Tujuan",
"tahun": "Tahun Data"
},
"data": [
{
"value": 1015060.142,
"netweight": 243755,
"kodehs": "[03] Ikan dan krustasea, moluska serta invertebrata air lainnya",
"pod": "BELAWAN",
"ctr": "ALBANIA",
"tahun": "2019"
},...
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

# **Sustainable Development Goals (SDGs)**

##### **List All SDGs Table**

This service is used to displays all SDGs table, domain must be "0000"

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display sdgs table is "sdgs" |
| goal **optional** | String | Number of Goal Allowed values: 1... 17 |
| key | String | Key app to access API |

**Send a Sample Request**

##### **SDGs Table List**

This table is updated annually without prior notice

| Goals | Variable | Variable (id) | Id Var |
| ----- | ----- | ----- | ----- |
| ![][image1] | Number of Deaths, Disappeared, and Hurt Victims Affected | Jumlah Korban Meninggal, Hilang, dan Terluka Terkena Dampak Bencana | 1804 |
|  | Number of Deaths, Disappeared, and Hurt Victims Affected by 100,000 People | Jumlah Korban Meninggal, Hilang, dan Terluka Terkena Dampak Bencana Per 100.000 Orang | 1246 |
|  | Percentage of Poor People by Province | Persentase Penduduk Miskin Menurut Provinsi | 192 |
|  | Percentage of Poor People by Region | Persentase Penduduk Miskin Menurut Wilayah | 184 |
|  | Percentage of Poor People In Disadvantaged Areas | Persentase Penduduk Miskin Di Daerah Tertinggal | 1238 |
|  | Percentage of population living below the national poverty line, according to age group | Persentase Penduduk Yang Hidup Di Bawah Garis Kemiskinan Nasional, Menurut Kelompok Umur | 1539 |
|  | Percentage of Population Living Below the National Poverty Line, According to Gender | Persentase Penduduk Yang Hidup di Bawah Garis Kemiskinan Nasional, Menurut Jenis Kelamin | 1538 |
|  | Proportion of households with access to basic services by area of residence | Proporsi rumah tangga dengan akses terhadap pelayanan dasar menurut Daerah Tempat Tinggal | 2017 |
|  | Proportion of households with access to basic services by province | Proporsi rumah tangga dengan akses terhadap pelayanan dasar menurut provinsi | 2016 |
|  | Proportion of households with ownership and lease / contract status by province | Proporsi rumah tangga dengan status kepemilikan rumah milik dan sewa/kontrak menurut provinsi | 2018 |
|  | Proportion of households with ownership status of owned and leased / contracted houses according to gender | Proporsi rumah tangga dengan status kepemilikan rumah milik dan sewa/kontrak menurut jenis kelamin | 2020 |
|  | Proportion of households with ownership status of owned and leased / contracted houses by area of residence | Proporsi rumah tangga dengan status kepemilikan rumah milik dan sewa/kontrak menurut Daerah Tempat Tinggal | 2019 |
|  | Spending on basic services (education, health and social protection) as a percentage of total government spending. | Pengeluaran untuk layanan pokok (pendidikan, kesehatan dan perlindungan sosial) sebagai persentase dari total belanja pemerintah | 1759 |
| ![][image2] |  |  |  |
|  | Agricultural Added Value Divided by Number of Labor in Agricultural Sector | Nilai Tambah Pertanian Dibagi Jumlah Tenaga Kerja Di Sektor Pertanian | 1344 |
|  | Percentage of Toddlers (Under Five Years Old) Short And Very Short | Persentase Balita Pendek Dan Sangat Pendek | 1325 |
|  | Population Prevalence With Moderate Or Severe Food Insecurity, Based On The Scale Of Food Insecurity Experience | Prevalensi Penduduk Dengan Kerawanan Pangan Sedang Atau Berat, Berdasarkan Pada Skala Pengalaman Kerawanan Pangan | 1474 |
|  | Prevalence of Anemia in Pregnant Women | Prevalensi Anemia Pada Ibu Hamil | 1333 |
|  | Prevalence of Insufficient Food Consumption | Prevalensi Ketidakcukupan Konsumsi Pangan | 1473 |
|  | Prevalence of Toddler Very Short and Short in Regency / City SSGBI | Prevalensi Balita Sangat Pendek dan Pendek pada Kabupaten/Kota SSGBI | 1614 |
|  | The prevalence of anemia in pregnant women according to age group | Prevalensi anemia pada ibu hamil menurut kelompok umur | 1782 |
|  | Toddler Prevalence is Very Short and Short by Regency / City in 2018 | Prevalensi Balita Sangat Pendek dan Pendek Menurut Kabupaten/Kota Tahun 2018 | 1531 |
| ![][image3] |  |  |  |
|  | Age Specific Fertility Rate/ASFR (15-19) by Area | Angka Kelahiran Pada Perempuan Usia 15-19 Tahun Menurut Daerah Tempat Tinggal | 1398 |
|  | Age Specific Fertility Rate/ASFR (15-19) by Province | Angka Kelahiran Pada Perempuan Usia 15-19 Tahun Menurut Provinsi | 1397 |
|  | Alcohol consumption by people aged ≥ 15 years in the past year | Konsumsi Alkohol Oleh Penduduk Umur ≥ 15 Tahun Dalam Satu Tahun Terakhir | 1475 |
|  | Birth Rate In Women Aged 15-19 Years by Provinsi | Angka Kelahiran Pada Perempuan Umur 15-19 Tahun Menurut Provinsi | 1353 |
|  | Birth Rates for Women Aged 15-19 Years by Region of Residence | Angka Kelahiran Pada Perempuan Umur 15-19 Tahun (ASFR) (per 1.000 perempuan umur 15-19 tahun) Menurut Daerah Tempat Tinggal | 1612 |
|  | Density and Distribution of Health Workers | Kepadatan Dan Distribusi Tenaga Kesehatan | 1477 |
|  | Incidence of Tuberculosis (ITB) Per 100,000 Population | Insiden Tuberkolosis (ITB) Per 100.000 Penduduk | 1763 |
|  | Infant Mortality Rate (IMR) Per 1000 Live Births According to Wealth Quantile | Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup Menurut Kuantil Kekayaan | 1572 |
|  | Infant Mortality Rate (IMR) Per 1000 Live Births by Age of Mother During Childbirth | Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup Menurut Umur Ibu Saat Melahirkan | 1569 |
|  | Infant Mortality Rate (IMR) Per 1000 Live Births by Province | Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup Menurut Provinsi | 1584 |
|  | Infant Mortality Rate (IMR) Per 1000 Live Births by Residence Area | Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup Menurut Daerah Tempat Tinggal | 1568 |
|  | Infant Mortality Rate (IMR) Per 1000 Live Births of Mothers Education | Angka Kematian Bayi (AKB) Per 1000 Kelahiran Hidup Menurut Pendidikan Ibu | 1574 |
|  | Malaria Occurrences Per 1000 Persons | Kejadian Malaria Per 1000 Orang | 1393 |
|  | Maternal Mortality Rate by Island | Angka Kematian Ibu Menurut Pulau | 1349 |
|  | Mortality Rate Per 1000 Live Births by Area of Residence | Angka Kematian Balita Per 1000 Kelahiran Hidup Menurut Daerah Tempat Tinggal | 1379 |
|  | Mortality Rate Per 1000 Live Births by Maternal age at delivery | Angka Kematian Balita Per 1000 Kelahiran Hidup Menurut Umur Ibu saat Melahirkan | 1381 |
|  | Mortality Rate Per 1000 Live Births by Mother education level | Angka Kematian Balita Per 1000 Kelahiran Hidup Menurut Pendidikan Ibu | 1374 |
|  | Mortality Rate Per 1000 Live Births by Province | Angka Kematian Balita Per 1000 Kelahiran Hidup Menurut Provinsi | 1373 |
|  | Mortality Rate Per 1000 Live Births by Wealth Quintile | Angka Kematian Balita Per 1000 Kelahiran Hidup Menurut Kuantil Kekayaan | 1382 |
|  | Neonatal Death Rate And Infant Mortality Rate Per 1000 Birth By Area Of Residence | Angka Kematian Neonatal (AKN) Dan Angka Kematian Bayi Per 1000 Kelahiran Menurut Daerah tempat tinggal | 1384 |
|  | Neonatal Death Rate And Infant Mortality Rate Per 1000 Birth By Maternal age at delivery | Angka Kematian Neonatal (AKN) Dan Angka Kematian Bayi Per 1000 Kelahiran Menurut Umur Ibu saat Melahirkan | 1388 |
|  | Neonatal Death Rate And Infant Mortality Rate Per 1000 Birth By Mother education level | Angka Kematian Neonatal (AKN) Dan Angka Kematian Bayi Per 1000 Kelahiran Menurut Pendidikan Ibu | 1385 |
|  | Neonatal Death Rate And Infant Mortality Rate Per 1000 Birth By Province | Angka Kematian Neonatal (AKN) Dan Angka Kematian Bayi Per 1000 Kelahiran Menurut Provinsi | 1383 |
|  | Neonatal Death Rate And Infant Mortality Rate Per 1000 Birth By Wealth quintile | Angka Kematian Neonatal (AKN) Dan Angka Kematian Bayi Per 1000 Kelahiran Menurut Kuantil Kekayaan | 1387 |
|  | Number of Clients Accessing Post-rehabilitation Services | Jumlah Klien Yang Mengakses Layanan Pascarehabilitasi | 1479 |
|  | Number of districts / cities that have achieved malaria elimination | Jumlah Kabupaten/Kota yang mencapai eliminasi Malaria | 1764 |
|  | Number of districts / cities with filariasis elimination (successfully passed the phase I transmission assessment survey) | Jumlah Kabupaten/Kota dengan eliminasi filariasis (berhasil lolos dalam survei penilaian transmisi tahap I) | 1778 |
|  | Number of People Accessing Post Rehabilitation Services | Jumlah yang Mengakses Layanan Pasca Rehabilitasi | 1790 |
|  | Number of Population Which Is Included Health Insurance Or Public Health System Per 1000 people | Jumlah Penduduk Yang Dicakup Asuransi Kesehatan Atau Sistem Kesehatan Masyarakat per 1000 Penduduk | 1434 |
|  | Number of Provinces with Leprosy Elimination | Jumlah Provinsi dengan eliminasi Kusta | 1770 |
|  | Percentage of Smokers Age √¢‚Ä∞¬• 15 years by Age | Persentase Merokok Pada Penduduk Umur ≥ 15 Tahun Menurut Kelompok Umur | 1438 |
|  | Percentage of Smokers Age √¢‚Ä∞¬• 15 years by Area | Persentase Merokok Pada Penduduk Umur ≥ 15 Tahun Menurut Daerah Tempat Tinggal | 1436 |
|  | Percentage of Smokers Age √¢‚Ä∞¬• 15 years by Percentile Group of Expenditure | Persentase Merokok Pada Penduduk Umur ≥ 15 Tahun Menurut Kelompok Pengeluaran | 1437 |
|  | Percentage of Smokers Age √¢‚Ä∞¬• 15 years by Province | Persentase Merokok Pada Penduduk Umur ≥ 15 Tahun Menurut Provinsi | 1435 |
|  | Persentase Perempuan Pernah Kawin Berusia 15-49 Tahun Yang Proses Kelahiran Terakhirnya Ditolong Oleh Tenaga Kesehatan Terlatih Menurut Daerah Tempat Tinggal | Persentase Perempuan Pernah Kawin Berusia 15-49 Tahun Yang Proses Kelahiran Terakhirnya Ditolong Oleh Tenaga Kesehatan Terlatih Menurut Daerah Tempat Tinggal | 1346 |
|  | Persentase Perempuan Pernah Kawin Berusia 15-49 Tahun Yang Proses Kelahiran Terakhirnya Ditolong Oleh Tenaga Kesehatan Terlatih Menurut Kelompok Pengeluaran | Persentase Perempuan Pernah Kawin Berusia 15-49 Tahun Yang Proses Kelahiran Terakhirnya Ditolong Oleh Tenaga Kesehatan Terlatih Menurut Kelompok Pengeluaran | 1347 |
|  | Persentase Perempuan Pernah Kawin Berusia 15-49 Tahun Yang Proses Kelahiran Terakhirnya Ditolong Oleh Tenaga Kesehatan Terlatih Menurut Provinsi | Persentase Perempuan Pernah Kawin Berusia 15-49 Tahun Yang Proses Kelahiran Terakhirnya Ditolong Oleh Tenaga Kesehatan Terlatih Menurut Provinsi | 1345 |
|  | Prevalence of high blood pressure according to sex | Prevalensi tekanan darah tinggi menurut jenis kelamin | 1780 |
|  | Prevalence of high blood pressure according to the area of residence | Prevalensi tekanan darah tinggi menurut daerah tempat tinggal | 1779 |
|  | Prevalence of High Blood Pressure by Province | Prevalensi Tekanan Darah Tinggi Menurut Provinsi | 1480 |
|  | Prevalence of Obesity in Age Population\> 18 Years Old | Prevalensi Obesitas Pada Penduduk Umur \> 18 Tahun | 1481 |
|  | The Number Of Drug Abuse And Harmful Alcohol Users, Who Access Medical Rehabilitation Services | Jumlah Penyalahgunaan Narkotika dan Pengguna Alkohol Yang Merugikan, Yang Mengakses Layanan Rehabilitasi Medis | 1789 |
|  | The prevalence of obesity in people aged\> 18 years according to sex | Prevalensi Obesitas Pada Penduduk Umur \> 18 Tahun Menurut Jenis Kelamin | 1781 |
|  | The proportion of women of reproductive age (15-49 years) or their partners who have family planning needs and use contraception methods | Proporsi Perempuan Usia Reproduksi (15-49 tahun) atau Pasangannya yang Memiliki Kebutuhan Keluarga Berencana dan Menggunakan Alat Kontrasepsi Metode Modern | 1394 |
|  | Total Fertility Rate by Area | Angka Kelahiran Total Menurut Daerah Tempat Tinggal | 1401 |
|  | Total Fertility Rate by Expenditure Groups | Angka Kelahiran Total Menurut Kelompok Pengeluaran | 1400 |
|  | Total Fertility Rate by Province | Angka Kelahiran Total Menurut Provinsi | 1399 |
|  | Unmet Need Pelayanan Kesehatan Menurut Daerah Tempat Tinggal | Unmet Need Pelayanan Kesehatan Menurut Daerah Tempat Tinggal | 1403 |
|  | Unmet Need Pelayanan Kesehatan Menurut Jenis Kelamin | Unmet Need Pelayanan Kesehatan Menurut Jenis Kelamin | 1404 |
|  | Unmet Need Pelayanan Kesehatan Menurut Kelompok Pengeluaran | Unmet Need Pelayanan Kesehatan Menurut Kelompok Pengeluaran | 1405 |
|  | Unmet Need Pelayanan Kesehatan Menurut Kelompok Umur | Unmet Need Pelayanan Kesehatan Menurut Kelompok Umur | 1406 |
|  | Unmet Need Pelayanan Kesehatan Menurut Provinsi | Unmet Need Pelayanan Kesehatan Menurut Provinsi | 1402 |
| ![][image4] |  |  |  |
|  | Education Completion Rate According to Education Level and Expenditure Group | Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Kelompok Pengeluaran | 1983 |
|  | Education Completion Rate According to Education Level and Gender | Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Jenis Kelamin | 1982 |
|  | Education Completion Rate According to Education Level and Province | Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Provinsi | 1980 |
|  | Education Completion Rate According to Education Level and Region | Tingkat Penyelesaian Pendidikan Menurut Jenjang Pendidikan dan Wilayah | 1981 |
|  | Literacy Rate (AMH) of Population above 15 Years Old by Area | Angka Melek Huruf Penduduk Berumur 15 Tahun Ke Atas Menurut Daerah Tempat Tinggal | 1461 |
|  | Literacy Rate (AMH) of Population above 15 Years Old by Group of Income | Angka Melek Huruf Penduduk Berumur 15 Tahun Ke Atas Menurut Kelompok Pendapatan | 1459 |
|  | Literacy Rate (AMH) of Population above 15 Years Old by Province | Angka Melek Huruf Penduduk Berumur 15 Tahun Ke Atas Menurut Provinsi | 1458 |
|  | Literacy Rate (AMH) of Population above 15 Years Old by Sex | Angka Melek Huruf Penduduk Berumur 15 Tahun Ke Atas Menurut Jenis Kelamin | 1460 |
|  | Number of Children Out of School by Education Level and Area of Residence | Angka Anak Tidak Sekolah Menurut Jenjang Pendidikan dan Daerah Tempat Tinggal | 1984 |
|  | Number of Children Out of School by Education Level and Expenditure Group | Angka Anak Tidak Sekolah Menurut Jenjang Pendidikan dan Kelompok Pengeluaran | 1988 |
|  | Number of Children Out of School by Education Level and Gender | Angka Anak Tidak Sekolah Menurut Jenjang Pendidikan dan Jenis Kelamin | 1986 |
|  | Participation rate in organized learning (one year before primary school age) by Gender | Tingkat partisipasi dalam pembelajaran yang teroganisir (satu tahun sebelum usia sekolah dasar) menurut Jenis Kelamin | 1994 |
|  | Participation rate in organized learning (one year before primary school age) by province | Tingkat partisipasi dalam pembelajaran yang teroganisir (satu tahun sebelum usia sekolah dasar) menurut provinsi | 1990 |
|  | Participation rate in organized learning (one year before primary school age) by Residence | Tingkat partisipasi dalam pembelajaran yang teroganisir (satu tahun sebelum usia sekolah dasar) menurut Daerah Tempat Tinggal | 1992 |
|  | Proportion of Adolescents And Adults Aged 15-24 Years With The Information and Computer Technology Skills (ICT) by Area | Proporsi Remaja Dan Dewasa Usia 15-24 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Daerah Tempat Tinggal | 1453 |
|  | Proportion of Adolescents And Adults Aged 15-24 Years With The Information and Computer Technology Skills (ICT) by Province | Proporsi Remaja Dan Dewasa Usia 15-24 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi | 1451 |
|  | Proportion of Adolescents And Adults Aged 15-24 Years With The Information and Computer Technology Skills (ICT) by Sex | Proporsi Remaja Dan Dewasa Usia 15-24 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Jenis Kelamin | 1454 |
|  | Proportion of Adolescents And Adults Aged 15-59 Years With The Information and Computer Technology Skills (ICT) by Area | Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Daerah Tempat Tinggal | 1449 |
|  | Proportion of Adolescents And Adults Aged 15-59 Years With The Information and Computer Technology Skills (ICT) by Province | Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Provinsi | 1447 |
|  | Proportion of Adolescents And Adults Aged 15-59 Years With The Information and Computer Technology Skills (ICT) by Sex | Proporsi Remaja Dan Dewasa Usia 15-59 Tahun Dengan Keterampilan Teknologi Informasi Dan Komputer (TIK) Menurut Jenis Kelamin | 1450 |
|  | Proportion of Schools with Access to Proper Water Source Facilities | Proporsi Sekolah dengan Akses Fasilitas Sumber Air Layak | 1797 |
|  | Proportion of Schools with Computer Access | Proporsi Sekolah dengan Akses Komputer | 1796 |
|  | Proportion of Schools with Electricity Access | Proporsi Sekolah dengan Akses Listrik | 1794 |
|  | Ratio of Pure Participation Participation (APM) Female / Male by Area | Rasio Angka Partisipasi Murni (APM) Perempuan/Laki-Laki Menurut Daerah Tempat Tinggal | 1456 |
|  | Ratio of Pure Participation Participation (APM) Female / Male by Province | Rasio Angka Partisipasi Murni (APM) Perempuan/Laki-Laki Menurut Provinsi | 1455 |
|  | Ratio of Pure Participation Participation (APM) Female / Male by Revenue Group (Expenditures) | Rasio Angka Partisipasi Murni (APM) Perempuan/Laki-Laki Menurut Kelompok Pendapatan (Pengeluaran) | 1608 |
|  | Ratio of Pure Participation Rate (APM) for Women / Men by Expenditure Group | Rasio Angka Partisipasi Murni (APM) Perempuan/Laki-Laki Menurut Kelompok Pendapatan | 1607 |
|  | Rough Participation Rate of University by Area | Angka Partisipasi Kasar (APK) Perguruan Tinggi (PT) Menurut Daerah Tempat Tinggal | 1445 |
|  | Rough Participation Rate of University by Groups of Expenditure | Angka Partisipasi Kasar (APK) Perguruan Tinggi (PT) Menurut Kelompok Pengeluaran | 1444 |
|  | Rough Participation Rate of University by Province | Angka Partisipasi Kasar (APK) Perguruan Tinggi (PT) Menurut Provinsi | 1443 |
|  | Rough Participation Rate of University by Sex | Angka Partisipasi Kasar (APK) Perguruan Tinggi (PT) Menurut Jenis Kelamin | 1446 |
|  | Youth and adult participation rates in formal and non-formal education and training in the last 12 months, by gender | Tingkat partisipasi remaja dan dewasa dalam pendidikan dan pelatihan formal dan non formal dalam 12 bulan terakhir, menurut jenis kelamin | 1998 |
|  | Youth and adult participation rates in formal and non-formal education and training in the last 12 months, by Residence | Tingkat partisipasi remaja dan dewasa dalam pendidikan dan pelatihan formal dan non formal dalam 12 bulan terakhir, menurut Daerah Tempat Tinggal | 1996 |
|  | Youth and adult participation rates in formal and non-formal education and training in the past 12 months, according to Expenditure Groups | Tingkat partisipasi remaja dan dewasa dalam pendidikan dan pelatihan formal dan non formal dalam 12 bulan terakhir, menurut Kelompok Pengeluaran | 2000 |
| ![][image5] |  |  |  |
|  | Level of Proportion of women in managerial positions, according to marital status | Proporsi perempuan yang berada di posisi managerial, menurut status perkawinan | 2007 |
|  | Level of Proportion of women in managerial positions, by area of residence | Proporsi perempuan yang berada di posisi managerial, menurut Daerah Tempat Tinggal | 2004 |
|  | Level Proportion of women in managerial positions by province | Proporsi perempuan yang berada di posisi managerial menurut provinsi | 2003 |
|  | Level The proportion of women in managerial positions, by education level | Proporsi perempuan yang berada di posisi managerial, menurut tingkat pendidikan | 2006 |
|  | Percentage of Seats Occupied In DPR and DPRD | Persentase Kursi Yang Diduduki Perempuan Di DPR Dan DPRD | 1337 |
|  | Proportion of Adult Women and Girls (Aged 15-64 Years) Experiencing Violence (Physical, Sexual, Or Emotional) By Couples Or Former Couples In The Last 12 Months | Proporsi Perempuan Dewasa Dan Anak Perempuan (Umur 15-64 Tahun) Mengalami Kekerasan (Fisik, Seksual, Atau Emosional) Oleh Pasangan Atau Mantan Pasangan Dalam 12 Bulan Terakhir | 1375 |
|  | Proportion of Adult Women and Girls (Aged 15-64 Years) Experiencing Violence (Physical, Sexual, Or Emotional) By Couples Or Former Couples In The Last 12 Months by Type of Violence | Proporsi Perempuan Dewasa Dan Anak Perempuan (Umur 15-64 Tahun) Mengalami Kekerasan (Fisik, Seksual, Atau Emosional) Oleh Pasangan Atau Mantan Pasangan Dalam 12 Bulan Terakhir Menurut Jenis Kekerasan | 1378 |
|  | Proportion of Adult Women and Girls (Ages 15-64 Years) Experiencing Sexual Violence By Others In addition to Couples In The Last 12 Months | Proporsi Perempuan Dewasa Dan Anak Perempuan (Umur 15-64 Tahun) Mengalami Kekerasan Seksual Oleh Orang Lain Selain Pasangan Dalam 12 Bulan Terakhir | 1362 |
|  | Proportion of Individuals Using Mobile Phones | Proporsi Individu Yang Menggunakan Telepon Genggam | 1221 |
|  | Proportion of Individuals Who Use Mobile Phones by Age Group | Proporsi Individu Yang Menggunakan Telepon Genggam Menurut Kelompok Umur | 1222 |
|  | Proportion of Individuals Who Use Mobile Phones by Sex | Proporsi Individu Yang Menggunakan Telepon Genggam Menurut Jenis Kelamin | 1224 |
|  | Proportion of Women Aged 20-24 Years Who Are Married Or Living Status Together Before Age 15 Years | Proporsi Perempuan Umur 20-24 Tahun Yang Berstatus Kawin Atau Berstatus Hidup Bersama Sebelum Umur 15 Tahun | 1358 |
|  | Proportion of Women Aged 20-24 Years Who Are Married or Living Status Together Before Age 15 Years by Area of Residence | Proporsi Perempuan Umur 20-24 Tahun Yang Berstatus Kawin Atau Berstatus Hidup Bersama Sebelum Umur 15 Tahun Menurut Daerah Tempat Tinggal | 1359 |
|  | Proportion of Women Aged 20-24 Years Who Are Married or Living Status Together Before Age 18 Years By Area of Residence | Proporsi Perempuan Umur 20-24 Tahun Yang Berstatus Kawin Atau Berstatus Hidup Bersama Sebelum Umur 18 Tahun Menurut Daerah Tempat Tinggal | 1361 |
|  | Proportion of Women Aged 20-24 Years Who Are Married Or Living Status Together Before Age 18 Years by Province | Proporsi Perempuan Umur 20-24 Tahun Yang Berstatus Kawin Atau Berstatus Hidup Bersama Sebelum Umur 18 Tahun Menurut Provinsi | 1360 |
| ![][image6] |  |  |  |
|  | Percentage of Household Population by Province and Improved Sanitation | Persentase Rumah Tangga menurut Provinsi dan Memiliki Akses terhadap Sanitasi Layak | 847 |
|  | Percentage of Industrial Wastewater Flows Safely Treated | Persentase Limbah Cair Industri Cair yang Diolah Secara Aman | 1279 |
|  | Proportion of Hazardous and Toxic Waste (B3) Processed In accordance with the Regulations | Proporsi Limbah Bahan Berbahaya dan Beracun (B3) Yang Diolah Sesuai Peraturan | 1281 |
|  | Proportion of Households Having Hand Washing Facility With Soap And Water By Province | Proporsi Rumah Tangga Yang Memiliki Fasilitas Cuci Tangan Dengan Sabun Dan Air Menurut Provinsi | 1273 |
|  | Proportion of Households Who Have Access to Decent Sanitation Service by Area of Residence | Proporsi Rumah Tangga Penduduk Yang Memiliki Akses Terhadap Layanan Sanitasi Layak Dan Berkelanjutan Menurut Daerah Tempat Tinggal | 1270 |
|  | Proportion of Households Who Have Handwashing Facility With Soap And Water by Area of Residence | Proporsi Rumah Tangga Yang Memiliki Fasilitas Cuci Tangan Dengan Sabun Dan Air Menurut Daerah Tempat Tinggal | 1274 |
|  | Proportion of Population Populations Who Have Access to Decent and Sustainable Sanitation Services By Revenue Group | Persentase Rumah Tangga yang Memiliki Akses Terhadap Layanan Sanitasi Layak Menurut Kelompok Pengeluaran | 1272 |
| ![][image7] |  |  |  |
|  | Electricity Consumption per Capita | Konsumsi Listrik per Kapita | 1156 |
|  | Electrification Ratio | Rasio Elektrifikasi | 1155 |
|  | Number of gas network connections for households | Jumlah sambungan jaringan gas untuk rumah tangga | 1786 |
|  | Primary Energy Intensity | Intensitas Energi Primer | 1808 |
|  | Ratio of Domestic Gas Use | Rasio Penggunaan Gas Rumah Tangga | 1157 |
|  | Supply of Primary Energy | Bauran Energi Terbarukan | 1824 |
| ![][image8] |  |  |  |
|  | \[2010 Version\] Growth Rate of per Capita Gross Regional Domestic Product at 2010 Constant Market Prices | \[Seri 2010\] Laju Pertumbuhan Produk Domestik Regional Bruto Per Kapita Atas Dasar Harga Konstan 2010 | 296 |
|  | \[2010 Version\] Per Capita Gross Regional Domestic Product by Province | \[Seri 2010\] Produk Domestik Regional Bruto Per Kapita | 288 |
|  | Average Working Hourly Wage by Province | Upah Rata \- Rata Per Jam Pekerja Menurut Provinsi | 1172 |
|  | Average Working Hour Rate by Area of Residence | Upah Rata \- Rata Per Jam Pekerja Menurut Daerah Tempat Tinggal | 1173 |
|  | Average Working Hours Period by Age Group | Upah Rata \- Rata Per Jam Pekerja Menurut Kelompok Umur | 1176 |
|  | Average Working Hours Rate by Education Level | Upah Rata \- Rata Per Jam Pekerja Menurut Tingkat Pendidikan | 1175 |
|  | Average Working Hours Wage by Gender | Upah Rata \- Rata Per Jam Pekerja Menurut Jenis Kelamin | 1174 |
|  | Growth Rate of GDP Per Labor / Growth Rate of Real GDP Per Person Work Per Year | Laju Pertumbuhan PDB Per Tenaga Kerja/Tingkat Pertumbuhan PDB Riil Per Orang Bekerja Per Tahun | 1161 |
|  | Half Unemployment Rate by Age Group | Tingkat Setengah Pengangguran Menurut Kelompok Umur | 1185 |
|  | Half Unemployment Rate by Area of Residence | Tingkat Setengah Pengangguran Menurut Daerah Tempat Tinggal | 1182 |
|  | Half Unemployment Rate by Education Level | Tingkat Setengah Pengangguran Menurut Tingkat Pendidikan | 1184 |
|  | Half Unemployment Rate by Province | Tingkat Setengah Pengangguran Menurut Provinsi | 1181 |
|  | Half Unemployment Rate by Sex | Tingkat Setengah Pengangguran Menurut Daerah Jenis Kelamin | 1183 |
|  | Number of foreign tourist visits per month to Indonesia according to the entrance, 2008 \- 2017 | Jumlah Kunjungan Wisatawan Mancanegara per bulan ke Indonesia Menurut Pintu Masuk, 2008 \- 2017 | 74 |
|  | Number of foreign tourist visits per month to Indonesia according to the entrance, 2017 \- now | Jumlah Kunjungan Wisatawan Mancanegara per bulan ke Indonesia Menurut Pintu Masuk, 2017 \- sekarang | 1150 |
|  | Number of Foreign Tourist Visits to Indonesia by Nationality, 2000-2014 | Jumlah Kunjungan Wisatawan Mancanegara ke Indonesia Menurut Kebangsaan, 2000-2014 | 351 |
|  | Number of Foreign Tourist Visits to Indonesia by Nationality, 2015-now | Jumlah Kunjungan Wisatawan Mancanegara ke Indonesia Menurut Kebangsaan | 1821 |
|  | Number of Nusantara Tourist Travels | Jumlah Perjalanan Wisatawan Nusantara | 1189 |
|  | Percentage and number of working children aged 10-17 years by province | Persentase dan jumlah anak usia 10-17 tahun yang bekerja menurut provinsi | 2008 |
|  | Percentage and number of working children aged 10-17 years by sex | Persentase dan jumlah anak usia 10-17 tahun yang bekerja menurut jenis kelamin | 2009 |
|  | Percentage of Young Age (15-24 Years) Who Are Not School, Working Or Following Training | Persentase Usia Muda (15-24 Tahun) Yang Sedang Tidak Sekolah, Bekerja Atau Mengikuti Pelatihan | 1186 |
|  | Proportion of Informal Employment in Total Employment by Age Group | Proporsi Lapangan Kerja Informal Menurut Kelompok Umur | 2156 |
|  | Proportion of Informal Employment in Total Employment by Educational Level | Proporsi Lapangan Kerja Informal Menurut Tingkat Pendidikan | 2157 |
|  | Proportion of Informal Employment in Total Employment by Province | Proporsi Lapangan Kerja Informal Menurut Provinsi | 2153 |
|  | Proportion of Informal Employment in Total Employment by Sex | Proporsi Lapangan Kerja Informal Menurut Jenis Kelamin | 2155 |
|  | Proportion of Informal Employment in Total Employment by Urban-Rural Classification | Proporsi Lapangan Kerja Informal Menurut Daerah Tempat Tinggal | 2154 |
|  | Proportion of MSME Credits to Total Credit | Proporsi Kredit UMKM Terhadap Total Kredit | 1192 |
|  | Proportion of Tourism Contribution to GDP | Proporsi Kontribusi Pariwisata Terhadap PDB | 1188 |
|  | Total Foreign Exchange of Tourism Sector | Jumlah Devisa Sektor Pariwisata | 1160 |
|  | Unemployment Rate by Age Group | Tingkat Pengangguran Terbuka Berdasarkan Kelompok Umur | 1180 |
|  | Unemployment Rate by Area of Residence | Tingkat Pengangguran Terbuka Berdasarkan Daerah Tempat Tinggal | 1178 |
|  | Unemployment Rate by Education Level | Tingkat Pengangguran Terbuka Berdasarkan Tingkat Pendidikan | 1179 |
|  | Unemployment Rate by Sex | Tingkat Pengangguran Terbuka Berdasarkan Jenis Kelamin | 1177 |
| ![][image9] |  |  |  |
|  | Growth Rate of GDP Manufacturing Industry | Laju Pertumbuhan PDB Industri Manufaktur | 1216 |
|  | Number of Airports In Indonesia By Airport Usage | Jumlah Bandara Di Indonesia Menurut Penggunaan Bandar Udara | 1202 |
|  | Number of Domestic Passengers by Airplane Mode of Transportation by province | Jumlah Penumpang Domestik berdasarkan Moda Transportasi Pesawat Terbang menurut provinsi | 2024 |
|  | Number of Domestic Passengers by Mode of Ship Transportation by province | Jumlah Penumpang Domestik berdasarkan Moda Transportasi Kapal menurut provinsi | 2022 |
|  | Number of Ferry Ports in Indonesia | Jumlah Pelabuhan Penyeberangan Di Indonesia | 1208 |
|  | Number of Ferry Ports in Indonesia by Type of Operation | Jumlah Pelabuhan Penyeberangan Di Indonesia Menurut Jenis Pengoperasian | 1210 |
|  | Number of International Passengers by Airplane Mode of Transportation by province | Jumlah Penumpang Internasional berdasarkan Moda Transportasi Pesawat Terbang menurut provinsi | 2027 |
|  | Number of Passengers based on Railway Transportation Mode | Jumlah Penumpang berdasarkan Moda Transportasi Kereta Api | 2051 |
|  | Number of Strategic Ports | Jumlah Pelabuhan Strategis | 1211 |
|  | Number of Strategic Ports According to Their Management | Jumlah Pelabuhan Strategis Menurut Pengelolaannya | 1213 |
|  | Percentage of Toll Road Lengths Operated By Operator | Persentase Panjang Jalan Tol yang Beroperasi Menurut Operatornya | 1200 |
|  | Proportion of Added Value of Manufacture Sector To GDP | Proporsi Nilai Tambah Sektor Industri Manufaktur Terhadap PDB | 1214 |
|  | Proportion of Added Value of Manufacturing Industry Sector per Capita | Proporsi Nilai Tambah Sektor Industri Manufaktur per Kapita | 1215 |
|  | Proportion of Added Value of Small Industry to Total Value Added Industry | Proporsi Nilai Tambah Industri Kecil Terhadap Total Nilai Tambah Industri | 1219 |
|  | Proportion of Government Research Budget to GDP | Proporsi Anggaran Riset Pemerintah Terhadap PDB | 1825 |
|  | Proportion of Manpower in Manufacturing Industry Sector | Proporsi Tenaga Kerja pada Sektor Industri Manufaktur | 1217 |
|  | Proportion of Small Industry With Loans Or Credit | Proporsi Industri Kecil Dengan Pinjaman Atau Kredit | 1220 |
|  | Railway Network Length In Indonesia | Panjang Jaringan Jalan Rel Kereta Api Di Indonesia | 1195 |
|  | Steady Condition of National Roads | Kondisi Mantap Jalan Nasional | 1197 |
| ![][image10] |  |  |  |
|  | Average Economic Growth In Disadvantaged Areas | Rata-Rata Pertumbuhan Ekonomi Di Daerah Tertinggal | 1237 |
|  | Gini Ratio | Gini Rasio | 98 |
|  | Indonesia Democracy Index (IDI) by Aspect and Province | Indeks Demokrasi Indonesia (IDI) Menurut Aspek dan Provinsi | 599 |
|  | Number of complaints handling of human rights violations of women especially violence against women | Jumlah penanganan pengaduan pelanggaran Hak Asasi Manusia (HAM) perempuan terutama kekerasan terhadap perempuan | 1414 |
|  | Number of Disadvantaged Villages | Jumlah Desa Tertinggal | 1231 |
|  | Number of Independent Villages by Province (Villages) | Jumlah Desa Mandiri Menurut Provinsi | 2190 |
|  | Number of Underdeveloped Villages (Villages) | Jumlah Desa Tertinggal menurut Provinsi (Desa) | 2191 |
|  | Percentage of Budget Plan for Central Government Social Protection Function Expenditures | Persentase Rencana Anggaran Untuk Belanja Fungsi Perlindungan Sosial Pemerintah Pusat | 1611 |
|  | Persentase Penduduk Miskin Menurut Kabupaten/Kota | Persentase Penduduk Miskin Menurut Kabupaten/Kota | 621 |
|  | Proportion of population living below 50 percent of median income, by province | Proporsi penduduk yang hidup di bawah 50 persen dari median pendapatan, menurut provinsi | 2011 |
| ![][image11] |  |  |  |
|  | Number of Deaths, Disappeared, and Hurt Victims Affected | Jumlah Korban Meninggal, Hilang, dan Terluka Terkena Dampak Bencana | 1804 |
|  | Number of Deaths, Disappeared, and Hurt Victims Affected by 100,000 People | Jumlah Korban Meninggal, Hilang, dan Terluka Terkena Dampak Bencana Per 100.000 Orang | 1246 |
|  | Percentage of Households who Have Access To A Decent And Affordable Housing According to the Area of Residence | Persentase Rumah Tangga yang Memiliki Akses Terhadap Hunian Yang Layak Dan Terjangkau Menurut Daerah Tempat Tinggal | 1242 |
|  | Percentage of Households who Have Access To A Decent And Affordable Residential by Province | Persentase Rumah Tangga yang Memiliki Akses Terhadap Hunian Yang Layak Dan Terjangkau Menurut Provinsi | 1241 |
|  | Percentage of households with convenient access (0.5 km distance) to public transportation by province | Persentase rumah tangga yang memiliki akses nyaman (jarak 0.5 km) ke transportasi umum menurut provinsi | 2012 |
|  | Percentage of population aged 10 years and over using public motorized vehicles on certain routes by province | Persentase penduduk berumur 10 tahun ke atas yang menggunakan kendaraan bermotor umum dengan rute tertentu menurut provinsi | 2013 |
|  | Percentage of Victims of Violence in the Last 12 Months Reporting to the Police | Persentase Korban Kekerasan Dalam 12 Bulan Terakhir Yang Melaporkan Kepada Polisi | 1252 |
|  | Percentage of Victims of Violence in the Last 12 Months Reporting to the Police by Sex | Persentase Korban Kekerasan Dalam 12 Bulan Terakhir Yang Melaporkan Kepada Polisi Menurut Jenis Kelamin | 1253 |
|  | Proportion of People Who Became Victims of Violent Violence In The Last 12 Months By Age Group | Proporsi Penduduk Yang Menjadi Korban Kejahatan Kekerasan Dalam 12 Bulan Terakhir Menurut Kelompok Umur | 1310 |
|  | Proportion of People Who Became Victims of Violent Violence In The Last 12 Months By Sex | Proporsi Penduduk Yang Menjadi Korban Kejahatan Kekerasan Dalam 12 Bulan Terakhir Menurut Jenis Kelamin | 1309 |
|  | Proportion of Population Who Became Victims of Violent Violence in the Last 12 Months by Province | Proporsi Penduduk Yang Menjadi Korban Kejahatan Kekerasan Dalam 12 Bulan Terakhir Menurut Provinsi | 1311 |
|  | Proportion of Population Who Became Victims of Violent Violence In The Last 12 Months By Region Classification | Proporsi Penduduk Yang Menjadi Korban Kejahatan Kekerasan Dalam 12 Bulan Terakhir Menurut Klasifikasi Wilayah | 1308 |
|  | Unemployment Rate by Sex | Tingkat Pengangguran Terbuka Berdasarkan Jenis Kelamin | 1177 |
| ![][image12] |  |  |  |
|  | Number of Companies Implementing SNI ISO 14001 Certification | Jumlah Perusahaan yang Menerapkan Sertifikasi SNI ISO 14001 | 1744 |
|  | Number of Public Facilities that Implement Community Service Standards (SPM) and Registered | Jumlah Fasilitas Publik yang Menerapkan Standar Pelayanan Masyarakat (SPM) dan Teregister | 1748 |
|  | Number of Registered Green Products | Jumlah Produk Ramah Lingkungan yang Teregister | 1746 |
| ![][image13] |  |  |  |
|  | Number of Deaths, Disappeared, and Hurt Victims Affected | Jumlah Korban Meninggal, Hilang, dan Terluka Terkena Dampak Bencana | 1804 |
|  | Number of Deaths, Disappeared, and Hurt Victims Affected by 100,000 People | Jumlah Korban Meninggal, Hilang, dan Terluka Terkena Dampak Bencana Per 100.000 Orang | 1246 |
| ![][image14] |  |  |  |
|  | Number of Water Conservation Areas | Jumlah Kawasan Konservasi Perairan | 1289 |
|  | Proportion of catches of fish species that are within safe biological limits | Proporsi Tangkapan Jenis Ikan yang Berada Dalam Batasan Biologis yang Aman | 1586 |
| ![][image15] |  |  |  |
|  | Number of Endangered Animals | Jumlah Satwa Terancam Punah | 1297 |
| ![][image16] |  |  |  |
|  | Anti-Corruption Behaviour Index (ACBI) by Age Group | Indeks Perilaku Anti Korupsi (IPAK) Menurut Kelompok Umur | 1499 |
|  | Anti-Corruption Behaviour Index (ACBI) by Dimension | Indeks Perilaku Anti Korupsi (IPAK) Menurut Dimensi | 635 |
|  | Anti-Corruption Behaviour Index (ACBI) by Dimension and Age Group | Indeks Perilaku Anti Korupsi (IPAK) Menurut Dimensi dan Kelompok Umur | 594 |
|  | Anti-Corruption Behaviour Index (ACBI) by Dimension and Level of Education | Indeks Perilaku Anti Korupsi (IPAK) Menurut Dimensi dan Jenjang Pendidikan | 597 |
|  | Anti-Corruption Behaviour Index (ACBI) by Dimension and Sex | Indeks Perilaku Anti Korupsi (IPAK) Menurut Dimensi dan Jenis Kelamin | 592 |
|  | Anti-Corruption Behaviour Index (ACBI) by Dimension Urban-Rural Classification | Indeks Perilaku Anti Korupsi (IPAK) Menurut Dimensi dan Daerah Tempat Tinggal | 595 |
|  | Anti-Corruption Behaviour Index (ACBI) by Level of Education | Indeks Perilaku Anti Korupsi (IPAK) Menurut Jenjang Pendidikan | 1504 |
|  | Anti-Corruption Behaviour Index (ACBI) by Urban-Rural Classification | Indeks Perilaku Anti Korupsi (IPAK) Menurut Daerah Tempat Tinggal | 1501 |
|  | Household Poporsi Who Has Child Age 1-17 Years Who Have Physical Sentence And / Or Psychological Aggression From The Caregiver In The Last Year By Region Of Residence | Poporsi Rumah Tangga Yang Memiliki Anak Umur 1-17 Tahun Yang Mengalami Hukuman Fisik Dan/Atau Agresi Psikologis Dari Pengasuh Dalam Setahun Terakhir Menurut Wilayah Tempat Tinggal | 1392 |
|  | Indonesia Democracy Index (IDI) by Indicators | Indeks Demokrasi Indonesia (IDI) Menurut Indikator | 598 |
|  | Indonesia Democracy Index (IDI) by Variables | Indeks Demokrasi Indonesia (IDI) Menurut Variabel | 598 |
|  | Indonesian Democracy Index (IDI) by Province | Indeks Demokrasi Indonesia (IDI) Menurut Provinsi | 598 |
|  | Number of Complaints Handling Human Rights Violations | Jumlah Penanganan Pengaduan Pelanggaran Hak Asasi Manusia | 1240 |
|  | Number of Murder Crimes cases in the past year | Jumlah Kasus Kejahatan Pembunuhan Pada Satu Tahun Terakhir | 1306 |
|  | Percentage of children who have birth certificate by Area of Residence | Persentase anak yang memiliki akta kelahiran Menurut Daerah Tempat Tinggal | 1413 |
|  | Percentage of children who have birth certificate by Province | Persentase anak yang memiliki akta kelahiran Menurut Provinsi | 1412 |
|  | Percentage of Compliance with the implementation of Public Service Law for Ministry/Institution | Persentase Kepatuhan pelaksanaan UU Pelayanan Publik untuk KL | 1236 |
|  | Percentage of coverage of birth certificate ownership among population 0-17 years old by province | Persentase cakupan kepemilikan akta kelahiran pada penduduk 0-17 tahun menurut provinsi | 2014 |
|  | Percentage of Population Age 0-17 With Birth Certificate Ownership (Bottom 40%), by Province | Persentase Penduduk Usia 0-17 Tahun Dengan Kepemilikan Akta Lahir (40% Terbawah), Menurut Provinsi | 1570 |
|  | Percentage of Population Age 0-17 With Birth Certificate Ownership (Lower 40%), According to Gender | Persentase Penduduk Usia 0-17 Tahun Dengan Kepemilikan Akta Lahir (40% Terbawah), Menurut Jenis Kelamin | 1573 |
|  | Percentage of Population Age 0-17 With Birth Certificate Ownership (Lower 40%), by Area Type | Persentase Penduduk Usia 0-17 Tahun Dengan Kepemilikan Akta Lahir (40% Terbawah), Menurut Daerah Tempat Tinggal | 1487 |
|  | Poporsi Rumah Tangga Yang Memiliki Anak Umur 1-17 Tahun Yang Mengalami Hukuman Fisik Dan/Atau Agresi Psikologis Dari Pengasuh Dalam Setahun Terakhir | Poporsi Rumah Tangga Yang Memiliki Anak Umur 1-17 Tahun Yang Mengalami Hukuman Fisik Dan/Atau Agresi Psikologis Dari Pengasuh Dalam Setahun Terakhir | 1391 |
|  | Prevalence of Violence Against Girls | Prevalensi Kekerasan Terhadap Anak Perempuan | 1364 |
|  | Prevalence of Violence Against Girls by Age | Proporsi laki-laki muda umur 18-24 tahun yang mengalami kekerasan seksual sebelum umur 18 tahun | 1371 |
|  | Prevalence of Violence Against Girls by Type of Violence | Prevalensi Kekerasan Terhadap Anak Laki-Laki | 1369 |
|  | Proportion of Households with 1-17 Years Old Children Who Have Physical Sentence And / Or Psychological Aggression From Caretakers In The Last Year | Proporsi Rumah Tangga Yang Memiliki Anak Umur 1-17 Tahun Yang Mengalami Hukuman Fisik Dan/Atau Agresi Psikologis Dari Pengasuh Dalam Setahun Terakhir | 1313 |
|  | Proportion of Households with Children Aged 1-17 Years Experiencing Physical Sentence And / Or Psychological Aggression From Caretakers In The Last Year By Territory | Proporsi Rumah Tangga Yang Memiliki Anak Umur 1-17 Tahun Yang Mengalami Hukuman Fisik Dan/Atau Agresi Psikologis Dari Pengasuh Dalam Setahun Terakhir Menurut Wilayah Tempat Tinggal | 1314 |
|  | Proportion of prisoners who exceed the period of detention of the entire number of prisoners | Proporsi tahanan yang melebihi masa penahanan terhadap seluruh jumlah tahanan | 1191 |
|  | Proportion of Safe Residents Walking Alone In The Area Where Its Healed | Proporsi Penduduk Yang Merasa Aman Berjalan Sendirian Di Area Tempat Tinggalnya | 1312 |
|  | The proportion of children under 5 years of age whose birth is recorded by civil registration agencies by Province | Proporsi anak umur di bawah 5 tahun yang kelahirannya dicatat oleh lembaga pencatatan sipil Menurut Provinsi | 1410 |
|  | The proportion of children under 5 years of age whose birth is recorded by civil registration agencies by sex | Proporsi anak umur di bawah 5 tahun yang kelahirannya dicatat oleh lembaga pencatatan sipil Menurut Jenis Kelamin | 1411 |
|  | The proportion of crime victims in the last 12 months reporting to the police | Proporsi Korban Kekerasan dalam 12 bulan terakhir yang Melaporkan Kepada Polisi | 1187 |
|  | The proportion of major government expenditures to approved budgets | Proporsi pengeluaran utama pemerintah terhadap anggaran yang disetujui | 1235 |
|  | The proportion of women and young men aged 18-24 years who experienced sexual violence before the age of 18 years | Proporsi perempuan dan laki-laki muda umur 18-24 tahun yang mengalami kekerasan seksual sebelum umur 18 tahun | 1318 |
| ![][image17] |  |  |  |
|  | Growth of Non Oil and Gas Product Exports | Pertumbuhan Ekspor Produk Non Migas | 1261 |
|  | Percentage of Data Users Who Use BPS Data as The Basis for National Development Planning, Monitoring and Evaluation | Persentase Pengguna Data yang Menggunakan Data BPS Sebagai Dasar Perencanaan, Monitoring dan Evaluasi Pembangunan Nasional | 1606 |
|  | Percentage of subscribers served by fixed broadband internet access networks to total households, by province | Persentase pelanggan terlayani jaringan internet akses tetap pitalebar (fixed broadband) terhadap total rumah tangga, menurut provinsi | 2015 |
|  | Proportion of Debt and Debt Service to Export of Goods and Services | Proporsi Pembayaran Utang Dan Bunga (Debt Service) Terhadap Ekspor Barang Dan Jasa | 1260 |
|  | Proportion of Realization of Government Revenues to Gross Domestic Product | Proporsi Realisasi Pendapatan Pemerintah Terhadap Produk Domestik Bruto | 1588 |
|  | Proportion of Remittance Volume (In US Dollars) To Total GDP | Proporsi Volume Remitansi (Dalam US Dollars) Terhadap Total PDB | 1258 |
|  | Ratio of Tax Revenue to GDP | Rasio Penerimaan Pajak Terhadap PDB | 1529 |

---

---

##### **How to View SDGs data**

Data table can be consumed using "data" Model, and 0000 Domain to display specific id var (refer to menu Dynamic Data documentation [above](https://webapi.bps.go.id/documentation/#dynamicdata)).

https://webapi.bps.go.id/v1/api/list/model/data/domain/0000/var/id\_var\_in\_table\_above/key/your\_api\_key/  
example: Number of Deaths, Disappeared, and Hurt Victims Affected  
https://webapi.bps.go.id/v1/api/list/model/data/domain/0000/var/1804/key/your\_api\_key/

               
**Send a Sample Request**

# **Special Data Dissemination Standard (SDDS)**

##### **List All SDDS Table**

This service is used to displays all SDDS table, domain must be "0000"

https://webapi.bps.go.id/v1/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display sdds table is "sdds" |
| key | String | Key app to access API |

**Send a Sample Request**

### **SDDS Table List**

This table is updated annually without prior notice

| Variable | Variable (id) | Model | Id Var |
| ----- | ----- | ----- | ----- |
| Wholesale Price Index (WPI) (2018=100) | Indeks Harga Perdagangan Besar (IHPB) Indonesia (2018=100) | data | 1721 |
| Number and Percentage of Employment and Unemployment | Jumlah dan Persentase Penduduk Bekerja dan Pengangguran | data | 1953 |
| Average of Net Wage/Salary | Rata-Rata Upah/Gaji | data | 1521 |
| Inflation by Personal Care and Other Services Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 11 Perawatan Pribadi dan Jasa Lainnya | data | 1904 |
| Inflation by Provision of Food and Beverages / Restaurant Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 10 Penyediaan Makanan dan Minuman / Restoran | data | 1903 |
| Penduduk Berumur 15 tahun ke atas menurut jenis kegiatan | Penduduk Berumur 15 tahun ke atas menurut jenis kegiatan | data | 529 |
| Value of Export Oil\&Gas \- Non Oil\&Gas | Nilai Ekspor Migas-NonMigas | data | 1753 |
| \[2010 Version\] 3\. Distribution of GDP at Current Market Prices by Expenditure | \[Seri 2010\] 3\. Distribusi PDB Triwulanan Atas Dasar Harga Berlaku menurut Pengeluaran | data | 110 |
| \[2010 Version\] 4\. Growth Rate of GDP at Constant Market Prices By Expenditure | \[Seri 2010\] 4\. Laju Pertumbuhan PDB menurut Pengeluaran | data | 108 |
| Consumer Price Index of 90 City (General) | Indeks Harga Konsumen 90 Kota (Umum) | data | 1709 |
| Consumer Price Index of Foods, Beverages and Tobacco Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 01 Makanan, Minuman dan Tembakau | data | 2212 |
| Value of Import Oil\&Gas \- Non Oil\&Gas | Nilai Impor Migas-NonMigas | data | 1754 |
| GDP Implicit Growth by Industry (2010=100) | \[Seri 2010\] Laju Implisit PDB Menurut Lapangan Usaha Seri 2010 | data | 105 |
| Distribution of GDP at Current Market Prices by Industry (2010=100) | \[Seri 2010\] Distribusi PDB Menurut Lapangan Usaha Seri 2010 Atas Dasar Harga Berlaku | data | 106 |
| Growth Rate of GDP by Industry (2010=100) | \[Seri 2010\] Laju Pertumbuhan PDB Seri 2010 | data | 104 |
| Consumer Price Index of Health Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 05 Kesehatan | data | 2216 |
| Consumer Price Index of 38 Province (2022=100) | Indeks Harga Konsumen 38 Provinsi (2022=100) | data | 2261 |
| Inflation by Food, Beverage and Tobacco Group and Sub (2018 \= 100\) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 01 Makanan, Minuman dan Tembakau | data | 1890 |
| Inflation by Clothing and Footwear Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 02 Pakaian dan Alas Kaki | data | 1894 |
| Inflation by Housing, Water, Electricity and Household Fuel Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 03 Perumahan, Air, Listrik dan Bahan Bakar Rumah Tangga | data | 1895 |
| Inflation by Equipments and Routine Household Maintenance Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 04 Perlengkapan, Peralatan dan Pemeliharaan Rutin Rumah Tangga | data | 1897 |
| Inflation by Health Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 05 Kesehatan | data | 1898 |
| Inflation by Transportation Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 06 Transportasi | data | 1899 |
| Inflation by Information, Communication and Financial Services Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 07 Informasi, Komunikasi dan Jasa Keuangan | data | 1900 |
| Inflation by Recreation, Sports and Culture Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 08 Rekreasi, Olahraga dan Budaya | data | 1901 |
| Inflation by Education Group and Sub (2018=100) | Inflasi (2018=100) Menurut Kelompok dan Sub Kelompok 09 Pendidikan | data | 1902 |
| Source of Growth of GDP by Industry (2010=100) | \[Seri 2010\] Sumber Pertumbuhan PDB Menurut Lapangan Usaha Seri 2010 | data | 554 |
| Mid Year Population | Jumlah Penduduk Pertengahan Tahun | data | 1975 |
| Population Growth Rate | Laju Pertumbuhan Penduduk | data | 1976 |
| Consumer Price Index of Transportation Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 06 Transportasi | data | 2217 |
| Consumer Price Index of Information, Communication and Financial Service Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 07 Informasi, Komunikasi dan Jasa Keuangan | data | 2218 |
| Consumer Price Index of Recreation, Sport and Culture Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 08 Rekreasi, Olahraga dan Budaya | data | 2219 |
| Consumer Price Index of Education Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 09 Pendidikan | data | 2220 |
| Consumer Price Index of Provision of Food and Beverages / Restaurant Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 10 Penyediaan Makanan dan Minuman / Restoran | data | 2221 |
| Unemployment Rate by Province | Tingkat Pengangguran Terbuka Menurut Provinsi | data | 543 |
| Consumer Price Index of Foods, Beverages and Tobacco Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 01 Makanan, Minuman dan Tembakau | data | 1905 |
| Consumer Price Index of Clothing and Footwear Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 02 Pakaian dan Alas Kaki | data | 1906 |
| Consumer Price Index of Housing, Water, Electricity and Household Fuel Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 03 Perumahan, Air, Listrik dan Bahan Bakar Rumah Tangga | data | 1907 |
| Consumer Price Index of Equipments and Routine Household Maintenance Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 04 Perlengkapan, Peralatan dan Pemeliharaan Rutin Rumah Tangga | data | 1908 |
| Consumer Price Index of Health Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 05 Kesehatan | data | 1909 |
| Consumer Price Index of Transportation Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 06 Transportasi | data | 1910 |
| Consumer Price Index of Information, Communication and Financial Service Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 07 Informasi, Komunikasi dan Jasa Keuangan | data | 1911 |
| Consumer Price Index of Recreation, Sport and Culture Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 08 Rekreasi, Olahraga dan Budaya | data | 1912 |
| Consumer Price Index of Education Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 09 Pendidikan | data | 1913 |
| Consumer Price Index of Provision of Food and Beverages / Restaurant Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 10 Penyediaan Makanan dan Minuman / Restoran | data | 1915 |
| Consumer Price Index of Personal Care and Other Services Group and Sub (2018=100) | Indeks Harga Konsumen (2018=100) Menurut Kelompok dan Sub Kelompok 11 Perawatan Pribadi dan Jasa Lainnya | data | 1916 |
| GDP by Industry (2010=100) | \[Seri 2010\] PDB Menurut Lapangan Usaha Seri 2010 | data | 65 |
| Consumer Price Index of Clothing and Footwear Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 02 Pakaian dan Alas Kaki | data | 2213 |
| Consumer Price Index of Housing, Water, Electricity and Household Fuel Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 03 Perumahan, Air, Listrik dan Bahan Bakar Rumah Tangga | data | 2214 |
| Quaterly Large and Medium Manufacturing (2010=100) | IBS Triwulanan (2010=100) | data | 89 |
| Monthly Large and Medium Manufacturing (2010=100) | IBS Bulanan (2010=100) | data | 88 |
| \[2010 Version\] 1\. GDP at Current Market Prices by Expenditure | \[Seri 2010\] 1\. PDB Triwulanan Atas Dasar Harga Berlaku menurut Pengeluaran | data | 1955 |
| \[2010 Version\] 2\. GDP at Constant Market Prices by Expenditure | \[Seri 2010\] 2\. PDB Triwulanan Atas Dasar Harga Konstan menurut Pengeluaran | data | 1956 |
| Wholesale Price Index (WPI) of Indonesia (2023=100) | Indeks Harga Perdagangan Besar (IHPB) Indonesia (2023=100) | data | 2498 |
| Consumer Price Index of Equipments and Routine Household Maintenance Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 04 Perlengkapan, Peralatan dan Pemeliharaan Rutin Rumah Tangga | data | 2215 |
| Consumer Price Index of Personal Care and Other Services Group and Sub (2022=100) | Indeks Harga Konsumen (2022=100) Menurut Kelompok dan Sub Kelompok 11 Perawatan Pribadi dan Jasa Lainnya | data | 2222 |
| Indeks Harga Perdagangan Internasional (IHPI) 2010=100 | Indeks Harga Perdagangan Internasional (IHPI) 2010=100 | data | 1722 |
| Export Price Index (2023=100) | Indeks Harga Ekspor (2023=100) | data | 2487 |
| Import Price Index (2023=100) | Indeks Harga Impor (2023=100) | data | 2490 |

---

##### **How to View SDDS data**

Data table can be consumed using "data" or "statictable" Model (check the table below), and 0000 Domain to display specific id var (refer to menu Dynamic Data documentation [above](https://webapi.bps.go.id/documentation/#dynamicdata)). For more information about SDDS, [click here](https://www.bi.go.id/id/statistik/sdds/Default.aspx)

https://webapi.bps.go.id/v1/api/list/model/Model\_in\_table\_below/domain/0000/var/id\_var\_in\_table\_below/key/your\_api\_key/  
example: Value of Export Oil\&Gas \- Non Oil\&Gas  
https://webapi.bps.go.id/v1/api/list/model/data/domain/0000/var/1753/key/your\_api\_key/

               
**Send a Sample Request**

### **Statistical Classifications**

There are two kind of classifications that WebAPI provides: Klasifikasi Baku Lapangan Usaha Indonesia (KBLI: 2009, 2015, 2017, and 2020\) that based on International Standard Industrial Classification of All Economic Activities (ISIC), and Klasifikasi Baku Komoditi Indonesia (KBKI 2015). For more information, [Click here](https://www.bps.go.id/klasifikasi)

---

##### **Detail of Statistical Classification**

This service is used to displays detail of a statistical classification are shown on the website

https://webapi.bps.go.id/v1/api/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model that allowed: Allowed values: KBLI: "kbli2009", "kbli2015", "kbli2017", "kbli2020" KBKI: "kbki2015" |
| lang | String | Language to display Default value: ind Allowed values: "ind", "eng" |
| id | String | statistical classification id to display Example: kbli\_2009\_01, kbki\_2020\_012 ![][image18] |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success Response**

```
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": x,
"pages": x,
"per_page": x,
"count": x,
"total": x
},
[
{
"_index": "...",
"_type": "...",
"_id": "kbli_2020_011",
"_score": x,
"_source": {
"konten": "...",
"jenis": "...",
"id": "...",
"source": "Metadata Management System (MMS)",
"judul": "...",
"title": "...",
"deskripsi": "...",
"description": "...",
"isbn": x,
"issn": x,
"no_katalog": x,
"no_publikasi": x,
"last_update": "date",
"tgl_rilis": "date",
"lokasi": null,
"url": "https://www.bps.go.id/klasifikasi/app/view/model/code",
"level": "...",
"mfd": null,
"sebelumnya": [
{
...,
"kode": "...",
"judul": "...",
"deskripsi": "..."
},
...
],
"turunan": [
{
...,
"kode": "...",
"deskripsi": "...",
"judul": "..."
},
...
],
"flag": ...,
"tags": [
...,
"...",
...
]
}
}
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List of Statistical Classification**

This service is used to list all of the statistical classification

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model that allowed: Allowed values: KBLI: "kbli2009", "kbli2015", "kbli2017", "kbli2020" KBKI: "kbki2015" |
| page **optional** | Number | Page to display statistical classification Allowed values: 1, 2, 3, 4, ..., n |
| per page **optional** | Number | Number of statistical classification to display |
| level **optional** | String | level of item [KBLI:](https://www.bps.go.id/klasifikasi/app/kbli) kategori, golongan pokok, golongan, subgolongan, kelompok [KBKI:](https://www.bps.go.id/klasifikasi/app/kbki) seksi, divisi, kelompok, kelas, subkelas, kelompok komoditas, kelompok |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success Response**

```
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 2710,
"per_page": 1,
"count": 1,
"total": 2710
},
[
{
"_index": "datacontent",
"_type": "_doc",
"_id": "kbli_2020_01",
"_score": null,
"_source": {
"konten": "...",
"jenis": "...",
"id": "klasifikasi_tahun_kode",
"source": "Metadata Management System (MMS)",
"judul": "...",
"title": "...",
"deskripsi": "...",
"description": "...",
"isbn": null,
"issn": null,
"no_katalog": null,
"no_publikasi": null,
"last_update": "date",
"tgl_rilis": "date",
"lokasi": null,
"url": "https://www.bps.go.id/klasifikasi/app/view/klasifikasi/kode",
"level": "...",
"mfd": null,
"sebelumnya": [
{
"kode": "...",
"judul": "...",
"deskripsi": "..."
}
],
"turunan": [
...,
{
"kode": "...",
"deskripsi": "...",
"judul": "..."
},
...
],
"flag": true,
"tags": [
...,
"...",
...
]
},
"sort": [
"..."
]
}
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

### **Searching**

This service is used to search website contents

https://webapi.bps.go.id/v1/api/list/

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model that user wants to search |
| lang **optional** | String | Language to display strategic indicators Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed derived period data (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page | Number | Page to display contents Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |
| keyword **optional** | String | Keyword to search. (Use "+" symbol if you have space on your keyword) |

**Send a Sample Request**

### **News**

---

##### **Detail News**

This service is used to display detail of news

https://webapi.bps.go.id/v1/view

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| domain | Number | Domains that will be displayed news (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| model | String | Model to display news (news) for news is "news" |
| lang | String | Language to display news Default value: ind Allowed values: "ind", "eng" |
| id | Number | news id to display Allowed values: 1, 2, 3, 4, ..., n |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list news. |
| data | Object | Information status |
|   news\_id | Number | ID unique of news |
|   newscat\_id | String | ID of news category |
|   title | String | Title of news |
|   news | String | News |
|   rl\_date | String | Release Date of news |
|   picture | String | Picture of news if available |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data":{
"news_id":"news-890232",
"newscat_id": "Statistik Lain",
"title": "1212 1212 314",
"news": "Saat ini telah dilaksanakan Sensus Ekonomi 2016 tahap kedua.",
"rl_date":"2016-09-01",
"picture" : "http://jabar-dev.bps.go.id/new/website/galeri/"
}
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List All BPS News**

This service is used to displays all BPS News are shown on the website

https://webapi.bps.go.id/v1/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display news (news) for news is "news" |
| lang **optional** | String | Language to display news Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed news (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| page **optional** | Number | Page to display news Allowed values: 1, 2, 3, 4, ..., n |
| newscat **optional** | String | News Category to display news Allowed values: "sensus", "survey", "lainnya" |
| month **optional** | Number | Month selected to display news Allowed values: "01", "02", "03", "04", "12" |
| year **optional** | Number | Year selected to display news Allowed values: 1, 2, 3, 4, ..., n |
| keyword **optional** | String | Keyword to search |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list news. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List news |
|     news\_id | Number | ID unique of news |
|     newscat\_id | String | ID of news category |
|     newscat\_name | String | Name of news category |
|     title | String | Title of news |
|     news | String | News |
|     rl\_date | String | Release Date of news |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 0,
"pages": 1,
"per_page": 10,
"count": 3,
"total": 3
},
[
{
"news_id": 9,
"newscat_id": "Sensus dan Survey",
"newscat_name": "KEGIATAN STATISTIK",
"title": "tes berita OK",
"news": "tes berita.....",
"rl_date": "2016-12-27"
},
{
"news_id": 4,
"newscat_id": "Statistik Lain",
"newscat_name": "KEGIATAN STATISTIK LAINNYA",
"title": "Apel Siaga Sensus Ekonomi 2016 Jawa Barat",
"news": "Apel siaga yang dilaksanakan pada Minggu pagi tanggal 28 Februari 2016 dipimpin oleh Gubernur Jawa Barat Ahmad \\r\\nHeryawan (Aher) di Halaman Gedung \\r\\nSate, Jl. Diponegoro No. 22, Kota Bandung......",
"rl_date": "2016-02-28"
},
{
"news_id": 2,
"newscat_id": "Sensus dan Survey",
"newscat_name": "KEGIATAN STATISTIK",
"title": "Perubahan Tahun Dasar PDB Indonesia Berbasis SNA 2008",
"news": "Perubahan tahun dasar Produk Domestik Bruto (PDB) merupakan suatu proses\\r\\n yang lazim dilakukan oleh kantor statistik suatu negara untuk \\r\\nmenggambarkan kondisi perekonomian terkini. BPS telah melakukan \\r\\nperubahan tahun dasar PDB sebanyak 5 (lima) kali yaitu pada tahun 1960, \\r\\n1973, 1983, 1993, dan 2000\. Saat ini, BPS sedang melakukan proses \\r\\npenyusunan perubahan tahun dasar PDB dari tahun 2000 m.....",
"rl_date": "2014-12-31"
}
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
```

---

##### **List News Category**

This service is used to display list of news category

https://webapi.bps.go.id/v1/api/list

###### **Parameter**

| Field | Type | Description |
| ----- | ----- | ----- |
| model | String | Model to display list news category (newscategory) for news is "newscategory" |
| lang **optional** | String | Language to display news category Default value: ind Allowed values: "ind", "eng" |
| domain | Number | Domains that will be displayed news (see master [domain](https://webapi.bps.go.id/documentation/#domain)) Size range: 4 |
| key | String | Key app to access API |

**Send a Sample Request**

###### **Success 200**

| Field | Type | Description |
| ----- | ----- | ----- |
| status | String | Return status, OK if success and Error if any error occured. |
| data-availability | String | Availability status of list news. |
| data | Object\[\] | Response Data |
|   0 | Object | Information status |
|     page | Number | Information page |
|     pages | Number | Information total page |
|     per\_page | Number | sum of per page |
|     count | Number | count on this return list |
|     total | Number | total page |
|   1 | Object | List news category |
|     newscat\_id | Number | ID unique of news |
|     newscat\_name | String | Name of news category |

###### **Success Response**

```
HTTP/1.1 200 OK
{
"status": "OK",
"data-availability": "available",
"data": [
{
"page": 1,
"pages": 1,
"per_page": 10,
"count": 2,
"total": 2
},
[
{
"newscat_id": "Sensus dan Survey",
"newscat_name": "KEGIATAN STATISTIK"
},
{
"newscat_id": "Statistik Lain",
"newscat_name": "KEGIATAN STATISTIK LAINNYA"
}
]
]
}
```

###### **Error 4xx**

| Name | Description |
| ----- | ----- |
| UserNotFound | The id of the User was not found. |

###### **Error Response**

```
HTTP/1.1 404 Not Found
{
"error": "UserNotFound"
}
[image1]: <data:image/png;base64,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QAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQAIaKgAACWioAAAkoKECAJCAhgoAQIL/C0L4soE3zHQkAAAAAElFTkSuQmCC>
[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAJwCAIAAACGccv0AAAqrUlEQVR4Xu3dTW4cx7Yu0DuuNwBNwAPQADwBD0AT0ADcf2qoZUBQyw27pQ5b7ggGQRgyJIMQbEEmINiCUbeOeIq3vHdlsjIzmBkZuT6sxsFx1FYUpYyP9cPi/1z+//8HAEz0P/n/AgCGUqgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACWi7Ut99//en6Ynd29ovfXzzNcwDgXq0V6tXzRx+vXsSqHJ7PN+/2o/L89dp/uzDa8ZwPr5/lBee4fvVk6H5+/+nbvV+++yrfnRH23y3Fv+aj7O9XvgnA+Rop1H35xQOyXPZnev4TVyfeqyE5nvNpyIP+44QvY/zPZyfftX79PZpTqr+BrVl9oT5olR5n7edsvD9Dcjxn8ULdfXlyPt/Bk/75+8944zPi0SowwroL9bcfv4ln4UNmfzrnPaxFvDNDcjynhkK9Tb6PwZuXj+Ntzs7Hqxd5IECPtRbqbA9Mc/764+e8n/rFuzEkx3PqKdRdb6cOfaY3J88E6LHKQp35genJ5F1VLt6BITmeU1Wh9nxzE5cOz6qfkADmt75CjcfecmnsbcDx7h0S7mZPoeaZPeKND8lvAet/HTRPvrzvCYxwj/atHFccEt6ZDNBjZYX64fWzeOYtmrzDleppoLBy/kLd2xdbXHdIXrx38+sPcd0hefFl92Z2HesBsjUVag3P9IY089aVrgbKd3CRQr3s/nNPviM3Ljqk663aPT+7nBcDnLSmQo1HXR1p45W2eK8OySu7im13anGPeONDugq15yZTVk65CcCx1RRq/wtpy6anA9Yi3qVD8sr6C/Xt91/HFYfkmUOHA3RZR6HW3Ka3yXteka5Xpk++h7b+Qu16+nqXVp4z/M3Lx3kxQLaCQu15wFFP8muNKxLvzCEn38Zcf6GO22Fcesj+n19eDJCtoFDjCVdr8s7XIt6TQ/LKy7F1lcUbHzK9UON/Pkqeee+tevYDcKz2Qu35cY4Kk/dfv3gfDvntx2/y4kuFCtCh9kL9fPMunnAVJ++/fvE+HJJX3lKoACdVXairePX0OF0/5lizeB++5OQPd96qrVA/pd88E1ccJc+891Y9+wE4VnWhxrOt+px8W2zNuj5BPq+8s1Shdv25+anpuOIoeey9t+raD0CwuULdP/baH8H7x757PR/iOjr5XtQs7v6QvPJOV7Htem+VxRsfcrLABn30YFxxlLz43lud3A9AtpVCzcMf6A/KD5iq1fPrQvPiOz2F2pU85LL7a35cYPtveu79486fvDu1+N5bKVTgTPUWas+DkqHJw7NSnx2RX9KrVtdd7v+e4N6Gy8lDLrsLbFBOtl1cdJS8+N5bnfwjALJ6CzUebKMy6EXNeOOxyZMr1PPzSHnxsXoKtav447qj5MX33kqhAmdqvFDz2B49v3JkUPLkCnV9Pl/P+3tvVVKon2/e5Zn3Ts6L772VQgXOVGmh9ry8Nyh5cr94+1E5+Yl9tYmbPiSvDGoo1P4fT4qrj5IX33srhQqcqdJCHXFq53Q9JdijyJ+7iiM4bvqQvDIY8SXKQy67N3BO8rQzJ+fF995qFX+bQA0qLdR4qo1KHnuvIh8lUf/7kvaP8OKmD8mLg55Cvf1hpCwPuez+K/549eLuhvG/HZKnnTN513vDuPQQhQqcqdlCHd1qcdCo5LFVids95Jwnq3sKNS/uEW98yHGBdb0Pub/k4uqj5MX33qr/zwK402yhdj0wulccNCp5bFXidg/JK7M5C7XnR6fywHsn70bdSqECZ2q2UPPMM8VBo5LH1qPrzcxn/krXOQu1Z1keeO9NdqNupVCBMynUKA4alTy2HnGvh+SVJ1VSqD09F5ceJS++91Y9fxDAMYUaxUGjksfWI+71S87/BIyZC/XD62dxxSF5Zv/kXfdNem6lUIEzKdQoDhqVPLYSI369TDBzofaszDP71++6b9Jzq7wfgJMUahQHjUoeW4m40UPyyi4KFeAkhRrFQaOSx1YibvSQvLJL/YXa81v58uI7cekheT8AJynUKA4antE/AvvQPt+8i3v9kkEfKTV/oXb9NGrXx/l2fUzxrneHcekho3/+CtgahfovPZ/Oc37u/Xz5pcSNHpJX9pi/ULte9911/IlD19+KSw/JKwFOUqj/0vUYblDqfEzT9eOnucD6zV+oPYu7vtRx3SF55ZSbABxTqP8Sp4xKHluDuMtD8sp+VRVq10/7xHWH5JW3pny4McAthfovccqo5LE1iLs8JK/st0ihDv1p1LjokOtXT/Liy95nJvJigJMU6v/peXfo+el6p8yyCj4CW6RQe9bnlXtXzx/FdYfkB7U9r7lW+3I4UCGFWvIP3XU/BlpW1/cK+/rfF+S9jkf1FGq+4bFQTvHGhxQp1J71t9nvZ/8H9dyX2+SxAF0qLdRFxNN0VPLYGsRdDszxqHtLqCuhmON/PqSrUPf/f1z6JV2f6d/zLPGZ2T+sz2MBuijU/+p6E+yg/PP3n3lyDeJGB+Z41FKF2nOTvLJ//ZnJAwF6KNT/iqfpqAz6hIQ5xY0OzPGoFRVqz03uzZuXj/M0gB4K9T/iaTo2eXIl4kYH5nhUhYXa9azvrZ538J5MzwYAeijU/4hn6tjkyZWIGx2Y41EVFuruvq98z5ucQ7o+KQLgXgq18x2wQ1Pn+3vJ9q25r+1b+//tzUdAEVsv1J4fWByaPByA7dh6ocZWHJv+l/EAaN6mC3Xo21V6kocDsCmbLtTYihOShwOwKdstVA9PAShoo4X65uXj2IpjE34aBIBt2mihxlYcm2o/axCAmW2xUH/78ZtYjGNz9fxRng/ABm2xUGMrTkgeDsA2ba5QYyVOSB4OwGZtq1D/+fvP2IpjE35dNgAbt6FCLfgpgzsPTwH4tw0VaqzECfE5+AAEWynUD6+fxVYcGz8qA0C2lUKNrTgheTgAbKJQS/3G053PRQKgQ/uFuq/A2Ipjsy/mPB8ALpsv1F+++yq24oTk+QBwq/FCjZU4IftuzvMB4FbLhVrwM3u9sxeAfi0XamzFCcnDAeBYs4UaK3FC8nAACBTq/cnDASBos1BjJU6I9yIBcI4GC7Xgr5TRpgCcqbVCLfjOXh+KBMD5WivU2IoTkocDQJemCrXgr5R5f/E0z2eD9v8S9v+uPl1f3Pr9p2/ffv91XgbQTqEW/P3hTX6Mw74G4v08JC++E5ce5fzFeeWdrk9aPvl8e1jz+eZdXtN/k13H5Oycb872a/INs677eG9Cc8f/3JubX3/YXxF5M8DDaadQ44kyIXl4A9or1H3evHycl/Xf5OTk/pv0595vv7ru472ZUqjH+Xj1Iu8KKK6RQi34Ifj3Hrgr1WSh7nqHn7zJyck9689MHnWn6z7em1KFepu8MaCsFgpVm55Dod7m5OSuxeen53Fq1328N2ULdZ/rV0/y9oBSWijUeGxMSB7ejFYLtf8tQnF1x+TL3q/PmenaSdd9vDfFC3UfL6zCw1l9od78+kM8M8am7Y9x6CmMvPhOXHqU8xfnlXe6yuZk7cVFh+SVPTc5OfnkyhHJYy+77+O9eYhC3XVsEphu9YUaT4ux6XnKrg0NF2rPM5lxacfknvf05m+z9n9cXHRInnzZfR+7HtF2ibc/5Pefvg0re/6udx2bBKZbd6F+vnkXT4uxycMb03PI5sV34tKjnL84r7zTVTYnay8uOkpe3HWTIpO7tp1X9ix+uELtX+9ZX3ggKy7Uv/74OR4VY5OHt6ftQu36kdC4buDknu6JS7/k5A+odN3HpQr15FcAmG7FhRrPiQnJw9vTdqHuOv6UuGjg5Lyy/yYnXzjouo8PXajvL57GpYfkxcB0ay3UnsNiaPKLZE1SqLcZNDmvHHGTrvv40IXac5O8EphulYVa8FfKbKRNLzdQqCef9Y2LBk7OK0fcpOs+KlRozCoLNR4PY3PybG1V84W6O/UHxRWnJpf9yuSVXfdRoUJj1leo8WyYkDy8YWVrY3fqVnHFIXnlna6yybXXM/8u+VZxxak1+0KKiw7Je+iZfJu8sus+KlRozMoKteCvlNnaL2jbQqHu0p8V//OpyQoVKGJlhRoPhrE5+W7MtinU2+TJ4wr1fF338aELdegHUAATralQ46kwIXl48zZSqOGG8T+nBZftFmpcd8jWnpuB2WyxUPORugUbKdTdv/+4+N9OTd5aoeaVQBGrKdR4KoxNPk83YjuF+vnmXc9N8uT2CrX/IznzZKCIdRRqwV8pk4dvRE+hjkv+I+KKQ/LKO11lk2uvZ35Oz03y5KUKtSd5yOWp+3KbfX3u/4i9/h69zQbfPQCzWUGhFnxn73Y+xiFrtVBPfqTz3Wfqxv9wavLaC3VQ8liglBUUajwSxmbj35u3Wqg9///J/5Qnb6RQN/7vH2ZQe6G+efk4Hgxjk4dvSsOFevIVga6b5MnnF+p+5b3CTS6772NP8pDLU/dlUPJAoKyqC/WX776Kp8LY5OFb03Ch9vyn+H+dmnx+ocb/fCrhJpfd97EneciZf/rJnPyUY6C4qgs1HgwTkodvTduF+vHqRfwPX36bafy/Tk1uvlB3HQOBsjZRqFt+L9KdnkLNi+/EpUc5f3FeeaerbHLtdc3v+a8n3/WaJy9VqA/xYzPxvx2SpwHF1Vuo8UgYG216a4OFejJ5ckuFevJ7iJ1nfWEWlRZq17lQc/JJXZXmC7VrVEie3FKh+vxeWFClhRoPgzUkn9RVab5QuxaE5MnnF+qxrq9nXtl1Hx+iUHuW5YFAWQq1WPJJXZWuAtj1HrVx6VHOX5xX3ukqm5NfzLjoS44XnHxrUkierFCBIhRqseSTuipdBbDrPWrj0qOcvzivvNNVNie/mHHRl5yz5jh5cmOF+tuP38QVX3L96kmeCRSkUIsln9RV6SqA3akOuBOXHuX8xXnlna6yOfnFjIu+5Jw1x8mTGyvUrpU+KQkemkItlnxSV6WrAHanOuBOXHqU8xfnlXe6yubkFzMu+pIzB94lT+56SLdLw491fT3zyq4tzVyou1N7AwpSqMWST+qqdBXArvecjUuPcv7ivPLem+SS6Fp85rK75L+mno+3zMPvdD2uzSvrKdT9tw55LFCKQi2WfFJXZV2F+v7i6ZmL87L+tyad/GuKiw7JK+/9U/LK+Qv1n7//jIu+5Pg3xQLFKdRiOXlS12PBQj3Zjv03ySu7FudlXStvc/KvKS46JK8ccZP5C7XnQ7DzWKAUhVosJ0/qesxQqCMeGMWlh+SVXYvzssvuh4+7jr+muOiQno/ZiksPySvnL9SexZ71hYejUIvl5EldjxkKtetlxd2pxf3z88quxXlZz+Jdx19TXHTIycX9N8krqyrUnm9ugIkUarH0HL41mKFQh66PKw7peoo4rvuSvKxn8a7jr+mvP36O6w7Ji3uG706tX6RQx711GZhCoRbLyZO6HvMUatezvrsvj42unj+6XdbzkbO7jsmXHZvJy26d/K3ju46/pp4XHXf/fpq058t4mzx8kULtWZ9XAkUo1GI5eVLXo6cJ8uI7celR8uJ7b3Jm8syeyXlZ//quv6au2huagpPP/EzBoYXa88IwMIVCLZauk7oSaynUnk/Ii0u/JC+7c/KtST1/TXHpqOSxtRXq/rF7XgxMp1CLpeekrsFshdrzOQn3pv/j8eLqL8nL+m/S89cUl96Xk89v57FLFerJ7d0mLwamU6jF0nNS12C2Qr33hl3pb9OumXlZ/036/5pOPqg9mdu3y+Zf3JtnLlWoPd/Z3L2YDRSkUIul/6Re3MyFetn7CCmn6529x+JtviQvO5bfmnTvX1PuyJO5Xfzh9bOT//+xpQq15yb77xvyYmCiSguV4vYPSvadelJefCcvPudWx3757queh309r5hmeQ/nbCOs3z9uy2tOOvmzNKGK8lc1z9n/iXnb5wjvHsoLTi475yZvT+0TmEihAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKis24fXz/75+8/dIe8vnuY1lbt6/uj3n769uwufri/WeC9++/Gb/c7v7sXNrz+8/f7rvAwaplBZq7uz+2Ty+grtKyfu+yifb97lm1To49WLuPWj7L9XyDeBJilUVubNy8fxzO5Ovnkl9o9K4147sn/8nW9eieOHpP25fvUk3xwao1BZmXhU35c8YXGDvie4TR6yuKH3Yv9ANg+BlihU1iQe0udl/3Awj1pQ3N8Zqe1x6ofXz+IWz0ht9wLKUqisxvGbj4YmT1vK6HtRz3t8zn++OidPg2YoVNbhl+++imfzkOSBi/h88y7ubEjywEXEbQ2JJ35pmEJlHeLBPDB54PyGvuiYk2fOb+J3Nrs67gU8BIXKChz/mOa41PB8adzT8OSZ84t7Gp48E9qgUKld/w9rnpnFC3X6A7tdBVU0+gXg4+Sx0AaFSu3ieTwqi7/RN25oVPLYmcUNjUoeC21QqFRtyhtKj5Mnz2nie5HukifPqci9+PD6WZ4MbVCoVC2ex2OTJ88p7mZUFn9/bNzQqOSx0AyFSr2KvO64W/oT8z3IPk6eDM1QqNQrHsajsmybXha6F3nsnKa/y/o2eTK0RKFSr3gej0oeO6c2qijuZlQW/84GHppCpVLxPB6VPHZObTzZe1ni72LxF4BhBgqVGrVRRUVed/ztx2/y5Dmd/zvaepLHQnsUKjUqUkW/fPdVnjynuKFRyWNnFjc0KnkstEehUp3pn3m7z+8/fZsnz6nIW5QXf6bURyPB+RQq1Ynn8ajksTNro4rihobn0/VFHgtNUqhUJx7Jw7P4L7Iu8iB78aesi7ySncdCqxQqdSlyiC/+yb1tPDwt8kp2HgutUqjUpY1DPG5oeBZ/eHpZ4l4s/kt+YE4KlbrEI3l48sz5xT0NT545s5tff4h7GpjFn3iHmSlUKvLx6kU8lQdm/wA3j53Zh9fP4rYGpoYqinsansWfeIeZKVQqEo/k4ckz5xf3NDx55szeXzyNexqYv/74OY+FtilUKhJP5eHJM2c2/f29NTzIjnsaHg9P2SCFSkXiqTwwNTxTOv1NVW28HSnPhOYpVGoxvYryzPnFPQ1Pnjm/uKfhyTOheQqVWsQjeXjyzJldv3oS9zQ8eezM3n7/ddzTwOy/DnksNE+hUoXffvwmnsoD08YzpW9ePs5jZxb3NDx5JmyBQqUKf/3xczyVBybPnF/c0/DkmfOLexqYm19/yDNhCxQqVYin8vDkmfOLexqYGt5UNf2X5NTwVAEsQqFShXgqD0+eOb+4p4GpoYraeKoAFqFQWd7vP30bT+WBeX/xNI+d2fR3JOWZ84t7Gp48EzZCobK8eCQPT545v7ingank94bGbQ1MDZ9KAUtRqCwvnsrDk2fOL+5pYH778Zs8c35xWwNTw1MFsBSFyvLiqTwwbTy2ywMXEbc1MHkgbIdCZXnxVB6YGj42dvqHIeSZ85v+Ft88E7ZDobK8eCoPTB44v+nvq8oz5zfxXtTwYz+wIIXKwvaPL+PBPDB55vzinoYnz5zfxI9T9gIqG6dQWdjEDx2s5G2lcVvDk2fOL+5pYGp47h0WpFBZ2MSnGT+8fpZnzi9ua2C8rwoaoFBZ2L5L4sE8JG+//zrPnF/c1sC08TMzeSBsikJlYfFUHpg8cBFxWwNTw4cOXk6+F3kgbIpCZWHxVB6YPHARcVsDkwcuIm5rYPJA2BSFysLiqTwweeAi4rYGJg9cRNzWkFTy7jBYkEJlYfFgHpg8cBFxWwOTB85v4mdTVPK+KliQQmVh8WAemDxwEXFbA5MHzk+hwkQKlYXFg3lg8sBFxG0NTB44P4UKEylUFhYP5oHJAxcRtzUweeD8FCpMpFBZWDyYByYPXETc1sDkgYuI2xoShQoKlYXFg3lg8sBFxG0NTB64iLitgckDYVMUKguLp/LA5IGLiNsamDxwEXFbA5MHwqYoVBYWT+WBaeOjB9u4F3kgbIpCZWEfr17Eg3lIfv/p2zxzfnFbA1PJC5BxWwOTB8KmKFQW9v7iaTyYh6SSD+iJ2xqePHN+cU8D49e3sXEKleXFg3lg8sD5/fP3n3FbA5Nnzm/ib/75ePUiz4TtUKgsLx7MA5MHzm/iE9e7Ou7FxN9Nu6vjXsBSFCrLi6fywNTwy0QnfirCro4qevPycdzWwOSZsB0KleXFU3l48sz5xT0NzL7M8sz5xW0NTA3f3MBSFCrLi6fy8OSZ84t7Gpg23uhbyXvEYBEKleVNfC/MPh9eP8tjZ9bGy6hxT8OTZ8JGKFSWN/0FyF0F5/gv330V9zQw16+e5LEzi3sanjwTNkKhUoV4Kg9Pnjm/uKfhyTNnNv2NvpW8GAzzU6hU4fPNu3gwD0wN53jc0/DU8KaeuKfhyTNhCxQqVdgXSTyVhyePnVnc0KjksTOLGxqeSj6aGGamUKlFPJWHZ/HP9Z3+c5y7Cgp1+ovBuwruBcxPoVKL6e+S3VVwjscNDU8NH+AX9zQ8eSY0T6FSkXgqD0+eObO//vg57ml48tiZxQ0NTyU/VgtzUqhUJJ7Ko5LHzixuaFTy2DlNf6/vroJn4GFmCpWKTH+v766Cc9yD1LvksdAwhUpd4pE8Ku8vnubJc4obGpU8dk7Xr57EDY1KngytUqjUpchbk3ZLn+NxN6Pyz99/5slzihsalV+++ypPhiYpVKoTj+RRWfYTEkp9W7DsQ+0ir6Tulv7mBmajUKlOPI/HZtmfP9k/vowbGpU8eU5xN2OTJ0N7FCrVKfLBArfJw2dz9fxR3M3Y5OGzKfI2sV0dvw4IHppCpUbvL57GI3ls9sWW588jbmVC8vDZxK2MzeIvCcNDU6hUKp7HE5KHz6PgQ+2//vg5z59HwYfafv04bVOoVKrgOb5brlNLPWW6W/Ql4biVCcnDoRkKlXrFw3hCFny+sdS7k3bL/Yq6st/cLPsGbHg4CpWqxcN4Qhb8dNm4lQlZ6iXhD6+fxa1MSJ4PDVCo1C4exhOy1CO8sm201G8bLfVjqbfJ82HtFCq1iyfxtOT58yj4xO9uuXsR9zEhC77NCh6IQmUF4mE8LXn+POI+JmSplyHLPki9fvUk/xGwXgqVdYiH8bTk+TN4+/3XcR8TstQv1Xnz8nHcyoTk+bBeCpXViIfxhOTh8yj1Gb+3yfPnEfcxIQu++xqKU6isRhuPjQp+2sOCn5NQ5He+3kan0gyFypqU+iWdu0XP8biVCVnqfcuXRd9mlYfDGilUViYexhOSh88mbmVC8vDZxK2MzVKvB0NZCpX1Kfh8Yx4+m7iVCcnDZxO3MjZLvW8ZClKorFI8j8dmqQ9JuCz6knAePpuCLwnn4bAuCpW1iufx2Cz1YX634m5GZcHXgy+LvnU5D4cVUais1W8/fhPP41FZto1KPU7dP1LMw2dT6g1KeTKsiEJlxUq9mJonzynuZmzy5DnF3YzKgm9ahukUKusWj+RReX/xNE+eU9zQqOSxcyr1qYR5MqyFQmXd9l0Yj+RRyZPnVORTCRf/4ZO4oVH58PpZngyroFBZvSKPjT5evciT5xQ3NCp57MzihkYlj4VVUKi0IB7Jo5LHzqnIu5MW/7agyE/R5LGwCgqVFrRxjhd5r2weO7O4oeFZ/CVtGEeh0oh4Kg9PDb+eM+5peBZvoyI/zpTHQv0UKo0o8kpqHjuzIp/+n8fOLG5oePz8DGukUGlHPJWHZ9lPTboV9zQ8eeb84p6GJ8+EyilU2jH9fT2Lv6nnspUqinsanjwTKqdQaUo8lYcnz5zZ9J9JreE3t8Q9DU8NL2nDIAqVpsRTeXjyzPnFPQ1Pnjmzq+eP4p6GJ4+FmilUmvLh9bN4Kg9Mnjm/6R//lGfOL+5pePJMqJlCpTXxVB6YGt6XdDn5XtTwLtnp71jOM6FmCpXWxFN5YBb/Oc5bcVsDs/jn+t6K2xqYPBBqplBpzfQ39eSZ84t7Gp48c35xTwOz7C95haEUKg2KB/PA5IHz+3R9Ebc1MHnm/D5evYjbGpJKni2AMylUGhQP5oHJA+c3/QP88sz5TXy24ObXH/JMqJZCpUHxYB6YPHARcVsDkwcuIm5rYPJAqJZCpUETny/NAxcRtzUweeAi4rYGJg+EailUGjTx5zjffv91njm/uK2ByQMXEbc1MHkgVEuh0qCJL90p1ILitgYmD4RqKVQapFB31VRR3NbA5IFQLYVKgxTqrpoqitsamDwQqqVQaZBC3VVTRXFbA5MHQrUUKg2a+KakSj6gJ25rYPLARcRtDUweCNVSqDTo95++jQfzkOSBi4jbGpg8cBFxWwOTB0K1FCoN8nOoO/cCZqdQaVA8lQcmD5zfm5eP47YGJs+c38RfM77/xijPhGopVBoUD+aByQPnN/FZ610T96KSX0IHZ1KotGbiW3z/+uPnPHN+cVvDk2fOL+5pYPJAqJlCpTUTX0Ct5FFR3NbAfLx6kWfOL25rYPJAqJlCpTXxVB6YNn5mpoYfpd1/JeO2BibPhJopVJoy8fneXR2HeBtVFPc0PHkm1Eyh0pR//v4znsoDk2fO7/PNu7itgckz5xf3NDx5JtRModKUeCQPT545v7ingXl/8TTPnNn07wlquBcwiEKlKfFUHpgafvDxrz9+jtsamDxzfnFPw5NnQuUUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKtVK//fjNh9fPPl1fAE3aX+D7yzxf+6yXQq3R9N+SLSKryOebd/kEYKUUanW0qcimsr/k8znAGinU6sSrTURaz4fXz/JRwOoo1OrES01ENpB8FLA6CrU68ToTkdbz6foiHwWsjkKtTrzURKT1/P7Tt/koYHUUanXipSYirefq+aN8FLA6CrU68VITkdaTzwHWSKFWJ15qItJ68jnAGinU6ny6vohXm4i0Gz8z0wyFWp3rV0/iBSci7ebNy8f5HGCNFGqN4gUnIu0mnwCslEKtUbzgRKTd5BOAlVKoNfp88y5ecyLSYj5evcgnACulUGv0y3dfxctORFpMvvxZL4VaqXjZiUiLydc+66VQKxUvOxFpMfnaZ70UaqXiZSciLSZf+6yXQq2U9yWJNJ+bX3/I1z7rpVArdfX8Ubz4RKSt5AufVVOo9YoXn4i0lXzVs2oKtV4fr17E609EWsn7i6f5qmfVFGq9POsr0nDyJc/aKdSqxUtQRFpJvt5ZO4VatQ+vn8WrUESaSL7eWTuFWrt4FYrI+uMHZpqkUGsXL0QRWX/ylU4DFGrt4oUoIutPvtJpgEKtnZdRRRrL9asn+UqnAQp1BeLlKCJrTr7GaYNCXYG//vg5XpEistrka5w2KNR1iFekiKwzPiCpYQp1HeJFKSLrTL66aYZCXYd4UYrICvPP33/mq5tmKNR18Lm+Ig0kX9q0RKGuRrw0RWRV8fC0eQp1TeIFKiLrSb6iaYxCXZN4gYrIepKvaBqjUNfk7fdfx2tURFaSfEXTGIW6MvEaFZE1JF/LtEehrky8TEWk+ny+eZevZdqjUNcnXqwiUnfyVUyTFOr6+GhfkXUlX8U0SaGuUrxeRaTWfLx6kS9hmqRQVylesiJSa/L1S6sU6ir9/tO38aoVkfry9vuv8/VLqxTqWv3z95/x2hWRmvLp+iJfuTRMoa6Vj8sXqTz5sqVtCnXFPt+8i1ewiFSTfM3SNoW6bvEKFpE68st3X+ULlrYp1HWLF7GIVBC/qW2bFOrqxUtZRJZOvk7ZAoW6en6ERqS25OuULVCoLYhXs4gsFz97ulkKtQWfri/iNS0iS+T3n77NVygboVAbES9rEVki+dpkOxRqO+KVLSLzJl+VbIpCbYd3J4ksm3xVsikKtSnx+haRueKTHFCoTXl/8TRe5SLy8PHOXi4VanvihS4iD598JbJBCrVB8VoXkYfM1fNH+TJkgxRqg/wWGpHZcvPrD/kaZJsUapviRS8iD5N89bFZCrVZ8boXkdLJ1x1bplCbFS99ESmazzfv8nXHlinUlv3z95/xDBCREvnrj5/zFcfGKdTGxWNAREokX2ugUNsXTwIRmZY3Lx/nCw0Uavv8FI1IwXy6vshXGVwq1I2IR4KIjE2+vuCWQt2KeCqIyPDkKwvuKNSt+Hj1Ip4NIjIk16+e5CsL7ijUDXn7/dfxhBCR8+IDe7mXQt0Wj1NFxiVfTRAo1M2J54SI3Jd8HUGmULconhYi0p18BcFJCnWLrp4/imeGiJxKvnygi0LdKG9QErk33ojEIAp1u37/6dt4fojIIftvOvNVAz0U6qbd/PpDPEVE5Evy9QL9FOrW+RVvIiF+NRvjKFR0qsj/RZsymkLlP+KhIrLJ7L+5zFcHnEmh8l/xaBHZXvJ1AedTqPyfeLqIbCn5ioBBFCr/Es8YkW0kXwswlEIliieNSOvJVwGMoFA5IZ43Iu0m//uHcRQqp8VTR6S5eE8vZSlUOsXjR6St5H/zMIVCpY/PfJAm49MbeAgKlXt8vnkXTyORNefT9UX+dw7TKVTu9/HqRTyTRNaZ61dP8r9wKEKhcpb9MRRPJpG15c3Lx/nfNpSiUDnX/jCK55PIeuJ1Ux6aQmWYeEqJrCH5XzIUp1AZLJ5VInUn/xuGh6BQGePD62fx0BKpL96CxJwUKiN5SVUqjx+PYWYKlfE8TpVq47Ep81OoTBVPMpGlk/+VwgwUKgX4NCWpJJ7mZUEKlWLi2SYyb66eP8r/LGE2CpWSfJi+LJX8rxFmplApLJ5zIg8cv9aUSihUHoSHqjJP8r89WIpC5aHoVHnQ+GxeaqNQeVjxFBQpkfwvDRanUHlwN7/+EI9DkbH5/adv878xqIFCZQ5Xzx/Fc1FkeN5fPM3/uqASCpX5/PLdV/GAFDkvHphSP4XKrDxUlaH5fPMu/0OCCilUluE9wHJvVCnrolBZzNvvv44nqMghH69e5H8zUDOFypKunj/yUFVCPDBlpRQqVfh0fRGPVdlePCpl1RQqFYnnq2wpb14+zv8kYEUUKtXxJPCm4jeY0gyFSo28trqR5L96WC+FStWuXz2JZ7CsP57dpUkKlRXwacDNxAce0TCFymp4EnjV8VopzVOorMwv332lWVcUv7WU7VCorFU8uaWyfL55d/X8Uf6Lg1YpVNZtf2TvHwPFs1yWiw9nYLMUKo3wxqXF8+H1s/z3AtuhUGnK/kyPx7w8fK5fPcl/F7A1CpVmfbx6EQ9+KRcfYQ+BQqVxv/34zf7oj20gk5O/1LBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVNiG0gk5O/yLBxCpVN+OW7r2IhyIS8/f7r/EWGjVOobMU/f/8Za0FGZf+VzF9eQKGyIbEZZFTyFxa4VKgAUIRCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAQoVAApQqABQgEIFgAIUKgAUoFABoACFCgAFKFQAKEChAkABChUAClCoAFCAQgWAAhQqABSgUAGgAIUKAAUoVAAoQKECQAEKFQAKUKgAUIBCBYACFCoAFKBQAaAAhQoABShUAChAoQJAAf8LH8jVZ7RzRcEAAAAASUVORK5CYII=>
[image3]: <data:image/png;base64,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>
[image4]: <data:image/png;base64,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DoZCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAKKFQAACqgUAEAqIBCBQCgAgoVAIAK/h+R6Iou/HhPewAAAABJRU5ErkJggg==>
[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAJwCAIAAACGccv0AAAnvElEQVR4Xu3dsY7cNts24P9UviNwv0BaNy5TvZVLF6kDpHcOwD4Auzfg2kXKVKlcpklrwL19APNPMshiwkfkakakRInXjatyOKRWu9G90mo0/+/08H8AwEL/L/4TAHArhQoAFShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBUoFABoAKFCgAVKFQAqEChAkAFChUAKlCoAFCBQgWAChQqAFSgUAGgAoUKABUoVACoQKECQAUKFQAqUKgAUIFCBYAKFCoAVKBQAaAChQoAFShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBUoFABoAKFCgAVKFQAqEChAkAFChUAKlCoAFCBQgWAChQqAFSgUAGgAoUKABUoVACoQKECQAUKFQAqUKgAUIFCBYAKFCoAVKBQAaAChQoAFShUAKhAoQJABX0X6o8/nN692YG45Tvy9cspl+/f/v4WxJdM+vzHna4n+fA+/a+//pwuNGfd8zwzRybO381fXt3wVd80+aTrSc5fbByQuPzI/fS/dAOArfVdqOejxi4St7x/N+XcrHGGJRNe53qSc2HExLWeXDcpqsLIJ/PpYzrPpLtzPcm5Ke/Lk792AO31Xajnc4VdJG555+5L+bzt7lxP0mGhXjJ5yltl8utJ7i7US+JWASvqu1AXHl9WS9zyni1JnG35tNeTTBZq+aL6ZKoX6jkvX6QTVpn8epLlP/DPn6UbBqxFodZI3PJuLdylhWu/d+d6kslCPRX38GRaFOo5f/2Zzrl88utJFn53Lpl5jRqoTaHWSNzybi1P7sLv3bmeJFeohZKYTKNCPeW/13fnepJaP/Bx84D2FGqNxC3vUyHJXS3lPR9nLkweRxbkCvWUn2cyNxXq9SXl868LhdueT5mZC5PHkQWF3Z6M/PA+HXAd9yjBFvou1MLhtavELe9TLpMXcs/VkkscXJg8jiwofMdzl1snM1l7ucS/0T5/lo65Tpy5MHkcWTC/UC8KiYOBxhRqjcQt79D5rCWXOPgilzjy1sE55e94HP+QWXdhoT4UO3XyoncucWTBrYX66WM67DFxMNCYQq2RuOUdymXy9PQi9z7gOLIwfxxZUP6Ox/EPmXWXF2ph/E2Tx5EFtxbqQ35dT36A1SnUGolb3qFcyu+wnMzkwTqXOLKg/B3/+iUd/5BZ96bOu7VQT1NfVC5xZMEdhZr7i2/uiwKa6btQ95K45R3KZbIdy6+aPFjnEkcWlAv1NHW5dTLjFGruJZN7AGhJodZI3PIO5bKvQo0XqCczWSe5TH45hfGnqS8qlziyINeOp/w8uZdM7gGgJYVaI3HLO5TLvgr1FCaczGSd5DL55TwUNyYOziWOLMi14yk/z9vX6chLJvcA0JJCrZG45R3KZXeFmlz1ncxkneQy+eU8FDcmDs4ljiy4o1BzL8l9UUAzCrVG4pZ3KJdyoX4OHx/2OfORarnEkQWFDntMctV3MuMUau6mpF9epSOBxhRqjcQt71Au5UKdL5c4sqDQYde5bovJjFOoucSRQGMKtUbilncolz0W6ulq2skMUqi//5YOe0wcDDSmUGskbnmHctlpoT5+TtlkBinUXCbfsAs0plBrJG55h3JpXaiFxEkmOyz3IPjCuv0UaiFxkjmFev5NIndn72PizEB7xy3UONvgcum/UHM1U1j3eIV6U+LMQHsHLdTJ4+ngctlFoU4+qv5ShJOZ/AHI5WCFGqcFVqFQh5HLLgo1N3/u3yd/AHI5TKHGx0gBKzpooeYOkSPLJSnUmZk/fyFxkskOu3w3f3mV/vvpn42fzICFOvklAytSqMPIZS+FetMSk+2SS+6nZXJjLomD70icZEmhvnyRzgas66CFWusy5pHk0rpQz/PnxEkmO2zXhRq/6sKXXyjUx1flPlT8rz/T2YB1KdRh5JLsq5mZP38cWTDZYY+FN3lr0mT6KdQ4sqBQqNfDcokTAis6aKHGqchlR4X6kF8liUIFVqdQh5FLUqjnY/q1XObPH0cWTHbYdeH9+nP6Xydz7ELNbVicEFiRQh1GLuXL47ksGVkwWRVJ4c3JsQv1IbPcp4/pMGBFCnUYuSjUwxTqKQwDVqRQh5HL7gp1zq1JChVYnUIdRi67K9SH/FqPGbZQP7xPRwJrUajDyGWPhfrkrUlVCrWQ+YPjyIL5hZp7N+opjATWolCHkcu5nOLgJ1+1ZGTBzEJ9yC93yeEL9aHSikA9CnUYuZQvEuayZGTB/EL9KfMU30tGLtTyNxRoRqEOo5A4+MlXLRlZML9QH/IrnhoX6uS7U3KJIwtuKtSbBgPtHbFQfYjVpN9/S3fUY+LgR7ksGVmwi0KdfAx9LnFkwa0dmUscCbR3xEKdPJhyroFcco0yWW+XxMG5xJEFkyvmNq9wa9Lkz0Auk/O/fZ0Oe0wcXJg8jixQqLBnRyzU86lYnIqH4v788YcbBp+mDtm5xJEFNxXqQ37RJYU6+cGrj8n9hTKXOLKgVqGWbzQD2jhioRaOvzm5j9M6mMJZ1yXnHjrvvclWSxInz+U8W9n1JJNLF76hufK7qVBvSpy2PHn8egtffq1C9VcP2MIRCzX36/nzZ6evX9LB5UzefrJr50NtlcSZ7871JLcWam7dRoU6Oe3Cya8nubVQCxe942CgsSMWajzXLBx35uRgtXprJp8hsHzax1xP0nOhlk/77s71JLcWamHd87l7HAy0dPRCnTxA35f4V8adujWTL1k+7WOuJ5n8fpULdfK3pRaFGiesMvn1JBUL9euXdCTQ2BEL9fLaWtc2kxzjF//CHb9JLuNj4px353qSOwp1cumKhXr+QXr+LJ0qujvXk9xRqB/epyMfEwcDLR20UP/6M/3HiplzeO1f+UlDlzx+pTFxwrtzPcl9hRpvTapSqOdJJt9yOunuXE9yR6EWlo4jgZaOWKgr5FzYcWv361yul5t7P/9zl+9hLm4DrEih3pu4tQAMTKEuSNxgAEalUJclbjMAQ+q4UJ8/S9urw8TNBmBIHRfqnNtQe0jccgDGo1AXZ/IdGgAMRqHWSHzYIQCDUaiVErcfgJF0XKiFp8Z0mLj9AIxEoVaKpwsBjG28Qr08YK96fLgHwNjGKNTCB5pW/EttnByAYXRcqLXOI+d8OEyV/PpzOi0Awzh6ocZpJ01+SPWt+f4tnRaAYRy6UN++TucsqNKpcVoAxnDoQo1zli1PnBOAMXRcqAsTJ3zS8sQ5ARiDQr2y/Jz45Yt0TgDGoFCvnOtwYd69SecEYAwHLdS7zxSXJ84JwAAOWqhxtpmWJ84JwAA6LtRNLP8zapwTgAEo1P96+zotyFsT5wRgAAr1v5Y/2jfOCcAAFGqwMOdKjnMCcHQKNViYm553CMBRKNRgYbwVFWBICjVYmN9/Syccx0//+/v3ictHuJ+dd4VfL4BhKNRgYc5FEufswZIPbI+zXZv5QT3xhVEu5b2aSxw5qZA4eFLu3Va3/j6Ry+OA3EK35pdX6b9c8uljukm3biEMTKEGC1M+9G+oRaH+9Wc68smUP+89l/JezSWOnFRIHDwp13PdFuqctSZNpvw9hWEo1GBhyof+DVUv1JknpjGFB0PmUt6rucSR0Y8/pK+6zsxbzHI9d7BCzT3sOo6EISnUYGHKh/4N1S3Ur1/SMTclTniRS3mv5hJHRk9WVHxJlJuk50L9/bf0Hy85/4YRN2zm5sHYFGqwMOVD/4YqFuryx198/5bOeZFLea/mEkdGTya+JMr1XM+F+vxZ+o+X/PVnulXlzSuMh8Eo1GBhyof+DVUs1CqZPBPKpbxXc4kjoycTXxLleq7nQp2z3LXcb1GT30cYkkINFqZ86N9QoVDj4LJcJk9WCpk/uLxXc4kjE+U/oF4SXxXleq56oebkUt5vub+C//IqHVlYIo6EUSnUYGHKh7AN1SrU3JnKKTNPYd14d2gu5b2aSxyZKGzbY+Krop0Wau6FkxfkJzPzpi0Yg0INFubWY+hqCuURBxcUEgeXX/L1y9yR5WLIJY6c+cLrzPmG7rdQc7cmJcM+fUwHXBInhIEp1GBhbj2GrqZ1oRaO3bm+OYWlcylMXnhVHDnzhdeJrR/lvsBbfxhyiSNnvrC83x7ytybNnD9OCAPrtVA///v4urvFOWdamF9/TifsROtCLZTH/KVzKX9Dc4kjZ74wSXxh4vNuCzX32uRWo1zibDCwXgt1eeKcMy1Mtx/fNr/VynIpfOG5B92dwtK5lIshlzjyyRdOXgKNL0wcr1BP/110MoUHdMCQFGqwMHHCTlQp1Nyzck7FQp1/H1Mu5WLIJY588oWTm1r40i52Xai550c+Dsj9PhSngrEp1GBh4oSdqFKok31zSaF1Cq9KRuZSLoZc4shrH96n40//vCTmyT+j7rpQcy9/fFD+ZJ58jD6MR6EGCxMn7IRCnfOqwr8XHLJQT/+uO5k4CQxPoQYLEyfshEKd86rCvxfsvVDfvk5feMlD/uEPcRIYnkINFiZO2AmF+uSrLh8OP5nJhwc92nuh5mbI/Xm1vDdgVMct1PgUnjlyb8ubnzhnJxTqtclzsktPTLZIeQOOWqi5xJcDRy7UW49lF7kLXDNz36LrUKhPvuTyn+64qfUAhTr5a0Qu8eXAkQt1/qHk2uSdn/NTKJXNFQq1kGSSQjUWvvbCq5KRuZS/m7nEkeWXzPyv0QEKdc7nBDwmvhzot1BzR6ibEqd9UqPPze6BQn3yJTP/a5T7cd1RoRYmSdLts8Bga70W6sJLr5fEaZ+0MHHCfijUJ18y879GxyjUmZdn4guBf/RaqMtvDjrd9X/+wsQJ+6FQn3zJ43+dvFBR+CTtYxRqYZ7HXG6EBqb0WqgPM/7ffjK3Hk1uui9jMnHOfijUR5O74vpxSJMXSArbcJhCnfxN4jrxJcC/Dl2opxv//1+eOGc/JlvkySSTFKpxR4U6WRtJ+U0mTnVxmEItPKv5kvgS4F8dF+r3b+n/zHckTluwMJ0/3bRQqHFwTqEad1Sok0m2fzJxqovDFGphqkvieOBfHRdq4Sg8P/MPKMsT5+yKQi2PnzMm94FlgxTq29fpYOBKx4X6UPx/e37m3OV/PrlcnjhtVxTqRW5jkmGTF0g+vE+HXRypUCevh18SBwNXBijUS+LkjwpHkPmZU9vbUqgXk015/sdk2OSzCU+ZOY9UqPO/WcB/DVOop39u47x+58PLF9PH1vsSN743CrUw+Dz/eSOv3fQAQoUK9F6oM99p3kPixvdGoZYHz0yc8EGhAn/ru1Af8keKrtL5/b0XCvUh/+D7+YlzPihU4G/dF2rFq7LtEje7Q7so1NyzNcrFkEscmWu++YlzFqZVqDCS7gv1IX+w6CSFJ9J1pUqhPuS/HVUKNddM5WLIZf7I+Zm8GpHbbIUKI1GoyxLvDu1W60ItvElx/tLzR17LZf7ImxKnVajAPgr1IX+82DxxU7t1X1dFuRQem57rm1NYuvDouzjtxU1fVy5x5EP+nrg4MvcFKlQYyU4KNXdo2za5t/n36abiKSgkDr7jJbnEkRe5v7JPdslkJkc+5KsljlSowG4K9SF/3NwqO7rYe1GrUAtPlYqDL3KZ/I0kl8k/XhbGx0dt5E5/C7U3mXhxW6ECeyrUh/xRY5PEzetcrUJ9yH8jYocVBp8y695U2DcNztVeHPkol5kzK1QYya4K9SF/4Fg5ccP6t0KhnsIRPPc2mNN/P390/vzXnV1+ZuT8aePIW1+iUIH9FepD/tixTnZ3pfdRoVCfTMWpHhO38NHyTF4fziWOfJT7Sp8/+8+wXKE+maTwcokblshFocKKdlioD8XznqaZPEzvRa4b5iTOtjC5z0FbvqmXxDlzPVG4Ofnsxx/S8Zckp54KFdhroT7kbzBpl+SkZHeWtFSc7bw3liROmFhyD9pkW+f+2vrLq3RkYjLJ9WqFCuy4UC9yJxB1s/cqvahbqBd3ZP5Z/n3P3Y3zXOQSR97xQoUK7L5QL379Of0/v1aePH3ZkRaF+vDUnUFJytdXo5u2ufzn7VziyDteqFCBgxTqtZsOwTHng/Ktd2buxfls/qf/fuTnfHG2aM6eL9zZW3b+nSn3h/PzKe+cSwjxi5r5pcWXxBe+fJH+15mSq9NxwEXcqkR8yeT8c5x3Zpxn5mbA2A5XqNfOR5PzUf78S3ruWHyuz/N/PY+547jDkyYzp/wAdujQhcq23r5O2/QSnQockUKlpdzN2K4fAoejUGkslzgSYM8UKu3F94DOf/MMwE4oVFaRdKo/owKHo1BZy3XifwXYOYXKih7vUYr/CWDnFCrrujwtMv47wM4pVACoQKECQAUKFQAqUKgAUIFCBYAKFCoAVKBQAaAChQoAFShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBUoFABoAKFCgAVKFQAqEChAkAFChUAKlCoAFCBQgWAChQqAFSgUAGgAoUKABUoVACoQKECQAUKFQAqUKgAUIFCBYAKFCoAVKBQAaAChQoAFShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBUoFABoAKFCgAVKFQAqEChAkAFChUAKlCoAFCBQgWAChQqAFSgUAGgAoUKABUoVACoQKECQAUKFQAqUKgAUIFCBdp7+eI0VJ4/S/cAA1CoQHuj5fMf6R5gAAoVaG+0KNQhKVSgvdGiUIekUIH2RotCHZJCBdobLQp1SAoVaG+0KNQhKVSgvdGiUIekUIH2RotCHZJCBdobLQp1SAoVaG+0KNQhKVSgvdGiUIekUIH2RotCHZJCBdobLQp1SAoVaG+0KNQhKVSgvdGiUIekUIH2RotCHZJCBdobLQp1SAoVaG+0KNQhKVSgvdGiUIekUIH2RotCHZJCBdobLQp1SAoVaG+0KNQhKVSgvdGiUIekUIH2RotCHZJCBdobLQp1SAoVaG+0KNQhKVSgvdGiUIekUIFVvHvT0O+/pZW2bRTqkBQqsHMvX6R9tnkU6pAUKrBn37+lZdZDFOqQFCqwWx2em16iUIekUIF96vPc9BKFOiSFCuxQt+emlyjUISlUYG86b9OTQh2UQgV2pecrvY9RqENSqMB+9H9ueolCHZJCBXZiF+emlyjUISlUYA/2cm56iUIdkkIFurevNj0p1EEpVKBvO7rS+xiFOiSFCh04n4FdHvJ+PhD/9Wd6dE5yHnAedh780/9OP/6QTnUwuzs3vUShDkmhwlrO/bfah6J8eH96/izdgN3Z47npJQp1SAoVWjqX6PnYum3OLX7ejLhtndvpueklCnVIChUa+PQxPcJ2kndv0k3t067b9KRQB6VQoYZzATz5t8/ecj5z7fNPsPu90vsYhTokhQrLdHsyOj9dnbbu/dz0EoU6JIUKt3v+LD2AHibxi13TAc5NL1GoQ1KocIu3r9ND5yETv/AVHOPc9BKFOiSFCvP8+nN60Dx81rw3+EhtelKog1KoUHQulcHz/Vu6T6o7zJXexyjUISlUyNv8LaT95NPHdOfUsvm5aYvvskIdkkKFwFlpIXXfabPtuenltwSFSiUKFf5Lnkytt9lsfm562QyFSiUKFf517gmZn4W3LHXSpg8KlWoUKvzf34+Sl/vy68/pzpyjhyu9jxQqlShUhtfieDpUbr0C3M+56UWLHwCFOiSFysCkYn55le7eSV2dm14oVCpRqAzpwM8O3DBPvmO1t3PTC4VKJQqVIUm7xL190WebPihUqlGojMSJ6WpJ9nyHV3ofKVQqUaiMRFbL9eXfbs9NLxQqlShUxiCb5FyrPZ+bXihUKlGoDOCvP9PjnQyS+MMQKVQqUagcnQyb+MMwSaFSiULluDb/051smPjzkKNQqUShclADfh64PCb+PBQoVCpRqBzR77+lBzgZJHPuQkooVCpRqBzOfm9B+vrl7wPxuzd/f5DL5Ge5XP79POA8bNu7Z7tN3GlPUqhUolA5lh3VzLn4z9X48kX6Jdzh0rIS98wcCpVKFCoH0nmb3vdJZ3cb7bp33AMzKVQqUagcRbdtesdf9eoaoVnjVz2fQqUShcoh9NamH96nW9iJc7sfLMt/X1GoVKJQ2b+u2vTt63TzOnTu+8MkfnW3UqhUolDZuX7u6X33Jt22zh3gbDV+UXdQqFSiUNmzHiph+SXHzbVolBUSv5D7tPjyFeqQFCq71cOzkOJW7dRP/0u/tM4Tv4S7KVQqUajs07YfFf71S7o9h9HVH6QnU/2SgEKlEoXKPm2Yc5fH7TmSH39Iv+SuEjd4IYVKJQqVvdnw3PTwVXqtw1qtfm56oVCpRKGyN1slbskIukrcvCpa/Io21O9e/EuhsiubfMTp7t4PU1cnD1qKGwadUajsx9vX6UG2db5/S7dhWBum0ZVeqE2hsh8rp9vHB26lxd8a5yRuCXRJobITK7+dw9/AJq18p9KB357EESlU9mDNi70u8z5pzZwrPG4AdEmhsgdrJq5OYuVbw+IGQJcUKt1bLbv4oJh+rPYg5cHvsmY/FCp9W/OPdnF1ylZLXBr6o1DpWIt33E/m5Yt0aWZa7SMK4tLQGYVKx9aJu5AWWifu+KV7CpWOrRBtWsU6ietCTxQqvVohv/6cLsrdVoiTVPqmUOnSOp93HddliRXigRt0TKHSnxXuRfrrz3RRqljhgVZxUeiDQqU/Dsq71jpxReiDQqU/rePTS5o6n/03jc/uplcKlc60fv6Ot5yuoPWbU91NRpcUKp1pmt9/S5ejkdaJK8LWFCo9aZ24Iu00jQu/9Eeh0pOm8UFgK2v93qe4ImxKodKTdnGxdxNfv6TfiIqJy8GmFCrdaJq4HOtoF4+NpDMKlT40/Zg2H3S6oQ/v029HxcTlYDsKlT60i4+n3tznP9JvSsXE5WAjCpUOvHyRHiUrJi7H+tolrgUbUah0oN2zBj3GoRPtEteCjShUOtAucS220ig+041uKFQ60CgeUNeVdg+VjGvBFhQqW2t0vdeJS4caxZuM6YNCZWuNEhdic+3eHBXXgtUpVDb1y6v0yFgrcS160CjPn6ULweoUKptqlCrvPT1PQmL585DbvSc1rgXrUqhsqlHiQrdq+tbYXSfuq1s1SlwI1qVQ2VSLVLm5t/Unpew3cV/dqtHDCONCsC6FynbOzdcicaE7KNRc4r66Q4ssvxwNyyhUttPiDTO13kGhUHOJ++oOLVLrWw/3Uqhsp0XiKvdRqLnEfXWHv/5Mp62SuBCsSKGykUZvmIkL3Ueh5hL31R2eP0unrRJvnmFTCpWNtMj5vCcudB+FmkvcV/dpkc9/pKvAihQqG2mRirelKNRc4r66T8+3pMFdFCobaZG4yt0Uai5xX92tReIqsBaFyhZavBPx08d0lSUUai5xX92txa1JcRVYi0JlCy1S94YUhZpL3Fd3a7GT4yqwFoXKFlokrrJEi2P9MRL31RLV88urdAlYi0JlCy0SV1lCoeYS99US1eNGX7ajUNlCi8RVllCoucR9tUSLxFVgFQqVLVTPh/fpEgsp1Fzivlqixae5xVVgFQqV1bV4Sk7Fd6BeKNRc4r5aosW7UeMqsAqFyurevUmPgMsTV1lIoeYS99VC1XP+3sVVoD2Fyup2cZVPoeYS99VC1XP+jS2uAu0pVFZXPS1u7FSoucR9tdDXL+kSC/P9W7oErEKhsrrq+fXndInlFGoucV8t1OKxWXEVaE+hsrrqqfuMpAuFmkvcVwu12NVxFWhPobK66olLLNfiKH+MxH21XPXEJaA9hcrqqicusZxCzSXuq+WqJy4B7SlU1tWiqOIqVZw3lUTcS1VUT1wC2lOorOuXV+mxb3niKuxL9VR/0AfMoFBZV/WnOnz9ki7B7lRPu5NpyFOorKt6obZ4Eyorqx6FyhYUKuuq/pgkj8U5gOrxU8EWFCrrUqhE1eOngi0oVNalUImqx08FW1CorEuhElWPnwq2oFBZl0Ilqh4/FWxBobIuhUpUPX4q2IJCZV0Klah6/FSwBYXKurwPlah6vA+VLShU1qVQiapHobIFhcq6PMuXqHpafEQuPEWhsq6f9vNpM6ymeuIS0J5CZXXVE5dgX6onLgHtKVRWVz1xiSok5vu3dC9VUT1xCWhPobK66olLLNfi0vQxEvfVQi12dVwF2lOorK563r5Ol1iuxVH+GIn7aqEP79MllieuAu0pVFZXPS3eOaNQc4n7aqHv39IlFqbRdWl4ikJlddUflnRqcJRXqLnEfbVQ9XhMEhtRqKyu+rMdTg2O8go1l7ivFqoeT3VgIwqV1bXoqrjKQi028hiJ+2qJly/S+ZcnrgKrUKhsoXo+vE+XWEih5hL31RJ//ZnOvzxxFViFQmULLRJXWUKh5hL31RItEleBVShUttAicZUlFGoucV8tUT0tbvmGeRQqW2iRuMoSCjWXuK+WqJ5fXqVLwFoUKltokbjKEgo1l7ivlqieuASsRaGyhRYPx/n0MV1lCYWaS9xXd/v6JZ18eeIqsBaFyhZ+/CE9DlZJXOhuCjWXuK/u1iJxFViLQmUjLfLyRbrK3RRqLnFf3efXn9OZqyQuBGtRqGykRb5+SVe5m0LNJe6r+7SIW3zZlEJlIy0eQHiqd7hXqLnEfXWfFvHQQTalUNlOi8RV7qNQc4n76g4tHpB0qrRtcC+FynZa5Nef01Xuo1BzifvqDo0SF4IVKVS20/NtKQo1l7iv7tAiP/6QrgLrUqhsqkWqnKQq1FzivrrVp4/pnFUSF4J1KVQ21ShxoVsp1FzivrpVo8SFYF0KlU01yvJPc1OoucR9dZPPf6QT1kpcC9alUNlUo6t/p8WH10bPcjpA4r66SaNUuc4PyyhUttYocSE21+7XlLgWrE6hsrXv39KDY5VUfGoStTTK77+lC8EWFCpbe/kiPT7WyvNn6VpsyOkpR6dQ6UC7xLXYSqO4FEE3FCodaJe4Fpto8dGnl3ieA91QqHSg3cXAk07tQ7vEtWAjCpU+tMvy96SyULv3np4UKh1RqPSh6Unq29fpcqzm99/Sb0fFxOVgOwqVbjRNXI51tMv3b+lasCmFSjcaffjMJW5d2UTTJzj6ntIZhUpPmubli3Q5mvrlVfotqJu4ImxKodKTRk9NekxckXaa5vMf6XKwNYVKZ5rGUXg1rRNXhK0pVDrz7k166Kybn/6Xrkh1rb+JPluGLilU+tM6nvHbVNN3QF0SF4UOKFT60/ovqSdH5JZaJ64IfVCodKl1PFG9Eb8MMTCFSpeavn/xMXFd7vb8Wbp7W8TlejqmUOnVCuc67m2paIW4rkDfFCq9WueMR6dW0fq23kviutAThUrH1olHwi60Tpye0j2FSt/WiacS3q3pE5ivE5eGzihU+rbOhd9L4uqUrZa4NPRHodK91fLpY7o0BU0/Nvw6796kS0OXFCrda/2hJdf56890dSZ9/ZLuunaJq0OXFCp7sGannhzBn7JmfOgp+6FQ2Yk1T4lOHiCQ8fJFuqOa5vff0g2AjilU9mPl+JNq4q8/013UOnEboGMKlf1Y+cLvJXEzBrTmvdaPcbGXvVGo7Mr6J0ke+/Cw+rWBcz68T7cBuqdQ2ZutErdkBJvEh8CzTwqVvdnk8uMlQ12EXPn+o+vEjYE9UKjs04Y5fK1uWKUnbcqOKVR2a8Mc+EHtK3xqXiFxe2A/FCq7te2h/3S4P/Wt9pj7XDymip1TqOzZ29fpQXn9fP4j3ardWfmhGZM52G8nDEmhsnOd5Fztcdv69+F9+oVsEh/zziEoVPZv/TenFrKLN1B++phu9obxRCqOQqFyCF116qnXknj+7O+n43YVfzflQBQqR9Fhvn/7+3GJcVPXt/kNR7nETYXdUqgcyOb3/Zaz5gdln09GeztrT+LclMNRqBzLLvL1S5Ny/fGHv6ft/LeKS3wuG0ekUDmczs/Myvn8x9+lePbT//7zTpLzGeflXy7/9Txsv+nzD8ywmELliLq6i1Wu4x0yHJdC5aCkw/gsPA5NoXJcG34ujcTEbxAci0Ll0N69SQ/rsknitwYOR6EygF3fwrP3uAWJYShUxrCLN5McLwf+nDsIFCrDcOvvytnpBwbAvRQqg5EV4m5ehqRQGU9vD4g/WHbxeTvQgEJlVP6qWj1OTBmbQmVgOrVirh+UCENSqIztl1dpMcgd0aagUOFvb1+nDSEzo0rhXwoV/iW3Ju5DGJhChf/yh9Un4w2mMEWhQvDjD2mFyCXn3zaeP0t3F/APhQp5Hq70mHdv0p0D/JdChaLz2ergF4E9jxfmUagwz5iJ+wHIUKhwixHet+qBR3AXhQp3OeR1YFUKCyhUWOYAD4X49ef0iwJup1ChhufP9vchNp8+pl8FsIBChap+/KH3N9ucN897SaEBhQotnfv1w/u00lbOuzcaFFagUGEt53I9d9tff6aFVz1fv3gOA6xPocJGzp3XKNoUtqBQYSMKFY5FocJGFCoci0KFjShUOBaFChtRqHAsChU2olDhWBQqbEShwrEoVNiIQoVjUaiwEYUKx6JQYSMKFY5FocJGFCoci0KFjShUOBaFChtRqHAsChU2olDhWBQqbEShwrEoVNiIQoVjUaiwEYUKx6JQYSMKFY5FocJGFCoci0KFjShUOBaFChtRqHAsChU2olDhWBQqbEShwrEoVNiIQoVjUaiwEYUKx6JQYSMKFY5FocJGFCoci0KFjShUOBaFChtRqHAsChU2olDhWBQq5Mlk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqlMhk4o4CFCqUyGTijgIUKpTIZOKOAhQqbObdm7SoauU8c1wOaEyhwkYUKhyLQoWNKFQ4FoUKG1GocCwKFTaiUOFYFCpsRKHCsShU2IhChWNRqLARhQrHolBhIwoVjkWhwkYUKhyLQoWNKFQ4FoUKG1GocCwKFTaiUOFYFCpsRKHCsShU2IhChWNRqLARhQrHolBhIwoVjkWhwkYUKhyLQoWNKFQ4FoUKG1GocCwKFTaiUOFYFCpsRKHCsShU2IhChWNRqLARhQrHolBhIwoVjkWhwkYUKhyLQoWNKFQ4FoUKG1GocCwKFTaiUOFYFCpsRKHCsShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBUoFABoAKFCgAVKFQAqEChAkAFChUAKlCoAFCBQgWAChQqAFSgUAGgAoUKABUoVACoQKECQAUKFQAqUKgAUIFCBYAKFCoAVKBQAaAChQoAFShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBUoFABoAKFCgAVKFQAqEChAkAFChUAKlCoAFCBQgWAChQqAFSgUAGgAoUKABUoVACoQKECQAUKFQAqUKgAUIFCBYAKFCoAVKBQAaAChQoAFShUAKhAoQJABQoVACpQqABQgUIFgAoUKgBU8P8Bcljz4UnORVYAAAAASUVORK5CYII=>
[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAJwCAIAAACGccv0AAA7mklEQVR4Xu3dT67jRLjG4buarIANsILeQK+AFbABVsAK2AAr4A4YMDgTBgxAYsCgBd1CLdSiQYBoodzIlnN93reqXHbKdpX9e/VMuvNVxU586ssfJ/mfy/++AgAAD/of/y8AADAXDRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFHDYhvry21+/ePX+Oidfvv7zNsqnAgBg0tEa6q0pap9clKd3//jkh/TDH//qzg/55e8PXu9ePL253VxBXpzgwzP5VM5H9T778Z0XB8nAz3/63WvSQ3pelsPnSUz16fe/SeXtPvKyBTMnhqQH3h7devECj094u3Ey9+Xudl/ffPzNa98vYOwgDTXRFR6P/AUeg+5kMreHKT7D3e1pvQ4Y4sUJOjg7PpVIbOE1Y3hPh12vH339s5elh1yzr07oLF28LFb8FG91WtrFyyaH9Im9xnPbAC1dlMcnlEdCenF2fB+B5hvq+w//6ZG+Tvyq26X7lhefp5doV16coIOz41OJ9OsWXh+kwzKeweuALl6WQ2fp4mVrFyeG9Ik99lrc/ySPT1iqoV6TD1NwTg031I+/ea0H+Mr56u1fvhnN0b2aE5/t0kJD1QHP4/VBOqyLlz04JEZn6eJlRYonj3Md8Dxef3mg/0ken7BgQ73GH0DgnFptqJs9MfUk3o6q3+JlqM8n3731OVtvqF+8eu9DnA7rkn7VV6u7eFmOWxvQia7X2BvAWtfFyy7du61aF3/Ztjd5rp8PuTx84N3z+IRlG2of31+cU5MNVQ/nzdPuu6q6J/Pjc7beUK8ZM8QmSb/qq9VdvCxH8EaOPZXUui5edom8GO5lY1pt8SGXB/qf5PEJ12ioP/zxr+8yTqi9hqrH8k5psafqPowiT0oSq5W/xhVc6/v4NiTo4CFeOUuwZ0h8lNMxQxInf2ppFy/LpBN18bKVKtNDxvEhl+5U8Ntx4nTwkFuL8uLxURo7RHPOvh7T8UN8nvSrYj4zTqixhqpH8a5p7rVf3YEht5XCi2ML1tXWjsSy6NMm6OAhXjmLTheKj3I6Zkjw1ksM8bJMOlEXL4vdHcHGr0VdvGxyyDjpl8EzZ5s83yd2fHojTNPxQ4LzBF8h7+PFOKGWGmr6EeIu8Y2sVvBNuD5e3NO6IVIWW8GvVpmmg4d45Sw6XSg+yumYUbw4McTLMulEXbws9ow82CG0qIuX3SU6yj3BK4rRwUPqbKiJ+sx34nFszTTUT757q4dwBWnovRPd9CGJXdDSIVJWc0O9PVvS6ULxgU7HPI/Xx4Z4WaZgC/EyrRglpzjWSGL1wfjAGB05pNqGuuCBKc6jmYaqB281mfUC1450u4fEFo5L/CUBKau5oSaWv3Fip8uO6Zjn8frYEC/LFNyX8duKPa0YRSpfPL3RitCEmZOP4wNjdOSQahtqYohX4mzaaKh65FYW3+AK6UYPSSygsTVLympuqDpXl+ADBR+bM9U9wZPUtKiLl2UKPtv2dV8rRpHKYIf2682cfJz8R5k6cggNFS1qoKEG/+yrip/4WiHd6CEnbKjBT1L62Jypxskc4mX5dC5rPIn74mqn0QXvX7/SMa3uNkD/K9mNJifsQ0NFixpoqHrYVhnf7NroFg85YUMNbrCPzZlqHH9aphVdfOZ8OleXcUHsjKQ+0iT04i5+pekhwce76Y/npifsQ0NFi2ioZeKbXRvd4iFna6j9p1z0fzPeRtUBoeQM8Znz6VxdJgvGmSz2K7273URa3dXrf3Xx4UE6bAgNFS2qvaF+9fYvPWyrTPAttKroFg85W0PtX5/X/814UqUDQskZ4jPn07m6TBaMM1nsV3p3u4m0moY6ilfibGpvqHrMPpbbH8n9baRbGwguEIvjG18V3dwhB26owVcj++830P/t4jOMaXUoj7+mmqZzdRm/1CwX+XPKydn8Sifrl53klZjzWnFDjS0akxuMM6i6oabfEJqVRNsInqKyID5zVXRzhyRumUzVNtTEQq//28VnGNPqSCaH+Mz5dK4u918s8DvCh4wfUMpF16muoNXDh5iDf0E+PEiHDUlvyWW/hqp1Q4K/G4Gzqbqh6jG7NJNn4cYedc7K5Jtw+9LNHXLghqoTdZm8KEarIxnfnnpZF585X7CL3L+jxx+AXmwb7n0i+PQ91kUukXu5rw9elNlgdNiQOhtq4ouivBgndPyGGvwKUxf7+5wVn7Yeuq1D6m+oifgkkxP2F92eWukFi2YLJj3EZ84XW9D7S/V/Qw21/8/g/19DJyrfBR903i/VC5JfcTymw4YsbqiJ+CSX+AaMG+rtCJ+8Op8ZJ3Twhpr5V13q6nzOeui2DjlqQw32nvvvnQWfn6VvCq3uEnxV+X6Gml7QxWfOF/xuh2ukR/Y9Kfi01Yv7+DXeaWmXzEsTdMyQ3RvqrASfzuKE6m2ovhAsiE+boIPnx+esh27rkHQXyVFnQ9XSLuNvNtDLpk701eouif9PX7SYTtcleFF/z378zWv5/2BxH7+6nOudvDRBxwxpqKFmvriNM6i3oephuyg+bYIOnh+fsx66rUNO1VBnFWROGHySmh7yCJ2uS/Ci2JDgf/bxq+vFfpriXhB8+JvzWTIdM6SVhtrcbzhiVTTUktfoc9ZDt3UIDXUcn2ey3p8CXocz1PR/u/jMs+h0XYIXxYYE//Oa7GGx7nUvCB4DiQnvdMyQybGxTUrEJ7nENyAnmedn4DwqbajBv8+5ub9hlin4vtqs+Jz10G0dctqGGjzLJvHynZZ2SUyVHrJY8KtOLqG3V+9Dgv8v/3lNPqHU0iGTNT5V5sxNNFSfDSdXaUMNfrJtbua2ikRjyIzPWQ/d1iFzbyWXuN28OEEHD7nNH+OTpGcbFwQfPyXWcS3t0l/kzezafVhL/6uLzzxL8GSrS+h7Ae9D5P/7xin/eU2e4qulXeS20ou7+FQ5M19tchdrqLeb3Y+TxNGi44eM59HLhvhsOLlKG6oeuYvi007SKWam5jdUdFuHxBaafKVWHB08xCsnBbvO1abSi7v4bDnFekE8PvNcOmP32qO/lRurv1UGHwH4FcVm6CNHjl7cJfGsNzHq+kBDnXvCrY4fMp7Hb9s+c68Lh0dDLXm9jzen9ei2Dnl8mytsqMGPmfpJvFrRxWfLKY6tuR6feS6dsetb8j/jnfXeEzzJyK8ocY1Xq9eLu0z2RR0wZHKg71SfuU1Oxw8Zz+M37z0+Ic6Mhlryeh9vTuvRbR3y+DZX2FB1ii6+1GpFF58tpzh4alIwPvNcOmN3uoD8z3hn/dXg4MvRfkW9F09vtLTL5Fb18QlzRlXVUBNlPiHOjIZa8nonX+DakW7rkERDja1ZUtZKQ11cllkcPDXJ4zPPpTOGMndI4gy+zMMg+KrA1cqEVg+hoaJFh22o/vpeDp1lZub+MW9Jt3XI8RpqYntyEvsshNZ1GRcE35j0+Mxz+fNRjwzRiy2Jx4JaOjM+Yc7ktTXU2GmSiTO5cEKHbaiTf5BnozfQkOM11NhTpczEjhyt65JTI/GZ50rc4PfIEL3Y4teSPzYdnzBn8ti9cBc7OFdqqLHKZQ/ccVSHbaj+93ByegMNOV5D1fHz43PGppWanFOTfOYFdNLn8VU+dlfe41fRi72Bmp/EAXaJ70grDfUav+lwQjTUs9AbaEhivYutWVJGQ73LOTXJZ15AJ30eP/j9vCSJX0Uv9lJnftI/nqjVQ2ioaNFhG2qiT5yT3kBDEjdUbM2SsqoaamJj8hP8PLEWdfGyyVOTfMgCOunzeP2yIZOjMuPTTs5fYUONvfzgrwfgtGpsqEXWxESfOCe9gYb4wnEXW7OkLHF/+ZwJOniIVybETti57UuQ1nW5/2T3mBZ18bLJU5N8yAI66fN4/bIhsVG31uK35E3swYRPm57/WmVDTTzL92lxTjTUs9AbaEjiJ2O1dIiUJe4vnzNBBw/xygQdPMQr59ZrRRcvu0ydFeX1C+ikz+P1y4bERs39xuPEH6OWDqmwoSaKEzuIU6GhnkXs2cN15mJ6tfrE/eVzJujgIV6ZoIOHeGUvti57pVZ08bLL1JNUr19AJ30er182JDbKy9L1ibdRtXRIWw319hDKi3FCNTbU4PeizQ0NVSS+Pi34ycv8NplfmaaDh3hlgg4e4pW92MHmlVrRxcsSxX28eAGd9Hm8Pj0k8a0OWtrFy9L11/gQrRtSZ0MNfsNUHy/GCdXYUD8P/QzI3Pi00NtoFKlMdF9/f7Hphhob4k+qtKKLz9Zb8HrALOm/Ea+/JDcp9ugz1j+88i7W57yyp3VD6myoiXqvxAnRUE9k8oa9LaC3fhk7m7GPT5toqOMzVoLG8+jgIT5K3E/KjX1qJfEMLHG9OWU+Wy/xqq8XL5C4zWM7m7j3vbindUO88i525o5X9rRuiBwb7inSUG+PG/wIGZNHhDp+CA0VC9BQzyXxNCUnwS+oSyzukxnPo5dl5/4EK7bIBl/TnrzenDKf7S52apJXLqPzDgl+5ic9xCuX1SdGeVmi+PpAQ52MzKwXD5nbUP0lDZwQDfV09JaaE5/tUlND1QuG+DaPZb6wqRd38dnuYk9SvXIZnXeIVy4bEtv+yRNwdECX2Hfeat2Q5hrqNXIz4lRoqKcTe+Y0mdhj8NYbamz7pUwv7uKzPTgkn847xCvTQ2Kfm4r9GcY6zZ0O6BIbpXVDqm2osde0r8lbHidBQz0pvb2Sia25vVhDysniTRqnb6ixN1DTG5+46gU1IvgCu5ctE+soXnkXfCwV6xxaN8QrHxmoRUOqbaiJIbFHnDgPGup5xV7qlEwuE5U01Nhhk1gZ01d9ey4yWeNTjQV7vJctE9zf2BlJiSGxU3y1bohXPjJQi4a02FCvkX3EeZyuod7WuNi303luzzCCp+Ecz21Vvd3sd+mzeAAA7kQN9ZEnUukH/gAAnKWh6sWLcpJnqwCABY7fUPWCh5P4ZnAAwGkdvKHq/xbK5EfxAABnc+SGqv9VNDkfxgAAnMdhG2rwI4BlQ08FANwdtqFuE//pFQDAOdFQH03sS0oBAKdCQy0Q3wUAwNnQUAuEN1MBADTUMvG9AACcCg21TCa/QR4AcGw01GLxHQEAnAcNtVj4SkIAODMaasn4vgAAToKGWjK+LwCAkzhRQ/VvNfrku7da9Fh8XwAAJ3GKhvrL3x/8Wu5ePL3RAUvjPRsAcBLHb6g55wr98Me/OmxpfHIAwBkcvKH65DG3J5c6eFF8ZgDAGRy5ob54euOTJ+j4RXn57a8+MwDg8A7bUBf8CIxOsShP7/7xmQEAh3fYhurTTuJVXwDAYjTU/3d7UquzLIrPDAA4PBrqMzrLovi0AIDDo6E+o7Msik8LADg8GuozOsuicKIvAJwQDfWZp3f/6ETzc9t+nxkH88l3b2939O2A6X36/W9eAyTcjp8vX/95P4Ru/+SxeOtoqM+craF+/M1r3foh+R1CBk7+1vpt1ZAh18iNpkXJfPX2rw3Wo8lTwfNvN6ETDbntlxcHycD3H/7zmvSQPpllfXJq8hM8DO4Sf56Jj6tp6aKMN0wvG+JXHXS7Q3Wk5bMf3/lAp8MytkEHdPEyLENDfabIVSf+tmuTWKGu2behDpv6EPBKDXWcnF4y1y9/f9CriSfnCy/HbguoTjGK1wfpsIx3H3RAl8yyPjk1+QkeBplX4fU5ozLzeENd8CGCH/741+cZ0wFT31seHHKd2nLko6E+U+SqG2qouunP4/VBOmzqr3qDhton3ddnWXBgzHqqmv42aa8P0mFdvGzBEK0YJacmP8HDIPMqvD5nVGYebKiLf4EjfRRpdRcve3AI8tFQnyly1del17493e7n8fogHdbl429ee2Vvs4Z6LdRTb893dd68+FQxOvJ5Mp/v6rAu6RcPtbpLZlmfnJr8BA+DzKvw+pxRmXmwoWrpnCRebtHSIV6ZHuJlWIaG+kxwrV8Qn7lCk4+a04+O73RYl8QqELyRgyupFi2KTztL+sXYdPJfq9CRz5M5jw4b4pXpIZllfXJq8hM8DDKvwutzRmXmkYa6+AHZPbFHVFo3xCvTQ7wMy9BQnwmu9QviM1do8vyaybdwejpsiFf2gjdycCXVokWZPEkqTaebGZ/QBW8QiY9yOmaIV6aHZJb1yanJT/Aw6E0+/ov9GIbWLcrihpo4729WfOa5W5IY4mVYhob6TM7SlhOfuUK60aH4KKdjhsRe9Q3eyMGVVIuG+Lk26WPGZ86ncw2Rp++3tq0VXdJvJ/fSb6D28VFOxwwJ3raJIZllfbw4c6xXpqVPoLtmP4/vJQ4YLxY6YIhXJoqvofrEkeDFcydPDPEyLENDfSa41s/NrD/sHel2h+KjnI4ZEnvVN3gjBxd9LRriDfWSXIwWP0lNPL3w4tgre14pdEAoPsrpmFG8ODEks6yPF2eO9co0HR+Kj4pJLDJeLHTAEK9MFMc+DaV1Q4Kv+mrRKF6cGOJlWKbGhno7dPQOnx+fNkdwrZ+bJhrq5AtofXyg0zGjBFeB4I38eENN1F/zdsTFPjIY3K9LZANiL0WmR0l8lNMxo8QeUmhdl8yyPl6cOdYr03R8KD4qZpuGmnhW7cXpya+hIVrxPF4fG+JlWKbGhhpccOfGp81R5KqbaKiTb6D28YFOxzyP1wdv5CINNdb/rqHNyBFbEL2yp3Vdgrs2OUoSe/08fx6vjw3JLOvjxZljvTIheMx4YgeG26ahasUoXtybtWFa8TxeHxviZViGhvpMkaueXEBroBsdSc4KpWOex+uDN3LwRtOiIbGtSry24cU5dJYhXpmon3yApQNCuT0A8oGz5vH62JDMsj5enDnWKxNib1FLYk/E3ay+JXTAkPzKxCER/Ovo48Va8TxeHxviZVimxoaaeOMqPz5tjsTRnJ9gb6iNbnQkOSf66pjn8c/eBG/k4I2mRUNiDTUxxCtz6CxDZr3ke01ee/DWCD4z9rFCBzxPsNloUZfMsj5enDnWKxN0cDw+Nmjfhho82nuJL1Tyw14rLD6/VnTxMixTY0O9RO71WfE5cwRXt7nx475CutFd1ljHrzZD8EYOLjFaNCRxC2vpEK/MEbxBrvFzd8c1wQbmgi9TB5d7Hyt0gCVzSGZZHy/OHOuVCTo4Hh8bFLyF+3ix0AFD8iuDR/vkKD/stcLi7xRoRRffBixz2IY6eSZIUOLPLD8+bYV0o7tuGnzJ1MdOTiWR5aOhhpr4VgcvXkbn7RL8/8lDWgdY/HGAVnSZNbMXZ471ypjgAXPtTiPX/8qeNvGX7sVCBwzJrwwe7QtGaUUoOUN8G7DMYRtqYs1NSPyZ5cenrZBu9PDnqv+bcUvqgFDG9cH10ReLxMyJTdLSIV6ZSScakvNieA6dd3iDTf83421UHRBKzpBZM3tx5livjAm+gXq7/YP/78ODEn/pXix0wJD8yuDRvmCUVoQifyx6cRffBixDQ30m9hLfrPi0tQk+8epfHdL/jX9g7k4HhDK+O47RUK/ZL+omBE8X6L99V/+3i88wptWhSFfWi7vMmtmLM8d6ZYyO7PJ59+uh+r/Z056noV6fb5he1sW3AcsctqH6wZdDZ1kUn7Y2usVdJi+K0epI7vXBdTB4f2nRkEoa6vXhnhp8ANdfpP/bxWcY0+pIJofMmtmLM8d6ZYyO7BK7aPLxX4+GOo5vA5Y5bEPN/LsSOsv8xL4eqCq60V0mL4rR6kju9W011ODWjvPIa786V5fJi2K0OpLJIbNm9uLMsV4ZoyO7TF6UdqqGOj4pXS/r4tuAZQ7bUK+LjhKdYn7Sv5ZVg+B5+fcPxukFXXySMa2O5P4QJ9iifLFIzLxlQ7359PvfdDqLj8qhs3SZvChGqyMZP+bTy7rMmtmLM8d6ZYyO7DJ5UdqBG2r6XC29oItvA5aptKH+8vcHvc/nx6edpFPMT5Ef4FxVcCm5/63qBV18kjGt7hK8B/v65hrqJflFwffMveuDb6Beh01NvBoco9Vdgnd3ekjmzH28OHOsVwYFH//dT1cOfugo544I3ix9vFjogCH5lcGjfcEoreiS/vvSC7r4NmCZShtq4nDPj0+bFvzTnRuftjbBVnf/SEZwHU+vUFrdJXhj9l/ykP6Dn5z5ukdDvcRnHsdHJcS+/bG/NPi0OP36h1Z3Cf7/3BcktGIUL84c65VBwaXgfrQEP+gVPJZypu3jxUIHDMmvTG+hVg/xUVrRJfj3dR02T/+3i28Dlqm0oV4id/ys+Hf0pAXPwp8bn7Y2usVd7pcG/xoT35SWmFD/q0vsKnyxiM1w3amhXvKepwZ3JEhHDkkX+DyT9fpfXdJDcmbu48WZY70ySId1mVUQdOyGGnzQnBji24BljtxQ554fpOPn58FzPrehG91lVkHmhLH3ctptqJf4/ONkHgY6rMv4ZDq9rIvPM1kffKSYHpIzcx8vzhzrlUE6rMusgqBjN9Tg60P9cP3fLr4NWKbehhp7QWxWfNoEHTw/PmeFdKO7zCrIn1D/t3v3q+mGeom8zCjJ6ak6psv465D0si4+T069/m+XxP/nzNzHizPHeqVLv82cmD/9JsXl6A31Enk1JTbEtwHL1NtQL5H7flZ8zgQdPD8+Z4V0o7tMFviXgqbr+4uCLz213lAveW+3T77joAO6jAuC72cn3kbV0i79RcGHp7G9yJy5jxdnjvVKF2x78sqTXtwleDhNztzHi4UOGJJfmd48rR7io7Siy/2vQy/oHufpf3XxbcAyB2+o/uWlMcFzQObGp61N7NnVuCa4jvsf852WdukvCi7ZwS4bnF+LhuzeUC+R11ElPmpMq7uMC4JfaJX42KuWdklcGnxN/hrabK0YxYszx3qlC25hzpc9Tb7dc86GGotvA5Y5eEO9JheguxdPb3TY/ORc0e6CK5SccxR8BnmN/9VpXZf0pR5fLBJja2ioPb0aiw/pxfpxzvw+W06xXhBP5sx9vDhzrFc6HdNFXs4NPj67Ts1/hoYau2U8vg1YpuqGGlt05mbyDS0dsCiJF0XroRvdxV+c1IouPltOcbCFe3yxiM18ramhBp+Cj+O3bU/ruvjZ1FrRxWfLKc7/a8qcuY8XZ471SqdjukhNrDX6bDmjrlMDL5GtuoYGasWQ4NG+YJRWdLn/dUwenPf4NmCZqhvqJXLELEuw4SX+rmZl8iWmSuh2d8ksC96AseLJAokvFomB9TTUXrpXBU+Q0aIuvl9a0SV4W8WKJws8mTP38eLMsV7pdEwXqYm1DZ9tLPGH78VCBwzJr4zdg3NHaUWX8VEUPDXJ49uAZWpvqInjflluTwJuc95kHmqZmfytyhrE3kC9/QUKregS+/kwresyLsh56ckXi9jM11DjmRzilWXp9Y0SfC9Ai7r4HRE8SmNnBmhdl3FB8NQkT+bMfbw4c6xXOh3TxW8lrejis40lFhYvFjpgSH5l8GhfMEorushfh14cim8Dlqm9oV7yDojd45tdId3o+fE5Y9Pm1Izji0Vi1I4N9XbV468aH9OrHEUq089oc+LXHtuAnBpJ5sx9vDhzrFeKzPYfS/CIujtPQw2eYyjxbcAyDTTUzDfhdkzTr/fOis8Zm1Zqgs+0xvHFIjbz1ZaMnCFeme/F05vx4u7vdPby12i9eH782mPTSk1iI+/JnLmPF2eO9crMgZlJ/1UmbgcvFjpgSH5l8GhfMEoruvhfh1ZYfBuwTAMNNfYeST0JvklWId3u+fE5Y9NKzeSd6ItFbOZraMmYHOKVOXSWLrGGGqu/2rXrxfPjVx2bNrNsnFlDvDhzrFdmDsyPz3lHQx3HtwHLNNBQL4U+1rJSYi8A1ma9D9pqUZfMsnt8sUgM8SWjF/tinWtoe3LEnlh7ZU/rhmSW5cevOjZtZtk4s4Z4ceZYr8wcmB+f867FhuqHvVZ08bLYYXyPbwOWaaOhXvJObNklvql1ynkrZTI+7SXyV+1l6XswuMRo0RBfMnqx81Ouoe3JEfx1sGt8Nq0bklmWn+DDOC3q4mWT7+D6EK0YxYszx3rlWPBLLeYm9pmly94NNfFBvlnHsFZ08b+OydeHfGYs00xDvUSOnn3jG1kt3fQhXpmoD57oq0VdvCxW2adIQ02cxuLFOWKrW7CfXeIbPK6JrW4+W2LO4BuEWtTFy2KV98yq9+LMsV75yCitG+KVvX0bavDu683aMK3oEvzrSD+e9nos01JDjX3qY68k3kurkG79EK+cW68VXbzsknzpqUhD1bpRvDiTTtQltiBq3ZBxTWzF9Nl6sZPyvFIrunjZJb4NfbxeK0bx4syxXvnIqNjrH17ZS9wCXix0wBCvTBzwXtyL7cg1NEQrumz51wHRUkO9ZLxatWV882qmWz/EK3trrOOxJ2fXlRtq8JOgmXSuIV6ZWRxbMX22Xuxpt1dqRRcvSxT3ebA4c6xXTo5KPISNNUivTNdf40PudMAQr0ycuODF6cmDx7AWdZn713GNbwzmaqyhXpIP+raMb1jldAe6xL4i4BJfC7xSK7p4WaL4WqKhatEoXpxP5xriT1ITj/ZyJvSr7sUehfjLzlrRxSdMFPd5sDhzrFfexd5ADd7vd1rdxct62zTURPE1VJ84+9KLY5PHbqXYI7lrZHIs0F5DvVTQU32TKhd7LzDYxu60uov/fJhWdPHZerG/6uCWaNGQ8ZJx6yuxOft455sl0Savo2/Iij2h7zOeUC/rEnz+kR7iT9e0oovP1kvslxdrxShenDnWK+9if+BeOabVXbyst1lDjZ3XdrWHs4nKa2RyLeoSa6ixR2bXyORYoMmG2tODYpMkntLVrOAKdbVRenEXny1dP6uhzopPO5fOODPjqWLruD/dzNmAnDKfLV1/DQ3RilG8OHOsVz4yJDbKH//1YnfEdepaLpErusYHat38+IOnxMyxhnqJn5rklVim4YZ6iRxP6yX2x1k/3ZMhXrlglF7cxWe7Cz6hXKmhFvnOjcRD+8nIedGxJ7J+pWOZj4f04i4+212sqXilVozixZljvfKRIbFRsaf+sX2/Tl3LJXJF1/jAxMejM+NzJrYk0VBjQ7wMy7TdUC/xFap4/KobojszxCvHVlrHg/1ppYbqcy4Te1cvHX+1WSuG+DWOxVb/nMl9tgVDtGIUL84c65WPDJk7KnaTXiP1YzpgiFdODslJ7FeeYtPSUHfUfEPtPf4YMBZfE5sTewM19jrS5EAp04u7+GzpIcUbapHnpmOJJTiY4LsDWjTEK3MGLqgRwQcKXqYVo3hx5livfGTIJf7Y2isvyXvTi4UOGOKVY+m3SGPxeca0uku6oQZHeQ2WOUhD7ZX9oGri20zaEvtLznkFW8d0WVAj/FXfgg01+O0TRQSfWwcTvG1jx+fkI5tL5KaQHw3Ui7v4VJMz59Tc48WZY72yF3sYN3krxT5fFGww2zfUS/wtzGCCD8iEjukS3N/0KK/BModqqGO3xWvW4Xvt3m4JroOte2m/H9nzSuejbuQ1KC/ImTw9Z7AmZvsfo30ZWfTTvdy3vJfzZNpH+Y57wcv5d0RwiNckijPHemXvtlNe/LLcrdS7HW9e2fNi4UMyB97d1pnY8+n0ISR8G15m3FA+xGuwzGEbquj/fj7vflr87mXkjw0AgLnO0lABAFgVDRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqirkS0lq+ePXej2RgGRoqynh694+uVYS0ED+YgWVoqChDVylCGokfzMAyNFSUoasUIY3ED2ZgGRoqyuAlX9Jo/GAGlqGhoozPfnynCxUhLcQPZmAZGirK+Ojrn3WhIqSF+MEMLENDRTG6UBHSQvxIBpahoaIYXagIaSF+JAPL0FBRjC5UhFSfz3/63Y9kYBkaKorRtWqUj77+2euBbejhOMrLb3/1emAZGiqKef/hP12uhnz19i+vB7ahh+MoXgwsRkNFMV+8eq/L1SheD2xDj8VRvBhYjIaKYl5++6suV6N4PbANPRZH8WJgMRoqStLlahQvBrahx+KQL1//6cXAYjRUlKQr1iheDGzg0+9/02NxyCffvfV6YDEaKkpKnJfkxcAGfvjjXz0Wh3gx8AgaKkpKnJf02Y/vvB5Ymx6Io3gx8AgaKkpKnJf09O4frwfWpgfiKF4MPIKGisJ00RrFi4G16VE4ihcDj6ChojBdtEbxYmBVn3z3Vo/CUbweeAQNFYXpojXKp9//5vXAetK/e+/1wCNoqChMF61ReBsVG9NDcBSORhRHQ0Vhum49j9cD69HjbxReL0FxNFQUxotsqIcef6N4MfAgGioK+/yn33XpGsXrgfXo8TeKFwMPoqGiPF26RvFiYD16/I3ixcCDaKgoT5euUfilcWzmdrDp8Tfkhz/+9XrgQTRUlKer1yif//S71wNr+OzHd3r8DeE4xBpoqCiP85JQg8RPNfBKCdZAQ0V5nJeEGuiRN4oXA4+joWIVuoCN4sXAGvTIG8WLgcfRULEKXcBG4XfcsA098kbxYuBxNFSsQhewUTjBEhv49Pvf9Mgb8tXbv7weeBwNFau4dU1dxkbxeqCsX/7+oIfdkJff/ur1wONoqFgF5yVhX3rMjeLFQBE0VKxFl7FRvBgoS4+5UbwYKIKGirXoMjaKFwNl6TE3ihcDRdBQsRZdxkZ58fTG64GC9JgbxYuBImioWIsuY6Pw285Ymx5zo3gxUAQNFWvRZex5vB4o5cXTGz3gRvF6oAgaKtaiy9jzeD1Qypev/9QDbsgXr957PVAEDRVr+ertX7qYjfLxN699CFCEHm2j8CFUrIeGirV88t1bXcxG4fezsB492kbxYqAUGipWpIvZ83h9DV48vbk1+/Qv0P3y94dbDc91qqV32CheDJRCQ8WKdDF7Hq/fUeKrXyfz/sN/NNd6fPzNa72HRvF6oBQaKlaki9nz7P4jz1+8eq/bVCK3569+XdhM4m7l81pYFQ0VK0q/cLrj26jpE6ZK5fas168aa3v/4T+9J4bw04FYFQ0VK0q/jrr977i9eHqTWG1Xyu0afUuwQPC97dvN++XrP8cvuUvBOJxbjlXRULEuXdKex+vXcHteole8U3irdZb0jwAGk/jVtutWxxtOi4aKdemS9jxeX9BHX/+s11dHPvnurW8t7tK//fdI/LqAgmioWJcuac/j9Q968fQm/Rylquz4LnKF0h9cLhK/UqAgGirWpUva83j9Yv7uWivhTJnN7ju/aqAgGirWpUva8zz4O24fff1zQ89H0zlnW13wLukj8Q0ACqKhYl3phjfrc4G39lnP6UXr5au3f/m+H8le723POtiABWioWNfkCSY+5O7lt7/ehm//QZcacnvqdrzPeGzwLmkivGONtdFQsTpd2MjMfPn6T79VW1HPaWK+bUBZNFSsThc2sjRtPWdN/CjpLvEtBMqioWJ1urCRx/L+w3+7fw1ywuSL/HvFNxUoi4aK1Z3zTdDNsvu5Np9893bjk3UXhC+AxAZoqFhd4tc/SMH0v9K6zZPX27VU+0w0mKbfh0YraKhY3V4fkyB9br1k8e/e3O672xPQzb54Yb08+IlnIAcNFVvQ5Y2QbePHJFAcDRVb0OWNkG3jxyRQHA0VW+C8JLJv/JgEiqOhYgucl0R2zO4nQuMkaKjYAuclkR3D77pjGzRUbEQXOUK2ih+NwBpoqNiILnKEbBU/GoE10FCxEV3kCNkqfjQCa6ChYiO6yBGyVfxoBNZAQ8VGdJEjZKv40QisgYaKjRzg6+tIo/GjEVgDDRUbefntr7rOEbJ+vnr7lx+NwBpoqNiOLnWErJ/FPwwAzEVDxXZ0qSNk/fhxCKyEhort6FJHyPrx4xBYCQ0V2+G8JLJ9/DgEVkJDxXY4L4lsHL4WH1uioWJTuuARsmY+/+l3PwiBldBQsSld8AhZM/zODLZEQ8WmdMEjZM34EQish4aKTemCR8ia8SMQWA8NFZvSBY+QNeNHILAeGio2pQseIWvGj0BgPTRUbOqrt3/pmkfIavEjEFgPDRWbevH0Rtc8QtbJL39/8CMQWA8NFVvTZY9k5P2H//S/yFT4ECo2RkPF1nTZI1O5ddPb7UZPnZuPvv7ZDz9gPTRUbE2XPTIVbrpl8WMPWBUNFVvjvKRZ+ezHd/ebTi8jyfixB6yKhoqtcV7SrMitpxeTePzYA1ZFQ8UOdOUjkXz8zWu56W7/o0UkFH5nBtujoWIHuviRULyb9niKnxO+Fh/bo6FiB7r4EUv6CZZWE4vfaMDaaKjYgS5+xOI32tjnP/2uA8jz+I0GrI2Gih3o4keeZ3xmbww9NR2/xYC10VCxg1/+/qDrHxnSf41DDh1JRvGbC1gbDRU7+PT733T9I0P85orh7KRE/OYC1kZDxT50/SNd0uciuR/++FenIF38tgLWRkPFPnT9I138hpqkU5D5j0uAImio2IcugWRRN+3pRKcPH0LFLmio2AfnJUlePL3xWymTznX6+E0EbICGin1wXpLEb6JZdLpzx28fYAM0VOxGV8ETx2+cuT76+med9MTx2wfYAA0Vu9FV8Kz5/Kff/cZZQOc9a/I/yAuURUPFbnQhPGv8lllMpz5lSj1AAeaioWI3nJd0LX0+6iffvdUrOF9iv9IDrI2Git1wXlLZbtqjp/ptAmyDhoo96Vp4ptyeoPsNUoRe08niNwiwDRoq9qRr4Znit0YpT+/+0Ss7U/wGAbZBQ8WedC08Tb56+5ffGgWdtqd+8eq93xrANmio2JMuh6eJ3xTF6VWeI2u8LQ1koqFiT7ocniN+O6zhnL9A7rcDsBkaKvaky+EJsuXXDuh1nyB+IwCboaFiT1+8eq8r4tHjN8Kq9OqPHr8FgM3QULGnl9/+qivioeO3wNrO9h2/fgsAm6GhYme6Ih43e30lnm7HoeO7D2yGhoqd6Yp43Pi+b0Y35bjxfQc2Q0PFznRFPGj2/TjHSb6PcO1P9wJpNFTs7AznJd36me/4xnSbjph9H7UANFTs7AznJfleb+/jb17rZh0uvtfAlmio2J+ui8fK07t/fJd38cMf/+rGHSu+y8CWaKjYn66LB0o93bR37J7q+wtsiYaK/em6eKD4zu5ON/Eoqe2xC06Ihor96dJ4lPie1uCrt3/phh4iNZz5hZOjoWJ/ujQeJb6nldANPUR8N4GN0VCxP10aD5GPvv7Z97QShzzj13cT2BgNFfs73g+N3TqW72ZVdIvbj+8jsDEaKvZ3vCdMvo+1Od6X5vs+AhujoaIKujq2nJpf7B07WE/1HQQ2RkNFFXR1bDZtfZ3s07t/dAeaje8dsDEaKqqgq2Oz8V2rnO5Am/nl7w++a8DGaKiowjHOS/L9qt8xPpb66fe/+a4BG6OhogrHOC/J96sJuhsNppX3rXFsNFTUQtfI1uJ71BDdmdbiewRsj4aKWuga2VQ++/Gd71FDdH9ai+8RsD0aKmqha2RT8d1py6ff/6a71FR8j4Dt0VBRi3bPSzrG75y0+xGa25HjuwNsj4aKWrx4eqMrZSPxfWmU7lgjefntr74vwPZoqKiIrpQt5Egf2Pjsx3e6ey3EdwTYBQ0VFdGVsoX4XjRNd6+F+F4Au6ChoiK6UlafL1//6XvRNN3DFuJ7AeyChoqK6EpZfXwXWvfFq/e6k3WnrS9PxrHRUFERXSyrj+/CAehO1p0jvYeN1tFQUZG2vlf2qM+NfvjjX93ViuPbD+yFhoqKfPLdW10vK85Rvz+2re9V9u0H9kJDRV10vaw4vvGHobtacXzjgb3QUFEXXS9rzfHO7x3Tva04vvHAXmioqIuul7XmqK/39nRvK45vPLAXGirq0so3yvqWH0lDX5nkGw/shYaKurTysye+5QejO1xljvGzBDgMGiqqo6tmlfHNPhjd4SrT+s/Q4mBoqKiOrppVxjf7YHSHq4xvNrAjGiqqo6tmfTnDK41NvJntmw3siIaK6uiqWV/O8EpjE7/37psN7IiGiuroqllfzvCL1rd91N2uLL/8/cE3G9gRDRXV0YWzvvg2H5LudmX54tV732ZgRzRUVKf+Fxt9mw9Jd7uyfPzNa99mYEc0VFSn/hcbfZsPSXe7svgGA/uioaJGunZWFt/gQ9Ldriy+wcC+aKioka6dlcU3+JB0tyuLbzCwLxoqaqRrZ2XxDT4k3e3K4hsM7IuGihp98eq9Lp81hY/N1BDfZmBfNFTUqPLV/NPvf/NtPhjOtQbmoqGiUrp81pQzfPXgD3/8q7tdU2793rcZ2BcNFZXSFbSy+AYfjO5wZXnx9Ma3GdgXDRWVev/hP11Ea4pv8MHoDlcW32BgdzRUVKry85J8g4/k9vxPd7iy+DYDu6OholKVn5fkG3wkX739S3e4svg2A7ujoaJeuojWlGP/gpvubWX58vWfvs3A7mioqJeuo5XFN/gwdFcryxk+B4wW0VBRL11HK8tRf+2EN1CBZWioqJeuo5XlqD9wXfn51VcaKmpFQ0W9dB2tL77NB6A7WV98m4Ea0FBRr6d3/+hSWlmO96qv7mF9OcPXVKFRNFTUq/6vk33/4T/f7KbpHtYXvnQQ1aKhomq6mtaXI32Eo/6XBK683ouK0VBRNV1Nq4xvdqN0x6qMbzZQCRoqqqaraZU5xgu/9Z/c28e3HKgEDRVVa+JFyFs++vpn3/iGtNJNrzRUVIyGiqrVf17SPb7xDdGdqTi+8UAlaKionS6oFcc3vgm6G3XHtx+oBA0VtdMFteJ8+v1vvv2V032oOz/88a/vAlAJGipqp2tq3Xnx9MZ3oVr1f22vhA+homY0VNRO19Tq08qzqNt26qZXH98LoB40VNRO19QWUv9Jvy120ysNFXWjoaJ2uqY2kpo/nNrQh2Qkvi9APWioqN1Xb//SZbWR1PmthLqVTcV3B6gHDRW1++S7t7qsNhXfox3pxjWV20Mr3yOgHjRUNEBX1tZSw2lKuk0N5uW3v/p+AfWgoaIBurK2mb3OVPri1XvdlDbjuwZUhYaKBujK2nI2O1np429et3vyUTC+j0BVaKhoQLvnJcXyy98ffDdLubXS2/x6le3H9xSoCg0VDWj9vKREyn5b4W02vYIDxfcXqAoNFW3QxfWg+fL1n/mn3tweZ9zqdYrjxm8BoCo0VLRBF1dyvvhRAVSFhoo26OJKTha+Fh/1o6GiDcc7L4nMSv4r4cBeaKhow4HPSyI58UMCqA0NFc3QJZacKX48ALWhoaIZusSSM8WPB6A2NFQ0Q5dYcpo8vfvHjwegNjRUNENXWXKafPbjOz8egNrQUNEMXWXJabLX7woAs9BQ0YxDfj8tyYkfDECFaKhoxuc//a4LLTlH/GAAKkRDRUt0oSUnSA0/zw7koKGiJbrWkhOELx1EK2ioaImuteQE4UsH0QoaKlrCeUknjB8GQJ1oqGgJ5yWdMH4YAHWioaIxutySo8ePAaBONFQ0RpdbcvT4MQDUiYaKxuhyS44ePwaAOtFQ0Rhdbsmh8/7Df34MAHWioaIxuuKSQ+eLV+/9GADqRENFY3TFJYfOx9+89mMAqBMNFY15evePLrrkuPEDAKgWDRWNefntr7rokuPGDwCgWjRUtEcXXXLc+L0PVIuGivbooksOmqd3//i9D1SLhor26LpLDhq+Fh9toaGiPZyXdJL4XQ/UjIaK9nBe0knidz1QMxoqmqRLLzli/H4HakZDRZN06SVHjN/vQM1oqGiSLr3kiPH7HagZDRVN4rykM8Tvd6BmNFQ0ifOSDp+v3v7l9ztQMxoqWqULMDlWPvnurd/pQM1oqGiVLsDkWPF7HKgcDRWt0gWYHCt+jwOVo6GiVboAk2PF73GgcjRUtEoXYHKg8LX4aBENFa3ikzMHDl+LjxbRUNEwXYbJIfLDH//6fQ3Uj4YKlKTNofr4LgBYhoYKlKT9qvr4LgBYhoYKlKT9qvr4LgBYhoYKlKT9qvr4LgBYhoYKlKT9qvr4LgBYhoYKlNTch3l8FwAsQ0MFSvr8p9+1ZdUd3wUAy9BQgZLa+l05PvEJFERDBUr6+JvX2rUqDt/wBxREQwUK065VcT7/6XfffgDL0FCBwrRrVRy+MhcoiIYKFKZdq+L4xgNYjIYKFKZdq+L4xgNYjIYKFKZdq+L4xgNYjIYKFKZdq+L4xgNYjIYKFNbQlyX5xgNYjIYKFNbQlyX5xgNYjIYKFNbKlyXxrQ5AWTRUoDztXVXmy9d/+pYDWIyGCpSnvavK8DVJQFk0VKA87V1Vhq9JAsqioQLlae+qMr7ZAB5BQwXK095VZXyzATyChgqUp72ryvhmA3gEDRUoT3tXlfHNBvAIGipQnvauKuObDeARNFSgPO1dVcY3G8AjaKhAedq76gtfkwQUR0MFytP2VV/4VgegOBoqUN4Pf/yrHayy0FCB4mioQHlfvHqvHayy8DVJQHE0VKC8+n/BzbcZwINoqEB59f+Cm28zgAfRUIFVaAerLL7BAB5EQwVWoR2ssvgGA3gQDRVYhXawyuIbDOBBNFRgFdrBKotvMIAH0VCBqBdPb15+++sy2sEqi2/wzec//Z7DbygAFxoqkKaN6PTxmwhAj4YKTNCWcuL4jQPgjoYKTNPGcsr4zQJgjIYKZNH2crL4DQJA0FCBXNpkThO/KQA4Giowg7aaE8RvBABBNFRgHm04h47vPoAYGiowm7adg8Z3HEACDRVYQpvP4eK7DCCNhgospC3oQPGdBTCJhgosp43oEPHdBJCDhgo8RNtR4/EdBJCJhgo8SptSs/FdA5CPhgoUoK2pwfhOAZiFhgqUoQ2qqfjuAJiLhgoUo22qkfiOAFiAhgqUpM2q+vguAFiGhgoUpi2r4vjGA1iMhgqUp42ryvhmA3gEDRVYhbavyuIbDOBBNFRgLdrEqolvKoDH0VCBFWkrqyC+kQCKoKEC69KGtmt88wCUQkMFVqdtbaf4hgEoiIYKbEGb2+bxTQJQFg0V2Ii2uA3jGwOgOBoqsB1tdJvENwPAGmiowKa03a0c3wAAK6GhAlvTprda/KoBrIeGCuxAW98K8SsFsCoaKrAPbYBF41cHYG00VGA32gYLxa8IwAZoqMCetBk+HL8KANugoQI705b4QHxyAJuhoQL708a4KD4tgC3RUIEqaHucGZ8QwMZoqEAttElmx6cCsD0aKlARbZUZ8UkA7IKGCtRFG2YyPhzAXmioQHW0bUbiAwHsiIYK1Eibp8WHANgXDRWolLbQUbwYwO5oqEC9tJF28TIANaChAlWjmwKtoKECtaObAk2goQINoJsC9aOhAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoID/AyYDDKVK43lqAAAAAElFTkSuQmCC>
[image7]: <data:image/png;base64,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IRoqUB3tnKEcP730iQA2REMFaqT983FOX1/7FADboqECNTr+9Zt20Uv++9fHA9gcDRWo2unzn6fvH85t9PTPW78UQD1oqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKICGCgBAATRUAAAKoKECAFAADRUAgAJoqAAAFEBDBQCgABoqAAAF0FABACiAhgoAQAE0VAAACqChAgBQAA0VAIACaKgAABRAQwUAoAAaKgAABdBQAQAogIYKAEABNFQAAAqgoQIAUAANFQCAAmioAAAUQEMFAKAAGioAAAXQUAEAKOD/AUdQc7adh+QUAAAAAElFTkSuQmCC>
[image8]: <data:image/png;base64,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>
[image9]: <data:image/png;base64,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>
[image10]: <data:image/png;base64,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>
[image11]: <data:image/png;base64,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>
[image12]: <data:image/png;base64,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>
[image13]: <data:image/png;base64,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>
[image14]: <data:image/png;base64,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>
[image15]: <data:image/png;base64,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>
[image16]: <data:image/png;base64,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vP77re4QH0fe3AtsSu9/3YeGisV0jJvzxQ+/528IevzshdcAW9N+1X1oqFhMxwCwAe1X3YeGisV0DAAb0H7VfWioWEzHALAB7Vfdh4aKxXQMABvQftV9aKhYTMcAsAHtV92HhorFdAwAG9B+1X1oqFhMxwCwAe1X3YeGisV0DAAb0H7VfWioWEzHALAB7Vfdh4aKxXQMABvQftV9aKhYTMcAsAHtV92HhorFdAwAG9B+1X38IgAzdAwAG/jz7b/asvqOXwRgho4BYBvasjrO0P79+IEZOgaAzXzz2xvtXZ3l5Zt//LCBKjoGAAANdAwAABroGAAANNAxAABooGMAANBAxwCwgafPX73++62+p7bXvHzzzydffueXAojoGADO59OvftRmtat88cPvfqGAaToGgPPRBrXDfPPbG79cwAQdA8CZvHv/QbvTPsPjVFTRMQCcw+6+vDeOX0BA6RgAzkE70s7z6Mn3fhmBj+gYAFZ7+vyVdqSdh6/LxzwdA8BqL9/8ox1p//GLCXxExwCwGg0V90jHALDa59/+qu1o5+HfumGejgHgHLQj7TyffvWjX0bgIzoGgHPo/3+JL4pfQEDpGADORJvSbsPzvaiiYwA4H21NO8y79x/8cgETdAwAZ7Xrr0zyiwMU6RgAzu3xsxe7+15fvr8Xi+kYAAA00DEAAGigYwAA0EDHAACggY4BAEADHQMAgAY6BgAADXQMAAAa6BgAADTQMQAAaKBjAADQQMcAAKCBjgEAQAMdAwCABjoGAAANdAwAABroGAAANNAxAABooGMAANBAxwAAoIGOAQBAAx0DAIAGOgYAAA10DAAAGugYAAA00DEAAGigYwAA0EDHAACggY4BAEADHQMAgAY6BgAADXQMAAAa6BgAADTQMQAAaKBjAADQQMcAAKCBjgEAQAMdAwCABjoGAAANdAwAABroGAAANNAxAABooGMAANBAxwAAoIGOAQBAAx0DAIAGOgYAAA10DAAAGugYAAA00DEAAGigYwAA0EDHAACggY4BAEADHQMAgAY6BgAADXQMAAAa6BgAADTQMQAAaKBjAADQQMcAAKCBjgEAQAMdAwCABjoGAAANdAwAABroGAAANNAxAABooGMAALDc/wF8Ei2vBwi1FwAAAABJRU5ErkJggg==>
[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAnAAAAJwCAIAAACGccv0AABLqUlEQVR4Xu2dvc7dRPe+f6fxHAFnwBFQ/PscAEpLhYREB1IaqiBaonSIBlGkQoqElPKhDhINEhU0FBRIiHb//e79jl/nXp7xmg972+Pr1tUke82aj8ee2x9j+/8e/t9HAAAAUMn/2f8CAACAXDBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGnAwQ/3goy+ef/tDATbVLLbg3vj4y29ss/fG48+/Oinr0fsffmZT3bDBs9iClqy22eIFxFIN/bU1LtYuMcO+Y2OcjEmGAbG/CrcN9cmnX9l2ZjH0+hLRy1dvbLxgG3YjUTYxRDbYxuRGWorH7b0nn7x+fKvDdNXf//xr42EljmSow5ahG4tbNtssWmx/mt1j94Y22i2ngQ2DoCWDvvvxJxtv0WI+/f7nXzZVTUJRIpWtcbF2iRlmao1wa0wyzPj6m0/Ov+wNLRxX4lBDQ4MSe1BiiGywRgT5Ixf1+dff22xCzEetyqwasjiMoQ4TpW4gObIJZ9Fi+1NiOtgP2uhM2YRZ+W28RcvkaNYbNKhIiVS2xsXaJSbhFosakxQb6k3DKaBt/JThTEvLLMkmuaFxQYk9KDFENlgjgvyRHj1PXl3T6CU5DzehmGMYas256U025yxabH9KTAf7QRudqcXdXgu8Kxtv0TKZsqeqGlGkRKq0FWn0VRKTcItFjUkqDXXQYJm2/SMa7VDskqbGBSX2oMQQ2WCNCPJHOvXLb3/YnA+l5xizh4PQir0b6udff69bRJFs5lm02P6UmA72gzY6X7FZ8uF6o0uj35UtYtEy+ZJpTn8uUjqV7UW6dolJuMWixiT1hnqJn3XVHDfbbBoRlNiDEkNkgzUiyB+ZJck5bH4a4ZZtIbRi14aqG0KFbPJZtNj+lJgO9oM2ukixWz4vX73R0HflufOkZYo0PWvU34qUTpU4t9DQqyQm4RaLGpM0MdSLaVtl8y5zN1M1IiixByXaYIM1IsgfmaWGORMbElSyU0OtOVadla1iFi22PyWmg/2gjQ6yjU8faNvMieRT2VLOJBKWWGh60xg5zMUWjQ4aem2Dn4QDCI2eyHYkUURiEu2xCWMkDFUi08c9T5+9kHiNmGh6lTixwTgT2o1wJGuINCKoOHKoPdG76RWRxEWa6RrmxHolqRpasTtDXZzCymQrmkWL7U+J6WA/aKODZhufWIdigxPJp7KlnEls5EPOJC5odNDsOCyWusSr07irJCbLLWL4DfWGBk00DUvs9faeq0YEOcMSg581RBoRVBP54NvYfv/zL/3tKnujPfb3sgc00IR9GWrzE9NRtq5ZtNj+lJgO9oM2OijWeI0LspGJ4KlsKWcSG1kWny4VG4d0qUv8Yp3GXSUxWW4RIzZBX+JJNC7Ik3Z2oGKLcZz1zua8kTVEGhFUE5mOH48t9IcgmyoWbFfVQRP2Yqj6B28tW+MsWmx/SkwH+0EbHRRrfGzp2ezqFQ2a02xBTxIbeSN2CpWuSKODYuOQLnWTjY8VkZgst4gRc75LPInGBU3veupvQTZbIl7Oz/TnoMTgZw2RRgTVRN4YTh819KrXj28LEsay2Uio5/6G+hh/SL+hbL2zaLH9KTEd7AdtdFCs8bGrvrMPDGjQnBYPwLVAkI1MF4n1KFHkUlrqptkX/WjQVRKT5RYxGhrq9Gxbfwuy2RLxcnCjPwclBj9riDQiqCbSWUT/N8jmScTbMKjnboY67E76F15TtgGzaLH9KTEd7AdtdFCi8RoaJGGxy31WtoqC6lYqkhiHRKlRziISk+UWMQoMNbY6aep/+luQzXZj9ihcRlV/DkoMftYQaURQTaSziP5vkM2TiLdhUM8dDPX9Dz9b715pTLYZs2ix/SkxHewHbXRQovEaGuQMs7JVePLYyDWKJMYhUWqULa4RV0lMllvEKDDUWBGPocaegLI57ctAJGCUHb2RrCHSiKCaSGcR/d8gm2c2/vXj23FJObRlU0ONXdnbQLYxs2ix/SkxHewHbXRQovEaGrQY9vuff82er9gq0nluspFrFEmMQ6LUVJ4iEpPlFjGsk42ywekiU0P1LG21OWNLtG5ooqDE4GcNkUYE1UQ6i+j/Btk8Y/xwwGHXS0NzNjXU2YlvG9nGzKLF9qfEdLAftNFBicZraNBi2DCrzs6Dtop0nptsZLpIokexIpfSUlN5ikjM7CjdZNsQI+aOl3iS2F4/NdTEDaDF2+ExNFFQYvCzhkgjgmoinUX0fyeyqWBLMNR30GL7U2I62A/a6KBY4xOXLqZhs7P57bhb/3fpSTuNDrKR6SKzS4TSRS7xcUiXmkoy6M9XSdost4gx+ye4yQbf0LggueqoP09kc3rQLEGJwc8aIo0Iqol0FkmsJJhdxwebgaG+gxbbn+wr1naINjooNpfFXukyPieQSBv7KfE24Nn4m2zkjdiDPek/h0YHxcYhXUo0vYKnv10labPcIkZDQ5Ww2MsKbrK3SBfRFEGJwc8aIo0Iqom8EVvGNW25/vaubE7YBgz1HbTY/mTbvEO00UGxuUzjgjwnMYs/zaKhQTayLD5dKjYO6VKi6bVQ/e0qSZvlFjHWM9RE5E25515aPigx+FlDpBFBNZHp+OkSLf3tXaWPJmE9MNRN0Wbly+bcIdrooNhcpnFBnrDbT7OrWmxF6VSXSJHEyZMNnqLRQbFxSJeySheRtFluESPXUDUoaNYdF+cH+2q9BFo4KDH4WUOkEUE1kQ/Jy7nTsMQfYpRNDmuDoW6KNitfNucO0UYHTeeyYfKKXdoa5Ul7+2l2VUviNqqGBk1jhpzp57sWzwO0QFBiTo+Vmp1n0++ik7QJt0hIkiTm8THm/Q8/S4TdJGlHNG5OttQsWixo+KsN4z/L7GHZTf78ZZHDXyc9PdrFWbPbvIiVvRuDoW6HZwdIa3EG3wna7iLZkxiNuCrxa8K3NLRIi7OVFghKNCxWatYOx0lWf7hK0s5mWJQkWXRKpyTtSGJ52ii7Ycyixerkz++PzNLsxqZBc8o6rYdKMNTt0DblS+4p7hZtd77s8fjsVD5dq6K/XWXblgjOks1p0TJBZYY664i3TUL/9ypJO1t8UZJk9q+QK8lp0QJzSj+E6kzilz+/P9KvxJF04qx6VMGSLigDQ90ObVO+bM59ou3O1Oz0MXv1dXqEob9dZfMkgv2KvcHHWUuZocZ+Svz/lJ0YqiScxXOeellKpdF18uf3R/plc06ZvR0gcp7WQyUY6nZom/Jlc+4TbXembMJYzqyAxWCP7KlzAi0cdE5DzT1P0vJzsqWyivvlz++P9MhphLOHm6LZi8bQll0b6rAHls0CVrYx26NtylT6HQK7Qpvulk2VzpkVsBjskfPcNF1LsaFm3YaXtGW7kiSpMdT0M7uzeHzClrqhcXXy5/dHppV7/OE5rXfaMxSzU0MdN6ayWcDKNmZjsqbCWR3oAFObntSwVSzeG/Z801F/uyq2IkPjgm63KmM3LG+y2WJoyaBiQ439OitJm+jRtNeCJEkY6lgktpvLazqcxF76MZUt9RAfqN///GvoxSyJa6f+/P7IWd3OImwSD4m/zqisI0LIZV+Gap9zSMwCWbKN2RhtUL5szt2iTQ9KG0mC2TMVmaBnH8KJ1ahxQbkxabRkUKxViVLjJOvfIyRtoqBtQ4zElD0N09+CbEIPnoNRW0ojghKDnzVEGhFUE9mExGPTN9ki0Iq9GGrsclBiE8+Szbwx2qBMZd26uzva+qDEXJZGE10lh1+xTcVmiyW8+FzBf4yvJYPS46DRV03PWvS3iCRtbHwuJjJBpaEWX2X54KMvNNe7skOqEUE2ciRriDQiqCayFVrTu5pd9AdNuLOhLt4XTGziWbKZt8RzeyOtxYcEdoW2Pigxl6XRRFcVh8UiL+8GO80jgRYLSo+DRl81NdTElcmpJG1iV7JtiOEck9hJUu59wSmLO5HE689BicHPGiKNCKqJbIhW9q5iJzBQyX0M1V7ajZHYxLNkM2+J51mxtGzOPaOtD0rMZQliV/xspEZcNXsbVYOCysJiaLGg9Dho9FVyX01/npOkTexKtg0xnIaaMD+bMwtNN5FziBKDnzVEGhFUE9kWre9d2XioZ1NDLViVkNjEs2Qzb4m2Jl82557R1gcl5rIE9sJGlmbPijQoyBnmvGCgxYLS46DRVzndYipJm9iVbBtiOA31Id5CmzOLhFVf3k2uvwUlBj9riDQiqCayOVrlRDYY6tnUUAtIbOJZspm3RFuTL5tzz2jrgxJzWQLNki9/TgmLfbXtYiJn0TJB6XHQ6KvEUGPLnqeStIldybYhxgaGOrRzvKJjf32IZ76cz1A/+OiLcS2e/fXGu3X+T1z1XQMMdQu0NZk63CIC7UBQYi5LoFny5c9ZE2nRMkHpcdDoq8RQY2FTSXxiV7JtiFFvqLNLuobjg9nrEDby4fryfY0Lmo6S/haUGPysIdKIoJpIJ7N/BRt2I3Y/e0hig6ESDHULtDWZOtymrx0ISsxlCTRLvvw5ayItWiYoPQ4afZU11MWlSRKf2JVsG2LMTuU3SWTi+VGbViOCbGQ6frqn6G9BicHPGiKNCKqJdKKJrrJhN2LHH4lxgGIw1NWZPfTOks25c7QDQWX7sGbJl72NqhFB/tpn1zo5y6bHQaOvsoYaixwlwYldyWaO4TfUh3jzaiJvxPap6cDqb0GJwc8aIo0Iqol0oomumj31T8RfKhoAMTDU1dGm5Mvm3DnagaDEXBYjtgH88tsfj+Z7lrF59mLGUH8Osg3QiCDPW9y0TFB6HDT6qp4M1U79sdNZm/NGrBlnNtTEo+oaGmQjoRIMdXW0KZlafFR3h2gfghJzWYzYE0c28obGBZWFPSS3QBssaIGg9Dho9FWzhppemiTBNR0ZiTnZZS5J4qK0RMbe22Ct90asGScx1NkXh13iCTUuyEZCJRjqusT2fL+KXy5zR7QPQYm5LIamCLKRWfH6c5BNmAhevOqrBYLS46DRV80aaiz4JolM7Eo2bYzE9myDY3fvLnPBGhFkIx98C230t6DE4GcNkUYE1UQ6iS0+t5E3NO6qxDhAMRjqumg78mVz7h/tQ1DBPqwpgmzkjdhUW5NWg4IWu6MFgtIFNfqqmKH6zwITu5JNGyPLUB8ifbnMBWtE0OxJqgYFTR8F0d+CEoOfNUQaEVQT6UdzXTXbtdh7UWYHFirBUNdF25Evm3P/aB+CZnf4BLG/fmLZc2z6kBN9/TnIJnyInxBcIvEjGh2UHgeNvipmqLH4i2lbbDAvJjJBrqHGrtjb7iROZ+XPrT9P5AlLDH7WEGlEUE2kH8010fSo4tG9qgCagKGuSOzOUJZs2v2jfQhKzGWzxE6/0s+ka/RVzknZZiuLT5dKj4NGX2UdaGT2MzsX07bErvRo1nYJY5JcQ41VOrukS4My5fwTJwY/1trLXO80Iqgm0k/sNqpfNifUg6GuSP1GX/Cyxj2g3QhKzGWzaPkgG5lbSn8LstnK4tOl0uOg0VclDDVWRGJqdqUxSa6hxtp2icRrUI6cqRKDnxgiG6wRQTWRWWi6HC3e/ocyMNQV0Ubk66DbvXYjKDGXzaLlg2xkbin9LchmuxE7V06vwdbooPQ4aPRV/Rnq7LatQW7ZP4RGBCUGPzFENlgjgmois0hcJE9r9vIANAFDXRFtRL5szkOg3QhKzGWzaPmrEs/b3XiM3DdazHyJD3jinew2eERDg9LjoNFXpQ111u8lpmZXGpM0NNTYtK5xDs2m0qCgxOAnhsgGa0RQTWQumtEnmwdagaGuiDYiXzbnIdBuBCXmslm0/FWLX3qJbTOeZypstjWKpMdBo69KG+psKQmIDYtHY5ICQ429tOESLxJbqj0rW/yGxgUlBj8xRDZYI4JqIgvIOk+1rwyDtmCoa5G1oc8qsZZ152hPghJzmSV2UmgjLVrmquk3BvS3IJtqsYi92LhYJD0OGn3VoqHak1QJqNmVxiQFhprYEWav+i6WGpW+VqHRQYnBTwyRDdaIoJrIYjzLNWwpaA6GuhZZR9mzsjkBTsjgux9/+c3g5QM8PbnIMGfexmpg8TgM2oKhroW2IF82JwAA7BYMdS20BZmaXWcBAAC7BUNdBXtDK1dHfIUvAMCZwVBXQavPl80JAAB7BkNdBa0+XzYnAADsGQx1FbT6fNmcAACwZzDU9sQeoPTroK/wBQA4Mxhqe2Jf//Ar8cA7AADsEwy1PVp3vmxOAADYORhqe7TufNmcAACwczDUxtQ3+Liv8AUAODMYamO04nzZnAAAsH8w1MZoxfmyOQEAYP9gqI3RivNlcwIAwP7BUFvy+POvWnG+bFoAANg/GGpLtNZ8fffjTzYtAADsHwy1JVprvmxOAAA4BBhqS7TWfNmcAABwCDDUlmitmfr7n39tTgAAOAQYajNeP77VWjPFK3wBAI4LhtoMrTJfNicAABwFDLUZWmW+bE4AADgKGGobPv7yG60yU7zCFwDg0GCobfj9z7+0ykzZnAAAcCAw1DZoffmyOQEA4EBgqG3Q+vJlcwIAwIHAUNug9eXL5gQAgAOBoTbg6bMXWl+meIWvkw8++uL5tz88/vzryMdffvPek09sJBwR+eMO/2zycPYwjUwzv3z15vOvv3//w89s5NEZ9oWha9MBHPpuw2AlMNQG/PLbH1pfpjrbt7V7btlUN4bN4O9//tXod/X7n38tDqOWSWqYj4a5ySbJRfMWKZ0qvURco4OcYYuqnLIHD9CMcxqOnGzZNMP2oFmMhs3GFvSgiSaywRYtE2QjnaRfLMNb2LYBQ22AVpYvm/PQaPfcsqmGkwkNWlJiftfQHNlsTjRRkdKpDmqoTiudarANm8cyHAlpySXlHjxp+YmGjdbGO4vbyEU0RVJczlkVDLWWgklB1N/Bo/bQLclTfOofu4SucZmKpU2jWYqUTnVEQ/3goy80kU+LF4GLN5sss9HC78rGO4vbyARlY2jzQCsw1FqK995RixPE4dAeujVNUnBuOtXsqGpQvgqOfjRFkdKpDmeolX/cRH81NFNPn72wOS2LF5NtEUELBNnIBFrYp4JtGJxgqLVoTfmyOY+O9tCtJklGNWzYVJ4Les0rTadKGEyilDNsUQWGqinyZXOunXnKMOBa7F3ZIoIWCLKRMRZXFSRU8CcDDxhqLVpTvmzOo6M9dGvMUDNZjLI2oxGlsl1OoIWLlE5le+ppgDNsUQWzs6bI1+zl98eff9W4fNm0Fi1jZIs4M9jIWervNNmcUA+GWsXigapHNu3R0R4GDfOdDbak7wxJcHpmkWD9eSLbjLSp2/gsEhu2DR7R0KC1DdXmrEGzT2SDE7dUJDKxJcy6rwYFea6IahkjW8SZwUbOosUmkjvBsc3Y5oR6MNQqtJoi2bRHR3sY5DTUxIuRbfBD8oaWROrPE9m0D/HJ6BKJ95PYsG3wiIYG9WGosRW8GhckYYnnRmzOh6QB22BBCxgtrhnWAkE2chYtFjS7rkqDrrJhUA+GWoVWky/nIohjoZ0MchqqFgtK3LyMebBcjdSfJ7I500VsZBaJDdsGj2ho0IEMdThZ1OxBNviGxgU5w4ZzXJszXSRth84VVbbgFI0OspGzaLGrYvuXxl01e9YOlWCoVWg1+bI5O0A7GRTb4Z3FE+9tiD13KLOG/jyRzZkuYiOzSGzYNnhEQ4MOZKiaeiIbnC7iPFpKHLNqaFD6bQ8aHZEt6EliI2fRYlfFNoPYrWUbCZVgqFVoNfmyOTtAOxlUaag2ciSxnXgyX+LJNS7IRmbhbLCgoUGxmTRdyhl2MZE1aOqgxLYR8wPptf4cZBMuFrmUlprKFvQksZGzaLGrYptB7N2oNhIqwVDLiZ0V+dXrVRftZ1Bi0vQUt5G5pfS3iWzCdBEbmUViw7bBIxoaFJtJ06WcYRcTWYOmDkp0IXZzVDYn/TnIJhyJWfUlWUpDI0pfN9boIBs5ixa7Kvfitg2DSjDUchIrVpxKXMM8NNrPIAx1JLFh2+ARDQ1KuFGilDPsYiJr0NRBiS7E1tLfxVBnD6Nnb+GXXTe2kbNosSAbKfHDrJW4Bg6VYKjlaB35sjn7QPsZhKGOJDZsGzyioUEJN0qUcoZdTGQNmjpIbohO2ZWhatxVH3/5jf7XVbZ4Os8lWcRTPHGSChuAoRaSflbSI8/jbgdFuxqEoY4kNmwbPKKhQRhqIrNNONLKUBP/H0NDg2zkLFpsosRIwtpgqIXE7uv4lb7Fcmi0q0EY6khiw7bBIxoa1LehOtGMQTZy5LiGmr7fZONhGzDUQrSCfNmc3aBdDcJQRxIbtg0e0dAgDPUhntlGjjQ01NmHU23xdJ5Lsogzw02zH4eAtcFQC9EK8mVzdoN2Nehwhup/710uiQ3bBo9oaBCG+hDPbCNHmhjq7d7N7B800SkNDbKRMRIb5022CKwNhlqIVpAvm7MbtKtBBzLUxHvpLi2ed0ps2DZ4REODMNSHeGYbOZJrqLN3c8d7N/pDcqGvhgbZyARa2Ig1ShuDoZaQeHmsXzZtN2hXl1S/usRZSn+baGjDDf1hTrb2XBIbtg0e0dA61Se3LVxEUwQdwlBnH48ZX5+rP1xlkySCL/H4WWKri6fqePHjDsFQS0i8j9SpxGtpO0B7u6Q9GKpf6dNBJ4kN2waPaGid6pPbFi6iKYIOYagadJXzV0+qSzw+hmcu6nu22RUYagmaPV82Z09ob5d0IEOd/ZpHAYkN2waPaGid6pPbFi6iKYI6MNRZb4u9RUHjgmykB80yJ1sKmoOhlqDZ82Vz9oT2dklHMdSGTzolNmwbPKKhdapPblu4iKYIEkP9+Mtvnn/7wyKezLYNI1mGGvuTpQNi6wY0LshGepitWsS13w3AULOZXR+fpfolLTtHO7ykQxiqrbGGxIZtg0c0tE71yW0LF9EUQWKoCaubypPZtsFTiw2evYHqMXWbKhZ5iQQ70Vxz4nGaVcFQs9HU+er1Fb4j2uElYahT2eARDa1TfXLbwkU0RdD+DVUjrpJ9WX++yqaKRV4iwX403ZxsKWgFhpqNps6XzdkZ2uGg2OUvZ3EbmVtKf5toMebjL7+xlRaT2LBt8IiGBqXXSWl0kDPsYiJr0NRBBzVUT8zsAbQGBdnIXNIvUbosbS1QA4aajabOl83ZGdrhoEMYauItzbbSYhIbtg0e0dCg9BSp0UHOsIuJrEFTB3VsqLObvQYF2cgCZpdHTcW635XAULPR1PmyOTtDOxw0O7NYtFiQjcwtpb9N5AmzlRaT2LBt8IiGBmGoicy2DZ5abLBGXOWJuZiwrMgyFh9RtUWgHgw1j/oVSU5TOTTa5yBn37VYkI3MLaW/TTQNm11+cmm6miyxYdvgEQ0N6s9QnaVyYwS/oT599kIjrpKw2OsAbdUaEWQji0lca7k0XbIOIxhqHpo3X+mJow+0z0FHMdTE0b2tt4zEhm2DRzQ0CEN1xgh+Q41FDs2eErvWaqvWiCAbWUNiS760rgseMNRcNG++bM7+0D4HHcVQE5G23jISG7YNHtHQIAzVGSPEbPJiSunPmbJVa0SQjXQSWzSXeE9qesyhAAw1gyaNsWn7Q/schKGOJLYlGzyioUEYqjNG2MxQ7dOfGhFkG5lg+LtP1/TagBuT9O/IuT+CHww1g8Tu59RJFtdpt4OcO7AWC7KRuaX0t4kkW+xmuZ0Zy0hs2DZ4REODOjDU2Cv60qVyY4TEHj0NS9+M9Mju+BoRZBs5ixa7yoYlgm+ywVADhpqBJs2Xzdkl2u2gAxlqIthGFpDYsG3wiIYGdWCo9V3Q34JsthGnoSbC/JKq9ecg28hZtNhVNuxG2cYGBWCoGWjSfNmcXaLdDsJQRxIbtg0e0dCgejdKhF1MZA2aOii9glqjg3JjhIRTejJnSarWn4NsI2fRYlfZsHT8JVkECsBQvbx+fKtJM5WeMnpCex60nqHGnmqQGvXniWxOjQhq8rxBYsO2wSMaGtSBoV6StWhokCcmcXdWQydaDEtszBp6ldws0J+DbLZZtNhVuU26uKsDJxiqF82Yr9k3kHWJ9jwoscN7iiecLHaqIUsf9eeJbM7EK9xscC6JDdsGj2ho0IEMNfaXusRriR0tXRy2d0keyGpo0LRI7AZqbFVtLK00Q38Ostlm0WJBNrIsHsrAUL1oxnzZnL2iPQ+qNNRLfAw1LsgZdjGRD8ln+GxwLokN2waPaGjQgQw14Y6xI06Nm6ggzFNkejbpf7R0MW1uTILYu0dmbX44EtW4IBsMNWCoXjRjvmzOXtGeBzkNNeFkrx/f2nj/qaT+PJFNm4ifnbaySGzYNnhEQ4MOZKgPmRW99+QTDZpoGpl44HL2s/Cxtxpdqp0vdhZemVbQkkH2jFwjguo3YxAwVC+aMV82Z69oz4OchprIcDEXfvXnd+VPa9uQiK//VnNiw7bBIxoadCxDjfnN5TqwU/Mb+qUR70oy688TTYdoqCJxECaDqT8HSdVTYmeElWkFLTnR4Km3YUwcm15y6gInGKqL+hVJfi/pAO18kH8QYjeusmTTasRENvgheX3SBmeR2LBt8IiGBq1tqGmla59FU5RK0qZPZ51yNtV2arHUYoBHTZJckmu1oBgM1YWmy9epNl/tfJDfUB+SF3I9so/SP8QbdolvIRoXZCOzSGzYNnhEQ4PSlqbRQc6wRaVrn0VTlKp55l9++8OZ0Fa9WGoxwKMmSS5L7YcyMFQXmi5fNmfHaOeDsgw1kccjmy2d0Aani9jILBIbtg0e0dCgtKVpdJAzbFHp2mcpOJWcvXppMycuKnhkE2rEVb//+ZeNXCw1vVuhv7k1raVgGG+aPdyEejDUZWb35FzZtB2jnQ/KNdREqoQSNzg1dCIbnC5iT2WySGzYNnhEQ4PSlqbRQc6wRaVrT6CJ4rotn9H/NV0oyDyVzRO717O4nEcLBC0GLMrWlVhdNSubAVqBoS4TW6Hu19mOB7X/QQWG+hDPNqv0TKfRE9ngG4krzzbYT2LDtsEjGhqUtjSNDnKGLSpdexrNNafxb6o/mC7kZh4V64LGBdnI3IL6g1u2roecOSr2bBI0Ye+GCkfkybsfiRypfLN87HTh4j5ksU0ascE33nvyiQ1OF/FQltYG30jPkjZ+tiIb4CRdu4fBMmcPXOTwyFZtUwlD22IPkl5Mfout0VmvLSIF7U9ObF0jQ2dn95FhbBd7Ck3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFeAYvP/hZ08+/WrEBgDAfcFQAe7PYJCPP/96aadffvvj6bMXtiIAWA8MFeA+fPzlN4PtqROuo5ev3tgGAEBbMFSAjRhOGX//8y/1unsIfwVYAwwVYHXaXs5tqOEs2bYWAMrAUAHWYrArdbBd6rsff7KNB4BcMFSAxjz59Cu1rIPo73/+td0BACcYKkAznn/7g3rUAfX7n3/ZrgHAIhgqQAPUlLoQl4IBssBQAarY7YKjVnr/w89srwHAgqECFDI4jZpPp3r+7Q+2+wAgYKgA2Rx32VGl7FAAwAiGCpDH3//8qz5zJvHoKkAMDBXAy07ec7QHffDRF3Z8AE4OhgrgQi3l9Prltz/sKAGcGQwVYIHT3jFdFJ4KMAVDBUihHoKMuPwLcANDBZjnvk/F/P3Pv68f3z7/9of0t8RvXx0fwu77OOzQVNs2gLOBoQLMMDiEmsaaWuNBz6fPXmzssrYNAKcCQwVQtnkw5pff/kiffbbivSeffPfjT1r9OuLyL5wZDBXgHdQiWuvuz3EORq5taqo1zrYBDgGGCvBfhjM5NYd22tuX0VY9Z+WWKpwTDBXgv6gttJOtayes9wn04ejEVgfQNxgqwFq+ciBTWeO28d5OygHWBkMFaH9uesT7iGtc8cZT4VRgqHBqPvjoCzWBOm2zcHdV2r6yGE+F84Chwnlp7qa2ioPS9jFc3lAIJwFDhfOiE3+FPv/6e5v/0LS9AmzzA/QHhgonRaf8Uj3+/KtN3g0NT+Lv/gAuwNpgqHBGdLIv1UleDKTdLtVJhgtOC4YKp6PJq4J+//Mvm7ljnj57oUNQJJsZoBswVDgXn3/9vc7xRbKZu6fVXVWbGaAPMFQ4EU0s4czPgTR5AwaLfqFXMFQ4ETq158vmPCE6KPniZip0CYYKZ6H+46CsUx3RocmXzQlwdDBUOAX1C5FszpNTf/nX5gQ4NBgqnAKdyzPFueksOkyZOvPdaOgSDBX65+WrNzqX5wg3TaCDlSmbEOC4YKjQOc+//UFn8RzZhCDokGXKJgQ4KBgqdI7O3zniAQ8PlQ8jvXz1xuYEOCIYKvSMTt454tGOLHT4cmSzARwRDBV6RmfuHNlskKDmqaTvfvzJJgQ4HBgqdEvNh7Lfe/KJTQhpdBBzZLMBHA4MFfqkZmWvzQZOap73tdkAjgWGCn2is7VbTz79ymYDPzqgbj3/9gebDeBAYKjQIe9/+JnO1m7ZbJBFzYfebDaAA4GhQofoPO2WTQUF/P3PvzqyPnHrGg4Nhgq9UXx6yiXHhujg+sTLCOHQYKjQGzpJu2VTQTHFq5N40SMcFwwVuqL4EyicnjZHh9gtmwrgEGCo0BU6N/v0+POvNhXUowPtk80DcAgwVOgKnZt9snmgCWUXfrnqCwcFQ4V+KL7ea1NBK3SsfbJ5APYPhgr9oLOyTzyqsSo63D49ffbCpgLYORgqdMKTT7/SWdknmwoawt8FzgOGCgdjmKCff/tDzbdNprL5oTk1XymYavijsxgb9gyGCnvn6bMXrezTasjMEphVqflKQVqDT+OvsCswVNgj73/42Xc//qQz6MoaahzqtY2BXD7/+nsd3PXFbVe4Oxgq7IWal6qvIc5c/bz35BMdvrtqOHm1jQRYGwwV7sze5mLR68e3LANOcJeTUb84bYUtwVDhPhQ/M3pHDeZhO3JC3v/ws1brjDYTL8OCDcBQYWuOaKVTnflS8HCyfjgrner141vbKYBWYKiwHcUfVtuhPvjoC9vBvllvrfXGYm0wrASGClvQzVws+uW3P2xnO+PoVxQSYlE3tAVDhXXp1Uqn6vj+nHa1R9leA5SBocJa/P3Pvzp1da2hv3YQDsr2DwHfXWe+NQ6twFChPT3dK81VB/dWD73sqEbDYYQdDQA/GCo05rTT8ahDn6pqZ84nOyYATjBUaMYZbpf6dawbq8XfhOlVvM0DCsBQoQ24qdVRPPWDj77QpiM8FfLBUKEWrvGmtfMrwNpc9K7siAHEwFChitePb3UGQkb7PFXlxNQpO3QAs2CoUI5OPOvr5as30wYU2PnD9X7hXS5Q7+oSojZufY2fLy14nmra8s+//v4ufz47hgAChgolbHlyM5hozIoqp+ZbRwpcuVg7+fiJNmtN2S8KFDzkartwY8tP/p3hrVhQCYYK2QwOp5PNCvLMX1rGIZvkxmavfb/7w47aoHWUOHQoeJehTSJsdoRnqwYYwVAhj8HndI5pp8HSsl6vquWX5LyXOczOBee+ft1rmdLa53NyQT6BllzSk0+/sklirH3AF7teAoChQgbr2cxgpQXzlGZZkn/Gf7i+72m9/l42P9dZ9Uvgud9v0fJLSpzvxhiapFnaqYP3YcEaYKjgRSeVFhocq8BHRzTdkrJOdEbWc1Zb10oU3Lb0KNdHRzTRkooreljNWXn3L1gwVHCh00kL1U9JmnFJZYZ6Y6V52VbUnDXWxP7+51+2Ij+abknOa/UxhoO2NQ6J6jdg6AwMFZbRiaRaNSccUzTvkmyGXDRjC9laGjJ4idZXrZqLCjc045IqDfXGGkNha4Ezg6HCAjqF1KnmHNGi2ZdkM5RRsE41LVtFE5pf6bVVlKF5l9TEUEc0e524nwojGCqk0MmjTlkreD1oBUuyGYpp/pyGraKStm76+vGtraIYze6QTVJD28XqeCrcwFAhSsPnMgtWaXrQapZkM1TS8EGUts/SNPx6TOXt0lm0Dodsknoa3litvwwOHYChwjyt3h/U1icErWxJNkMTWs3LnndZeGh4s3AnR0KX1f52Ddea2eRwNjBUmKHhPUKbvCFa2ZJshlZoTaXKelI2hiYtlX1rYCu0piW1vYcqNLw2bpPDqcBQQWl1fmMzN0erXJLN0Batr0iVFw+bnC63WoYdQ+tb0qqGeqPJJZkN2gl7BkMFRSeJIm2zTENrXVLzVVFCq5VKNrOTJo+ctrrynECrXNI2RtXkWGSli+RwCDBUeAedHvLV5KKlE617SW0f2onR5BKiTbtIEz+waddAa13S2mfMI00uz9z9+wdwLzBU+B9N1qzatOuhdS9ps3lZK85XwVt4NEW+trmu8JDf1C1P+5osILBp4QxgqPA/dFbI1KoLemfRFixpmyuHN+rPF23OBPXVrX09fIrWvaRtLi2M1HvqltdpYD9gqPBfdErI1PZu+lDUZptkPepNzrlAqb4im3M9Cp6RtUk2QBuRqbavwoBDgKHCf9DJIFN3cdOHIiOxSValoIUim9OiZTLltO1WFDz6aZNsQP0SM5sT+gZDhdqJY7Mbb5ZDTM2Vw7t4tVMLZMomXBttgUM2yWZoU3J0rwNNuBcYKlRNGZe7TnYFFw+3vFM4oo3IlE04UvmczF0OhrQRDtkkm/Hy1RttTY4Wj4egJzDUs1P5PLtNuDHaoCVtttBX0HbkKLaWqvIZj4KFxE3Qdixpg+di01S+Sd8mhF7BUM+O7v05stm2R9vkkE2yDdqOHNlslQk3vm86UnBR4V7GP6Wg2VPZhNAlGOqpqXkFwb1O9QRtlkM2yTZ8/vX32hS3Zk9SNShHNts2FFwRsUnugjYrRzYbdAmGel5qXuNwl3tvs2jLHLpj42sWKMmJmv7s1hqfY/OjrXHIJrkX2rIc2WzQHxjqedE93q1dPWCnjXPovu2vuSrQNsld0NY4ZJPcEW2cW6xOOgMY6kkpeOBklM12R8q+gm7zbIm2xq36DHd/kEMb5JBNcke0cTmy2aAzMNSTovu6W3e8XjpL2UVUm2dL3v/wM22QTzc7LF4gc9+LvQ/H/GNZtH1u2VTQGRjqGSl+3OLuDzDMoq10yCbZmOLnR4v/dpcd9Lrg+ZMdvhS3+E8wu7IMegJDPSO6o7tlU+0BbaVDe/jAlrZpZdkGbI+2ySGbZA8UX2PgTmrfYKino/iC4W6Pr8vuB9s8G1OzsKhAtgEbU/bUkM2zE7ShbtlU0A0Y6unQ/dstm2o/aFsdskm2R9u0mvZwYqRtcmi3x3APRQ/U3nSvV2rABmCop0P3b59snl2hzfXJ5tkebdMK2sP17bLrIjbPrij+lJBNBX2AoZ6LsnltzycKN457OXGDC7+20u3RNvlk8+wNbbFPNg/0AYZ6LnTP9snm2SHaaIfu8uUZizarqe7+4OkNbZZPNs/e0Bb79PTZC5sKOgBDPRFlTwFejjCvPRRNbYc2G6f2cMeubE3sfV9o5eTjL7/RdvtkU0EHYKgnouyWzx7Ws3jQdvtk82xPmd94tJMjhrINbw+HAh603T7ZPNABGOqJ0H3aobu/W8dPsS3ZVNtT/J6HtGxF21N2DreTQwEPZe952Oc7UqASDPUslC1+OcpZwg1tvU87OQXXZlVrJ0vJtFk+7e0Nl2m09T7ZPHB0MNSzoHuzTzbPnjn0TWJtU7VsFdtTdvZ2oNPTEe2DQzYJHB0M9Szo3uzQSea1yz6mtrLP5iRkq9iesrunxzo9vaF9cOhYl3/AA4Z6FnRvdugk89plH4cOxfeAZ3XoHtlU+0f74NAeXrgBbcFQT0HZDVSbZ/+Uvbniso+HNLRNFbLJt0fb5JZNtX+ePnuh3XDI5oFDg6GeAt2PHfr86+9tnkOgPXHLptqYsgWxs7LJN6bsYu9lN2/bKEB74pBNAocGQz0Fuh87ZJMcCO2MT3tYFqttKtLdr9WXrUW67ONPUEzBdaBD9xcsGGr/FJz3HOjx01mOe3pU8AluK5t2Y7RBbtlUB6LsMMLmgeOCofZPwRx99HeNlk1tN9lsW1L85M9UNu2WFJyojbLZjoX2xyGbBI4Lhto/ugc7ZJMcDu2SWy9fvbHZtkQblC+bc0u0NW7t5A0bNWiXHLJJ4LhgqP2je7BDNsnhKLjQPeq+F361NZm67205bU2ObLbDoV1yyCaB44Kh9o/uwQ7ZJEfk9eNb7Zhbgx/bhNugTcmUTbgZ2pQc2WxHpOC7vB2cl8MIhto/ugcv6egrkqZo33Jks21D5YvybcJtKF4Idrnr4UtztG9L4vUOPYGhdk7Biw56OmQ+ojkVv2DoJptwA2oWIl3u1OaV0L45ZJPAQcFQO+f5tz/o7rskm+TQaPdydK8X+Gk73LrL6U7N7erL8ZeUC9o9h2wSOCgYaucUnKLZJIem4Bx9qru8wVwb4dZdri5oI3J0r0OW9WCPOzMYaufovuuQTXJ0yt6zOmr7b0FrC9yyqVal5nnfm2zOo1NwAGeTwEHBUDtH990l3fehi/XQfmZqY08tXp9sU62KVp8pNrab7nJdAdYAQ+0c3XeX9PzbH2ySDqg/l9rSUwvOcm6yqVai/o1Oe/i8z0poV5fU6053QjDUztF9d0kdHywXPCMo2uyBomL7t6nWoN5NL1s19S5oV5fU65n6CcFQO0f33SXZDD2hvc3XZktStWKHNpuXteJ82Zw9ob1d0mZ/OFgbDLVnCq4c2iSdoR0u0gZLf7VKhza4cljwoQWrDdp5X7TDDtkkcEQw1J7BUC1NLlde1h8orc+htY2q8nnTm7a8FX0veHLmtGCoPYOhxtBuF2nVZyi1MofWu//dxEpvssn7A0M9LRhqz/CapBg1L56dar27X1qTQysZaqtz+stpti4M9bRgqD2DoSbQnldojVuqWodDaxhqgTfENBizzd8lBYNmk8ARwVB7BkNNo52vUPPLv1qBQ20NtWDjScjm7xgM9bRgqD1TMCfaJH2j/a9Tw1NVTe1QQ0PV1HV6+eqNraJjMNTTgqH2DIuSPDR5FGSqJu8A0qQONXlGVpNWy1bRPRjqacFQewZDdaKj0EKVZ6uazqHKx2Yqv2k6q7t8Tu7uFByi2SRwRDDUnilYn2mTnIHiV/2lVWMnmsuh4uoKthOPittzdHQgHLJJ4IhgqJ2jO+6SbIbzoGPRTp9//b2tLo2mcCj3VcPvf/hZq8eHZvX486+VJ80HRQdiSes9fAUbg6F2ju67S2q4sGX/DJ19+erN4EM6CuvIb6sF1+pvsqlmGaxUS66vwTaa3OXdP9rzJWGo3YChdo7uu0vqe0FmwWqRlfTxl9/Y5o0U3860qUYGEy3+zOoaGk6O/UcYx0K7uqRex+GEYKido/vukvp71ep7Tz4p9qe1NZwczzpr8UmzTfVQ8bnybTQ4a+UCrr2hPVzSqS4L9Q2G2jm67zpkkxyU+g+gbqnn3/4wnETeWq6/uTX2/emzF/rb7tXkcaO7U3C53iaBg4Khdk7BRU6b5EAc0UiQ6ND3FM+2x8EUDLVzzvOyJKy0P9m/8v7RPjhkk8BBwVD7R3ffJR3rUYeCK2zoWDrWBqmtX1Lzt0DDHcFQ+0f34CUdaA8vXryDDqdD2GrBG0L6Xld/NjDU/tE92CGbZG80/OQ1Oor2vx644A4LS3x7AkPtH92DHbJJ9oO2FZ1P43LovaENdcgmgeOCofaP7sEO2SR7gLNSNGqfNya0lQ7ZJHBcMNT+Kfj2xezbBu4IK3jRrHJfX7w22j6HbBI4Lhhq/xS40a4O/1d9gTs6uvbjqWVvSLZ54LhgqKdAd2KHbJK7gJsij/awtKfglQ59vBwKRjDUU6D7sUN3X82/8zfQor3p7pdVtEEO2SRwaDDUUzC4o+7KDtk8m6FNQTvQL7/9MRzlPP/2h4Gnz14MJ4UDt39+9+NPBedna8huS9tQtmLO5oFDg6GeBd2VHbrL0qSyialegx8UXzYc3GUndtJEbS9OFDyaWam7fDFJG+HQcBRi88ChwVDPgu7NPtk8q1KwILlGa3yH8v0PP9vt1+ISGg4IPvjoC9udhmz5QdbtL/9qCxyySeDoYKhnQfdmn2ye9djs3HQNH51lM/+o0do+ailbDZurLc//Ct44eNl254JtwFDPQtlt1G1eSVM2H2Xp6bMXtt4tKRv/lbSl2aRZ+4KwrXENtFafbB44OhjqidAd2iebpzlaZTv9/c+/2xwTONnsLDym/VjplFVt1VbXluEUX6t06C43emFtMNQTUfZtllWXJq1nMDt/i/p6HZ/VUT7ZvdLtZ1tRQ7Qyn2we6AAM9UQU37uyqVqhNbXQqkcAbdnmJqutd+doB1rI1tKEsnPr7ddMwTZgqOdC92yfbJ4maDXV2s9b6LLQbrSWrXH/rPHdeFtLPVqHT9svBINtwFDPRdn9nuYH1M0veB73FW5l1+GzZCs9CsXXVGKyVdRQ3DybCvoAQz0dunP71PaWpGavUHOz35INljdfjr/+RftTJ5u/GE3tlk0FfYChng7dud2yqQooO0WOqa3Nb4/2ZzU9//YHW/uxaPjSD5u8gOJLCzYVdAOGejqKLa3JHUpNWiGb/FgUz8hlsg04HK1GrMmaZ03q06EvqMAiGOoZ0b3cLZsqi1YvNzj6Ncwb2quVdfSz+Rut7r5Xvi2r4BvDN+3qqWhoDoZ6UnRH96nm+LrVl01t5iPSajSyZJtxULRjRSo+LCtegdzkzBj2DIZ6UnRfd6v40F4TFcmmPSLF5zf1so05KE1uqdq0HjSLWzYVdAaGelJqLp3ZbGmarGUtPp/YIdq3bWXbc1DKXqogsmnTaPkc2WzQGRjqedHd3a3c1UlaPl/7fANtGU1OrWpkm3Rcao4LR9m0MYoX9F24e3oOMNRTozt9jmy2WbRYvmzO43KXW6dWfSxQulFjcjc572LUmHcHjy2BBwz11NRcNPNcgy1+lcyonl7S1uTN761e/2ubd1zqPdXmtGiZHNls0CUY6tnRXT9HNlvD5Je+3PShejQuYUCaGHNnY7u2p1aOuU0IXYKhnp3KZ0MTFw81NFMH+miMB+1evqbfSH/8+Vf9OV893Zl+qLske0k+ElZ5od4mhF7BUKF2rrcJ69M6b2sdBe1evuyANFnc1NlRS80tjEtkS64c586uBEAaDBX+g04DmWqbMHHWe0S0e/mK3a7WuCJ1NuNX+p9kq7zS++TTr2wLoWMwVPgPlRe1Lu/ORDUXJBNX3o5I/cBezCw/RUOL1JmnavdyND1lr3TTS/IPB12CocJ/0ckgX7c8la9xsA07Lmu76UP1aI+ymQ+Ndi9HTZIMevnqjW0Y9A2GCv9Dp4R8VSaxTTou2rciTRciJdBiReI89aZhHOrPTe09bzgDGCr8j/pnD2rU06JT7VuRYrdOLU1OhS99rVGqvJlaKdseOAMYKrzDvaahbl4l0+oabO6XSVr94V4/vrXJD0rNvfwa2ZbAScBQQdHpYX11sxCp8lHIqWzyRTRFqbr5czy0GxO/OrtyDllgqDCDThIryzbgiLQ6N72UWppmqVA3l99bXQx3qptxgzIwVJih+BPKBfLfKdwz2qs62fxONFGd+linqr1aTWWHQdATGCrMU/lKQr9s1YdDu1SnmvdaNDxLvqmDZUrNxyQmWzWcDQwVomwwE9lKj4X2p4VsLVmssVS7xuP3gPZnBdlK4YRgqJBi7VtQtsajsNJV8SafodakLZS76nhX1H9GMK2jH3BAKzBUWGA9Tz3uLbrPv/5eO9NCrW7Crfcns3UdhfXGhGW9MIKhwjI6hbRQK/PYGO1GU9nqitHUTXXQEzLtRgvZWuDMYKjgQieSFjrWMwaVnwZbVNtXWzR8InZWw/HQgWx1pevznJuCgKGClzVWu9xk69oPK83FVrbqSrSCdbTzo6Lf//xLW9xIti4ADBUyaPV+u1nt7eOR73/42Xo33qxsAyrZsvE7fBf868e32sp2OtDZOWwJhgp5rDpPXfbx4ONwLr6lG13W6fXaS1ut9rDKbLC6tV/haysFuIGhQjZr35+7afu7dOtdHlyUbUwT7tijje8vbrZN2qoBRjBUKGGDdz6MGk441rsa3OTjl5VyfvS0gC3/TDGtcfI9svZKsal6+g4PrASGCuXolLOVhhOvYSbNPQd6/8PPhlKr3gYuk21qQ+54khrT4EwFR0hDkbWv5SbUxxunYW0wVChHZx1UJDuwDdn+TmqvsmMLIGCoUI5OOShfG5z6aJWoSHZgAQQMFQpZ6fV7Z5Md2OZolahIdmABBAwVCtn4wZJeZQe2OTu8jXpEbbzmHI4IhgqF6HyD8rXZ+xC0YpSvQ39vB7YBQ4US9vA8RgeyA7sSWjEqkh1YgCkYKpSw5fN/HcsO7Epw1beJ7MACTMFQoQSdac6t2wvi9X+XtOWLAgo+bHD7+o3+77nV5PPv0DEYKpSgM81ZNX5rpeCjNAUvN6hBq1/S+Jq9gq71qraf2IP+wFChBJ1pHHro686rrPkseImPHdVV0eodkgx3f0djK41vQ9QflsS7fCENhgrZlJ2yVBbfj2bPLDXIIZtkVbR6h2ySh6JDh/1Ivt6qPztkBwRgBEOFbApWJNlD+6fPXmjQ7pV4i72GOmSTrIpW75BNcmODT6Q11+yH0DXIIZsEYARDhWwK3i+ffuByz2tQZydiixZzyCZZlYJBThxAjOz8wCj9BQWNdsgmARjBUCEbnWMc8iyPLFiJuqrSc7GghR2ySVbl5as32oIlZX0wvMCw15PzJQxazCGbBGAEQ4VsdI5xyCZZpODCcqVq1nBqriXZa+BrU3DruriR25+2Dk3NOgC6UXDh2iYBGMFQIRudYxyySfwMTrDe+tIh8+wio1w075Kcp1Bt0UY4ZJPkst43aIcxrPx6ecFBm00CMIKhQjY6xzhkkxQz+N8wDxacW1yuU/BQtomDClrTkmrOhovRRjhkk1QyWGDBxedL+Kp8279dwZm0TQIwgqFCNjrHOGSTdIZ2eEltjcGJNsIhm6QnCm7b2yQAIxgqZKNzjEM2SWdoh5eEoe4E7fCSbAaAEQwVstE5Zkl3uV+4MdrnJdkMG6CNcMgm6Qzt8JJsBoARDBWy0TlmSRiqlc2wAdoIh2ySztAOL8lmABjBUCEbnWOWhKFa2QwboI1wyCbpDO3wkmwGgBEMFbLROWZJGKqVzbAB2giHbJLO0A4vyWYAGMFQIRudY5aEoVrZDBugjXDIJukM7fCSbAaAEQwVstE5ZkkYqlXBa33q0UY4ZJN0hnZ4STYDwAiGCtnoHLOkX377wybpDO3zknhsZidoh5dkMwCMYKiQjc4xDtkknaEdXtJp35S0Kwreb2yTAIxgqJCNzjEO2SSdoR1ekvOrcG3RRjhkk/QE7/KFtmCokI3OMQ7ZJJ2hHV7SXe4rayMcskl64vXjW+3wkmwSgBEMFbLROcYhm6QztMMO2SSrUvDe2svmjdwY7a1DNgnACIYK2egc45BN0hnaYYdsklX5/OvvtQVLustp9JZohx2ySQBGMFTIRucYh54+e2Hz9IR22CGbZFUKPnh3l5VTW6IddsgmARjBUCGbgqn5LmtwtkQ77JBNsipavUN3ebZnS7TDDtkkACMYKmRTsDby0vtMpL11yCZZFa3eIZukM7TDDtkkACMYKpSg04xDNklPFBxkvPfkE5tnPbR6h2ySztAOL6n7Cy1QCYYKJehM45BN0hMFa2g3vkOp1Ttkk/TE02cvtMNL6v4aOFSCoUIJOtM4ZJN0hnbYIZtkJYazYa17Sa8f39o8PaEddsgmAZiCoUIJv/z2h042S7JJOkM77JBNshIFV6RZmG1lkwBMwVChhIKHGl++emPz9ETBQcZm35zRih2ySTpDO+yQTQIwBUOFQnSyccgm6YmC26iXrcZEa3XIJumJ3//8Szu8pO5P2aEeDBUK0fnGIZukM7TDDtkkzfn4y2+01iUNfmPz9IR22CGbBEDAUKGQ7378SaecJXX/YVTtsEMbXAnXKh16/8PPbJ5uKDjCuGCo4ABDhUKGOVenHIdsnp7Q3vpk87RF63PIJukJ7a1PNg+AgKFCOTrlOGST9MTf//yrHXbI5mmL1ueQTdIT2lufbB4AAUOFcnTKcWizda13oeysfdVXJhVcmb/0bh7aW4d4pQN4wFChHJ11HBrO4WyentAOO7TqrWWtzKG+X+nAEQasB4YK5RS8vO3S+4KXl6/eaIcdWukkFfOwaG8d6vsIAxqCoUIVOvc4xEmq1UqPqWg1Ptk83VB2hLHS4Q70B4YKVejc45PN0xPaW59snkqefPqV1uHQxq/s3xjtrU82D8AsGCrUotOPQ31f9S1bmtR8TLQCn2yentDeOvTxl9/YPACzYKhQi85APtk8PaG99cnmqUGz+2TzdEPB6wYvXQ8INAdDhVp0BvKp7281a299ajgmmtqnhg3YG2VvR7pgqJADhgq1MFVZCr7Gc5NNVUDZNedLo9r3iXbVp46PMGANMFRogM5DPvX9NIL21qfHn3+1qXLRpD51vPq64HOwN9lUAAkwVGhA2YLSS9cT1h1P3DWjTzZPN2hXfep7wTOsAYYKbdDZyKe+5yztrU+VJ+5l7xNe6UHYPcDpKWwGhgpteO/JJzoh+dTxd5u1q24Vf9Ptl9/+0Fw+2VR9UPYyr5tsNoA0GCo0Qyckt2yqPiheHHQpGpONqzsE2k+3eBs+FIChQjN0TnKr41e7aVfdKvgsj6Zwq9e1rMVXTS79HmHAqmCo0BKdltzCU62yLoYX3ym8dGoenK/D9mCo0JKyb63cZLP1wQZWV3Mq1uuhjPbTrSZPLsE5wVChMTo/5chm6wPtZ45sNouWyZHN1gGDKWo/3bLZAJxgqNCY4oWml6Ibh4egZn5fvMFZ9kmym7pcelP8BPCl68eHYAMwVGiPzlI5stn6QPuZo4TtFb9S4yab8OjUXP2+9DggsCUYKqyCTlQ5stn6QPuZo9k7nTUnvpdOx1k7maPZQQbwg6HCKrx+fKvTlVu9XnbTfmaqbcLmn1/dA9rJTNmEAFlgqLAWOl1lyibsAO1kpsY8H3z0hf6WKdu2o6M9zJRNCJALhgprUfwJs1E259FpZYT6v5nq79pm2RuMRw3bqs0JkAuGCitSOc0tLnA9IjWroG+qHNXiFwXvlsoB6fi7dbAxGCqsi85e+bI5j472cFvZ9hwa7V6+bE6AMjBUWJeadyfdVPk5sx1S+axLjTq72KvdyxcXe6EhGCqsTs2D9qM6e+dD5eOSZbLNOC5NBrCzjQruDoYKW1B/4/DSlx88tDi7ylLi7RCHo+Yrp1PZzAA1YKiwETqZFamzpye1e2vK1n5Qah5xnqqzq9+wBzBU2A6d0orU2cdAtHvryNZ7RJpc5r3JJgeoB0OF7ah/CnOUTX5ctG+tZWs8KNqxUnFuCiuBocKm1HwcVNTNqWrDEy+rDsyj4XHYhYVIsCYYKmxNzefGrGz+I9LWM0Z1YB6t1h/d9PGX39gqAFqBocIdaLLod6oOFitVfjrG6ujvmWrytNVUuCmsDYYK96G5pz7/9gdby1H4/c+/tD+NdMRhWePFF0c/vIBDgKHC3WjuqZcDXgFewzxEg1sf6E5q8zP1C+emsBUYKtyTNTz1cpAvqmqj19eez9Lqv00UE24Km4Ghwp1p9Zy+1W79o/LrKJXa29dmmt8rnaqDZVlwIDBUuD+rTqmXfZywvv/hZ9qse2vw9afPXtimbsAwGitdnJjqQBe6oQ8wVNgFKz03IrrLYuC1DxfqteX3fNo+NJWQrRpgbTBU2Aurvt9AtMGVwP37qNVwKr/GyAx/2TWWGiW0Ri8AFsFQYV+s9wBJQi9fvan8GMvTZy/Wuxl8Xw1eOBwceMZnsLFhHDb2TpGnnQArgaHC7tA58h4aXOH5tz8MDBO0cPv/+9oGmtXe1lvB2cBQYafoZIlQUnYTAtgYDBX2i06ZCM3piG+Dgi7BUGHXvHz1RqfPc+t2j1D/98Sy2wzAvcBQ4QBs8Mzi/iXnYVsuit6n7vIQFEACDBWOwQ5fjLCl7IDcuMui6Lvr73/+tUMBcHcwVDgSJzwts4NgOc+S4z289AogBoYKx+Mk/pG71kbLdyfbZYBdgaHCUdHpti/Z/no44uuZPMo9tgC4CxgqHJvOzlZbOcdmr8xdVcMf13YNYLdgqNADgw/pZHw0rfHhl+MebRzro+gANzBU6IrDPWCzzUdb1/t8d1vx7kA4NBgqdMhwtqdT9f60/WOUH3z0xT4fs7njl1kBGoKhQs8MM7VO3vfWcA5t27kx+zlhbXXPGGAPYKhwFu54n/XjL7+x7dkJ7z35ZMv3Ow51bX9qDrANGCqcjg8++mKD1TqvH98ecVnNcNjR9rLw3//8y51ROAkYKsB/GMyv4CunQ/x3P/70+dff24RdMn4UdjjnHoZr6Pj4PzYY4GxgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGgAhgoAANAADBUAAKABGCoAAEADMFQAAIAGYKgAAAANwFABAAAagKECAAA0AEMFAABoAIYKAADQAAwVAACgARgqAABAAzBUAACABmCoAAAADcBQAQAAGoChAgAANABDBQAAaACGCgAA0AAMFQAAoAEYKgAAQAMwVAAAgAZgqAAAAA3AUAEAABqAoQIAADQAQwUAAGjA/wez6PPBCEqueAAAAABJRU5ErkJggg==>
[image18]: <data:image/png;base64,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>
```