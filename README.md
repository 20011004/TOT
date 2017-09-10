![Screen](https://i.imgur.com/ccqwEUv.png)

# OSMT
OnionScan Maltego Transform

This project aim to handle the `json` report from [Onionscan](https://github.com/s-rah/onionscan) to [Maltego](https://www.paterva.com/web7/buy/maltego-clients/maltego-ce.php) with a transform.

## 0x00
What you need is:
* Onionscan and its dependencies
* Maltego (tested on CE)

## 0x01
I suggest you to install every entities available in Maltego (free ones), now as now you don't need them all, but the project is just at the beginning. Remember to run `. setVar.sh` to set the right env var before you compile the package.

## 0x02
To compile the package just `cd Onionscan/src` and then `canari create-profile OnionScan`. This should have created a `OnionScan.mtz` file in the directory where you ran the command. Let’s import this profile into Maltego:

1. Open Maltego.
2. Click on the Maltego home button (big Maltego icon in the top left corner).
3. Navigate to Import then click on Import Configuration
4. Select your Onionscan.mtz file and accept the defaults in the wizard.

## 0x03
Since `input_type = Domain`, drop a `Domain` entity and name it with `hiddenService.onion`. If a `scanned.onion.scan` file is not present in `pathToReports` it will connect to a server that hosts it (at least this is what makes sense). To setup the server just edit `onionServ.py` and remember to re-run `. setVar.sh` and then `canari create-profile OnionScan`.

## 0x04
Updates that are coming:
- support for SSL in "report Server"
- just ask

## 0xISSUES
If `API Key` is not accepted the transform does not exit.
