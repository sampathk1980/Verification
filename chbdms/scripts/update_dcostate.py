import grpc
import threading
import sys
import time

from infinera.chm6.common.v2 import sys_constants_pb2

from grpc_client_adaptor import CrudService

from infinera.hal.chm6.v1 import chm6_constants_pb2

def create_dcostate_object(dco_id):
    dco_state = sys_constants_pb2.DcoState()
    dco_state.base_state.config_id.value = "dco-" + str(dco_id)
    dco_state.base_state.timestamp.value = time.ctime()
    dco_state.base_state.mark_for_delete.value = False
    
    dco_state.aid = "dco-" + str(dco_id)
    
    dco_state.hal.dco_capabilities.SupportedClient.name = "client-2"
    dco_state.hal.dco_capabilities.SupportedClient.band_width = 2
        dco_state.hal.dco_capabilities.SupportedClient.name = "client-3"
    dco_state.hal.dco_capabilities.SupportedClient.band_width = 1
    
    dco_state.hal.dco_capabilities.SupportedLineMode.application_code = "line_app_code_2"
    dco_state.hal.dco_capabilities.SupportedLineMode.client_mode = 3
    dco_state.hal.dco_capabilities.SupportedLineMode.capacity = 100
    dco_state.hal.dco_capabilities.SupportedLineMode.baud_rate = 20
    
    return dco_state


def create(dco_id):
    try:
        crud = CrudService()
        dcostate = create_dcostate_object(dco_id)
        print(crud.create(dcostate))
    except grpc.RpcError as err:
        print("Set failed")
        print(err.details)

if __name__ == '__main__':
    dco_id = sys.argv[1]
    create(dco_id)