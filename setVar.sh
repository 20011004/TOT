#!/bin/sh

echo "[?] Use the compiled version? [Yes/No]"
read compiled
if [ $compiled = "Yes" ]
then
  echo "compiled = '" + ${compiled} + "'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input Full pathToCompiled:"
  read pathToCompiled
  echo "pathToCompiled = '" +${pathToCompiled} + "'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input Full pathToReports:"
  read pathToReports
  echo "pathToReports = '" ${pathToReports} + "'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "##################################"
  echo "[+] PATH COMPILED setted: " + ${pathToCompiled}
  echo "[+] PATH TO REPORTS setted: " + ${pathToReports}
else
  echo "[?] Input Full PathToOnionscan: "
  read PathToOnionscan
  echo "PathToOnionscan = '" ${PathToOnionscan} + "'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "##################################"
  echo "[+] GOPATH setted: " ${PathToOnionscan}
fi
