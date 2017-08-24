# OSMT
OnionScan Maltego Transform

This project aim to handle the `json` report from [Onionscan](https://github.com/s-rah/onionscan) to [Maltego](https://www.paterva.com/web7/buy/maltego-clients/maltego-ce.php) with a transform.

## 0x00
What you need is:
* Go 1.6 or 1.7
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
Since `input_type = Domain`, drop a `Domain` entity and name it with `http://hiddenService.onion`.
Now enjoy.

## 0x04
Updates are coming...
