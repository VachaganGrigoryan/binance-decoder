package main

// #include <Python.h>
// int PyArgParseTuple(PyObject* args, const char** ptr, Py_ssize_t* size);
import "C"

import (
	"crypto/sha256"
	"encoding/base64"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"github.com/bnb-chain/go-sdk/types"
	"github.com/bnb-chain/go-sdk/types/tx"
)

type Transaction struct {
	Hash string   `json:"hash"`
	Data tx.StdTx `json:"data"`
}


//export binance_decoder
func binance_decoder(self *C.PyObject, args *C.PyObject) *C.PyObject {
    var s *C.char
    var size C.Py_ssize_t
    if C.PyArgParseTuple(args, &s, &size) == 0 {
        return nil
    }

	codec := types.NewCodec()
    parsedTx := Transaction{}
    decodeTx64, err := base64.StdEncoding.DecodeString(C.GoString(s))
    if err != nil {
        fmt.Println("error:", err)
        return nil
    }

    decodeTxStr := string(decodeTx64)

    h := sha256.New()
    h.Write(decodeTx64)
    parsedTx.Hash = hex.EncodeToString(h.Sum(nil))

    err = codec.UnmarshalBinaryLengthPrefixed([]byte(decodeTxStr), &parsedTx.Data)
    if err != nil {
        fmt.Println("Error - codec unmarshal")
        return nil
    }


	bz, err := json.Marshal(parsedTx)

	if err != nil {
		fmt.Println("Error - json marshal")
		return nil
	}

    return C.PyUnicode_FromString(C.CString(string(bz)))
}


func main() {}