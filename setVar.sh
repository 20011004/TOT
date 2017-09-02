#!/bin/sh

echo "[?] Use the compiled version? [Yes/No]"
read compiled
if [ $compiled = "Yes" ]
then
  echo "compiled = '"${compiled}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input Full pathToCompiled:"
  read pathToCompiled
  echo "pathToCompiled = '"${pathToCompiled}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input Full pathToReports:"
  read pathToReports
  echo "pathToReports = '"${pathToReports}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "##################################"
  echo "[+] PATH COMPILED setted: " ${pathToCompiled}
  echo "[+] PATH TO REPORTS setted: " ${pathToReports}
else
  echo "[?] Input Full PathToOnionscan: "
  read PathToOnionscan
  echo "PathToOnionscan = '"${PathToOnionscan}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input Full pathToReports:"
  read pathToReports
  echo "pathToReports = '"${pathToReports}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "compiled = 'No'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "pathToCompiled = 'No'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "##################################"
  echo "[+] GOPATH setted: " ${PathToOnionscan}
fi

echo "[?] Set up a reportServer: [Yes/No]"
read repo
if [ $repo = "Yes" ]
then
  echo "[?] Input hostname: "
  read hostName
  echo "host = '"${hostName}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input port: "
  read hostPort
  echo "port = ${hostPort}" >> Onionscan/src/Onionscan/transforms/envVar.py
  echo "[?] Input API Key: "
  read apiKey
  echo "key = '"${apiKey}"'" >> Onionscan/src/Onionscan/transforms/envVar.py
fi
