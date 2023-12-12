'''

h1,h3,h5---  s1				s5 -----h2,h4,h6
               \          /
                s2 ---- s4
               /           \
h7,h9  ---  s3				s6------h8,h10



DOI: 10.1109/ANTS.2016.7947874 : Adaptive QoS for Data Transfers Using Software-Defined Networking  (Publisher: IEEE )


'''
#  !pip install mininet
#  !pip install macpath

import os
import time
from mininet.node import RemoteController
from mininet.cli import CLI
from time import sleep
from macpath import join
from mininet.topolib import TreeTopo
from mininet.topo import Topo
from mininet.net import Mininet
from pydoc import cli
import re
from mininet.log import setLogLevel
from mininet.link import TCLink


scenario = 8
workingDir = os.getcwd()
capture_script = join(workingDir, 'capture.sh')
sd_flow_filepath = join(workingDir, 'testVideos/360x240_2mb.mp4')
hd_flow_filepath = join(workingDir, 'testVideos/720x480_5mb.mp4')
be_flow_filepath = join(workingDir, 'testVideos/caribbean.mp4')
stream_time = 620
savedStreamsDir = join(workingDir, 'savedStreams')
capturedTracesDir = join(workingDir, 'capturedTraces')


class MyTopology(Topo):
    "6 switch connected to n hosts."

    def build(self):
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        h1 = self.addHost('h1', mac="00:00:00:00:00:01", ip="10.1.1.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:02", ip="10.1.1.2/24")
        h3 = self.addHost('h3', mac="00:00:00:00:00:03", ip="10.1.1.3/24")
        h4 = self.addHost('h4', mac="00:00:00:00:00:04", ip="10.1.1.4/24")
        h5 = self.addHost('h5', mac="00:00:00:00:00:05", ip="10.1.1.5/24")
        h6 = self.addHost('h6', mac="00:00:00:00:00:06", ip="10.1.1.6/24")
        h7 = self.addHost('h7', mac="00:00:00:00:00:07", ip="10.1.1.7/24")
        h8 = self.addHost('h8', mac="00:00:00:00:00:08", ip="10.1.1.8/24")
        h9 = self.addHost('h9', mac="00:00:00:00:00:09", ip="10.1.1.9/24")
        h10 = self.addHost('h10', mac="00:00:00:00:00:10", ip="10.1.1.10/24")

        self.addLink(s1, s2, cls=TCLink, bw=10)
        self.addLink(s3, s2, cls=TCLink, bw=10)
        self.addLink(s2, s4, cls=TCLink, bw=10)
        self.addLink(s4, s5, cls=TCLink, bw=10)
        self.addLink(s4, s6, cls=TCLink, bw=10)

        self.addLink(h1, s1, cls=TCLink, bw=10)
        self.addLink(h3, s1, cls=TCLink, bw=10)
        self.addLink(h5, s1, cls=TCLink, bw=10)
        self.addLink(h7, s3, cls=TCLink, bw=10)
        self.addLink(h9, s3, cls=TCLink, bw=10)
        self.addLink(h2, s5, cls=TCLink, bw=10)
        self.addLink(h4, s5, cls=TCLink, bw=10)
        self.addLink(h6, s5, cls=TCLink, bw=10)
        self.addLink(h8, s6, cls=TCLink, bw=10)
        self.addLink(h10, s6, cls=TCLink, bw=10)


def initiateCapture(h):
    def getOutFilepath(inFilepath, i):
        def stream(src, dst, input_filename, output_filename, dstIP, portID):
            def waitOutput(process):
                process.wait()


