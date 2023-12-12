
# !pip install ryu

from ryu.lib.packet import *
from ryu.lib.packet import in_proto
from ryu.lib.packet import packet, ethernet, ipv4, tcp, udp, icmp, in_proto
from ryu.base import app_manager
from ryu.controller import ofp_event
from ryu.lib.packet import ipv4
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.lib.packet import icmp
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet
from ryu.lib.packet import tcp
from ryu.lib.packet import ethernet
from ryu.lib.packet import ether_types
from ryu.lib.packet import udp
from ryu.lib import hub
from ryu import cfg
import configparser

keystore = {}
INTERVAL = 10


def calculate_value(key, val):
    '''
    store the val in kv. and calculate the rate per sec
    '''
    global keystore
    if key in keystore:
        # calculate the rate per second
        rate = (val - keystore[key]) / INTERVAL
        keystore[key] = val
        return rate
    else:
        keystore[key] = val
        return 0


class QosApp(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(QosApp, self).__init__(*args, **kwargs)
        self.mac_to_port = {}
        self.datapaths = {}
        self.stats = {}
        # reading input from config file.

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):

        def run_adaptive_algo(self):
            self.logger.info("Run Adaptive algorithm Check")
        self.logger.info(self.stats)

    def send_meter_stats_request(self, datapath):

        @set_ev_cls(ofp_event.EventOFPMeterStatsReply, MAIN_DISPATCHER)
        def meter_stats_reply_handler(self, ev):
            stats = []
            for stat in ev.msg.body:
                stats.append('meter_id=%d len=%d flow_count=%d '
                             'packet_in_count=%d byte_in_count=%d '
                             'bandwidth=%d' %
                             (stat.meter_id, stat.len, stat.flow_count,
                              stat.packet_in_count, stat.byte_in_count,
                              stat.band_stats[-1].byte_band_count /
                              INTERVAL))
            self.logger.info('MeterStats: %s', stats)

            def add_meter(self, datapath):
                ofproto = datapath.ofproto
                parser = datapath.ofproto_parser
                QOS1_METER_ID = 1
    # meter table for QoS1 traffic
                bands = [parser.OFPMeterBandDrop(rate=self.qos1_bw)]
                req = parser.OFPMeterMod(datapath=datapath, command=ofproto.OFPMC_ADD,
                                         flags=ofproto.OFPMF_KBPS, meter_id=QOS1_METER_ID,
                                         bands=bands)
                datapath.send_msg(req)

    # meter table for QoS2 traffic
                bands = [parser.OFPMeterBandDrop(rate=self.qos2_bw)]
                req = parser.OFPMeterMod(datapath=datapath, command=ofproto.OFPMC_ADD,
                                         flags=ofproto.OFPMF_K)

                def add_flow(self, datapath, priority, match, actions, buffer_id=None, idle=0, hard=0, meterid=0):

                    def get_meter_id(self, protocol, src_port=0, dst_port=0):

                        @ set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
                        def _packet_in_handler(self, ev):

                            CONF = cfg.CONF
                            QOS_ENABLED = CONF.DEFAULT.QOS_ENABLED
                            ALGORITHM = CONF.DEFAULT.ALGORITHM
                            QOS1_BANDWIDTH = CONF.DEFAULT.QOS1_BANDWIDTH
                            QOS2_BANDWIDTH = CONF.DEFAULT.QOS2_BANDWIDTH
                            BE_BANDWIDTH = CONF.DEFAULT.BE_BANDWIDTH

                            QOS1_METER_ID = 1
                            QOS2_METER_ID = 2
                            BE_METER_ID = 3

    class QosApp(app_manager.RyuApp):
        OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(QosApp, self).__init__(*args, **kwargs)
        self.mac_to_port = {5000}
        self.datapaths = {}
        self.stats = {}
        self.meter_configs = {}
        self.meter_tables = {}
        self.adaptive_last_run = 0
        self.adaptive_interval = 60

    @ set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def switch_features_handler(self, ev):
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser

        self._set_meter_configs()
        # configure meter tables
        for meter_id, bandwidth in self.meter_configs.items():
            meter = parser.OFPMeterMod(command=ofproto.OFPMC_ADD,
                                       flags=ofproto.OFPMF_KBPS,
                                       meter_id=meter_id,
                                       bands=[parser.OFPMeterBandDrop(rate=bandwidth)])
            datapath.send_msg(meter)

            self.meter_tables[meter_id] = {
                "utilized": 0, "free": bandwidth}

    def _set_meter_configs(self):
        # Define constants for QoS1
        QOS1_METER_ID = 1
        # Define constants for QoS2
        QOS2_METER_ID = 2
        BE_BANDWIDTH = 2500
        BE_METER_ID = " "
        # Define constants for QoS1
        INTERVAL = 5  # seconds
        QOS1_BANDWIDTH = 5000  # kbps
        QOS2_BANDWIDTH = 2500  # kbps
        self.meter_configs[QOS1_METER_ID] = QOS1_BANDWIDTH
        self.meter_configs[QOS2_METER_ID] = QOS2_BANDWIDTH
        self.meter_configs[BE_METER_ID] = BE_BANDWIDTH

    def _get_meter_id(self, protocol, src_port=0, dst_port=0):
        QOS1_METER_ID = 1
        QOS2_METER_ID = 2
        BE_METER_ID = " "
        if protocol == in_proto.IPPROTO_UDP:
            if dst_port == 5000:
                return QOS1_METER_ID
            elif dst_port == 6000:
                return QOS2_METER_ID
        elif protocol == in_proto.IPPROTO_TCP:
            if dst_port == 8000:
                return QOS1_METER_ID
            elif dst_port == 9000:
                return QOS2_METER_ID
        return BE_METER_ID


@ set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
def _packet_in_handler(self, ev):
    msg = ev.msg
    datapath = msg.datapath
    parser = datapath.ofproto
