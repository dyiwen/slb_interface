#! /usr/bin/env python
# coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkslb.request.v20140515 import DescribeLoadBalancersRequest
from aliyunsdkslb.request.v20140515 import DescribeLoadBalancerHTTPListenerAttributeRequest
from aliyunsdkslb.request.v20140515 import DeleteLoadBalancerRequest
from aliyunsdkslb.request.v20140515 import AddBackendServersRequest
from aliyunsdkslb.request.v20140515 import RemoveBackendServersRequest
import json
import sys
import os



accessKey = "KEY"
accessSecret = "Secret"
region = "Region"
client = AcsClient(
	accessKey,
	accessSecret,
	region
	)

def get_single():
	request = DescribeLoadBalancersRequest.DescribeLoadBalancersRequest()
	request.set_accept_format('json')
	request.set_PageSize(100)
	request.set_PageNumber(1)
	response = json.loads(client.do_action_with_exception(request),encoding='utf-8')

	for info in response.get('LoadBalancers').get('LoadBalancer'):
		slb_no = info.get('LoadBalancerId')
		print slb_no
		slb_name = info.get('LoadBalancerName')
		print slb_name
		slb_status = info.get('LoadBalancerStatus')
		print slb_status
		slb_address = info.get('Address')
		print slb_address
		address_type = info.get('AddressType')
		print address_type
		bandwidth = info.get('Bandwidth')
		print bandwidth
		create_time = info.get('CreateTime')
		print create_time
		ListenerPort = info.get('ListenerPort')
		print ListenerPort
		print "-"*80

def get_keys():
	request = DescribeLoadBalancersRequest.DescribeLoadBalancersRequest()
	request.set_accept_format('json')
	# request.set_PageSize(100)
	# request.set_PageNumber(1)
	response = json.loads(client.do_action_with_exception(request),encoding='utf-8')
	print json.dumps(response,sort_keys=True, indent=4, separators=(',', ':'))

def slb_set():
	request = DescribeLoadBalancerHTTPListenerAttributeRequest.DescribeLoadBalancerHTTPListenerAttributeRequest()
	request.set_LoadBalancerId('slb_id')
	request.set_ListenerPort(18080)
	response = client.do_action_with_exception(request)
	# data = json.loads(response)
	# HealthCheck = (data['HealthCheck'])
	# print "更新前的配置信息"
	# print json.dumps(data,sort_keys=True,indent=2)


def delete_slb():
	request = DeleteLoadBalancerRequest.DeleteLoadBalancerRequest()
	request.set_accept_format('json')
	request.set_LoadBalancerId('')
	response = json.loads(client.do_action_with_exception(request),encoding='utf-8')
	print json.dumps(response,sort_keys=True, indent=4, separators=(',', ':'))


def add_backend_server(key):
	request = AddBackendServersRequest.AddBackendServersRequest()
	request.set_accept_format('json')
	request.set_LoadBalancerId('slb_id')
	request.set_BackendServers([{"ServerId":key,"weight":"100"}])
	response = json.loads(client.do_action_with_exception(request),encoding='utf-8')
	print "-"*80
	print json.dumps(response,sort_keys=True, indent=4, separators=(',', ':'))
	print ""
	print "-"*80

def remove_backend_server(key):
	request = RemoveBackendServersRequest.RemoveBackendServersRequest()
	request.set_accept_format('json')
	request.set_LoadBalancerId('slb_id')
	request.set_BackendServers([key])
	response = json.loads(client.do_action_with_exception(request),encoding='utf-8')
	print "-"*80
	print json.dumps(response,sort_keys=True, indent=4, separators=(',', ':'))
	print ""
	print "-"*80



