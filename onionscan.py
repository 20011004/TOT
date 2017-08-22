import json, subprocess, os

from canari.maltego.message import Entity, StringEntityField, IntegerEntityField, FloatEntityField, BooleanEntityField, DateEntityField
from canari.maltego.transform import Transform
from canari.maltego.entities import URL, Phrase, IPv4Address, EmailAddress, Domain
from canari.framework import EnableDebugWindow

@EnableDebugWindow

class BtcAddress(Entity):
    _category_ = 'Personal'
    _namespace_ = 'PR'
    properties_btcaddress = StringEntityField('properties.btcaddress', display_name='BtcAddress', is_value=True)

class onionService(Transform):
    """OnionScan Transform Hidden Service Name"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        response += Phrase(str(data["hiddenService"]))
        return response

class onionDate(Transform):
    """OnionScan Transform dateScanned"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        response += Phrase(data["dateScanned"])
        return response

class onionDetected(Transform):
    """OnionScan Transform Detected"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        response  += Phrase("web: "      + str(data["webDetected"]))
        response  += Phrase("tls: "      + str(data["tlsDetected"]))
        response  += Phrase("ssh: "      + str(data["sshDetected"]))
        response  += Phrase("ricochet: " + str(data["ricochetDetected"]))
        response  += Phrase("irc: "      + str(data["ircDetected"]))
        response  += Phrase("ftp: "      + str(data["ftpDetected"]))
        response  += Phrase("smtp: "     + str(data["smtpDetected"]))
        response  += Phrase("bitcoin: "  + str(data["bitcoinDetected"]))
        response  += Phrase("mongodb: "  + str(data["mongodbDetected"]))
        response  += Phrase("vnc: "      + str(data["vncDetected"]))
        response  += Phrase("xmpp: "     + str(data["xmppDetected"]))
        response  += Phrase("skynet: "   + str(data["skynetDetected"]))
        return response

class onionPGPKeys(Transform):
    """OnionScan Transform PGPKeys"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        response += Phrase(str(data["pgpKeys"]))
        return response

class onionIpAddress(Transform):
    """OnionScan Transform IP Address"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        response += IPv4Address(str(data["identifierReport"]["ipAddresses"]))
        return response

class onionEmail(Transform):
    """OnionScan Transform Email"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())
        for i in data["identifierReport"]["emailAddresses"]:
            response += EmailAddress(str(i))
        return response

class onionBitcoin(Transform):
    """OnionScan Transform Bitcoin"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        try:
            for i in data["identifierReport"]["bitcoinAddresses"]:
                response += BtcAddress(str(i))
        except:
            response += BtcAddress(str("None"))
        return response

class onionRelatedServices(Transform):
    """OnionScan Transform Related Onion Services"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        try:
            for i in data["identifierReport"]["relatedOnionServices"]:
                response += Domain(fqdn=str(i))
        except:
            response += Domain("None")
        return response

class onionRelatedDomains(Transform):
    """OnionScan Transform Related Onion Domains"""

    input_type = Domain

    def do_transform(self, request, response, config):
        Domain = request.entity.value
        PathToOnionscan = "/home/user/onionscan/src/github.com/s-rah/onionscan/" ## CHANGE ME
        os.environ["GOPATH"] = PathToOnionscan
        URL = Domain.split("//")[1]

        if os.path.isfile(PathToOnionscan + URL + ".scan"):
            pass
        else:
            subprocess.call(PathToOnionscan + " go run main.go -jsonReport -reportFile scan " + URL + ".scan", shell=True)
        data = json.loads(open(PathToOnionscan + URL + ".scan", "r").read())

        try:
            for i in data["identifierReport"]["relatedOnionDomains"]:
                response += Domain(fqdn=str(i))
        except:
            response += Domain("None")
        return response
