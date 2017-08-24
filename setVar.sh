#!/bin/sh

echo "[?] Use the compiled version? [Yes/No]"
read compiled
if [ $compiled = "Yes" ]
then
  export COMPILED=${compiled}
  echo "[?] Input Full pathToCompiled:"
  read pathToCompiled
  export PATHCOMPILED=${pathToCompiled}
  echo "[?] Input Full pathToReports:"
  read pathToReports
  export PATHTOREPORTS=${pathToReports}
  echo "##################################"
  echo "[+] PATHCOMPILED setted: " + ${pathToCompiled}
  echo "[+] PATHTOREPORTS setted: " + ${pathToReports}
else
  echo "[?] Input Full PathToOnionscan: "
  read PathToOnionscan
  export GOPATH=$PathToOnionscan
  echo "##################################"
  echo "[+] GOPATH setted: " ${PathToOnionscan}
fi
