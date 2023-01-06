# binance-decoder
### Motivation
Binance Chain using Amino logic in the transaction encoding, I have looked for decoder in Python but can't find properly solution for that and I made this Python package using https://github.com/bnb-chain/node-binary/issues/53 Github discussion.

### Pre-Installation
Please make sure you have up-to-date pip and setuptools

``` shell
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
```

### Install Package
You can use [PyPi](https://pypi.org/project/binance-decoder/) to get `binance-decoder` package.

``` shell
pip install binance-decoder
```

### Usage
``` python
from binance_decoder import binance_decoder
import json

encoded_tx = "6wHwYl3uCnHObcBDChSIhrF81iDjeLmz0sHwkVU0WIR5xRIwODg4NkIxN0NENjIwRTM3OEI5QjNEMkMxRjA5MTU1MzQ1ODg0NzlDNS0xOTE2MDI1GhFCQUtFLTVFMF9CVVNELUJEMSACKAEwlNqqEDiAjI7jgB5AARJyCibrWumHIQOhYvTqdPrZQxXuEW4VhRdTqhAHi1kbnJUagWQGVOCqqxJAvLXcvsQuGGOfnS+aw9+6/DBpn7ptHU3Tgz406JelZetV4P0icmXOlu530maz7+VlwFtoTuQKZTQ2rjac57a1OxjCjwEg+Ph0"

decoded_tx_str = binance_decoder(encoded_tx)  # Decode transaction, return type will be `str`
decoded_tx_json = json.loads(decoded_tx_str)
```

### About
First version of project was just use binance-tx-decoder binary from Python writen by Golang. But here we got some issue related on OS arg parse limitations.
#### Example 
- we had `binance-tx-decoder` binary file writen by Golang
``` go
package main

import (
	"crypto/sha256"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"github.com/binance-chain/go-sdk/types"
	"github.com/binance-chain/go-sdk/types/tx"
	"os"
)

type Transaction struct {
	Hash string   `json:"hash"`
	Data tx.StdTx `json:"data"`
}

func main() {
	txs := os.Args[1:]

	codec := types.NewCodec()
	parsedTxs := make([]Transaction, len(txs))
	for i := range txs {
		decodeTx64, err := base64.StdEncoding.DecodeString(txs[i])
		if err != nil {
			fmt.Println("error:", err)
		}

		decodeTxStr := string(decodeTx64)

		h := sha256.New()
		h.Write(decodeTx64)
		parsedTxs[i].Hash = hex.EncodeToString(h.Sum(nil))

		err = codec.UnmarshalBinaryLengthPrefixed([]byte(decodeTxStr), &parsedTxs[i].Data)
		if err != nil {
			fmt.Println("Error - codec unmarshal")
		}
	}

	bz, err := json.Marshal(parsedTxs)

	if err != nil {
		fmt.Println("Error - json marshal")

	}
	fmt.Println(string(bz))
}
```
- used following code to call `binance-tx-decoder` from Python code
``` python
import os
import json


txs = [
  "2AHwYl3uCl4WbmgbChTXj1deyGieL/2pir/GvjCJzzoRZRIRUlVORS1CMUFfQlVTRC1CRDEaL0Q3OEY1NzVFQzg2ODlFMkZGREE5OEFCRkM2QkUzMDg5Q0YzQTExNjUtMjc3MzM4EnIKJuta6YchAof/uuUFK7rjP6j+XolHCm6iwEI6OL9pay27Td50xFE8EkAry+YVeHb/KYo6ptBKcxmFv5uIZtpTHw4QrajK3dntKAZ1UkpV62jfUVNPVj01fUQdrAe5QBrSLRjRL4nwJn8GGIqeJyDb9hA=",
  "7AHwYl3uCnHObcBDChRlmTns6WEaqmu7vqLF/cM5jKgDmBIwNjU5OTM5RUNFOTYxMUFBQTZCQkJCRUEyQzVGREMzMzk4Q0E4MDM5OC0zODk4MjQzGhFBVE9NLTU5Nl9CVVNELUJEMSACKAEwuIjOsgM4gJK4rCJAARJzCibrWumHIQPzxSPM0ZHrLoHz0G83k77S+g0WlS/14u2TT9Oj9IrCAxJAU+D1OiN9DbULcOqAdZ//sXq3ZIgdZ4DrL9N883JOpr9EN2IXe5tvwyPzbi6XtvsQo5chI2vzp/jULs1dQhkzoBiEgy8ggvftAQ==",
]

cmd = f'./binance-tx-decoder {" ".join(txs)}'

with os.popen(cmd) as proc:
    transactions = json.loads(proc.read())
    
print(ransactions)
```

Finally, I had some idea to check is there way to make Python Package by Golang. 
This is Open source Python Package and everyone can take to use.