def stream_traffic(net):
    if __name__ == '__main__':
        setLogLevel('info')
        topo = MyTopology()
        c1 = RemoteController('c1', ip='127.0.0.1', port=6653)
        net = Mininet(topo=topo, link=TCLink, controller=c1)
        net.start()
        print(" Waiting for 10 seconds to start the traffic test ...")
        sleep(1)
        net.pingAll()
        if scenario == 0:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
            # qos1
            h1.cmd(
                'command to be defined in order to carry out the test scenario 0 streaming rtp port udp')
            h3.cmd(
                'command to be defined in order to carry out the test scenario 0 streaming rtp port udp')
            h5.cmd(
                'command to be defined in order to carry out the test scenario 0 streaming rtp port udp')
            # server h1 streams to client h2
            # server h3 streams to client h4
            # server h5 streams to client h6
            # demo static QOS(5,5,5)
            h2 = net.get('h2').cmd(
                'command to be defined in order to carry out the test scenario 0 streaming rtp port udp')
            # qos2 traffic
            h4 = net.get('h4').cmd(
                'command to be defined in order to carry out the test scenario 0 streaming rtp port udp &')
            # be traffic
            h6 = net.get('h6').cmd(
                'command to be defined in order to carry out the test scenario 0 streaming rtp port udp &')
            # streaming rtp port udp
        if scenario == 1:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
            # qos1
            h1.cmd('command to be defined in order to carry out the test scenario 1')
            h3.cmd('command to be defined in order to carry out the test scenario 1')
            h5.cmd('command to be defined in order to carry out the test scenario 1')
            # server h1 streams to client h2
            # server h3 streams to client h4
            # server h5 streams to client h6
            # demo1 for adaptive qos (5,3,2)
            # qos1 traffic
            h2 = net.get('h2').cmd(
                'command to be defined in order to carry out the test scenario 1')
            # qos2 traffic
            h4 = net.get('h4').cmd(
                'command to be defined in order to carry out the test scenario 1')
            # be traffic
            h6 = net.get('h6').cmd(
                'command to be defined in order to carry out the test scenario 1')

            # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )
        elif scenario == 2:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
            # qos1
            h1.cmd('python3 -m http.server 8001 &')
            h3.cmd('python3 -m http.server 8003 &')
            h5.cmd('python3 -m http.server 8005 &')
            # server h1 streams to client h2
            # server h3 streams to client h4
            # server h5 streams to client h6
            # demo2 for adaptive qos (5,3,2)
            # qos1 traffic
            h2 = net.get('h2').cmd(
                'python3 -m curl http://10.0.0.1:8001/big_buck_bunny_480p_stereo.ogg > /dev/null &')
            # qos2 traffic
            h4 = net.get('h4').cmd(
                'python3 -m curl http://10.0.0.3:8003/big_buck_bunny_480p_stereo.ogg > /dev/null &')
           # be traffic
            h6 = net.get('h6').cmd(
                'python3 -m curl http://10.0.0.5:8005/big_buck_bunny_480p_stereo.ogg > /dev/null &')
           # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )

           # Variation of network latency
           # 1. Define the list of latencies to test
            latencies = [10, 50, 100]
            # 2. For each latency, set the network delay using NetEm
            for latency in latencies:
                print(f"Setting network latency to {latency}ms")
            h2.cmd(
                f"sudo tc qdisc add dev h2-eth0 root netem delay {latency}ms")
            h4.cmd(
                f"sudo tc qdisc add dev h4-eth0 root netem delay {latency}ms")
            h6.cmd(
                f"sudo tc qdisc add dev h6-eth0 root netem delay {latency}ms")
            # 3. Measure video quality using PSNR
            # ... command to measure PSNR ...
            # 4. Record
            # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )
        elif scenario == 3:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')

            # Set up video streaming servers on h1, h3, h5
            h1.cmd(
                'vlc-wrapper -vvv video.mp4 --sout "#standard{access=http,mux=ts,dst=:8081}" &')
            h3.cmd(
                'vlc-wrapper -vvv video.mp4 --sout "#standard{access=http,mux=ts,dst=:8082}" &')
            h5.cmd(
                'vlc-wrapper -vvv video.mp4 --sout "#standard{access=http,mux=ts,dst=:8083}" &')

            # Define clients h2, h4, h6
            h2 = net.get('h2')
            h4 = net.get('h4')
            h6 = net.get('h6')
           # Set up network jitter on h2, h4, h6
            low_jitter = 'sudo tc qdisc add dev {} root netem delay 10ms'.format(
                h2.defaultIntf())
            medium_jitter = 'sudo tc qdisc add dev {} root netem delay 30ms'.format(
                h4.defaultIntf())
            high_jitter = 'sudo tc qdisc add dev {} root netem delay 50ms'.format(
                h6.defaultIntf())

           # Measure video quality using PSNR
            capture_h2 = 'ffmpeg -i http://h1:8081 -f null - 2> /dev/null | grep PSNR'
            capture_h4 = 'ffmpeg -i http://h3:8082 -f null - 2> /dev/null | grep PSNR'
            capture_h6 = 'ffmpeg -i http://h5:8083 -f null - 2> /dev/null | grep PSNR'

            # Run the test with different levels of jitter
            print("Running the test with low jitter...")
            os.system(low_jitter)
            time.sleep(5)
            psnr_h2_low = h2.cmd(capture_h2)
            psnr_h4_low = h4.cmd(capture_h4)
            psnr_h6_low = h6.cmd(capture_h6)
            print("PSNR h2 (low jitter):", psnr_h2_low)
            print("PSNR h4 (low jitter):", psnr_h4_low)
            print("PSNR h6 (low jitter):", psnr_h6_low)

            print("Running the test with medium jitter...")
            os.system(medium_jitter)
            time.sleep(5)
            psnr_h2_medium = h2.cmd(capture_h2)
            psnr_h4_medium = h4.cmd(capture_h4)
            psnr_h6_medium = h6.cmd(capture_h6)
            print("PSNR h2 (medium jitter):", psnr_h2_medium)
            print("PSNR h4 (medium jitter):", psnr_h4_medium)
            print("PSNR h6 (medium jitter):", psnr_h6_medium)

            print("Running the test with high jitter...")
            os.system(high_jitter)
            time.sleep(5)
            psnr_h2_high = h2.cmd(capture_h2)
            psnr_h4_high = h4.cmd(capture_h4)
            psnr_h6_high = h6.cmd(capture_h6)
            print("PSNR h2 (high jitter):", high_jitter)

       # Scenario 4
        elif scenario == 4:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')

          # QoS1
            h1.cmd('command to be defined in order to carry out the test scenario 4')
            h3.cmd('command to be defined in order to carry out the test scenario 4')
            h5.cmd('command to be defined in order to carry out the test scenario 4')

           # Server h1 streams to client h2
           # Server h3 streams to client h4
           # Server h5 streams to client h6
           # Demo 4 for adaptive QoS (5, 3, 2)
           # QoS1 traffic
            h2 = net.get('h2').cmd(
                'command to be defined in order to carry out the test scenario 4')
            # QoS2 traffic
            h4 = net.get('h4').cmd(
                'command to be defined in order to carry out the test scenario 4')
           # Best-effort traffic
            h6 = net.get('h6').cmd(
                'command to be defined in order to carry out the test scenario 4')

       # Vary packet loss rate
            packet_loss_rates = [0, 1, 5, 10, 20, 30]
            psnrs = []
            for loss_rate in packet_loss_rates:
                # Set the loss rate on h2's interface eth0
                h2.cmd(
                    'sudo tc qdisc replace dev eth0 root netem loss {}%'.format(loss_rate))
        # Wait for a few seconds to stabilize the network
                time.sleep(5)
        # Measure video quality using FFmpeg and PSNR
                output = h2.cmd(
                    'ffmpeg -i video.mp4 -i video_received.mp4 -lavfi "psnr" -f null -')
        # Extract PSNR value from FFmpeg output
                psnr = float(re.findall(
                    'average.*?PSNR.*?([0-9\.]+)', output)[0])
                psnrs.append(psnr)
                print("PSNR h2 (packet loss rate {}%): {:.2f}".format(
                    loss_rate, psnr))

    # Plot results
                import matplotlib.pyplot as plt
                plt.plot(packet_loss_rates, psnrs)

