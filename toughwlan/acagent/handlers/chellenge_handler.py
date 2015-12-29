#!/usr/bin/env python
# coding=utf-8

from twisted.internet import defer
from txportal.packet import cmcc, huawei
from toughwlan.acagent.handlers import base_handler

class ChellengeHandler(base_handler.BasicHandler):

    @defer.inlineCallbacks
    def proc_cmccv2(self, req):
        resp = huawei.Portal.newMessage(
            cmcc.ACK_CHALLENGE,
            req.userIp,
            req.serialNo,
            cmcc.CurrentSN(),
            secret=self.config.ac.key
        )
        resp.attrNum = 1
        resp.attrs = [
            (0x03, '\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08')
        ]
        yield
        defer.returnValue(resp)

    @defer.inlineCallbacks
    def proc_huaweiv2(self,req):
        resp = huawei.PortalV2.newMessage(
            huawei.ACK_CHALLENGE,
            req.userIp,
            req.serialNo,
            cmcc.CurrentSN(),
            secret=self.config.ac.key
        )
        resp.attrNum = 1
        resp.attrs = [
            (0x03, '\x01\x02\x03\x04\x05\x06\x07\x08\x01\x02\x03\x04\x05\x06\x07\x08')
        ]
        yield
        defer.returnValue(resp)