# Scenario 5
        if scenario == 5:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')

            # qos1
            h1.cmd('command to be defined in order to carry out the test scenario 5')
            h3.cmd('command to be defined in order to carry out the test scenario 5')
            h5.cmd('command to be defined in order to carry out the test scenario 5')

            # server h1 streams to client h2
            # server h3 streams to client h4
            # server h5 streams to client h6

            # Set network bandwidth to low (2 Mbps)
            h1.cmd(
                'tc qdisc add dev h1-eth0 root tbf rate 2mbit burst 32kbit latency 400ms')

            # Set network bandwidth to medium (5 Mbps)
            h3.cmd(
                'tc qdisc add dev h3-eth0 root tbf rate 5mbit burst 32kbit latency 400ms')

            # Set network bandwidth to high (10 Mbps)
            h5.cmd(
                'tc qdisc add dev h5-eth0 root tbf rate 10mbit burst 32kbit latency 400ms')

            # demo5 for adaptive qos (5,3,2)
            h2 = net.get('h2').cmd('vlc-wrapper rtp://239.0.1.1:5004')
            # qos2 traffic
            h4 = net.get('h4').cmd('vlc-wrapper rtp://239.0.1.1:5006')
            # be traffic
            h6 = net.get('h6').cmd('vlc-wrapper rtp://239.0.1.1:5008')

           # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )

 # Scenario 6

        if scenario == 6:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
        # qos1
            h1.cmd('command to be defined in order to carry out the test scenario 6')
            h3.cmd('command to be defined in order to carry out the test scenario 6')
            h5.cmd('command to be defined in order to carry out the test scenario 6')
    # server h1 streams to client h2
    # server h3 streams to client h4
    # server h5 streams to client h6
    # demo6 for adaptive qos (5,3,2)
    # qos1 traffic
            h2 = net.get('h2').cmd(
                'ffplay -i tcp://10.0.0.1:1234')
          # qos2 traffic
            h4 = net.get('h4').cmd(
                'ffplay -i tcp://10.0.0.3:1234')
       # be traffic
            h6 = net.get('h6').cmd(
                'ffplay -i tcp://10.0.0.5:1234')
       # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )

        # Set video resolution to 720p using ffmpeg
            h1.cmd('ffmpeg -i bbb.mp4 -vf scale=1280:720 -c:a copy bbb_720p.mp4')

        # Stream the video from h1 to h2 using ffmpeg
            h1.cmd('ffmpeg -re -i bbb_720p.mp4 -vcodec copy -f flv tcp://10.0.0.2:1234')

 # Scenario 7

        elif scenario == 7:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
            # qos1
            h1.cmd('command to be defined in order to carry out the test scenario 7')
            h3.cmd('command to be defined in order to carry out the test scenario 7')
            h5.cmd('command to be defined in order to carry out the test scenario 7')
    # server h1 streams to client h2
    # server h3 streams to client h4
    # server h5 streams to client h6
    # demo7 for adaptive qos (5,3,2)
    # qos1 traffic
            h2 = net.get('h2').cmd(
                'command to be defined in order to carry out the test scenario 7')
    # qos2 traffic
            h4 = net.get('h4').cmd(
                'command to be defined in order to carry out the test scenario 7')
    # be traffic
            h6 = net.get('h6').cmd(
                'command to be defined in order to carry out the test scenario 7')
    # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )

    # Scenario 8
        #!/usr/bin/env python3
        elif scenario == 8:
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
            # qos1
            h1.cmd('command to be defined in order to carry out the test scenario 8')
            h3.cmd('command to be defined in order to carry out the test scenario 8')
            h5.cmd('command to be defined in order to carry out the test scenario 8')
            # server h1 streams to client h2
            # server h3 streams to client h4
            # server h5 streams to client h6
            # demo8 for adaptive qos (5,3,2)
            # qos1 traffic
            h2 = net.get('h2').cmd(
                'command to be defined in order to carry out the test scenario 8')
            # qos2 traffic
            h4 = net.get('h4').cmd(
                'command to be defined in order to carry out the test scenario 8')
            # be traffic
            h6 = net.get('h6').cmd(
                'command to be defined in order to carry out the test scenario 8')
            # streaming rtmp port tcp - dash / hls /nginx (H.264 & H.265 )

            def run_scenario_8():
             # Create network topology
                topo = TreeTopo(depth=2, fanout=2)
                net = Mininet(topo=topo)

           # Start network
            net.start()

           # Run scenario
            print("Starting the servers in h1, h3, h5")
            h1 = net.get('h1')
            h3 = net.get('h3')
            h5 = net.get('h5')
         # Set up video compression rates
            crf_values = [20, 25, 30]
            rate_suffixes = ['05rate', '07rate', '09rate']
            for i in range(len(crf_values)):
                crf = crf_values[i]
                suffix = rate_suffixes[i]
        # Encode video with current compression rate
                in_filename = 'bbb.mp4'
                out_filename = 'bbb_{}.mp4'.format(suffix)
                cmd = 'ffmpeg -i {} -crf {} -preset medium -c:a copy {}'.format(
                    in_filename, crf, out_filename)
                h1.cmd(cmd)
        # Stream video to client
                client = net.get('h2')
                cmd = 'ffmpeg -i {} -vcodec copy -acodec copy -f mpegts udp://{}:1234'.format(
                    out_filename, client.IP())
                h1.cmd(cmd)
            if __name__ == '__main__':
                setLogLevel('info')
                run_scenario_8()

    # Stop network
    CLI(net)
    net.stop()
